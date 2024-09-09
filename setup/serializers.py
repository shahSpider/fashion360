from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, clean_data):
        user = User.objects.create(
            email = clean_data['email'],
            username = clean_data['username']
        )
        user.set_password(clean_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    class Meta:
        username = serializers.CharField()
        password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(username=clean_data['username'], password=clean_data['password'])
        if not user:
            raise ValidationError('User not found')
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


"""
{
    "email": "test102@fashion360.com",
    "username": "test102",
    "password": "testing102"
}

"""