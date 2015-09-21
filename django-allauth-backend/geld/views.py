from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.template import RequestContext

from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from allauth.socialaccount.helpers import complete_social_login

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from geld.models import *
from geld.serializers import *
from geld.auth import EverybodyCanAuthentication

from django.core.context_processors import csrf

import logging
logger = logging.getLogger('geld')


# HTML HOME
class HomeView(TemplateView):
    def get(self, request):
        return render_to_response('geld/home.html', context_instance = RequestContext(request))


# Add a user to the system based on facebook token
class FacebookLoginOrSignup(APIView):   
    
    permission_classes = (AllowAny,)
    
    # this is a public api!!!
    authentication_classes = (EverybodyCanAuthentication,)
             
    def dispatch(self, *args, **kwargs):
        return super(FacebookLoginOrSignup, self).dispatch(*args, **kwargs)
    
    def post(self, request):        
        data = JSONParser().parse(request)
        access_token = data.get('access_token', '')    
        
        try:
            app = SocialApp.objects.get(provider="facebook")
            token = SocialToken(app=app, token=access_token)
                            
            # return SocialLogin(account)                    
            login = fb_complete_login(app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
        
            # add or update the user
            ret = complete_social_login(request, login)

            # if we get here we've succeeded
            return Response(status=200, data={
                'success': True,
                'username': request.user.username,
                'user_id': request.user.pk,
                'csrf_token': unicode(csrf(request)['csrf_token'])
            })
            
        except:
            
            # FIXME: Catch only what is needed
            #, HttpForbidden
            return Response(status=401 ,data={
                'success': False,
                'reason': "Bad Access Token",
            })


# BAR REST VIEWS
class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

    # assign the model to the user before saving
    def pre_save(self, obj):
        obj.user = self.request.user    


# COMMENT REST VIEWS
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    # assign the model to the user before saving
    def pre_save(self, obj):
        obj.user = self.request.user

