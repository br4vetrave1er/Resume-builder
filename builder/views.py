import json
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import ResumeUploadForm
from .models import FileUpload
from .chatbot import chatbot_build, chatbot_response
# Create your views here.
def home(request):
    return render(request, 'homepage.html')

# file upload API
def upload_file(request):
    if request.method == "POST" and request.FILES['file']:
        resume = request.FILES.get('file')
        if resume:
            resume_file_instance = FileUpload(file=resume)
            resume_file_instance.save()
        
        request.session['file_path'] = resume_file_instance.file.url

        data = {
            'doc': resume_file_instance.file.url,
            'success': True
        }
        return JsonResponse(data=data)
    else:
        return JsonResponse({
            'error': 'No file Uploaded'
        }, status=400)
    

# for sending PDF file to frontend    
def view_pdf(request):
    if request.method == "GET":
        doc = request.session.get("file_path")  # getting file_path from session storage

        path = settings.MEDIA_ROOT

        file_path = r"{}{}".format(path[:-1], doc[6:])  # removing unecessary strings from file path

        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;'
        try:
            return response
        except:
            raise Http404()

# used to render template on the frontend after file upload
def chat_room(request):
    # chatbot = chatbot_build()
    return render(
        request=request,
        template_name='chat_room.html',
    )

# for passing query to LLM model and fetching response
def chat_response(request):
    if request.method == "POST":
        data = json.loads(request.body)

        query = data.get("user-message")

        result = chatbot_response(query)    # request to model function

        response = json.dumps(result)

        return JsonResponse({
            "result": response
        })
    
    return JsonResponse({
        'error': "Invalid Request"
    }, status=400)

# used for building the inital model using the document provided
def bot_build(request):
    if request.method == "POST":

        file_path = request.session.get("file_path")
        print("File _path: ", file_path)

        chatbot_build(file_path=file_path) # model build function


        return JsonResponse({
            'success': True,
        })
    
    return JsonResponse({
        'error': "Invalid Request"
    }, status=400)