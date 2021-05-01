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
    product = models.ForeignKey('webapp.Product', related_name="product_reviews", on_delete=models.CASCADE)
    description_review = models.TextField(max_length=3000, null=True, blank=True, verbose_name='description')
    date = models.DateField(null=True, blank=False)
    date_end = models.DateField(null=True, blank=True)
    author = models.ManyToManyField(
        get_user_model(),
        related_name='products'
    )
    boolen_field = models.BooleanField(default=False)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Product(BaseModel):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=True)
    category = models.ForeignKey('webapp.Category', related_name="products", on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars',
        null=True,
        blank=True,
        verbose_name='Картинка продукта'
    )
