class PluginBase:
    def onLoad(self):
        """
        插件加载时调用的函数。
        """
        pass

    def onUnLoad(self):
        """
        插件卸载时调用的函数。
        """
        pass

    def onEvent(self, event):
        """
        插件处理事件时调用的函数。
        """
        pass


plugins: list[PluginBase] = []
