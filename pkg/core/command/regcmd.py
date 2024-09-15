from pkg.core.command.command import Command, regNoCommand, command_list


def regCommand(name: str, description: str = "", permission: int = 1):
    """
    注册命令。

    注意:命令名不能重复。

    注意:若是未注册任何群聊事件处理器,那么命令在群聊中将不会被执行。(好友同理)


    Args:
        name (str): 命令名。
        description (str): 命令描述。默认为"".
        permission (int): 权限等级。默认为1.\n
            1:普通用户
            2:管理员
            3:超级管理员
    """

    def cmd_func(func):
        if name == "" or name is None:
            raise Exception("没有指定命令名。")
        command_list.append(Command(name, func, description, permission))

    return cmd_func


def disableCommand(name: str) -> bool:
    """
    注销命令。

    Args:
        name (str): 命令名。

    Return (bool): 是否注销成功。
    """
    for cmd in command_list:
        if cmd.cmd_name == name:
            command_list.remove(cmd)
            return True
    return False
