import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")
django.setup()

from movies_app import models


"""
Get movies that last less than 2.5 hours and were released after 2005
Get all the movies that contain a word “criminal”, “mob” or “cop” in their description
Like previous, but get only movies that were released before 2010
Get list of actors, and add amount of movies they played in (for each one)
Get average, min, and max rating in the system
Get Movies with their avg ratings
Get ratings that were created in 2023
Get all the actors in the system with min and max rating of the movies they played in
Get movies with average salary for actors in each one
Get actors with their average salaries
Get actors who played main roles at least once
Get movies and amount of actors who played main roles 
"""

def get_young_actors():
    return models.Actor.objects.filter(birth_date__gt='1970-01-01')

def get_movies_longer_than_2_5_hours_and_after_2005():
    return models.Movie.objects.filter(duration__gt=150, year__gt=2005)

def get_movies_with_criminal_mob_or_cop():
    return models.Movie.objects.filter(description__icontains="criminal") | models.Movie.objects.filter(description__icontains="mob") | models.Movie.objects.filter(description__icontains="cop")

def get_movies_with_criminal_mob_or_cop_before_2010():
    return models.Movie.objects.filter(description__icontains="criminal", year__lt=2010) | models.Movie.objects.filter(description__icontains="mob", year__lt=2010) | models.Movie.objects.filter(description__icontains="cop", year__lt=2010)

def get_actors_with_movies_count():
    return models.Actor.objects.annotate(movies_count=models.Count('movieactor'))

def get_avg_min_max_rating():
    return models.Rating.objects.aggregate(models.Avg('rating'), models.Min('rating'), models.Max('rating'))

def get_movies_with_avg_rating():
    return models.Movie.objects.annotate(avg_rating=models.Avg('rating__rating'))

def get_ratings_in_2023():
    return models.Rating.objects.filter(rating_date__year=2023)

def get_actors_with_min_max_rating():
    return models.Actor.objects.annotate(min_rating=models.Min('movieactor__movie__rating__rating'), max_rating=models.Max('movieactor__movie__rating__rating'))

def get_movies_with_avg_salary():
    return models.Movie.objects.annotate(avg_salary=models.Avg('movieactor__salary'))

def get_actors_with_avg_salary():
    return models.Actor.objects.annotate(avg_salary=models.Avg('movieactor__salary'))

def get_actors_with_main_roles():
    return models.Actor.objects.filter(movieactor__main_actor=True)

def get_movies_with_main_roles_count():
    return models.Movie.objects.annotate(main_roles_count=models.Count('movieactor', filter=models(movieactor__main_actor=True)))

