from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Task_User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "id"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task_User
        fields = "__all__"


class TaskUserListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, obj: Task_User):
        return obj.user.username

    taskTitle = serializers.SerializerMethodField()

    def get_taskTitle(self, obj: Task_User):
        return obj.task.titulo

    class Meta:
        model = Task_User
        fields = ["user", "userName", "taskTitle", "hoursTaken"]
