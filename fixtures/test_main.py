import pytest

from main_app.tasks import ItemTask
from fixtures.conftest import ItemFactory


@pytest.mark.django_db
class TestItem:
    def test_item(self, celery_worker):
        ItemFactory.create_batch(10)
        ItemTask().apply()
