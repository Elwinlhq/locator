from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from allauth.socialaccount.models import SocialToken
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Auth based on facebook token and existing socialaccount_socialaccount entity
class FacebookTokenAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        logger.debug('Attempting facebook auth -----')
        
        #for header in request.META:
        #    if header == 'HTTP_X_AUTH_FACEBOOK_TOKEN' or header == 'HTTP_X_AUTH_USERNAME':
        #        logger.debug(header + ":" + request.META[header].__str__())
        
        token = request.META.get('HTTP_X_AUTH_FACEBOOK_TOKEN')
        username = request.META.get('HTTP_X_AUTH_USERNAME')
        
        # Next auth method will be dispatched 
        # TODO: If no other method is provided it must die!
        if not token or not username:
            logger.debug('Auth info not provided, skipping')
            return None

        logger.debug('Auth attempt with [' + username + ':' + token + ']')

        # find the user by the facebook token
        try:
            user = User.objects.get(username=username)
            tokens = SocialToken.objects.filter(account__user=user, account__provider='facebook', token=token)
            
            if not tokens:
                logger.debug('Token not found!')
                raise AuthenticationFailed('Access denied')
                
        except User.DoesNotExist:
            logger.debug('User not found!')
            raise AuthenticationFailed('Access denied')

        return (user, None)
        
        
1.0
===
        
(*) Mas campos para el bar
 - ciudad
 - fecha de creacion y modificacion
 - fecha de validacion
 - el bar pertenece al creador
 - direccion
 - cp
 
(*) Lista de bares
- Filtrar por ciudad
- lista con nombre, descripcion, ciudad y foto
- swipe para paginar
- ordenar por valoraciones, nombre, ciudad

(*) Pagina del bar
- Foto, Nombre, Descripcion, Direccion
- Votos (tabla aparte)
- Lista de comentarios (paginada con scroll vertical)
- pie para comentar

(*) Registro de usuarios
- Al comentar o votar se requiere registro con facebook
- Ordenar
- Posibilidad de poner alias y avatar
- Indicadores de actividad (comentaron en tu bar, comentaron en un bar que comentaste)

(*) Admin
- bares pendientes de validacion
- validar bar
- modificar bar 
- borrar comentario
- banear comentario
- banear usuario

(*) Requisitos
- Apaisado/vertical
- Calidad de diseno













