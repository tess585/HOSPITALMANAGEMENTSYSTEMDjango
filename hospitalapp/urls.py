from django.contrib import admin
from django.urls import path
from hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner',),
    path('about/', views.about, name='about',),
    path('blog/', views.inner, name='blog',),
]
