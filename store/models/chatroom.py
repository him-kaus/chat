from django.db import models


class USER(models.Model):
    """The user is basically what is what is going to be presented in the chat ."""

    userName = models.CharField(max_length=50, default="anonymous")

    class Meta:
        """Meta definition for USER."""

        verbose_name = 'USER'
        verbose_name_plural = 'USERs'

    def __str__(self):
        """Unicode representation of USER."""
        pass


class CHAT_MESSAGE(models.Model):
    """chat Message"""

    messageText = models.CharField(max_length=512)
    author = models.CharField(max_length=25, default="Anonymous")

    class Meta:
        """Meta definition for chatMessage."""

        verbose_name = 'chatMessage'
        verbose_name_plural = 'chatMessages'

    def __str__(self):
        return self.messageText



