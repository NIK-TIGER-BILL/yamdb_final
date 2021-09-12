import os
import re

from django.conf import settings


class TestDockerfileCompose:

    def test_dockerfile_compose(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "docker-compose.yaml")}', 'r') as f:
                docker_compose = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл docker-compose.yaml'

        assert re.search(r'image:\s+postgres:', docker_compose), (
            'Проверьте, что добавили образ postgres:latest в файл docker-compose.yaml'
        )
        assert re.search(r'image:\s+([a-zA-Z0-9]+)\/([a-zA-Z0-9_\.])+(\:[a-zA-Z0-9_-]+)?', docker_compose), (
            'Проверьте, что добавили сборку контейнера из образа на вашем DockerHub в файл docker-compose.yaml'
        )
