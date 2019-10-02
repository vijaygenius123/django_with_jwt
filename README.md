# Introduction

This reposository steps to setup a Django project with JWT authentication.

1.  Install django and setup the project

        pip install django
        django-admin startproject Main .

2.  Install the djangorestframework_simplejwt

        pip install djangorestframework_simplejwt

- Add the `rest_framework` to `INSTALLED_APPS` list in settings.py
- Add the below 'REST_FRAMEWORK' object in the settings.py

      REST_FRAMEWORK = {
          'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
      )
      }

- Run the `migrations` command

      python manage.py migrate

3.  Add the following lines below in the root `urls.py` file to start using the endpoints

- Import the views provided by `rest_framework_simplejwt'

      from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
      )

- Append the following paths to the `urlpatterns`

      [ ...,
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      ]

4. Create a Superuser and start the server to start using the endpoints

- Create Superuser

      python manage.py createsuperuser

- Start server

      python manage.py runserver

5. Test the JWT

- Create a views.py with the code below

      from django.contrib.auth import get_user_model
      from rest_framework import serializers, generics
      from rest_framework.permissions import IsAuthenticated
      from rest_framework.response import Response

      class UserDetailSerializer(serializers.ModelSerializer):

        class Meta:
          model = get_user_model()
          fields = ('first_name', 'last_name', 'email')

      class UserDetailView(generics.ListAPIView):
        permission_classes = [IsAuthenticated]

        def list(self, request):
          queryset = get_user_model().objects.get(id=request.user.id)
          serializer = UserDetailSerializer(queryset, many=False)
          return Response(serializer.data)

- Add the view to urls.py, first import the view like below

      from .views import UserDetailView

  Then append it to the urlpatterns

      path('api/user_detail/', UserDetailView.as_view())

- Create a token by using the /api/token endpoint and pass the token using the syntax `Bearer <token>` in the Authorization header field while making any request.
