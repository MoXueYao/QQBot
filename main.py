from pkg.core.bot.message import (
    MessageList,
    Text,
    Face,
    Image,
    Record,
    At,
    Video,
    Node,
    NodeList,
)
from pkg.core.bot.event import FriendEvent, GroupEvent
from pkg.core.bot.regfunc import regFriendHandler, regGroupHandler, regLoopHandler
from pkg.core.command.regcmd import regCommand
from init import Init

# 创建机器人
bot = Init("127.0.0.1", 8080, 3000)


# 注册好友消息处理函数(注册其他同理)
@regFriendHandler()
def onFriendMsg(event: FriendEvent):
    """
    这只是一个示例。
    此函数会在收到好友消息时被调用。
    参数 event 是一个 FriendEvent 对象，包含了发送者信息、消息内容等信息。
    MessageList 是一个消息列表，重载了 == 运算符，可以很方便的与字符串进行比较。
    bot 是机器人对象，可以通过它发送消息。
    Text 和 Face 是消息对象，可以通过它们发送文本和表情。
    所有的消息对象都重载了 + 运算符，可以很方便的拼接消息。

    好友向你发送一条消息，如果这条消息是"你好"，则回复 "Hello World!(狗头)"
    """
    msg: MessageList = event.message  # 获取消息
    sender_id: int = event.sender.user_id  # 获取发送者QQ

    if msg == "你好":
        bot.send_friend_msg(sender_id, Text("Hello World!") + Face(277))


@regGroupHandler()
def onGroupMsg(event: GroupEvent):
    pass


# 启动机器人
bot.start()
