from django.db import models


class Base(models.Model):
    """
    auto_now_add argument set to True, which means that the field
    will be automatically set to now when the object is first created.
    Details for Model: https://docs.djangoproject.com/en/5.2/topics/db/models/
    """

    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    """
    Meta class is used to define metadata about the model. Examples:
        ordering = ['-published_at'] means that the results will be ordered by the published_at field in descending order.
        verbose_name_plural = 'Bases' is used to set the plural name of the model.
        permissions = [('can_view_base', 'Can view base')] is used to define custom permissions for the model.
    """

    class Meta:
        """Defining an abstract class."""

        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["id"]

    """
    toString like method for Course model.
    If you're using print(course), should return only course title.
    """

    def __str__(self):
        return self.title


class Review(Base):
    course = models.ForeignKey(Course, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    """
    blank=True means that the field is not required.
    """
    comment = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        """
        unique_together is used to define a unique constraint on multiple fields.
        In this case, it means that the combination of email and course fields must be unique.
        """
        unique_together = ["email", "course"]

    def __str__(self):
        return f"{self.name} rated {self.course} at {self.rating}"
