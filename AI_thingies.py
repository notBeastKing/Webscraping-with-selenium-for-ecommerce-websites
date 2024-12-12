import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_ollama.llms import OllamaLLM

os.environ["GOOGLE_API_KEY"] = "AIzaSyDbJPhGJWHSsmpPEwa9hW4L6ZBNrFIsGU8"


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def Dore_no_website(item):  #figures out which website use 
    messages = [ 
        (
            "system",
            """AN item will be given to you, YOU have to tell whether that item would be classified as a product available in amazon/flipkart (code named as amaflip) or if it would be available in blinkit/zepto(codename : zekit), an easy way to classify would be so segregate grocery or related items as zekit or if the items seem to be more viable to get on sites like amazon/flipkart,
              YOU don't HAVE TO CHECK THE WEBSITE just what would be more suitable for that item
              ONLY REPLY USING THE CODENAME RESPECTIVELY AND NOTHING ELSE ONLY CODENAME either amaflip OR zekit AND nothing else
              REPLY WITH amaflip|zepkit IF BOTH ARE PERFECTLY VIABLE""",
        ),
        ("human", item),
    ]
    website = llm.invoke(messages)
    return website.content

