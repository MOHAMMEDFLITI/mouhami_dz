from rest_framework import serializers
from .models import Lawyer, Evaluation

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('id', 'rating', 'confirmed', 'name', 'email', 'comment')


