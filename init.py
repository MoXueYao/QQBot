from pkg.core.command.regcmd import regCommand, regNoCommand, command_list
from pkg.core.bot.message import Text
from pkg.core.bot.event import GroupEvent, FriendEvent
from pkg.core.bot.ntbot import NTBot, BotManager
from pkg.core.plugin.pluginloader import PluginManager


def Init(host: str, port: int, target_port: int) -> NTBot:
    """
    初始化机器人

    Args:
        host (str): 机器人监听地址
        port (int): 机器人监听端口
        target_port (int): 目标端口
    Returns:
        NTBot: 机器人实例
    """
    bot = BotManager.init(host, port, target_port)
    PluginManager.loadPlugin()
    return bot


@regCommand("help", "查看命令帮助。")
def onHelp(event: GroupEvent | FriendEvent) -> None:
    bot = BotManager.getBot()
    re_msg = "帮助菜单:\n"
    if isinstance(event, GroupEvent):
        for cmd in command_list:
            if cmd.description != "":
                re_msg += f"/{cmd.cmd_name} - {cmd.description}\n"
        re_msg = re_msg[:-1]
        bot.send_group_msg(event.group_id, [Text(re_msg)])
        return
    if isinstance(event, FriendEvent):
        for cmd in command_list:
            if cmd.description != "":
                re_msg += f"/{cmd.cmd_name} - {cmd.description}\n"
        re_msg = re_msg[:-1]
        bot.send_friend_msg(event.sender.user_id, [Text(re_msg)])
        return


@regNoCommand
def onNoCommand(event: GroupEvent | FriendEvent) -> None:
    bot = BotManager.getBot()
    if isinstance(event, GroupEvent):
        bot.send_group_msg(
            event.group_id, [Text("未找到该命令。\n请输入/help查看帮助菜单。")]
        )
        return
    if isinstance(event, FriendEvent):
        bot.send_friend_msg(
            event.sender.user_id, [Text("未找到该命令。\n请输入/help查看帮助菜单。")]
        )
        return