from django.contrib import admin
from messenger import models


# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'surname', 'first_name')


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipient', 'dispatch_date')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_subject', 'author', 'created_at')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author',)


@admin.register(models.Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'status')
