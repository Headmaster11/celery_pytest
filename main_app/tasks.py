from celery import Task

from main_app.models import ItemModel
from celery_pytest import celery_app


class ItemTask(Task):
    name = 'item-task'

    def run(self, *args, **kwargs):
        ItemModel.objects.last()


celery_app.register_task(ItemTask)
