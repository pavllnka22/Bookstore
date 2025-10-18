from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email

CustomUser = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_check = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_check']

    def validate_email(self, value):

        validate_email(value)
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email вже зареєстрований.")
        return value

    def validate(self, data):

        password1 = data.get('password')
        password2 = data.get('password_check')

        if password1 != password2:
            raise serializers.ValidationError({"password2": "Паролі не збігаються."})

        if len(password1) < 8:
            raise serializers.ValidationError({"password1": "Пароль має містити щонайменше 8 символів."})

        if not any(char.isdigit() for char in password1):
            raise serializers.ValidationError({"password1": "Пароль має містити принаймні одну цифру."})

        return data

    def create(self, validated_data):

        validated_data.pop('password_check')
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
