from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone
# Create your models here.

now = timezone.now()

class Counter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.users
    
class VisitorCount(models.Model):
    count = models.PositiveIntegerField(default=0)

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    anonymous_uuid = models.UUIDField(null=True, blank=True, unique=True)
    
class Like(models.Model):
    ip_address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Comments(models.Model):
    fname = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    comment = models.CharField(max_length=250)
    date = models.DateField(default=now, verbose_name='date commented')
    
    def __str__(self):
        return self.fname
    class Meta:
        # Override the verbose_name_plural to remove the extra 's'
        verbose_name_plural = "Comments"
        
        
class Products(models.Model):
    pname = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    downloads = models.IntegerField(default=0)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    file = models.FileField(upload_to='files/')
    
    django = models.BooleanField(default=False)
    php = models.BooleanField(default=False)
    tailwind = models.BooleanField(default=False)
    bootstrap = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    js = models.BooleanField(default=False)
    
    def __str__(self):
        return self.pname
    
    class Meta:
        # Override the verbose_name_plural to remove the extra 's'
        verbose_name_plural = "Product"
        