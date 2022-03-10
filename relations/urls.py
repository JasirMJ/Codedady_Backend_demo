from django.urls import path

from relations import views

urlpatterns = [
    path('',views.ProductSAPI.as_view()),
    path('tags/',views.TagsAPI.as_view()),
    path('variant/',views.ProductVariantAPI.as_view()),
    # path('asd/',views.ProductSAPI.as_view()),
]