class Command:
    def __init__(self, cmd_name: str, func, description: str):
        self.cmd_name = cmd_name
        self.func = func
        self.description = description

    def run(self, *args):
        self.func(*args)


command_list: list[Command] = []
noCommand: list[Command] = []


def regNoCommand(func: callable):
    noCommand.append(Command("", func, ""))
