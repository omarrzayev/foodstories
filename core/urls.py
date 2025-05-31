from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('story/<int:id>/', story_detail,name='story_detail'),
    path('recipe/<int:id>/', recipe_detail,name='recipe_detail'),
    path('stories/', stories, name='stories'),
    path('recipes/', recipes, name='recipes'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]