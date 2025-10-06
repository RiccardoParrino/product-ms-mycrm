import graphene
from graphene_django import DjangoObjectType
from product_ms_2.products.models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"

class Query (graphene.ObjectType):
    all_items = graphene.List(Product)

    def resolve_all_items(root, info):
        return Product.objects.all()

schema = graphene.Schema(query=Query)