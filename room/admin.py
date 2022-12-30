from django.contrib import admin
from .models import Chat,Room,MCQ,Option,Quiz,Score

# Register your models here.
admin.site.register([Chat,Room,MCQ,Option,Quiz,Score])