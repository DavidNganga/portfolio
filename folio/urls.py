from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^project/', views.project, name='project'),
    url(r'^viewproject/', views.viewproject, name='viewproject'),


]
