from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Review(BaseModel):
    rating = models.DecimalField('Рейтинг', max_digits=5, decimal_places=2, default=0)
    product = models.ForeignKey('webapp.Product', related_name="review", on_delete=models.PROTECT)
    description_review = models.TextField(max_length=3000, null=True, blank=True)
    date = models.DateField(null=False, blank=False)
    date_end = models.DateField(null=True, blank=True)
    author = models.ManyToManyField(
        get_user_model(),
        related_name='reviews'
    )
    boolen_field = models.BooleanField(default=False)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Product(BaseModel):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=True)
    category = models.ForeignKey('webapp.Category', related_name="products", on_delete=models.PROTECT)
    avatar = models.ImageField(
        upload_to='avatars',
        null=True,
        blank=True,
        verbose_name='Картинка продукта'
    )

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('add_users', 'добавление пользователя')
        ]



