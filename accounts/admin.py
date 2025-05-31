from django.contrib import admin
from accounts.models import User
from django.contrib.auth.models import Group

admin.site.register(User)
admin.site.unregister(Group)

admin.site.site_header = "Food Stories Admin"
admin.site.index_title = "Welcome to Food Stories Admin Portal"