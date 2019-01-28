import graphene


class Book(graphene.ObjectType):

    name = graphene.String()


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

    def resolve_book(self, info, name):
        # Perform any look-up logic you want here.
        return Book(name=name)

class Mutations(graphene.ObjectType):
    create_book = CreateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)