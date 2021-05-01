from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from webapp.views import (
    IndexView,
    ReviewView,
    ReviewUpdateView,
    ReviewDeleteView,
    CreateReviewView,
    ProductList,
    ProductView,
    ProductCreate,
    ProductUpdate,
    ProductDelete,
    UserUpdateView
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('accounts/', include('django.contrib.auth.urls')),
    path('tracker/', IndexView.as_view(), name='review-list'),
    path('tracker/add/<int:pk>/', CreateReviewView.as_view(), name='review-add'),
    path('tracker/<int:pk>/', ReviewView.as_view(), name='review-view'),
    path('tracker/update/<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('tracker/delete/<int:pk>/', ReviewDeleteView.as_view(), name='review-delete'),
    path('', ProductList.as_view(), name='product-list'),
    path('project/<int:pk>/', ProductView.as_view(), name='product-view'),
    path('project/add/', ProductCreate.as_view(), name='product-add'),
    path('project/update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('project/delete/<int:pk>/', ProductDelete.as_view(), name='product-delete'),
    path('user/add/<int:pk>/', UserUpdateView.as_view(), name='user-add'),
    path('accounts/', include('accounts.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
