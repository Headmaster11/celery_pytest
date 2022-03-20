from celery import Task

from main_app.models import ItemModel


class ItemTask(Task):
    name = 'item-task'

    def run(self, *args, **kwargs):
        ItemModel.objects.last()
