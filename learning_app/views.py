from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


class CourseAPIView(APIView):
    """
    Courses API view to define all endpoints
    """
    
    permission_classes = (AllowAny,)
    
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"id": serializer.data['id'], "title": serializer.data['title']}, status=status.HTTP_201_CREATED)
    
    
class ReviewAPIView(APIView):
    """
    Review API view to define all endpoints
    """
    
    permission_classes = (AllowAny,)
    
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"id": serializer.data['id'], "name": serializer.data['name']}, status=status.HTTP_201_CREATED)
