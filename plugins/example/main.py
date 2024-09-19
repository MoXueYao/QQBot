from pkg.core.plugin.pluginloader import PluginManager, PluginBase
from pkg.core.bot.event import FriendEvent, GroupEvent
from pkg.core.bot.message import Text, MessageList
from pkg.core.bot.ntbot import BotManager
from pkg.core.command.regcmd import regCommand, disableCommand
from pkg.tools.log import log
from pkg.tools.state import setEventTransmit


# 插件的入口类
class Plugin(PluginBase):
    """
    测试插件。

    将收到的任意消息修改为"你好"。
    """

    def __init__(self):
        # 需要有name属性
        self.name = ""

    # 插件加载时调用(即机器人启动时)
    def onLoad(self):
        # 注册插件的命令
        @regCommand("test", "测试插件的测试命令。")
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
    # 技术力有限,请在event后加个下标0
    def onEvent(self, *event: FriendEvent):
        # 设置事件是否继续传递
        setEventTransmit(True)
        event[0].message = MessageList([Text("你好")])
