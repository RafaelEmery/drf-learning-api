from rest_framework import serializers

from .models import Course, Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for reviews only
    """

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


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for courses and reviews
    """

    """
    Nested relationships are not supported by default in DRF
    many=True indicates all the entities from the relation
    read_only=True indicates that this field is not writable
    Details: https://www.django-rest-framework.org/api-guide/fields/#nested-relationships
    """
    # reviews = ReviewSerializer(many=True, read_only=True)

    """
    Using the HyperLikedRelatedField class
    To deal better with relationships, showing a URL on reviews array instead
    of all serialized object from reviews
    Details: https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#hyperlinking-our-api
    """
    # reviews = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="review-detail"
    # )

    """
    Using PrimaryKeyRelatedField
    Showing only the ID of the related reviews instead the full object
    or a bunch of URLs 
    Details: https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#hyperlinking-our-api
    """
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    """
    Many relation arguments on RelatedField base class
    MANY_RELATION_KWARGS = (
        'read_only', 'write_only', 'required', 'default', 'initial', 'source',
        'label', 'help_text', 'style', 'error_messages', 'allow_empty',
        'html_cutoff', 'html_cutoff_text'
    )
    """

    class Meta:
        model = Course
        fields = ["id", "title", "url", "published_at", "active"]
