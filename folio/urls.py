from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^project/', views.project, name='project'),
    url(r'^viewproject/', views.viewproject, name='viewproject'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^skills/', views.skills, name='skills'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
