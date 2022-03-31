import pytest

from main_app.tasks import ItemTask
from fixtures.conftest import ItemFactory


def some_func():
    print('1')
    ItemTask().delay()
    print('2')


@pytest.mark.django_db
class TestItem:
    def test_item(self):
        ItemFactory.create_batch(10)
        ItemTask().apply()

    def test_item2(self, celery_session_worker, celery_session_app):
        some_func()
