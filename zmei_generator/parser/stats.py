from datetime import datetime
from collections import defaultdict
from time import perf_counter

from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class StatsCollector(ZmeiLangParserListener):

    def __init__(self) -> None:
        super().__init__()

        self.stats = defaultdict(int)
        self.start_time = perf_counter()

    def enterEveryRule(self, ctx):
        name = type(ctx).__name__[:-7]

        if name.startswith('An_'):
            name = '@' + name[3:]

        self.stats[name] += 1

    def get_data(self):
        return {
            'date': datetime.utcnow(),
            'time': perf_counter() - self.start_time,
            'features': self.stats
        }

