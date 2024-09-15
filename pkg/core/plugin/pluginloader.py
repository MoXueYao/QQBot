from pkg.core.plugin.pluginbase import PluginBase, plugins
from pkg.tools.log import log
from pkg.tools.state import state
import os
import importlib.util
from pathlib import Path
import threading


class PluginManager:
    """
    插件管理器。

    插件管理器负责加载、卸载插件。
    """

    def loadAllPlugin():
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
                        plugin_instance: PluginBase = plugin_class()
                        plugin_instance.name = plugin
                        plugins.append(plugin_instance)
                        # 调用 onLoad 方法
                        plugin_instance.onLoad()
                except Exception as e:
                    log.error(f"插件加载失败: {e}")

    def unLoadAllPlugin():
        """
        卸载所有插件。
        """
        for plugin in plugins:
            try:
                plugin.onUnLoad()
            except Exception as e:
                log.error(f"卸载错误:{e}")
                continue
        plugins.clear()

    def unLoadPlugin(pluginName: str):
        """
        卸载指定插件。

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
                return
        except Exception as e:
            log.error(f"插件卸载失败:{e}")
            return
        log.error(f"插件 {pluginName} 未找到")

    def loadPlugin(pluginName: str):
        """
        加载指定插件。
        """
        try:
            path = Path(__file__).resolve().parents[3] / "plugins" / pluginName
            spec = importlib.util.spec_from_file_location("main", str(path / "main.py"))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # 动态实例化 Plugin 类
            if hasattr(module, "Plugin"):
                plugin_class = getattr(module, "Plugin")
                # 实例化 Plugin 类
                plugin_instance: PluginBase = plugin_class()
                plugins.append(plugin_instance)
                # 调用 onLoad 方法
                plugin_instance.onLoad()
        except Exception as e:
            log.error(f"插件加载失败: {e}")

    def onEvent(event):
        """
        事件处理。
        """
        for plugin in plugins:
            threading.Thread(target=plugin.onEvent, args=(event,)).start()
            if not state["event_transmit"]:
                # 阻止事件继续往下传递
                return
