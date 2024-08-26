from rest_framework import serializers
from todo.models import ToDo , Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields =['id','title','description']

class ToDoSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model= ToDo
        fields = ['id' , 'title','completed', 'created_at', 'updated_at','category']

    #for validating category owner
    def validate_category(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError("You cannot assign a ToDo to a category that doesn't belong to you.")
        return value
    