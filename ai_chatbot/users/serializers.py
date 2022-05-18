from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password  # 장고 패스워드 검증
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # 토큰 모델
from rest_framework.validators import UniqueValidator  # 이메일 중복 방지 검증


class RegisterSerializer(serializers.ModelSerializer):  # 시리얼라이저
    email = serializers.EmailField(  # 이메일 중복 검증
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(  # 비밀번호 검증
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)  # 비밀번호 재확인

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, data): # 1차, 2차 비밀번호 일치 검증
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "비밀번호가 일치하지 않습니다."}
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "회원 정보가 잘 못되었습니다."}
        )

