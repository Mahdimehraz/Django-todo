from rest_framework import viewsets,permissions
from todo.models import ToDo
from todo.serializers import ToDoSerializer
from todo.permissions import IsOwner

class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    permission_classes=[permissions.IsAuthenticated,IsOwner]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user.id)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
