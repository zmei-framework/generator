import os

import click
import yaml


class Config(object):

    def __init__(self, workdir=None) -> None:
        super().__init__()

        if not workdir:
            raise ValueError("Wroking directory is required!")

        self.workdir = workdir

        self.config = None

    def get_path_local(self):
        return os.path.join(self.workdir, '.zmei-app.yaml')

    def get_path_global(self):
        return os.path.expanduser('~/.zmei/config.yaml')

    def load(self, interactive=False):
        config_path_global = self.get_path_global()
        config_path_local = self.get_path_local()

        self.config = {}

        if os.path.exists(config_path_global):
            with open(config_path_global) as f:
                self.config.update(
                    self._filter_config(yaml.load(f.read()), self.get_global_defaults().keys())
                )

        if os.path.exists(config_path_local):
            with open(config_path_local) as f:
                self.config.update(
                    self._filter_config(yaml.load(f.read()), self.get_defaults().keys())
                )

        self.update(interactive=interactive)

    def update(self, interactive=False):
        self.config = self.config or {}

        for key, (description, default) in self.get_defaults().items():
            if key not in self.config or not self.config[key]:
                if interactive:
                    self.config[key] = click.prompt(description, default=default)
                    if key == 'ssh_public_key':
                        target_file = self.config[key]
                        self.generate_new_ssh_key(target_file)
                else:
                    self.config[key] = default

    def get_global_defaults(self):
        defaults = {
            'ssh_public_key': ('Default ssh key for this app', os.path.expanduser('~/.ssh/id_rsa.pub'))
        }
        return defaults

    def get_defaults(self):
        defaults = {
            'app_name': ('Application technical name (no spaces, ex: my-app)', os.path.basename(self.workdir)),
        }
        defaults.update(
            self.get_global_defaults()
        )
        return defaults

    def generate_new_ssh_key(self, target_file):
        if not os.path.exists(target_file):
            print('Ssh key does not exist. Should I generate one?')

            if target_file.endswith('.pub'):
                target_file = target_file[:-4]

            cmd = f'ssh-keygen -t rsa -b 4096 -f ~/{target_file}'

            if click.confirm(f'Run "{cmd}"?'):
                os.system(cmd)

    def save(self):
        conf = self._filter_config(self.config, self.get_defaults().keys())

        with open(self.get_path_local(), 'w') as f:
            f.write(yaml.dump(conf, default_flow_style=False))

    def _filter_config(self, conf, allowed_keys):
        return {key: val for key, val in conf.items() if key in allowed_keys}