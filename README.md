# Introduction

This reposository steps to setup a Django project with JWT authentication.

1.  Install django and setup the project

        pip install django
        django-admin startproject Main .

2.  Install the djangorestframework_simplejwt

        pip install djangorestframework_simplejwt

- Add the 'rest_framework' to 'INSTALLED_APPS' list in settings.py
- Add the below 'REST_FRAMEWORK' object in the settings.py

      REST_FRAMEWORK = {
          'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
      )
      }

- Run the 'migrations' command

      python manage.py migrate

3.  Add the following lines below in the root 'urls.py' file to start using the endpoints

- Import the views provided by `rest_framework_simplejwt'

      from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
      )

- Append the following paths to the 'urlpatterns'

      [ ...,
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      ath('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      ]

4. Create a Superuser and start the server to start using the endpoints
