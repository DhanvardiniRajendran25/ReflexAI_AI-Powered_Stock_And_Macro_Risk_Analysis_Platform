from django.urls import path

from financials_api.views.chatbot_views import ChatbotView
from financials_api.views.financial_views import FinancialDataView
from financials_api.views.rag_view import RAGView
from financials_api.views.pairs_view import PairTradingView
from financials_api.views.transformer_view import TransformerView

urlpatterns = [
    path('financials/<str:stock_symbol>/', FinancialDataView.as_view(), name='financial-data'),
    path('chatbot/', ChatbotView.as_view(), name='chatbot'), # Gemini endpoint
    path('ragbot/', RAGView.as_view(), name='ragbot'),    # RAG endpoint
    path('pairs/', PairTradingView.as_view(), name='pair-trading'),  # Pair trading backtest
    path('transformerbot/', TransformerView.as_view(), name='transformer-bot'),  # External transformer
]
