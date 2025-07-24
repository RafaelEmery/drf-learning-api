from django.contrib import admin

from .models import Course, Review


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'published_at', 'updated_at', 'active']
    
    """
    Other suggestions:
        list_filter = ['active', 'published_at']
        search_fields = ['title', 'url']
        date_hierarchy = 'published_at'
        ordering = ['published_at']
    """
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'email', 'rating', 'published_at', 'updated_at', 'active']
    
