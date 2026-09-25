from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
from .resources import RegisterResource
# Register your models here.

@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
    resource_classes = [RegisterResource]
    list_display = ('id', 'fio', 'phone', 'email', 'category', 'city', 'place', 'format', 'message', 'policy')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'policy')