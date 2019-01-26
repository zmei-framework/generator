from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    for app_name, application in project.applications.items():
        if application.gitlab:
            for file in [
                '.gitlab-ci.yml',
                '.gitignore',
                'README.md'
            ]:
                generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                    'gitlab': application.gitlab,
                })
            if application.gitlab.test:
                for file in [
                    'conftest.py',
                    'pytest.ini',
                    'requirements.dev.txt',
                    '.flake8',
                    '.coveragerc'
                ]:
                    generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                        'gitlab': application.gitlab,
                    })

                generate_file(target_path, 'app/settings_test.py', template_name='settings.py.tpl')
