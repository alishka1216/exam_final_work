# Generated by Django 3.2 on 2021-05-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description_review',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='desctiption'),
        ),
    ]
