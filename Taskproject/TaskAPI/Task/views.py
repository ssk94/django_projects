from rest_framework import permissions,viewsets
from .models import TaskModel
from rest_framework.generics import CreateAPIView
from .serializers import TaskSerializer,RegistrationSerializer
from django.contrib.auth.models import User

# Create your views here.
class TaskView(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticated,)
	model = TaskModel
	serializer_class = TaskSerializer

	def get_queryset(self):
		queryset = self.model.objects.all()
		queryset = queryset.filter(user=self.request.user)
		return queryset

	def perform_create(self, serializer):
		return serializer.save(user=self.request.user)

class RegistrationView(CreateAPIView):
	model = User
	serializer_class = RegistrationSerializer
	permission_classes = (permissions.AllowAny,)

