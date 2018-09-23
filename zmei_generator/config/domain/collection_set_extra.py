class CollectionSetExtra(object):

    def __init__(self, collection_set):
        self.collection_set = collection_set

    def get_required_apps(self):
        return []

    def get_required_deps(self):
        return []

    def get_required_settings(self):
        return {}

    def get_required_urls(self):
        return []

    def post_process(self):
        pass


