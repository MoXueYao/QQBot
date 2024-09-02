from pkg.core.plugin.pluginloader import PluginManager, PluginBase
from pkg.core.bot.event import FriendEvent, GroupEvent
from pkg.core.bot.message import Text, MessageList
from pkg.core.bot.ntbot import BotManager
from pkg.tools.log import log


# 插件的入口类
class Plugin(PluginBase):
    """
    测试插件。

    将收到的任意消息修改为"你好"。
    """

    # 插件加载时调用(即机器人启动时)
    def onLoad(self):
        log.info("测试插件加载成功。")

    # 插件事件处理函数(在机器人进行事件处理前调用)
    def onEvent(self, event: FriendEvent) -> bool:
        event.message = MessageList([Text("你好")])
        # 返回True表示其他插件/机器人不再处理此事件(False同理)
        return True
