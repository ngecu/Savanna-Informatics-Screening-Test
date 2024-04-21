from django.urls import path
from graphene_django.views import GraphQLView
from polls.schema import schema
from . import views

urlpatterns = [
    path("",views.login),
    path("callback",views.callback),

    path("grapql",GraphQLView.as_view(graphiql=True,schema=schema))
    ]