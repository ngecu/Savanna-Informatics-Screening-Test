import graphene
from graphene_django import DjangoObjectType
from .models import Customer,Order


class CustomersType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "name", "code")

class OrdersType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("item", "amount", "time","customer")

class Query(graphene.ObjectType):

    all_customers = graphene.List(CustomersType)
    all_orders = graphene.List(OrdersType)

    def resolve_all_customers(root, info):
        return Customer.objects.all()
    
    def resolve_all_orders(root, info):
        return Order.objects.all()

schema = graphene.Schema(query=Query)