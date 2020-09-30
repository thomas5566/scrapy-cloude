from django.contrib import admin
from .models import Movie
from .models import PttMovie


class MovieAdmin(admin.ModelAdmin):
    pass


class PttMovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(PttMovie, PttMovieAdmin)
