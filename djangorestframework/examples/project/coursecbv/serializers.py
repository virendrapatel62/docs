from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CourseSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            return request.build_absolute_uri(obj.thumbnail.url)
        return None

    class Meta:
        model = Course
        fields = ['id', 'author', 'title', 'description', 'thumbnail']
