from rest_framework import serializers

from todos.models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = TodoSerializerfields = ('url', 'id', 'created', 'name', 'user')
		extra_kwargs = {
			'url': {
				'view': 'todos:todo-detail',
			}
		}
