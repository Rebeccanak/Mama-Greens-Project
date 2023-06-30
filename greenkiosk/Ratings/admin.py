from django.contrib import admin
from .models import Ratings

# Register your models here.
class RatingsAdmin(admin.ModelAdmin):
    list_display = ("title", "review_Content", "rating", "cumulative_ratings", "author", 'created_date')

admin.site.register(Ratings, RatingsAdmin)