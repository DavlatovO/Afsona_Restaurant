from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Model for creating Users"""
    avatar = models.ImageField(upload_to='avatar/',default='avatar/default.png')
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.username}'
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    
    def save(self, *args, **kwargs):
        if not self.avatar:
            self.avatar = 'default.png'
        super().save(*args, **kwargs)
    

class AboutUs(models.Model):
  """Model for a Banner and news"""

  description = models.TextField()
  restaurant_name = models.CharField(max_length=255)
  establishment_year = models.IntegerField(blank=True, null=True)
  banner_img = models.FileField(upload_to='media/')
  number_chefs = models.IntegerField()


class MenuCuisine(models.Model):
  """Model for Cuisines"""
  name = models.CharField(max_length=255)
  slug = models.SlugField(blank=True, null=True)

  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    if not self.slug: 
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)


  
class MenuItem(models.Model):
  """Model for Menu """

  name = models.CharField(max_length=255)
  cuisine = models.ForeignKey(MenuCuisine, on_delete=models.CASCADE) 
  description = models.TextField()
  image = models.ImageField(upload_to='media/')
  price = models.DecimalField(max_digits=5, decimal_places=2)
  slug = models.SlugField(blank=True, null=True)

  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    if not self.slug: 
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)





  
class TeamMember(models.Model):
  """Model for adding members"""
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=100)
  experience = models.IntegerField()
  image = models.ImageField(upload_to='media/')
  slug = models.SlugField(blank=True, null=True)
  facebook_url = models.URLField(blank=True)  
  instagram_url = models.URLField(blank=True)  

  def save(self, *args, **kwargs):
    if not self.slug:  
        self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name
  
class Contact(models.Model):
    """Model for Contacting"""
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class ClientReview(models.Model):
    """Model for a Clients' Reviews"""

    name = models.CharField(max_length=255)
    body = models.TextField()
    profession = models.CharField(max_length=255)
    picture = models.FileField(upload_to='media/')

    def __str__(self):
        return f"{self.name} - {self.profession}"


class Reservation(models.Model):
    """Model for a booking"""

    name = models.CharField(max_length=255)
    email = models.EmailField()
    booking_date = (models.DateField)
    booking_time = (models.TimeField)
    num_people = models.PositiveIntegerField()
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date_time} ({self.num_people} people)"
    
class Subscriptions(models.Model):
   email = models.EmailField()    


class Service(models.Model):
    """Model for a service offered."""

    name = models.CharField(max_length=255)
    description = models.TextField()  # For a longer description
    icon = models.ImageField(upload_to='service_icons/')  # Assuming you have a 'service_icons' folder for icons

    def __str__(self):
        return self.name   



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.dish.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

