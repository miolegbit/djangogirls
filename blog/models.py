from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # computed non-storable field
    text_short = ""

    # это не работает
    # def __init__(self, *args, **kwargs):
    #     #self.text_short = self.text_clip(self.text)
    #     # calling base class constr does not work
    #     super().__init__(self, args, kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def text_clip(self, text:str, size: int = 100):
        l = text.length
        if l > size: l = size
        return text[0:l]

    