from django.db import models
import string, random


def generate_short_code():
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class ShortURL(models.Model):
    long_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=6, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.long_url} -> {self.short_code}"