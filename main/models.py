from django.db import models
from django.utils.text import slugify

class AboutUs(models.Model):
  description = models.TextField()
  restaurant_name = models.CharField(max_length=255)
  establishment_year = models.IntegerField(blank=True, null=True)
  banner_img = models.FileField(upload_to='media/')
  number_chefs = models.IntegerField()


class MenuCuisine(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField(blank=True, null=True)

  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    if not self.slug:  # Generate slug only if it's not already set
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)


  
class MenuItem(models.Model):
  name = models.CharField(max_length=255)
  cuisine = models.ForeignKey(MenuCuisine, on_delete=models.CASCADE) 
  description = models.TextField()
  image = models.ImageField(upload_to='media/')
  price = models.DecimalField(max_digits=5, decimal_places=2)
  slug = models.SlugField(blank=True, null=True)

  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    if not self.slug:  # Generate slug only if it's not already set
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)





  
class TeamMember(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=100)
  experience = models.IntegerField()
  image = models.ImageField(upload_to='media/')
  slug = models.SlugField(blank=True, null=True)
  facebook_url = models.URLField(blank=True)  
  instagram_url = models.URLField(blank=True)  

  def save(self, *args, **kwargs):
    if not self.slug:  # Generate slug only if it's not already set
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name
  
