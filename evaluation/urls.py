# urls.py
from django.urls import path
from .views import LawyerListCreateView, EvaluationListCreateView, EvaluationDetailView

urlpatterns = [
    path('lawyers/', LawyerListCreateView.as_view(), name='lawyer'),
    path('evaluations/', EvaluationListCreateView.as_view(), name='evaluation'),
    path('evaluations/<int:pk>/', EvaluationDetailView.as_view(), name='evaluation-detail'),
]
