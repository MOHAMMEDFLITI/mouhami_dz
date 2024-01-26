# views.py
from rest_framework import generics
from .models import Lawyer, Evaluation
from .serializers import LawyerSerializer, EvaluationSerializer

class LawyerListCreateView(generics.ListCreateAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

class EvaluationListCreateView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class EvaluationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
