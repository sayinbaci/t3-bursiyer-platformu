# Generated by Django 5.2.3 on 2025-06-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='content_tr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='title_tr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newscategory',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='newscategory',
            name='name_tr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
