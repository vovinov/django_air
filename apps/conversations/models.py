from django.db import models
from common import models as common_models


class Conversation(common_models.TimeStampModel):
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return self.created


class Message(common_models.TimeStampModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
