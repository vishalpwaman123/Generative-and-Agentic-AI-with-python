from fastapi import Body, FastAPI
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact-us")
def read_root():
    return {"email":"vishal.waman@zohomail.in"}

@app.post("/chat")
def chat(
        message: str = Body(..., description="The Message")
):
    response = client.chat(
        model="gemma:2b", 
        messages=[
        {"role":"user", "content":message}
    ]
    )
    return {"response : ": response.message.content}

# Run virtual environment : & c:\repos\GenAI\Generative-and-Agentic-AI-with-python\GenAI\.venv\Scripts\Activate.ps1
#Run file command : fastapi dev server.py
