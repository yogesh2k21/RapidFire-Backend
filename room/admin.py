from django.contrib import admin
from .models import Chat,Group

# Register your models here.
admin.site.register([Chat,Group])