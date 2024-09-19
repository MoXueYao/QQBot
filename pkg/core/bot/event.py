from pkg.core.bot.message import MessageList
from pkg.core.bot.sender import Sender
from pkg.config import loop_interval, command_prefix
from pkg.core.command.command import command_list, Command, noCommand
import time
import threading


class GroupEvent:
    """
    群事件。
    """

    def __init__(self, sender: Sender, message: MessageList, group_id: int):
        self.sender = sender
        self.message = message
        self.group_id = group_id

    def getType(self) -> str:
        return "group"

    def isCommand(self) -> bool:
        """
        判断该事件是否为命令事件。
        """
        return self.message.find(command_prefix) == 0

    def getCommand(self) -> Command:
        """
        从事件中获取命令。
        """
        for i in command_list:
            if i.cmd_name == str(self.message)[1:]:
                return i


class FriendEvent:
    """
    好友事件。
    """

    def __init__(self, sender: Sender, message: MessageList):
        self.sender = sender
        self.message = message

    def getType(self) -> str:
        return "private"

    def isCommand(self) -> bool:
        """
        判断该事件是否为命令事件。
        """
        return self.message.find(command_prefix) == 0

    def getCommand(self) -> Command:
        """
        从事件中获取命令。
        """
        for i in command_list:
            if i.cmd_name == str(self.message)[1:]:
                return i


# 事件处理器 列表
eventHandler_group: list = []
eventHandler_friend: list = []
Handler_loop: list = []


def friend_eventHandler_run(*event: FriendEvent):
    """
    运行好友事件处理器。
    """
    if event[0].isCommand():  # 如果是命令
        cmd = event[0].getCommand()
        if cmd is None or cmd.isGroup():  # 如果命令不存在
            noCommand[0].run(event[0])
            return
        if cmd.permission > event[0].sender.permission:  # 如果权限不足
            noCommand[1].run(event[0])
            return
        cmd.run(event[0])
        return
    for func in eventHandler_friend:
        threading.Thread(target=func, args=event).start()


def group_eventHandler_run(*event: GroupEvent):
    """
    运行群事件处理器。
    """
    if event[0].isCommand():  # 如果是命令
        cmd = event[0].getCommand()
        if cmd is None or not cmd.isGroup():  # 如果命令不存在
            noCommand[0].run(event[0])
            return
        if cmd.permission > event[0].sender.permission:  # 如果权限不足
            noCommand[1].run(event[0])
            return
        cmd.run(event[0])
        return
    for func in eventHandler_group:
        threading.Thread(target=func, args=event).start()


def loopHandler_run():
    """
    运行循环处理器。
    """
    while True:
        time.sleep(loop_interval)
        for func in Handler_loop:
            threading.Thread(target=func).start()
