from models import *
from rest_framework import serializers

class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        user = serializers.Field(source='user.username')        
        read_only_fields = ('user',)        
        fields = ('id', 'name', 'description', 'user')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        user = serializers.Field(source='user.username')
        read_only_fields = ('user',)
        fields = ('id', 'text', 'user', 'bar')
