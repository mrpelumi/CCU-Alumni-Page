from urllib import response
from django.test import TestCase
from news.views import (HomeView)
from django.urls import reverse
from news.models import (CCUAlumni,LatestNew,Event,Picture,Member)

class TestView(TestCase):

    def setUp(self):
        CCUAlumni.objects.create(title="First Trial",body="CCU Alumni is a great website")
        LatestNew.objects.create(title='News Article 1',newsletter="This is the latest news on the matter.",
                                news_img="../../../media/ccu_gallery/nysc_1.jpg",slug="news-article-1")
        Event.objects.create(title="Donation by Arthur Eze",event_img="../../media/event_image/course-1.jpg")
        Picture.objects.create(image="../../../media/ccu_gallery/nysc_2.jpg",image_name="Mona Lisa")
        Member.objects.create(member_name="Afam-Icham Chukwu",
                               member_img="../../../media/member_images/ume-joshua.jpg",
                               member_position="Vice Chancellor")

    def test_view_homeview(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        news_body = LatestNew.objects.first().newsletter
        self.assertTemplateUsed(response,'news/index.html')
        template = str(response.content)
        self.assertIn(news_body,template)
    
    def test_view_eventlist(self):
        response = self.client.get(reverse('events'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/events.html')
        event_image = Event.objects.first().event_img.url
        template = str(response.content)
        self.assertIn(event_image,template)

    def test_newsarticle_detail_view(self):
        response = self.client.get(reverse('news_article',args=['news-article-1']))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/news-item.html')
        news_body = LatestNew.objects.first().newsletter
        template = str(response.content)
        self.assertIn(news_body,template)

    def test_about_us_view(self):
        response = self.client.get(reverse('about_us'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/about.html')
        alumni_body = CCUAlumni.objects.first().body
        template = str(response.content)
        self.assertIn(alumni_body,template)

    def test_newsarticle_list_view(self):
        response = self.client.get(reverse('news_list_page'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/newslist.html')
        news_body = LatestNew.objects.first().newsletter
        template = str(response.content)
        self.assertIn(news_body,template)
    
    def test_picture_list_view(self):
        response = self.client.get(reverse('pictures'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/gallery.html')
        pic_text = Picture.objects.first().image_name
        template = str(response.content)
        self.assertIn(pic_text,template)
    
    def test_member_list_view(self):
        response = self.client.get(reverse('member_list_page'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'news/members.html')
        members = Member.objects.first().member_position
        template = str(response.content)
        self.assertIn(members,template)
