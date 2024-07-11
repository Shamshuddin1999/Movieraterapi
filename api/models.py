from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=500)

    def no_of_ratings(self):
        rating = Rating.objects.filter(movie=self)
        return len(rating)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings)>0:
            return (sum/len(ratings))
        else:
            return 0

    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.FloatField(validators=[MinValueValidator(1.0),MaxValueValidator(5.0)])




    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)