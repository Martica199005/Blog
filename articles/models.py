from django.db import models

# Create your models here.
class Articles(models.Model):
  title=models.CharField(max_length=100)
  slug=models.SlugField()
  body=models.TextField()
  date=models.DateTimeField(auto_now_add=True)
  thumb=models.ImageField(default='default.png',blank=True)
  #add in author

#function to see the title of each article in db
  def __str__(self):
    return self.title

  def snippets(self):
    return self.body[:50] + '...'








#makemigration
#migrate
#django ORM

