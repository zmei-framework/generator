import pkg_resources

from zmei_generator.parser.utils import BaseListener


parsers = []
for entry_point in pkg_resources.iter_entry_points('zmei.parser.stage1'):
    parsers += entry_point.load()

parsers.append(BaseListener)


class PartsCollectorListener(*parsers):
    pass
