To add JWT (JSON Web Token) support to your Django project using Django REST Framework (DRF), you can use the djangorestframework-simplejwt package. Here’s a step-by-step guide:

- Step 1: Install the required packages
  First, install djangorestframework-simplejwt:

  ```bash
  pip install djangorestframework-simplejwt
  ```

- Step 2: Update settings.py

  Add the JWT authentication classes to your Django settings.

  ```python
  # settings.py

  INSTALLED_APPS = [
      ...,
      'rest_framework',
      'rest_framework_simplejwt',
  ]

  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ),
  }

  # Optionally, you can configure JWT settings:
  from datetime import timedelta

  SIMPLE_JWT = {
      'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
      'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
      'ROTATE_REFRESH_TOKENS': True,
      'BLACKLIST_AFTER_ROTATION': True,
      'AUTH_HEADER_TYPES': ('Bearer',),
  }

  ```

- Step 3: Create views for obtaining and refreshing tokens

  You can use the built-in views provided by djangorestframework-simplejwt to handle token issuance and refresh.

  ```python
  # urls.py

  from django.urls import path
  from rest_framework_simplejwt.views import (
      TokenObtainPairView,
      TokenRefreshView,
  )

  urlpatterns = [
      ...,
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  ]

  ```

- Step 4: Protect your views with JWT

  You can now protect your views by requiring JWT authentication.

  ```python
  # views.py

  from rest_framework.permissions import IsAuthenticated
  from rest_framework.views import APIView
  from rest_framework.response import Response

  class ProtectedView(APIView):
      permission_classes = [IsAuthenticated]

      def get(self, request):
          return Response({"message": "This is a protected view"})

  ```

- Step 5: Test the JWT Authentication

  - Obtain a token:

    Send a POST request to /api/token/ with your username and password to obtain an access and refresh token.

    ```bash
    curl -X POST -d "username=myusername&password=mypassword" http://localhost:8000/api/token/
    ```

  - Access protected views:

    Use the access token in the Authorization header to access protected views.

    ```bash
    curl -H "Authorization: Bearer <access_token>" http://localhost:8000/protected-view/
    ```

    - Refresh the token:

      Send a POST request to /api/token/refresh/ with the refresh token to obtain a new access token.

    ```bash
    curl -X POST -d "refresh=<refresh_token>" http://localhost:8000/api/token/refresh/
    ```
