import graphene


class Book(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)
    name = graphene.String()


class BookConnection(graphene.relay.Connection):
    class Meta:
        node = Book


class CreateBook(graphene.Mutation):
    class Input:
        name = graphene.String(required=True)
        author = graphene.String(required=True)

    book = graphene.Field(Book)

    def mutate(self, info, name, author):
        # Do any logic for saving etc here
        # Return data at the end
        return CreateBook(book=Book(name=name))


class Query(graphene.ObjectType):
    book = graphene.Field(Book, name=graphene.String())
    books = graphene.relay.connection.IterableConnectionField(
        BookConnection, name_contains=graphene.String(),
    )

    def resolve_book(self, info, name):
        # Perform any look-up logic you want here.
        return Book(name=name)

    def resolve_books(self, info, name_contains):
        # Filter a collection here and return an array of ObjectTypes
        return [Book(name=name_contains)]

class Mutations(graphene.ObjectType):
    create_book = CreateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)