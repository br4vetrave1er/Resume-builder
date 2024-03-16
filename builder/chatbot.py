from django.conf import settings
from dotenv import load_dotenv
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatMessagePromptTemplate, SystemMessagePromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


load_dotenv()   # loading OpenAIApi key from env file

embeddings = OpenAIEmbeddings()

global_chatbot = None       # vraible to hold model configurations after build

# Used to build model with some configrurations
def bot_build(file_path):
    print("Status: loading document")
    path = settings.MEDIA_ROOT
    file_path = r"{}{}".format(path[:-1], file_path[6:])
    print("file from chatbot: ",file_path)

    # loading and splitting file data
    loader = PyPDFLoader(file_path=file_path)
    document = loader.load_and_split()
    
    # splitting data within file into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )

    docs = text_splitter.split_documents(documents=document)

    # formatting data from document based on embeddings
    db = Chroma.from_documents(
        docs,
        embeddings,
    )

    print("Status: configuring LLM")
    # llm model
    llm = ChatOpenAI(
        max_tokens=1024,
    )

    print("Status: Configurring Memory")
    # memory Configration for history management
    chat_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


    # pormpt template to be used by model
    general_prompt_template = """"
    As a Resume improving bot, your goal is to provide 
    accurate and helpful information about improving resume.
    You should answer user inquiries based on the context provided and chat history.
    If you don't know the answer, just say that you don't know, don't try to 
    make up an answer.\n\n
    Chat history: {chat_history}\n\n
    Question: {question}\n\n
    Helpful 
    Answer:,
    """ 

    print("Status: Configuring Prompt")
    prompt = PromptTemplate(
        template=general_prompt_template,
        input_variables=["question", "chat_history"],
    )

    print("Status: Configuring Chain")
    # bulding final chain using necessary configurations
    qa_bot = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=db.as_retriever(),
        verbose=False,
        memory=chat_memory,
        condense_question_prompt=prompt,
        chain_type="stuff",
    )

    print("Status: Complete")
    return qa_bot

# Used to build the inital chat-bot Model 
def chatbot_build(file_path):
    global global_chatbot
    if global_chatbot is None:
        global_chatbot = bot_build(file_path=file_path)
    
    
    return global_chatbot
    

# Used to fetch data from model when a query is passed
def chatbot_response(query):
    
    result = global_chatbot.invoke({"question": query})
    return result["answer"]

    
    