from django.urls import path

from products import views

urlpatterns = [
   
    path('tags/',views.TagsAPI.as_view()),
    path('products/',views.ProductsAPI.as_view()),
    path('variant/',views.ProductVariantAPI.as_view()),
    
]