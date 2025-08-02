from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import mixins


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

        return Response(
            {"id": serializer.data["id"], "title": serializer.data["title"]},
            status=status.HTTP_201_CREATED,
        )


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

        return Response(
            {"id": serializer.data["id"], "name": serializer.data["name"]},
            status=status.HTTP_201_CREATED,
        )


class ReviewsAPIGenericView(generics.ListCreateAPIView):
    """
    Generic view based of ListCreateAPIView to abstract the ReviewAPIView functions
    generics.ListCreateAPIView - List and create
    Methods that doesn't need any URL parameters
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.kwargs.get("course_pk"):
            return self.queryset.filter(course_id=self.kwargs.get("course_pk"))
        return super().get_queryset()


class ReviewAPIGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view based of RetrieveUpdateDestroyAPIView to abstract the ReviewAPIView functions
    generics.RetrieveUpdateDestroyAPIView - Retrieve, update and destroy
    Must be at a different class because it needs the PK (id)
    The PK can be passed as URL param
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        if self.kwargs.get("course_pk"):
            return get_object_or_404(
                course_id=self.kwargs.get("course_pk"), id=self.kwargs.get("review_pk")
            ).first()
        return get_object_or_404(self.get_queryset(), id=self.kwargs.get("review_pk"))


"""
API version 2
"""


class CourseViewSet(viewsets.ModelViewSet):
    """
    CourseViewSet using DRF ModelViewSet to abstract basic functions
    Details: https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def reviews(self, request, id=None):
        course = self.get_object()
        # many=True indicates all the entities from the relation
        review_serializer = ReviewSerializer(course.reviews.all(), many=True)

        return Response(review_serializer.data)


# To be used below
# class ReviewViewSet(viewsets.ModelViewSet):
#     """
#     Review using DRF ModelViewSet to abstract basic functions
#     Details: https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#     """

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


class ReviewViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    Using DRF mixins to abstract basic functions
    Details: https://www.django-rest-framework.org/api-guide/generic-views/#listmodelmixin
    ModelViewSet above means (inheritance):
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
