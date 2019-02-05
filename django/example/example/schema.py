from graphene_django import DjangoObjectType
import graphene
from books.models import BookModel


class Book(DjangoObjectType):
    class Meta:
        interfaces = (graphene.relay.Node, )
        model = BookModel


class BookConnection(graphene.relay.Connection):
    class Meta:
        node = Book


class Query(graphene.ObjectType):
    books = graphene.relay.connection.IterableConnectionField(
        BookConnection,
    )

    def resolve_books(self, info):
        return BookModel.objects.all()


schema = graphene.Schema(query=Query)