from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('semantic_segmentation/', views.semseg_add_image, name='semantic_segmentation'),
    path('remove_background/', views.remback_add_image, name='remove_background'),
    path('grayscale_background/', views.graysc_add_image, name='grayscale_background'),
    path('blur_background/', views.blur_add_image, name='blur_background'),
]
