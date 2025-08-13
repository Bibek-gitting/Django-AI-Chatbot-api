from django.shortcuts import render
from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer, loginSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

@api_view(['POST'])
def userRegister(request):
    try:
        data=request.data
        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status': 'error',
                'message': serializer.errors
            },status=400)
        username = serializer.validated_data['username'].strip().lower()
        password = serializer.validated_data['password'].strip()
        if username == User.objects.filter(username=username).exists():
            return Response({
                'status': 'error',
                'message': 'username already exists.',
            },status=400)
        if username == 'admin':
            return Response({
                'status': 'error',
                'message': 'Username can not be named as admin',
            },status=400)
        if len(password) <8:
            return Response({
                'status':'error',
                'message': 'Password must be at least 8 characters long.'
            },status=400)
        user_obj=User.objects.create_user(username=username, password=password)
        saved_serializer = UserSerializer(user_obj)
        return Response({
            'status': 'success',
            'message': 'User registered successfully.',
            'data': saved_serializer.data
        },status=201)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        },status=400)
    
@api_view(['POST'])
def userLogin(request):
    try:
        data = request.data
        serializer = loginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status': 'error,',
                'message': serializer.errors
            },status=400)
        username = serializer.validated_data['username'].strip().lower()
        password = serializer.validated_data['password'].strip()
        user_obj = authenticate(username = username, password = password)
        if user_obj:
            token, _ = Token.objects.get_or_create(user=user_obj)
            return Response({
                'status': 'success',
                'message': 'User login successfull.',
                'data': {
                    'username': user_obj.username,
                    'auth_token': str(token)
                }
            }, status=202)
        return Response({
            'status': 'error',
            'message': 'Invalid username or password.'
        }, status=401)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        },status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    try:
        serializer = ChatSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': 'error,',
                'message': serializer.errors
            },status=400)
        user_message=serializer.validated_data['message']
        user = request.user
        if user.tokens > 100:
            user.tokens -=100
            user.save()
        else:
            return Response({
                'status': 'error',
                'message': 'Insuffecient tokens'
            }, status=400)
        OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        )
        completion = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "user", "content": str(user_message)}
            ],
            max_tokens=500
        )
        ai_message=completion.choices[0].message.content
        chat = Chat.objects.create(
            user=user,
            message=user_message,
            response=ai_message
        )
        chat.save()
        output = {
            'username': str(user.username),
            'response': str(ai_message)
        }
        return Response({
            'status': 'success',
            'data': output
        }, status=200)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        },status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userTokenBalance(request):
    try:
        output = {
            'username': request.user.username,
            'tokens': request.user.tokens
        }
        return Response({
            'status': 'success',
            'data': output
        }, status=200)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        },status=400)
