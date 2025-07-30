from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import generics

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer

# About generic views: 
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

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
    

class CoursesAPIGenericView(generics.ListCreateAPIView):
    """
    Generic view based of ListCreateAPIView to abstract the CourseAPIView functions
    generics.ListCreateAPIView - List and create
    Methods that doesn't need any URL parameters
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class CourseAPIGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view based of RetrieveUpdateDestroyAPIView to abstract the CourseAPIView functions
    generics.RetrieveUpdateDestroyAPIView - Retrieve, update and destroy
    Must be at a different class because it needs the PK (id)
    The PK can be passed as URL param
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
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


class ReviewsAPIGenericView(generics.ListCreateAPIView):
    """
    Generic view based of ListCreateAPIView to abstract the ReviewAPIView functions
    generics.ListCreateAPIView - List and create
    Methods that doesn't need any URL parameters
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAPIGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view based of RetrieveUpdateDestroyAPIView to abstract the ReviewAPIView functions
    generics.RetrieveUpdateDestroyAPIView - Retrieve, update and destroy
    Must be at a different class because it needs the PK (id)
    The PK can be passed as URL param
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer