"""trans19app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.gis import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from graphql_playground.views import GraphQLPlaygroundView
from trans19app.schema import graphql_schema
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(
        GraphQLView.as_view(graphiql=True, schema=graphql_schema))),
    path('playground/',
         GraphQLPlaygroundView.as_view(endpoint="/graphql")),
    path('accounts/login/', auth_views.LoginView.as_view()),
]
