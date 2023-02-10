# Generated by Django 4.1.6 on 2023-02-10 16:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CNjokes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnjoke',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_jokes', to=settings.AUTH_USER_MODEL),
        ),
    ]