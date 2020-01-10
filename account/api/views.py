from django.db.models import Q
from rest_framework import mixins, generics

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )



from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import *

from .serializers import *

from account.models import *

class WalletDetailAPIView(ListAPIView):
    serializer_class = WalletDetailSerializer
    permission_classes = [IsWalletUser ]

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Wallet.objects.filter(profile__user=self.request.user)
        return queryset_list

class TransactionListAPIView(ListAPIView):
    serializer_class = TransactionDetailSerializer
    permission_classes = [IsWalletUser ]

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Transaction.objects.filter(profile__user=self.request.user)
        return queryset_list

class HeartbeatAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Account Management is up and running'})



class ProfileView(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.ListAPIView
                    ):
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        return ProfileViewSerializer

    def get_queryset(self):
        queryset_list = Profile.objects.filter(user=self.request.user)
        if self.request.method == 'Get':
            queryset_list = Profile.objects.filter(user=self.request.user)
        elif self.request.method == 'PUT':
            pass
        return queryset_list

    def post(self,request,*args,**kwargs):
        print("post")
        print(request)
        return self.create(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)