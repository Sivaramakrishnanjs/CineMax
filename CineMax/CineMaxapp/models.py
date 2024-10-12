from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class hollywood(models.Model):
    categ = (
        (1, 'Hollywood'),
    )
    poster1image = models.ImageField(upload_to='image')
    poster2image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)
    description1 = models.TextField()
    rating = models.FloatField()
    runtime = models.DurationField(help_text="Format: HH:MM:SS")
    release_date = models.DateField()
    description2 = models.TextField()  # Changed to TextField assuming it's text
    actorimage1 = models.ImageField(upload_to='image')
    actorimage2 = models.ImageField(upload_to='image')
    actressimage3 = models.ImageField(upload_to='image')
    actorname1 = models.CharField(max_length=256)
    actorname2 = models.CharField(max_length=256)
    actressname3 = models.CharField(max_length=256)
    actor1bio = models.CharField(max_length=256)
    actor2bio = models.CharField(max_length=256)
    actress3bio = models.CharField(max_length=256)
    card_image = models.ImageField(upload_to='image')
    card_name = models.CharField(max_length=100)
    watch_trailer = models.FileField(upload_to='videos',default=True)
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class tamilMovies(models.Model):
    categ = (
        (2, 'Tamil Movies'),
    )
    poster1image = models.ImageField(upload_to='image')
    poster2image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)
    description1 = models.TextField()
    rating = models.FloatField()
    runtime = models.DurationField(help_text="Format: HH:MM:SS")
    release_date = models.DateField()
    description2 = models.TextField()  # Changed to TextField assuming it's text
    actorimage1 = models.ImageField(upload_to='image')
    actorimage2 = models.ImageField(upload_to='image')
    actressimage3 = models.ImageField(upload_to='image')
    actorname1 = models.CharField(max_length=256)
    actorname2 = models.CharField(max_length=256)
    actressname3 = models.CharField(max_length=256)
    actor1bio = models.CharField(max_length=256)
    actor2bio = models.CharField(max_length=256)
    actress3bio = models.CharField(max_length=256)
    card_image = models.ImageField(upload_to='image')
    card_name = models.CharField(max_length=100)
    watch_trailer = models.FileField(upload_to='videos',default=True)
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class webseries(models.Model):
    categ = (
        (3, 'Web Series'),
    )
    poster1image = models.ImageField(upload_to='image')
    poster2image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)
    description1 = models.TextField()
    rating = models.FloatField()
    runtime = models.DurationField(help_text="Format: HH:MM:SS")
    release_date = models.DateField()
    description2 = models.TextField()  # Changed to TextField assuming it's text
    actorimage1 = models.ImageField(upload_to='image')
    actorimage2 = models.ImageField(upload_to='image')
    actressimage3 = models.ImageField(upload_to='image')
    actorname1 = models.CharField(max_length=256)
    actorname2 = models.CharField(max_length=256)
    actressname3 = models.CharField(max_length=256)
    actor1bio = models.CharField(max_length=256)
    actor2bio = models.CharField(max_length=256)
    actress3bio = models.CharField(max_length=256)
    card_image = models.ImageField(upload_to='image')
    card_name = models.CharField(max_length=100)
    watch_trailer = models.FileField(upload_to='videos',default=True)
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class anime(models.Model):
    categ = (
        (4, 'Anime'),
    )
    poster1image = models.ImageField(upload_to='image')
    poster2image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)
    description1 = models.TextField()
    rating = models.FloatField()
    runtime = models.DurationField(help_text="Format: HH:MM:SS")
    release_date = models.DateField()
    description2 = models.TextField()  # Changed to TextField assuming it's text
    actorimage1 = models.ImageField(upload_to='image')
    actorimage2 = models.ImageField(upload_to='image')
    actressimage3 = models.ImageField(upload_to='image')
    actorname1 = models.CharField(max_length=256)
    actorname2 = models.CharField(max_length=256)
    actressname3 = models.CharField(max_length=256)
    actor1bio = models.CharField(max_length=256)
    actor2bio = models.CharField(max_length=256)
    actress3bio = models.CharField(max_length=256)
    card_image = models.ImageField(upload_to='image')
    card_name = models.CharField(max_length=100)
    watch_trailer = models.FileField(upload_to='videos',default=True)
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class korean(models.Model):
    categ = (
        (5, 'Korean'),
    )
    poster1image = models.ImageField(upload_to='image')
    poster2image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)
    description1 = models.TextField()
    rating = models.FloatField()
    runtime = models.DurationField(help_text="Format: HH:MM:SS")
    release_date = models.DateField()
    description2 = models.TextField()  # Changed to TextField assuming it's text
    actorimage1 = models.ImageField(upload_to='image')
    actorimage2 = models.ImageField(upload_to='image')
    actressimage3 = models.ImageField(upload_to='image')
    actorname1 = models.CharField(max_length=256)
    actorname2 = models.CharField(max_length=256)
    actressname3 = models.CharField(max_length=256)
    actor1bio = models.CharField(max_length=256)
    actor2bio = models.CharField(max_length=256)
    actress3bio = models.CharField(max_length=256)
    card_image = models.ImageField(upload_to='image')
    card_name = models.CharField(max_length=100)
    watch_trailer = models.FileField(upload_to='videos',default=True)
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')




class Watchlist(models.Model):
    MOVIE_CATEGORIES = (
        ('hollywood', 'Hollywood'),
        ('tamilMovies', 'Tamil Movies'),
        ('webseries', 'Web Series'),
        ('anime', 'Anime'),
        ('korean', 'Korean Movies'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=MOVIE_CATEGORIES)
    added_at = models.DateTimeField(auto_now_add=True)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=20)  # eg... Monthly, Yearly
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)