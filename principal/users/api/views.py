from rest_framework.viewsets import ModelViewSet
from users.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from users.api.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response



class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]     

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def perform_update(self, serializer):
        password = self.request.data.get('password', None)

        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()
            
            
class UserView(APIView):          
    permission_classes = []  # Solo los administradores pueden acceder a esta vista  
    
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)