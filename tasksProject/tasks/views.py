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
import logging
from django.http.response import Http404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        logger = logging.getLogger("retrieveUsers")
        try:
            user = self.get_object()
            serializer = self.get_serializer(user)
            return Response(data=serializer.data)
        except Http404:
            logger.error(f"Usuário ID {pk} não encontrado")
            return Response({"detail": f"Usuário {2} não encontrado"})


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request):
        logger = logging.getLogger("createTasks")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Task created succesfully")
            return Response(serializer.data)
        return Response(serializer.errors)


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
        logger = logging.getLogger("listTaskUsers")
        tasks = Task_User.objects.all()
        userID = self.request.query_params.get("assignedTo")
        if userID != None:
            user = User.objects.filter(id=userID).first()
            tasks = tasks.filter(user=user)
            if len(tasks) == 0:
                logger.error(f"There are no users with the id {userID}")

        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
