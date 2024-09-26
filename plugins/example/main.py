from pkg.core.plugin.pluginloader import PluginManager, PluginBase
from pkg.core.bot.event import FriendEvent, GroupEvent
from pkg.core.bot.message import Text, MessageList
from pkg.core.bot.ntbot import BotManager
from pkg.core.command.regcmd import regCommand, disableCommand
from pkg.tools.log import log
from pkg.tools.state import setEventTransmit


# 插件的入口类
# 插件类必须继承PluginBase
# 插件类请不要重写plugin_name属性
class Plugin(PluginBase):
    """
    测试插件。

    将收到的任意消息修改为"你好"。
    """

    # 插件加载时调用(即机器人启动时)
    def onLoad(self):

        # 注册插件的命令、事件处理器,记得填写owner参数
        @regCommand("test", "这是测试的命令。", owner=self)
        def onTest(event: FriendEvent):
            log.info("测试插件收到命令。")

        log.info("测试插件加载成功。")

    # 插件卸载时调用
    def onUnLoad(self):
        # 插件卸载时会自动销毁插件注册的命令、事件处理器(前提是你填写了owner=self)
        log.info("测试插件卸载成功。")

    # 插件事件处理函数(在机器人进行事件处理前调用)
    # 技术力有限,请在event后加个下标0
    def onEvent(self, *event: FriendEvent):
        # 设置事件是否继续传递
        setEventTransmit(True)
        event[0].message = MessageList([Text("你好")])
