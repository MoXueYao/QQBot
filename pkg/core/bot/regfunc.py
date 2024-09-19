from pkg.core.bot.event import eventHandler_group, eventHandler_friend, Handler_loop
from pkg.core.bot.handler import Handler


def regGroupHandler(owner: str = "main"):
    """
    注册群事件处理器。

    在该装饰器下定义函数的参数为event,event为GroupEvent对象。
    Args:
        owner (str): 事件处理器拥有者。
    """

    def handler_func(func):
        def func_fix(*event):
            func(event[0])

        eventHandler_group.append(Handler(func_fix, owner, type="group"))

    return handler_func


def regFriendHandler(owner: str = "main"):
    """
    注册好友事件处理器。

    在该装饰器下定义函数的参数为event,event为FriendEvent对象。
    Args:
        owner (str): 事件处理器拥有者。
    """

    def handler_func(func):
        def func_fix(*event):
            func(event[0])

        eventHandler_friend.append(Handler(func_fix, owner, type="friend"))

    return handler_func


def regLoopHandler(owner: str = "main"):
    """
    注册循环事件处理器。

    该装饰器下定义函数的参数为None。
    """

    def handler_func(func):
        Handler_loop.append(Handler(func, owner, type="loop"))

    return handler_func


def disableHandler(owner: str = "main", type: str = "all"):
    """
    卸载所有拥有者为owner的事件处理器。

    Args:
        owner (str): 事件处理器拥有者。
        type (str): 卸载类型,可选all,friend,group,loop。
    """
    owner = str(owner)
    if type not in ["all", "friend", "group", "loop"]:
        raise ValueError("type错误。")
    if type == "all":
        for i in range(len(eventHandler_group) - 1, -1, -1):
            if eventHandler_group[i].owner == owner:
                eventHandler_group.pop(i)
        for i in range(len(eventHandler_friend) - 1, -1, -1):
            if eventHandler_friend[i].owner == owner:
                eventHandler_friend.pop(i)
        for i in range(len(Handler_loop) - 1, -1, -1):
            if Handler_loop[i].owner == owner:
                Handler_loop.pop(i)
        return
    if type == "group":
        for i in range(len(eventHandler_group) - 1, -1, -1):
            if eventHandler_group[i].owner == owner:
                eventHandler_group.pop(i)
        return
    if type == "friend":
        for i in range(len(eventHandler_friend) - 1, -1, -1):
            if eventHandler_friend[i].owner == owner:
                eventHandler_friend.pop(i)
        return
    if type == "loop":
        for i in range(len(Handler_loop) - 1, -1, -1):
            if Handler_loop[i].owner == owner:
                Handler_loop.pop(i)
