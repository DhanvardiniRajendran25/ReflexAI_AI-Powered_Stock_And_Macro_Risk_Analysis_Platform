import os
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY")
print("GOOGLE_API_KEY from env is:", "FOUND" if api_key else "NOT FOUND")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found. Set GOOGLE_API_KEY before running.")

genai.configure(api_key=api_key)

print("\nAvailable models that support generateContent:\n")

models = genai.list_models()
for m in models:
    # m.name is like "models/gemini-1.5-flash"
    methods = getattr(m, "supported_generation_methods", [])
    if "generateContent" in methods:
        print("-", m.name)
