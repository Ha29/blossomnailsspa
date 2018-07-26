from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('services/', views.services, name='services'),
	path('gallery/', views.gallery, name='gallery'),
]

handler404 = views.handler404
handler505 = views.handler505
handler500 = views.handler500