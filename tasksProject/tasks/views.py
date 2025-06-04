from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from tasksProject.tasks.serializers import (
    UserSerializer,
    TaskSerializer,
    TaskUserSerializer,
    TaskUserListSerializer,
)
from tasksProject.tasks.models import Task, Task_User
from rest_framework.response import Response


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

    def get_serializer_class(self):
        if self.action == "list":
            return TaskUserListSerializer
        return TaskUserSerializer

    def list(self, request):
        tasks = Task_User.objects.all()
        userID = self.request.query_params.get("assignedTo")
        if userID != None:
            user = User.objects.filter(id=userID).first()
            tasks = tasks.filter(user=user)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
