import pytest
import factory

from main_app.models import ItemModel


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': 'memory://',
        'result_backend': 'cache+memory://'
    }


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ItemModel

    name = factory.Faker('word')

