class Command:
    """
    命令

    Args:
        cmd_name (str): 命令名
        func (callable): 命令函数
        description (str): 命令描述.
        scope (str): 命令作用域. 可以是 public, group, friend.
        owner (str): 命令拥有者.
        permission (int, optional): 权限.
    """

    def __init__(
        self,
        cmd_name: str,
        func,
        description: str = "",
        scope: str = "public",
        owner: str = "main",
        permission: int = 1,
    ):
        self.cmd_name = cmd_name
        self.func = func
        self.description = description
        self.scope = scope
        self.owner = str(owner)
        self.permission = permission

    def run(self, *args):
        self.func(*args)

    def isGroup(self):
        return self.scope == "group"

    def isFriend(self):
        return self.scope == "friend"

    def isPublic(self):
        return self.scope == "public"


command_list: list[Command] = []
noCommand: list[Command] = []


def regNoCommand(func: callable):
    noCommand.append(Command("", func))
