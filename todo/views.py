from rest_framework import viewsets,permissions,status
from rest_framework.views  import APIView
from rest_framework.response import Response
from todo.models import ToDo , Category
from todo.serializers import ToDoSerializer,CategorySerializer,UserRegistrationSerializer
from todo.permissions import IsOwner

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    permission_classes=[permissions.IsAuthenticated,IsOwner]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user.id)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    permission_classes=[permissions.IsAuthenticated,IsOwner]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user.id)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
