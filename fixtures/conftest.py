import pytest
import factory

from main_app.models import ItemModel


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ItemModel

    name = factory.Faker('word')

