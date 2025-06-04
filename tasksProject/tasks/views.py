from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from tasksProject.tasks.serializers import (
    UserSerializer,
    TaskSerializer,
    TaskUserSerializer,
)
from tasksProject.tasks.models import Task, Task_User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class Tasks_UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be allocated to tasks
    """

    queryset = Task_User.objects.all()
    serializer_class = TaskUserSerializer
