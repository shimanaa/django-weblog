# Generated by Django 3.1.6 on 2021-02-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(default='background.jpg', upload_to=''),
        ),
    ]
