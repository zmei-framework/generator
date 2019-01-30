from zmei_generator.contrib.gitlab.extensions.application.gitlab import GitlabAppExtension
from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    for application in project.applications_with(GitlabAppExtension):
        for file in [
            '.gitlab-ci.yml',
            '.gitignore',
            'README.md'
        ]:
            generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                'gitlab': application[GitlabAppExtension],
            })
        if application[GitlabAppExtension].test:
            for file in [
                'conftest.py',
                'pytest.ini',
                'requirements.dev.txt',
                '.flake8',
                '.coveragerc'
            ]:
                generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                    'gitlab': application[GitlabAppExtension],
                })

            generate_file(target_path, 'app/settings_test.py', template_name='settings.py.tpl')
