class Command(object):
    def get_key(self):
        raise NotImplementedError(self.__class__.__name__ + ".get_key")
    def run(self):
        raise NotImplementedError(self.__class__.__name__ + ".run")
