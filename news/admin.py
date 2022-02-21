from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.sites import site
from .models import CCUAlumni, LatestNew,Event, Picture, Testimony, Member
from  django.contrib.auth.models import Group

admin.site.unregister(Group)

@register(LatestNew)
class NewsAdmin(admin.ModelAdmin):
  list_display = ('title','upload_date','image_tag')
  list_filter = ('title','upload_date')
  prepopulated_fields = {'slug':('title',)}
  search_fields=('title',)

@register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display = ('title','image_tag')
  list_filter = ('title','event_date')
  search_fields = ('title',)

@register(Picture)
class PictureAdmin(admin.ModelAdmin):
  list_display = ('image_name','image_tag')
  list_filter = ('image_name',)
  search_fields = ('image_name',)


@register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
  list_display = ('student_name','department','image_tag')
  list_filter = ('student_name','department')
  search_fields = ('student_name','department')

@register(CCUAlumni)
class CcuAdmin(admin.ModelAdmin):
  list_display = ('title',)

@register(Member)
class MembersAdmin(admin.ModelAdmin):
  list_display = ('member_name','member_position','image_tag')
  list_filter = ('member_name','member_position')
  search_fields = ('member_name','member_position')