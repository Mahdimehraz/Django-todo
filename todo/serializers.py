from rest_framework import serializers
from todo.models import ToDo , Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields =['id','title','description']

class ToDoSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model= ToDo
        fields = ['id' , 'title','completed', 'created_at', 'updated_at','category']

    #for validating category is yours
    def validate_category(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError("You cannot assign a ToDo to a category that doesn't belong to you.")
        return value
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user