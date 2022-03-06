from django.db import models
from random import choice
from string import ascii_letters, digits

class Shortener(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  long_url = models.URLField(blank=False, null=False)
  short_url = models.CharField(max_length=15, unique=True, blank=False, null=False)

  def __str__(self):
    return f'{self.long_url} to {self.short_url}'

  def create_random_code(self):
    return ''.join(choice(ascii_letters + digits) for _ in range(15))

  def create_short_url(self):
    random_code = self.create_random_code()
    codeRandomIsUsed = Shortener.objects.filter(short_url=random_code).exists()
      
    if codeRandomIsUsed:
      return self.create_short_url()
    
    self.short_url = random_code
    
    return self.short_url

  def save(self, *args, **kwargs):
    if not self.short_url:
      self.create_short_url()
    
    super().save(*args, **kwargs)