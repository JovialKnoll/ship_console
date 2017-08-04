import os

class Command(object):
    commands_visible = []
    for (dirpath, dirnames, filenames) in os.walk('commands'):
        for filename in filenames:
            if (
                not filename.endswith('.py')
                or not filename[0].isalpha()
                or filename == 'command.py'
            ):
                continue
            clean_name = filename[:-3]
            commands_visible.append(clean_name)
        break
    commands_visible.sort()
    commands_invisible = []

    @classmethod
    def get_all_commands(cls):
        return cls.commands_visible + cls.commands_invisible

    @classmethod
    def get_visible_commands(cls):
        return list(cls.commands_visible)

    def get_key(self):
        raise NotImplementedError(
            self.__class__.__name__
            + ".get_key"
        )

    def run(self, inputs):
        raise NotImplementedError(
            self.__class__.__name__
            + ".run"
        )
