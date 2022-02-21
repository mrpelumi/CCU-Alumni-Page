from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from .models import Event,LatestNew,CCUAlumni, Member, Picture, Testimony

# Create your views here.


class HomeView(TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = LatestNew.objects.order_by('-id')
        context['events_list'] = Event.objects.order_by('-id')
        context['ccualumni_body'] = CCUAlumni.objects.get(id=1)
        context['testimonies'] = Testimony.objects.all()
        context['pictures'] = Picture.objects.all()
        return context
    

class EventListView(ListView):
    model = Event
    template_name = "news/events.html"
    context_object_name = 'events'
    paginate_by = 3
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-event_date')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = LatestNew.objects.order_by('-id')
        return context

class NewsArticleDetailView(DetailView):
    model = LatestNew
    template_name = "news/news-item.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = LatestNew.objects.order_by('-id')
        return context


class About_UsView(TemplateView):
    template_name = "news/about.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ccu_alumni'] = CCUAlumni.objects.get(id=1)
        context['news_list'] = LatestNew.objects.order_by('-id')
        return context

class MemberBenefitView(TemplateView):
    template_name = "news/member_benefit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = LatestNew.objects.order_by('-id')
        return context



class NewsListView(ListView):
    model = LatestNew
    template_name = "news/newslist.html"
    context_object_name = 'news_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id')
        return queryset


class PictureListView(ListView):
    model = Picture
    template_name = "news/gallery.html"
    context_object_name = 'pictures'
    paginate_by = 3
    ordering = ['image_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = LatestNew.objects.order_by('-id')
        return context


class MemberListView(ListView):
    model = Member
    template_name = "news/members.html"
    context_object_name = 'members_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = LatestNew.objects.order_by('-id')
        return context



class ContactView(TemplateView):
    template_name = "news/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = LatestNew.objects.order_by('-id')
        return context