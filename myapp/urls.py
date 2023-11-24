from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login),
    path('register', views.register, name='register'),
    path('save_details', views.save_details,name='save_details'),
    path('meds', views.meds,name='meds'),
    path('search_meds', views.search_meds,name='search_meds'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('payment', views.payment, name='payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)