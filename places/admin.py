from django.contrib import admin

from places.models import Place
from places.models import Comment


class PlaceAdmin(admin.ModelAdmin):
    display_fields = ["title","description","route"]

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["place", "author", "created"]

admin.site.register(Place, PlaceAdmin)
admin.site.register(Comment, CommentAdmin)
