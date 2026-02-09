import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TransformerView(APIView):
    """
    Proxy to an external transformer model API.
    """

    def post(self, request):
        message = request.data.get("message", "").strip()
        if not message:
            return Response({"error": "No message provided."}, status=status.HTTP_400_BAD_REQUEST)

        bearer = request.data.get("token") or os.environ.get("TRANSFORMER_BEARER")
        if not bearer:
            try:
                from buffet_backend import secrets
                bearer = getattr(secrets, "TRANSFORMER_BEARER", None)
            except Exception:
                bearer = None

        if not bearer:
            return Response({"error": "Transformer API token not configured."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        url = "https://us-central1-aiplatform.googleapis.com/v1/projects/csye7380soros-glcoud-project/locations/us-central1/endpoints/6095682568785494016:predict"
        payload = {"instances": [{"question": message}]}
        headers = {
            "Authorization": f"Bearer {bearer}",
            "Content-Type": "application/json"
        }

        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=None)
            if not resp.ok:
                return Response({"error": f"Transformer API error: {resp.text}"}, status=resp.status_code)
            data = resp.json()
            preds = data.get("predictions", [])
            if not preds:
                return Response({"error": "Transformer API returned no predictions."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            reply = preds[0]
            return Response({"reply": reply}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Transformer API request failed: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
