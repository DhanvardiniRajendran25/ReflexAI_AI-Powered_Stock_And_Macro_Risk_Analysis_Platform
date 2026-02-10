import os
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY")
print("GOOGLE_API_KEY from env is:", "FOUND" if api_key else "NOT FOUND")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

response = model.generate_content("Hello Gemini, reply with one short sentence.")
print("MODEL RESPONSE:\n", response.text)
