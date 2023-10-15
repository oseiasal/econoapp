import factory

from .models.entry_model import Entry
from .models.category_model import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    category_name = factory.Faker('word')
    class Meta:
        model = Category

class EntryFactory(factory.django.DjangoModelFactory):

    description = factory.Faker('word')
    amount = factory.Faker('random_int')
    category = factory.SubFactory(CategoryFactory)
    class Meta:
        model = Entry

# poetry run python manage.py shell

# from FinancialTransactions.factories import EntryFactory
# EntryFactory.create()

# from FinancialTransactions.factories import CategoryFactory
# CategoryFactory.create()


