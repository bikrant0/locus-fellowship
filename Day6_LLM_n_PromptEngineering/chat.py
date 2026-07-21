import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

messages=[
    {
        "role":"system",
        "content":"You are a helpful assistant"
    }
]

while True:
    user_input=input("Please Type Here:")  #Taking the input or prompt from the user
    
    if user_input.lower() in ["quit","exit"]:
        print("Bot:Goodbye")
        break
    
    messages.append({
        "role":"user",
        "context":user_input
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
    )
    
    reply=response.choices[0].message.content
    
    print("Bot:{reply}\n")
    
    messages.append({
        "role":"assistant",
        "content":reply,
    })
    
    
    



