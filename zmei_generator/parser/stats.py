from collections import defaultdict

from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class StatsCollector(ZmeiLangParserListener):

    def __init__(self) -> None:
        super().__init__()

        self.stats = defaultdict(int)

    def enterEveryRule(self, ctx):
        self.stats[type(ctx).__name__[:-7]] += 1

