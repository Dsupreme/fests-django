from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

from polymer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)