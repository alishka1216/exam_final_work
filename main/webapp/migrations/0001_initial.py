# Generated by Django 3.2 on 2021-05-01 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=3000, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Картинка продукта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='webapp.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'product',
                'permissions': [('add_users', 'добавление пользователя')],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Рейтинг')),
                ('description_review', models.TextField(blank=True, max_length=3000, null=True)),
                ('date', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
                ('boolen_field', models.BooleanField(default=False)),
                ('author', models.ManyToManyField(related_name='products', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='webapp.product')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'db_table': 'reviews',
            },
        ),
    ]
