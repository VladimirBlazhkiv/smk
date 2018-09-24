from django.contrib import admin

# Register your models here.
from .models import Author, Ship_model

#admin.site.register(Author)
#admin.site.register(Ship_model)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('first_name','last_name',  'otch_name', 'date_of_birth', 'gorod', 'sport_razyad', 'sudeyskaja_kategorija' , 'fn_sportsmena' )
   fields = ['first_name', 'last_name', 'otch_name', 'fn_sportsmena', 'date_of_birth', 'photo_author' ,'gorod', 'sport_razyad', 'sudeyskaja_kategorija', 'author_hobby', 'author_site']

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
# Register the Admin classes for Book using the decorator

@admin.register(Ship_model)
class Ship_modelAdmin(admin.ModelAdmin):
    list_display = ('ship_name', 'author', 'ship_class_naviga')
#----------------------------------------------------------------------------------------------------------
