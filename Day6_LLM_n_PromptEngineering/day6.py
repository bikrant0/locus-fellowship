import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Setup the client (Groq free endpoint)
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# Your input paragraph
paragraph = """
Photosynthesis is the process used by plants, algae, and certain bacteria to convert 
light energy into chemical energy. This chemical energy is stored in carbohydrate molecules, 
such as sugars, which are synthesized from carbon dioxide and water. Oxygen is released as 
a byproduct of this process. Most plants perform photosynthesis using chlorophyll, a green 
pigment found in chloroplasts.
"""

# Create the prompt instructions using system & user roles
system_prompt = "You are an expert exam creator. Generate 5 multiple-choice questions (MCQs) with options (A, B, C, D) and an answer key based strictly on the provided text."

# Make the LLM call
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Create 5 MCQs from this text:\n\n{paragraph}"}
    ]
)

# Print the output
print(response.choices[0].message.content)
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


paragraph = """
Photosynthesis is the process used by plants, algae, and certain bacteria to convert 
light energy into chemical energy. This chemical energy is stored in carbohydrate molecules, 
such as sugars, which are synthesized from carbon dioxide and water. Oxygen is released as 
a byproduct of this process. Most plants perform photosynthesis using chlorophyll, a green 
pigment found in chloroplasts.
"""


system_prompt = "You are an expert exam creator. Generate 5 multiple-choice questions (MCQs) with options (A, B, C, D) and an answer key based strictly on the provided text."


response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Create 5 MCQs from this text:\n\n{paragraph}"}
    ]
)


print(response.choices[0].message.content)