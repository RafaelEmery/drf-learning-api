from django.urls import path

from .views import CourseAPIView, CoursesAPIGenericView, CourseAPIGenericView, ReviewAPIView, ReviewsAPIGenericView, ReviewAPIGenericView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='Courses'),
    path('reviews/', ReviewAPIView.as_view(), name='Reviews'),
    
    # Test endpoints for testing GenericAPIView
    path('courses/generics/', CoursesAPIGenericView.as_view(), name='Courses'),
    path('courses/generics/<int:pk>/', CourseAPIGenericView.as_view(), name='Course'),
    path('reviews/generics/', ReviewsAPIGenericView.as_view(), name='Reviews'),
    path('reviews/generics/<int:review_pk>/', ReviewAPIGenericView.as_view(), name='Review'),

    # Explicit PK from model when use both of them
    # Update on other methods either to review_pk instead pk (review only because is using ReviewAPI views)
    path('courses/<int:course_pk>/reviews/', ReviewsAPIGenericView.as_view(), name='Course and reviews'),
    path('courses/<int:course_pk>/review/<int:review_pk>/', ReviewAPIGenericView.as_view(), name='Course and review')
]