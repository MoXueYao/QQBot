class Command:
    """
    命令

    Args:
        cmd_name (str): 命令名
        func (callable): 命令函数
        description (str, optional): 命令描述. Defaults to "".
        permission (int, optional): 权限. Defaults to 1.
    """

    def __init__(self, cmd_name: str, func, description: str = "", permission: int = 1):
        self.cmd_name = cmd_name
        self.func = func
        self.description = description
        self.permission = permission

    def run(self, *args):
        self.func(*args)


command_list: list[Command] = []
noCommand: list[Command] = []


def regNoCommand(func: callable):
    noCommand.append(Command("", func))
