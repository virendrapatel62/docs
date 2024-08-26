# Django Rest Framework: API Views, Function-Based Views, Class-Based Views, and More

## 1. API View

### 1.1 Introduction

- The `APIView` class is the base class for all DRF views.
- It provides methods for HTTP methods (GET, POST, PUT, DELETE, etc.) and allows handling requests, responses, and exceptions.

### 1.2 Example: Using `APIView`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyAPIView(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, World!"}
        return Response(data)

    def post(self, request, format=None):
        data = request.data
        return Response(data, status=status.HTTP_201_CREATED)
```

## 2. Function-Based Views (FBVs)

### 2.1 Introduction

- Function-based views are simple Python functions that take a web request and return a web response.
- DRF provides decorators like `@api_view` to make FBVs compatible with DRF's request and response handling.

### 2.2 Example: Simple Function-Based View

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def my_function_based_view(request):
    if request.method == 'GET':
        data = {"message": "GET request received"}
        return Response(data)
    elif request.method == 'POST':
        data = {"message": "POST request received"}
        return Response(data, status=201)
```

## 3. Class-Based Views (CBVs)

### 3.1 Introduction

- Class-based views provide more structure and reusability for your views.
- They allow you to organize code into methods corresponding to HTTP verbs (e.g., `get`, `post`).

### 3.2 Example: Simple Class-Based View

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class MyClassBasedView(APIView):
    def get(self, request):
        data = {"message": "Hello from a class-based view!"}
        return Response(data)

    def post(self, request):
        data = {"message": "Data received"}
        return Response(data, status=201)
```

## 4. Generic Views

### 4.1 Introduction

- Generic views are provided by DRF to perform common patterns of data handling in views, like CRUD operations.
- They are more flexible than concrete view classes and can be easily extended or customized.

### 4.2 Example: `ListCreateAPIView`

```python
from rest_framework.generics import ListCreateAPIView
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateView(ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

### 4.3 Other Generic Views

- `RetrieveUpdateDestroyAPIView`
- `RetrieveAPIView`
- `UpdateAPIView`
- `DestroyAPIView`

## 5. Mixins

### 5.1 Introduction

- Mixins are used in combination with generic views to provide reusable blocks of behavior.
- DRF includes mixins like `CreateModelMixin`, `ListModelMixin`, `UpdateModelMixin`, etc.

### 5.2 Example: Combining Mixins with a Generic View

```python
from rest_framework import generics, mixins
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

## 6. ViewSets

### 6.1 Introduction

- ViewSets are classes that combine the logic for multiple related views in a single class.
- They provide actions like `list`, `create`, `retrieve`, `update`, `partial_update`, and `destroy`.

### 6.2 Example: Simple `ModelViewSet`

```python
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

### 6.3 Using Routers with ViewSets

- Routers automatically generate the URL conf for your ViewSets.
- Example:

```python
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'my-models', MyModelViewSet)

urlpatterns = router.urls
```
