from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt

# Import my app
from geld.views import *
from geld.models import *

# Rest framework
from rest_framework import serializers
from rest_framework import routers

# Set default router
router = routers.DefaultRouter()

# register rest for bar/comment models
router.register(r'bar', BarViewSet)
router.register(r'comment', CommentViewSet)

# ADD ADMIN
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home page
    url(r'^$', HomeView.as_view(), name='home'),

    # Rest api view for signup/login with facebook token
    url(r'^facebook-signup/$', csrf_exempt(FacebookLoginOrSignup.as_view()), name='facebook-login-signup'),

    # Allauth account management
    (r'^accounts/', include('allauth.urls')),

    # ADD ADMIN url schema
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
