# Generated by Django 3.2 on 2021-05-01 10:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_alter_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ManyToManyField(related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]
