from pkg.core.bot.event import eventHandler_group, eventHandler_friend, Handler_loop


def regGroupHandler(func):
    """
    注册群事件处理器。

    在该装饰器下定义函数的参数为event,event为GroupEvent对象。
    """

    def func_fix(*event):
        func(event[0])

    eventHandler_group.append(func_fix)


def regFriendHandler(func):
    """
    注册好友事件处理器。

    在该装饰器下定义函数的参数为event,event为FriendEvent对象。
    """

    def func_fix(*event):
        func(event[0])

    eventHandler_friend.append(func_fix)


def regLoopHandler(func):
    """
    注册循环事件处理器。

    该装饰器下定义函数的参数为None。
    """
    Handler_loop.append(func)
