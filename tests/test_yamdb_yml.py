import os
import re

from django.conf import settings


class TestWorkflow:

    def test_workflow(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "yamdb_workflow.yaml")}', 'r') as f:
                yamdb = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл yamdb_workflow.yaml в корневой каталог для проверки'

        assert (
            re.search(r'on:\s*push:\s*branches:\s*-\smaster', yamdb) or
            'on: [push]' in yamdb or
            'on: push' in yamdb 
        ), 'Проверьте, что добавили действие при пуше в файл yamdb_workflow.yaml' 
        assert 'pytest' in yamdb, 'Проверьте, что добавили pytest в файл yamdb_workflow.yaml'
        assert 'appleboy/ssh-action' in yamdb, 'Проверьте, что добавили деплой в файл yamdb_workflow.yaml'
        assert 'appleboy/telegram-action' in yamdb, (
            'Проверьте, что добавили доставку отправку telegram сообщения '
            'в файл yamdb_workflow.yaml'
        )
