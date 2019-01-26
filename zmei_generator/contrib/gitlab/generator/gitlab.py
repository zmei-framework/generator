from zmei_generator.generator.utils import generate_file


def generate(target_path, app):
    for app_name, collection_set in app.collection_sets.items():
        if collection_set.gitlab:
            for file in [
                '.gitlab-ci.yml',
                '.gitignore',
                'README.md'
            ]:
                generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                    'gitlab': collection_set.gitlab,
                })
            if collection_set.gitlab.test:
                for file in [
                    'conftest.py',
                    'pytest.ini',
                    'requirements.dev.txt',
                    '.flake8',
                    '.coveragerc'
                ]:
                    generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                        'gitlab': collection_set.gitlab,
                    })

                generate_file(target_path, 'app/settings_test.py', template_name='settings.py.tpl')
