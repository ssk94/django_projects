from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username',read_only=True)

	class Meta:
		model = TaskModel
		fields = ('user','task_name','tasl_description','status','date')

class RegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	def create(self, validated_data):
		user = User.objects.create(
			username = validated_data['password']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model=User
		fields = ('username','password')


