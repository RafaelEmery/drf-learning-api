from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

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
    
    
class ReviewAPIView(APIView):
    """
    Review API view to define all endpoints
    """
    
    permission_classes = (AllowAny,)
    
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data)
