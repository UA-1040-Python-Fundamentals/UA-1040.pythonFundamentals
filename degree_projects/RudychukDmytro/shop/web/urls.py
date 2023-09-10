from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('action/', views.action, name='action'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),

]
