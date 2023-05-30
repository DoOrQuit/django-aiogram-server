from rest_framework import generics

from accounts.models import User
from accounts.serializers import UserSerializer


class ListCreateUserAPI(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    