from pkg.core.command.command import Command, regNoCommand, command_list


def regCommand(name: str, description: str = ""):
    """
    注册命令。

    注意:命令名不能重复。

    注意:若是未注册任何群聊事件处理器,那么命令在群聊中将不会被执行。(好友同理)


    Args:
        name (str): 命令名。
    """

    def cmd_func(func):
        if name == "" or name is None:
            raise Exception("没有指定命令名。")
        command_list.append(Command(name, func, description))

    return cmd_func
