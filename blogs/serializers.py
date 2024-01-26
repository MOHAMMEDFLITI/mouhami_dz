
from rest_framework import serializers
from .models import Blog, Lawyer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class LawyerSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Lawyer
        fields = '__all__'
