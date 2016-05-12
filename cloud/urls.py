from django.conf.urls import url, include
from src import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^delete/(?P<file_id>[\d ]+)/$', views.delete_file, name='delete_file'),
    url(r'^download_file/(?P<file_id>[\d ]+)/$', views.download_file, name='download_file'),
    url(r'^accounts/', include('registration.backends.default.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

