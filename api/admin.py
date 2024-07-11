from django.contrib import admin
from .models import Movie, Rating

admin.site.register(Movie)
@admin.register(Rating)
class TrackRating(admin.ModelAdmin):
    list_display = ['movie','user','stars']