from django.urls import path

from .views import (
  ContactView, HomeView, EventListView, MemberListView, 
  NewsArticleDetailView,About_UsView, NewsListView, PictureListView,MemberBenefitView
)

urlpatterns = [
  path('',HomeView.as_view(),name='home'),
  path('events/',EventListView.as_view(),name='events'),
  path('news/<slug:slug>/',NewsArticleDetailView.as_view(),name='news_article'),
  path('news-list/',NewsListView.as_view(),name='news_list_page'),
  path('about-us/',About_UsView.as_view(),name='about_us'),
  path('members/',MemberListView.as_view(),name='member_list_page'),
  path('members-benefit/',MemberBenefitView.as_view(),name='member_benefit'),
  path('pictures/',PictureListView.as_view(),name='pictures'),
]
