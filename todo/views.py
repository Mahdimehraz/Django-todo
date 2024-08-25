from rest_framework import viewsets,permissions
from todo.models import ToDo , Category
from todo.serializers import ToDoSerializer,CategorySerializer
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
