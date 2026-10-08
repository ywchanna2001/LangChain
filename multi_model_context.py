from dotenv import load_dotenv
from base64 import b64encode

from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
 
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
)

with open("lion cubs.jpg", "rb") as image_file:
    image_base64 = b64encode(image_file.read()).decode("utf-8")

message = {
    'role': 'user',
    'content': [
        {'type': 'text', 'text': 'Describe the contents of this image.'},
        {'type': 'image', 'base64': image_base64, "mime_type": "image/jpeg"}
    ]
}

response = model.invoke([message])

print(response.content)