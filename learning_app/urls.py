from django.urls import path

from .views import CourseAPIView, CoursesAPIGenericView, CourseAPIGenericView, ReviewAPIView, ReviewsAPIGenericView, ReviewAPIGenericView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='Courses'),
    path('reviews/', ReviewAPIView.as_view(), name='Reviews'),
    
    # Test endpoints for testing GenericAPIView
    path('courses/generics/', CoursesAPIGenericView.as_view(), name='Courses'),
    path('courses/generics/<int:pk>/', CourseAPIGenericView.as_view(), name='Course'),
    path('reviews/generics/', ReviewsAPIGenericView.as_view(), name='Reviews'),
    path('reviews/generics/<int:pk>/', ReviewAPIGenericView.as_view(), name='Review'),
]