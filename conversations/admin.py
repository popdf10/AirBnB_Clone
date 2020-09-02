from django.contrib import admin
from . import models


@admin.register(models.Message)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    pass


@admin.register(models.Conversation)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    pass
