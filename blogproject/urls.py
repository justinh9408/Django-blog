from django.conf.urls import url
from bloger import views
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(\d+)?$', views.indexpage),
    url(r'artlist/', views.artlist),
    url(r'artid=(\d+)/',views.articlepage),
    url(r'taglist/',views.taglist),
]