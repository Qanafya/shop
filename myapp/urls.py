from django.contrib import admin
from django.urls import *
from . import views

urlpatterns = [
    path('about/', views.about),
    path('', views.account),
    path('account/', views.account),
    path('cart/', views.cart),
    path('home/', views.home),
    path('products/', views.product),
    path('support/', views.support),
    path('details/<int:id>/', views.details),
    path('comm/', views.comm),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('admins/<slug:post_slug>', views.admins),
    path('car/', views.cart_buy),
    path('dele/<int:id>', views.dele),
]