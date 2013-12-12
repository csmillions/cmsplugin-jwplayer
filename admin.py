from django.contrib import admin
from .models import VideoSource


class VideoSourceInline(admin.TabularInline):
	model = VideoSource
	extra = 1