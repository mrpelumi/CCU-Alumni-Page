# Generated by Django 4.0.1 on 2022-01-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20211111_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='news_img',
            field=models.ImageField(default='image_1.jpg', upload_to='event_image'),
        ),
    ]
