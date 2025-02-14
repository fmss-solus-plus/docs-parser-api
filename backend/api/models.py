from django.db import models


# Create your models here.


class OpenAIRequest(models.Model):
    document_type = models.CharField(max_length=225)
    ai_model = models.CharField(max_length=50)
    prompt_tokens = models.IntegerField()
    completion_tokens = models.IntegerField()
    total_tokens = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
