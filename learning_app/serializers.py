from rest_framework import serializers

from .models import Course, Review


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "url", "published_at", "active"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        """
        The write_only on email means that won't be available at 
        GET review requests and only at POST review requests
        """
        extra_kwargs = {"email": {"write_only": True}}
        fields = [
            "id",
            "course",
            "name",
            "email",
            "comment",
            "rating",
            "published_at",
            "active",
        ]
