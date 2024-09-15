from pkg.core.plugin.pluginloader import PluginManager, PluginBase
from pkg.core.bot.event import FriendEvent, GroupEvent
from pkg.core.bot.message import Text, MessageList
from pkg.core.bot.ntbot import BotManager
from pkg.core.command.regcmd import regCommand, disableCommand
from pkg.tools.log import log


# 插件的入口类
class Plugin(PluginBase):
    """
    测试插件。

    将收到的任意消息修改为"你好"。
    """

    # 插件加载时调用(即机器人启动时)
    def onLoad(self):
        # 注册插件的命令
        @regCommand("test", "测试插件的测试命令。", 1)
        def onTest(event: FriendEvent):
            log.info("测试插件收到命令。")

        log.info("测试插件加载成功。")

    # 插件卸载时调用
    def onUnLoad(self):
        # 销毁命令
        if disableCommand("test"):
            log.info("销毁命令成功。")
        else:
            log.error("销毁命令失败。")
        log.info("测试插件卸载成功。")

    # 插件事件处理函数(在机器人进行事件处理前调用)
    def onEvent(self, event: FriendEvent) -> bool:
        event.message = MessageList([Text("你好")])
        # 返回False表示其他插件/机器人不再处理此事件(True同理)
        return True
