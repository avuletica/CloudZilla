from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
