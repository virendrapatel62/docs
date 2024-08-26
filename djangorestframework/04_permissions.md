To implement permission classes in Django REST Framework (DRF), you can use predefined permission classes with both APIView and ViewSet, and you can also create custom permission classes. Below are examples for each scenario.

### Using Permission Classes with APIView

In a class-based view using APIView, you can set permission classes directly within the view.

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def get(self, request):
        return Response({"message": "This is a protected view accessible to authenticated users only"})

```

### Using Permission Classes with ViewSet

When using a ViewSet, you can also specify permission classes similarly.

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

```

### Creating Custom Permission Classes

You can create custom permission classes to handle more specific permission logic. Here’s an example:

```python
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user

```

### Using Custom Permission Classes

You can apply the custom permission class to either APIView or ViewSet

`With APIView:`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyModel
from .permissions import IsOwnerOrReadOnly

class MyCustomPermissionAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk):
        my_object = MyModel.objects.get(pk=pk)
        self.check_object_permissions(request, my_object)
        return Response({"message": "This object is owned by you!"})

```

`With ViewSet:`

```python
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from .permissions import IsOwnerOrReadOnly

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Ensure the owner is set on create

```

#### Explanation:

- `Permission Classes:` These are used to control access to views. IsAuthenticated ensures only authenticated users can access the view.

- `Custom Permission Classes:` By subclassing BasePermission, you can define custom logic. In the IsOwnerOrReadOnly example, only the owner of an object can edit it, while others can only read it.

- `Applying Permissions:` You can apply these permissions to APIView or ViewSet depending on your needs.
  This approach allows you to enforce security and access control across your API endpoints.
