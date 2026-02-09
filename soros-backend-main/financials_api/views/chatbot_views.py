from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
import google.generativeai as genai
from django.conf import settings
import os

# Load the Gemini key from env first, then from project-level secrets.py
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    try:
        from buffet_backend import secrets  # sibling project package
        GEMINI_API_KEY = getattr(secrets, 'GEMINI_API_KEY', None)
    except ImportError:
        print("Warning: secrets.py not found or GEMINI_API_KEY not set within it.")
        GEMINI_API_KEY = None

class ChatbotView(APIView):
    """
    API View for the chatbot.
    Accepts a POST request with a user message, calls the Gemini API,
    and returns the AI's response, styled like George Soros.
    """
    def post(self, request):
        """
        Handles POST requests to /api/chatbot/
        """
        # --- Get API Key ---
        api_key = GEMINI_API_KEY or os.environ.get('GEMINI_API_KEY')

        if not api_key:
            return Response(
                {"error": "Gemini API key not configured."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # --- Configure Gemini ---
        try:
            genai.configure(api_key=api_key)
        except Exception as e:
             print(f"Error configuring Gemini: {e}")
             return Response(
                {"error": "Failed to configure Gemini API."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # --- Get User Message ---
        user_message = request.data.get('message', '').strip()
        if not user_message:
            return Response(
                {"error": "No message provided."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # --- Construct Prompt ---
        prompt = (
            "You are a helpful AI assistant embodying George Soros—macro-focused, reflexivity-aware, and ruthless about risk management. "
            "Favor clear, direct answers. Emphasize policy regimes, capital flows, leverage, liquidity, and asymmetric risk/reward. "
            "If asked about a specific stock, connect it to macro drivers and risk controls; prioritize when to cut, when to press, and how to hedge. "
            "Default to concise, actionable replies.\n\n"
            f"User Question: \"{user_message}\"\n\n"
            "George Soros Style Answer:"
        )

        # --- Call Gemini API ---
        try:
            # ('gemini-1.5-flash')
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(prompt)

            # Extract the text response
            bot_reply_text = response.text

        # --- Handle Potential API Errors ---
        except Exception as e:
            print(f"Gemini API Error: {e}")
            # Check for specific safety feedback if available in the exception or response candidates
            try:
                 if response.prompt_feedback.block_reason:
                      error_msg = f"Request blocked due to: {response.prompt_feedback.block_reason}"
                 else:
                      for candidate in response.candidates:
                           if candidate.finish_reason != 'STOP':
                                error_msg = f"Response stopped due to: {candidate.finish_reason}"
                                break
                      else: # If loop finished without break
                           error_msg = "An error occurred while communicating with the AI."

            except Exception: # Fallback if accessing response parts fails
                 error_msg = "An error occurred while communicating with the AI."


            return Response(
                {"error": error_msg},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # --- Return Successful Response ---
        bot_reply = {
            "reply": bot_reply_text
        }
        return Response(bot_reply, status=status.HTTP_200_OK)
