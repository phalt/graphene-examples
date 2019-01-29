from graphene_django import DjangoObjectType
import graphene
from books.models import BookModel


class Book(DjangoObjectType):
    class Meta:
        interfaces = (graphene.relay.Node, )
        model = BookModel


class Query(graphene.ObjectType):
    books = graphene.List(Book)

    @graphene.resolve_only_args
    def resolve_books(self):
        return BookModel.objects.all()


schema = graphene.Schema(query=Query)