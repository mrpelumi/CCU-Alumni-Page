from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


class LatestNew(models.Model):
  title = models.CharField(max_length=250)
  newsletter = models.TextField()
  news_img = models.ImageField(upload_to='news_images')
  upload_date = models.DateField(default=date.today)
  slug = models.SlugField(unique=True)

  def image_tag(self):
    return mark_safe(f'<img src="/../../media/{self.news_img}" width="50" height="50" />') 
  image_tag.allow_tags = True

  class Meta:
    ordering = ('-upload_date',)

  def __str__(self):
      return self.title

  def get_absolute_url(self):
    return reverse('news_article', kwargs={'slug': self.slug})

class CCUAlumni(models.Model):
  title = models.CharField(max_length=250,default="CCU Alumni")
  body = models.TextField()

  def __str__(self):
      return self.title
  

class Event(models.Model):
  title = models.CharField(max_length=250)
  event_img = models.ImageField(upload_to='event_image',default='image_1.jpg')
  event_date = models.DateField(default=date.today)
  start_time = models.TimeField(default=timezone.now)
  end_time = models.TimeField(default=timezone.now)
  speaker = models.CharField(max_length=200, default='',blank=True,null=True)
  Venue = models.CharField(max_length=250, default='',blank=True,null=True)

  def image_tag(self):
    return mark_safe(f'<img src="/../../media/{self.event_img}" width="50" height="50" />')

  image_tag.allow_tags = True

  class Meta:
    ordering = ('-event_date',)

  def __str__(self):
      return self.title


class Picture(models.Model):
  image = models.ImageField(upload_to='ccu_gallery')
  image_name = models.CharField(max_length=150)
  date_added = models.DateField(default=datetime.today)

  def image_tag(self):
    return mark_safe(f'<img src="/../../media/{self.image}" width="50" height="50" />')

  image_tag.allow_tags = True

  def __str__(self):
      return self.image_name

class Testimony(models.Model):
  student_name = models.CharField(max_length=250)
  student_img = models.ImageField(upload_to='student_images')
  body = models.TextField(max_length=250)
  department = models.CharField(max_length=250)

  def image_tag(self):
    return mark_safe(f'<img src="/../../media/{self.student_img}" width="50" height="50" />')

  image_tag.allow_tags = True

  def __str__(self):
      return self.student_name


class Member(models.Model):
  member_name = models.CharField(max_length=250)
  member_img = models.ImageField(upload_to="member_images")
  member_position = models.CharField(max_length=200)
  twitter_url = models.CharField(max_length = 200,null=True,blank=True)
  facebook_url = models.CharField(max_length=250,null=True,blank=True)
  instagram_url = models.CharField(max_length=200,null=True,blank=True)

  def image_tag(self):
    return mark_safe(f'<img src="/../../media/{self.member_img}" width="50" height="50" />')

  image_tag.allow_tags = True


  def __str__(self):
      return self.member_name