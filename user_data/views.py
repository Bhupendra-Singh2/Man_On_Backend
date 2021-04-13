from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserTable
from .permissions import IsOwnerOrReadOnly
from .serializers import UserTableSerializer, AuthTokenSerializer
from rest_framework import status
from rest_framework import generics


# Create your views here.
class RegisterAPI(APIView):
    """API for sign by the user."""
    def post(self, request):
        print("hii")
        serializer = UserTableSerializer(data=request.data)
        # print(serializer)
        UserTable.objects.all().first()
        if serializer.is_valid():
            new_key = serializer.save()
            add_value = UserTable.objects.get(id=new_key.pk)
            add_value.user_id = add_value.id + 1000000
            add_value.save()
            return Response(UserTableSerializer(add_value).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(TokenObtainPairView):
    """Simple JWT login Authentiction view."""
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer


class ProfileUpdate(generics.RetrieveUpdateAPIView):
    """API to update user profile."""
    queryset = UserTable.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = UserTableSerializer
