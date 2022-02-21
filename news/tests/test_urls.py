from urllib import response
from django.test import SimpleTestCase,TestCase
from django.urls import reverse,resolve
from news.views import (HomeView,EventListView,NewsArticleDetailView,NewsListView,
                        About_UsView,MemberListView,PictureListView)
from news.models import (CCUAlumni,LatestNew)

class TestUrls(TestCase):

    def setUp(self):
        CCUAlumni.objects.create(title="New Page",body="This is a page")
        LatestNew.objects.create(title="New Message",newsletter="This is a body of news",
                                slug='new-message',news_img="../../../media/news_images/arthur_eze_donation.jpg" )

    def test_home_url_is_resolved(self):
        url = reverse('home')
        response = self.client.get(url)
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class,HomeView)
        self.assertEqual(response.status_code,200)

    def test_event_url_is_resolve(self):
        url = reverse('events')
        view_class = resolve(url).func.view_class
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(view_class,EventListView)

    def test_news_detail_url_is_resolve(self):
        url = reverse('news_article',args=['new-message'])
        view_class = resolve(url).func.view_class
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(view_class,NewsArticleDetailView)
    
    def test_news_list_url_is_resolved(self):
        url = reverse('news_list_page')
        response = self.client.get(url)
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class,NewsListView)
        self.assertEqual(response.status_code,200)

    def test_about_us_url_is_resolved(self):
        url = reverse('about_us')
        response = self.client.get(url)
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class,About_UsView)
        self.assertEqual(response.status_code,200)

    def test_member_url_is_resolved(self):
        url = reverse('member_list_page')
        response = self.client.get(url)
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class,MemberListView)
        self.assertEqual(response.status_code,200)

    def test_picture_url_is_resolved(self):
        url = reverse('pictures')
        response = self.client.get(url)
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class,PictureListView)
        self.assertEqual(response.status_code,200)