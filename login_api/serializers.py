from datetime import date
from django.urls.conf import path
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

     #makes username field unique
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message="please try different username",
                                    )]
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        password = data['password']
        password2 = data['password2']

        # check if entered password are same

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'passwords doesnt match. '})
        
        # check if password length is six or more character        
        elif len(password) < 6:
            raise serializers.ValidationError(
                {'password': 'passwords value should be six or more characters. '})

        return data
        

 # override default save method to create new account
    def save(self):
    
        account = User(
            username = self.validated_data['username']
        
        )
        account.set_password(self.validated_data['password'])

        account.save()
        return account
