from django.contrib import admin
from core.models import *

admin.site.register([Story, Recipe, Category, Tag, Comment, Subscriber, Contact])
