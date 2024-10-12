from django.contrib import admin
from CineMaxapp.models import hollywood, tamilMovies, webseries, anime, korean

class HollywoodAdmin(admin.ModelAdmin):
    list_display = [
        'poster1image', 'poster2image', 'title', 'description1', 'rating', 'runtime', 'release_date', 
        'description2', 'actorimage1', 'actorimage2', 'actressimage3', 'actorname1', 'actorname2', 
        'actressname3', 'actor1bio', 'actor2bio', 'actress3bio', 'card_image', 'card_name','watch_trailer','cat','is_active'
    ]
    list_filter= ['cat','is_active']

class TamilMoviesAdmin(admin.ModelAdmin):
    list_display = [
        'poster1image', 'poster2image', 'title', 'description1', 'rating', 'runtime', 'release_date', 
        'description2', 'actorimage1', 'actorimage2', 'actressimage3', 'actorname1', 'actorname2', 
        'actressname3', 'actor1bio', 'actor2bio', 'actress3bio', 'card_image', 'card_name','watch_trailer','cat','is_active'
    ]
    list_filter= ['cat','is_active']

class WebseriesAdmin(admin.ModelAdmin):
    list_display = [
        'poster1image', 'poster2image', 'title', 'description1', 'rating', 'runtime', 'release_date', 
        'description2', 'actorimage1', 'actorimage2', 'actressimage3', 'actorname1', 'actorname2', 
        'actressname3', 'actor1bio', 'actor2bio', 'actress3bio', 'card_image', 'card_name','watch_trailer','cat','is_active'
    ]
    list_filter= ['cat','is_active']

class AnimeAdmin(admin.ModelAdmin):
    list_display = [
        'poster1image', 'poster2image', 'title', 'description1', 'rating', 'runtime', 'release_date', 
        'description2', 'actorimage1', 'actorimage2', 'actressimage3', 'actorname1', 'actorname2', 
        'actressname3', 'actor1bio', 'actor2bio', 'actress3bio', 'card_image', 'card_name','watch_trailer','cat','is_active'
    ]
    list_filter= ['cat','is_active']

class KoreanAdmin(admin.ModelAdmin):
    list_display = [
        'poster1image', 'poster2image', 'title', 'description1', 'rating', 'runtime', 'release_date', 
        'description2', 'actorimage1', 'actorimage2', 'actressimage3', 'actorname1', 'actorname2', 
        'actressname3', 'actor1bio', 'actor2bio', 'actress3bio', 'card_image', 'card_name','watch_trailer','cat','is_active'
    ]
    list_filter= ['cat','is_active']

admin.site.register(hollywood, HollywoodAdmin)
admin.site.register(tamilMovies, TamilMoviesAdmin)
admin.site.register(webseries, WebseriesAdmin)
admin.site.register(anime, AnimeAdmin)
admin.site.register(korean, KoreanAdmin)
