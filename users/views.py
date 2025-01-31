import random
import uuid

from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device


class RegisterView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)
        # user, created = User.objects.get_or_create(phone_number=phone_number)


        device = Device.objects.create(user=user)

        code = random.randint(1000, 9999)
        cache.set(str(phone_number), code, 2*60)
        # send code (sms or email)

        return Response({'message': 'Code sent'}, status=status.HTTP_200_OK)


class GetTokenView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))
        if cached_code != code:
            return Response({'message': 'Invalid code'}, status=status.HTTP_403_FORBIDDEN)

        token = str(uuid.uuid4())
        return Response({'token': token}, status=status.HTTP_200_OK)