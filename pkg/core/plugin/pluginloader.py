from pkg.core.plugin.pluginbase import PluginBase, plugins
from pkg.tools.log import log
import os
import importlib.util
from pathlib import Path

eventCache = None


class PluginManager:
    """
    插件管理器。

    插件管理器负责加载、卸载插件。
    """

    def loadPlugin():
        """
        加载所有插件。
        读取文件中的插件(\plugins\插件名\main.py),并调用onLoad方法。
        """
        # 从上三层目录读取插件
        path = Path(__file__).resolve().parents[3] / "plugins"

        for plugin in os.listdir(path):
            if plugin in ["__pycache__", "__init__.py"]:
                continue
            log.info(f"加载插件：{plugin}")
            if os.path.isdir(path / plugin):
                try:
                    spec = importlib.util.spec_from_file_location(
                        "main", str(path / plugin / "main.py")
                    )
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # 动态实例化 Plugin 类
                    if hasattr(module, "Plugin"):
                        plugin_class = getattr(module, "Plugin")
                        # 实例化 Plugin 类
                        plugin_instance = plugin_class()
                        plugins.append(plugin_instance)
                        # 调用 onLoad 方法
                        plugin_instance.onLoad()
                except Exception as e:
                    log.error(f"插件加载失败: {e}")

    def unLoadPlugin(pluginName: str):
        """
        卸载插件。

        Args:
            plugin (str): 插件名称。
        """
        try:
            for plugin in plugins:
                if plugin.name == pluginName:
                    if hasattr(plugin, "onUnLoad") and callable(
                        getattr(plugin, "onUnLoad")
                    ):
                        # 调用 onUnLoad 方法
                        plugin.onUnLoad()
                    else:
                        log.error(
                            f"插件 {pluginName} 的 Plugin 类缺少必要的 onUnLoad 方法"
                        )
                plugins.remove(plugin)
        except Exception as e:
            log.error(f"插件卸载失败:{e}")

    def getEvent():
        """
        获取事件。
        """
        global eventCache
        return eventCache

    def onEvent(event):
        """
        事件处理。
        """
        global eventCache
        eventCache = event
        for plugin in plugins:
            # 调用 onEvent 方法,判断是否阻止事件
            flag = plugin.onEvent(event)
            if flag == True:
                # 阻止事件继续往下传递
                return False
        # 允许事件继续往下传递
        return True
