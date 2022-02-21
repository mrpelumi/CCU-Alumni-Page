from tkinter import image_names
from django.test import TestCase
from news.models import (CCUAlumni,LatestNew,Event,Picture,Testimony,Member)
from model_bakery import baker

# Use the Faker or model_library to populate the models
class TestModels(TestCase):

    def setUp(self):
        '''Create Database for the models'''
        baker.make('LatestNew',_quantity=3,_create_files=True)
        CCUAlumni.objects.create(title='A new title',body="Well done")
        baker.make('Event',_quantity=2,_create_files=True)
        baker.make('Picture',_quantity=3,_create_files=True)
        baker.make('Testimony',_quantity=4,_create_files=True)
        baker.make('Member',_quantity=2,_create_files=True)
    
    def test_ccualumni_model_create(self):
        obj_num = CCUAlumni.objects.count()
        self.assertEqual(obj_num,1)
    
    def test_ccualumni_model_content(self):
        title = CCUAlumni.objects.first().title
        self.assertEqual(title,'A new title')
        self.assertNotEqual(title,'A New Title')
        string_title = CCUAlumni.objects.first().__str__()
        self.assertEqual(string_title,title)
    
    def test_latestnew_model_create(self):
        obj = LatestNew.objects.all().count()
        self.assertEquals(obj,3)
    
    def test_latestnew_model_content(self):
        LatestNew.objects.filter(id=1).update(title="A new Message")
        title = LatestNew.objects.first().title
        slug_value = LatestNew.objects.first().slug
        url_path = LatestNew.objects.first().get_absolute_url()
        img_url = LatestNew.objects.last().news_img.url
        created_path = "/news/" + slug_value + "/"
        self.assertNotEqual(slug_value,'')
        self.assertEqual(url_path,created_path)
        self.assertTrue(img_url != '')
        self.assertEqual(title,"A new Message")
        self.assertNotEqual(title,"A New message")
        test_string = LatestNew.objects.first().__str__()
        self.assertEqual(test_string,title)
    
    def test_event_model_create(self):
        event = Event.objects.all().count()
        self.assertEqual(event,2)

    def test_event_model_content(self):
        Event.objects.filter(id=1).update(title="Convocation Ceremony")
        Event.objects.filter(id=2).update(title="Matriculation Ceremony")
        event_img = Event.objects.first().event_img.url
        event_obj = Event.objects.all()
        title_list = [i.title for i in event_obj]
        title_1 = title_list[0]
        title_2 = title_list[1]
        self.assertTrue(event_img != '')
        self.assertTrue(title_1 != title_2)
        test_string = Event.objects.first().__str__()
        self.assertEqual(test_string,'Convocation Ceremony')

    def test_picture_model_created(self):
        obj = Picture.objects.all().count()
        self.assertEquals(obj,3)
    
    def test_picture_model_content(self):
        Picture.objects.filter(id=1).update(image_name="A Wonderful Image")
        img1 = Picture.objects.first().image_name
        img_path = Picture.objects.first().image.url
        self.assertTrue(img1 == 'A Wonderful Image')
        self.assertFalse(img1 == 'a wonderful image')
        self.assertTrue(img_path != '')
        test_string = Picture.objects.first().__str__()
        self.assertEqual(test_string,'A Wonderful Image')
    
    def test_testimony_model_created(self):
        obj = Testimony.objects.all().count()
        self.assertEquals(obj,4)
        
    def test_testimony_model_content(self):
        Testimony.objects.filter(id=1).update(student_name="Jane Doe")
        students_name = Testimony.objects.first().student_name
        img_path = Testimony.objects.first().student_img.url
        self.assertTrue(students_name == 'Jane Doe')
        self.assertFalse(students_name == 'jane doe')
        self.assertTrue(img_path != '')
        test_string = Testimony.objects.first().__str__()
        self.assertEqual(test_string,students_name)

    def test_member_model_created(self):
        obj = Member.objects.all().count()
        self.assertEquals(obj,2)
    
    def test_member_model_content_none(self):
        Member.objects.filter(id=1).update(member_name="Nwachukwu Odigbo")
        members_name = Member.objects.first().member_name
        img_path = Member.objects.first().member_img.url
        members_twitter = Member.objects.first().twitter_url
        members_instagram = Member.objects.first().instagram_url
        members_facebook = Member.objects.first().facebook_url
        self.assertFalse(members_twitter != None)
        self.assertFalse(members_instagram != None)
        self.assertFalse(members_facebook != None)
        self.assertTrue(members_name == 'Nwachukwu Odigbo')
        self.assertFalse(members_name == 'nwachukwu odigbo')
        self.assertTrue(img_path != '')
        test_string = Member.objects.first().__str__()
        self.assertEqual(test_string,members_name)

    def test_member_model_content_full(self):
        Member.objects.filter(id=1).update(member_name='Kola',member_img='../../../media/ccu_gallery/nysc_1.jpg',
                            member_position='Chancellor',twitter_url='twitter.com',
                            facebook_url='facebook.com',instagram_url='instagram.com')
        # members_twitter = Member.objects.filter(id=1).twitter_url
        members_twitter = Member.objects.get(id=1).twitter_url
        members_instagram = Member.objects.get(id=1).instagram_url
        members_facebook = Member.objects.get(id=1).facebook_url
        self.assertTrue(members_twitter != None)
        self.assertTrue(members_instagram != None)
        self.assertTrue(members_facebook != None)