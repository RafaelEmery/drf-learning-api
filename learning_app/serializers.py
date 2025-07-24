from rest_framework import serializers

from .models import Course, Review


class CourseSerializer(serializers.ModelSerializer):
    pass

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
