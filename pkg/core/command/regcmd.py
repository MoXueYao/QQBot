from pkg.core.command.command import Command, regNoCommand, command_list


def regCommand(
    name: str, description: str = "", scope: str = "public", permission: int = 1
):
    """
    注册命令。

    注意:命令名不能重复。

    注意:若是未注册任何群聊事件处理器,那么命令在群聊中将不会被执行。(好友同理)


    Args:
        name (str): 命令名。
        description (str): 命令描述。.
        scope (str): 命令作用域. 可以是 public, group, friend.
        permission (int): 权限等级。.
            1:普通用户
            2:管理员
            3:超级管理员
    """

    def cmd_func(func):
        if name == "" or name is None:
            raise Exception("没有指定命令名。")
        if scope not in ["public", "group", "friend"]:
            raise Exception("命令作用域不正确。")
        command_list.append(Command(name, func, description, scope, permission))

    return cmd_func


def disableCommand(name: str) -> bool:
    """
    销毁命令。

    Args:
        name (str): 命令名。
    """
    for cmd in command_list:
        if cmd.cmd_name == name:
            command_list.remove(cmd)
            return True
    return False
