from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            # "password",
            "date_joined",
            "groups",
            "user_permissions",
            "last_login",
        ]

    def validate(self, attrs):
        # ? Dogrulama Fonksiyonu
        from django.contrib.auth.password_validation import validate_password
        from django.contrib.auth.hashers import make_password  # ? Şifreleme Fonksiyonu

        password = attrs["password"]  # ? Password al.
        validate_password(password)  # ? Validation'dan geçir
        # ? Password şifrele ve güncelle
        attrs.update({"password": make_password(password)})

        return super().validate(attrs)  # ? Orjinal metodu çalıştır
