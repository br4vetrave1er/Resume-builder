# Resume-builder
Chatbot that helps you improve your resume using the power of chatgpt

## Problem Statement
In today's world you are bombarded with so much information that it is hard to focus on one resource and more difficult 
to judge which information is right or wrong. Same is true for job seekers who wants to land their dream job so in journey of 
any job seeker first step is to build a resume which is filled with only the information which is most important and intrigues
any HR. But how do you build such a resume? if you google this you will get many answers talking about all different
topic and ways to improve your resume but which one would you trust? So to solve this problem in today's world where as each
day passes, AI becomes part of our daily life I developed this web application to tackle this very problem using the power
of Large Language Models.

### About the application

So, this application is developed using **django framework** on its backend and simple **HTML**, **CSS**, **Javascript** and 
**Bootstarp 5** for its frontend. Apart from this **Langchain** library was used to build the chatbot funcnalities for this
application.

### Working
- First, you have to upload your resume to the web application
- on successfull upload a chatbot is built in the backend using this document.
- Voila! The bot is ready to answer all your queries?

### Applicaiton working
As soon you start application you are presented with the homepage where user have to upload his resume. This could be done
in 2 ways a) selecting file from your device b) dragging and droping your resume here. As you add the file and click upload,
a fetch request is made to the server which verifies and save your file to database and on successfull request it redirects
you to next page where you can interact with cahtbot.

here many things are happening in background so let's discuss one by one
- As soon as your page loads your document is sent to **chatbot.py** where a bot model is built using your document
  and embedded properly so that your model can understand your questions. (more about this bot later)
- After loading of page you are presented with a panel on the right side where your can type your queries and your document
  is displayed on left side
- Now as ask any query, another request is made using fetch to the server where this query is passed to your model and
  you are presented with a reponse in your forntend using javascript

### Chatbot Model
For building this model, langchain library is used and most of the settings used here are according to my best understanding
you can change or tweak with these setting as you like as there are many option available in langchain docs

- Some key settings used
  - OpenAiEmbeddings: as i was buliding this model using ChatGPT so decided its best if i use both provided by same company and
                     also i could fetch these using same API calls.
  - PyPDFLoader: For loading the pdf documents and reteriving necessry information from the document
  - RecursiveTextSplitter: as my document can be of atmost 2-3(mostly 1) so gain more information from less data.
  - Chroma: for merging embedding and document toagther as its easy to configure and doesnot require additional resources
  - CoversationBufferMemory: To store the chat history and answer each subsequent question based on this history
  - ConversationalRetrievalChain: For creating a final model and combining ChatGPT model, Prompt, Mermory, embeddings.

  Here is a image which i found very heplful
  <img src="https://img-blog.csdnimg.cn/04865f1f428741a0bf816d88c153fd01.png">

### Installation & Usage
1. Clone the GitHub repository.
    ```
    !git clone https://github.com/br4vetrave1er/GreatKart-django.git
    ```
2. Create a virtual environment.
    ```
    python -m venv [environment name] 
   ```
3. Install necessary libraries using `requirement.txt`
    ```
    pip install -r requirements.txt
   ```
4. Add your OpenAi API key to the `.env` File
   ```
    OPENAI_API_KEY = "sk*******"
   ```
  
5. If you want to use this project in development server, then
    ```
    python manage.py runserver
    ```
6. Voila! You are ready go to
   ```
      http://127.0.0.1:8000/home/
   ```
 
 
