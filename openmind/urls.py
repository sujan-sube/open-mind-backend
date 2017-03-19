"""openmind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from journal.views import JournalViewSet
from emotion.views import EmotionViewSet
from journal.views_social import GoogleLogin

router = routers.DefaultRouter()
router.register(r'journal', JournalViewSet)
router.register(r'emotion', EmotionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # browser login - can be disabled
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # api auth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google-login'),

    # admin pages
    url(r'^admin/', admin.site.urls)
]
