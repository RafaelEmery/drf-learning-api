from django.urls import path

from .views import CourseAPIView, ReviewAPIView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='Courses'),
    path('reviews/', ReviewAPIView.as_view(), name='Reviews')
]