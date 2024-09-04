import json
import socket
import threading
from pkg.core.bot.message import toMessage, MessageList, Text
from pkg.core.bot.sender import Sender
from pkg.core.bot.event import (
    FriendEvent,
    GroupEvent,
    eventHandler_group,
    eventHandler_friend,
    group_eventHandler_run,
    friend_eventHandler_run,
)
from pkg.core.plugin.pluginloader import PluginManager
from pkg.config import only_At, Bot_QQ, admin, super_admin
from pkg.tools.log import log


class Listen:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def close(self, conn: socket.socket):
        response = "HTTP/1.1 200 OK\r\n\rn"
        conn.send((response.encode()))
        conn.close()

    def listen(self, conn: socket.socket, addr):
        # 接收数据
        data: dict = json.loads(conn.recv(4096).decode().split("\r\n\r\n")[1])
        # 判断数据是否为空
        if not data:
            log.error("数据为空。")
            conn.close()
            return
        # 创建消息列表对象
        msgList = MessageList([])
        try:
            for msg in data["message"]:
                msgList.append(toMessage(msg))
        except:
            self.close(conn)
            return

        # 判断消息列表是否为空
        if len(msgList.messages) == 0:
            log.warn("暂未支持的消息类型。")
            self.close(conn)
            return

        # 如果是群消息
        if data["message_type"] == "group" and len(eventHandler_group) != 0:
            # 根据config中的only_At参数判断是否做出响应
            if (
                only_At
                and msgList.getAt(True) == None
                or only_At
                and msgList.getAt().at_id != Bot_QQ
            ):
                self.close(conn)
                return
            # 消息列表去除第一个At消息
            msgList.pop(0)
            msg_list_oneMSG = msgList.messages[0]
            if isinstance(msg_list_oneMSG, Text):
                if msg_list_oneMSG.text.find(" ") == 0:
                    msg_list_oneMSG.text = msg_list_oneMSG.text[1:]
            # 创建事件对象
            event = GroupEvent(
                Sender(
                    data["sender"]["user_id"],
                    data["sender"]["nickname"],
                    data["sender"]["card"],
                ),
                msgList,
                data["group_id"],
            )
            if event.sender.user_id in admin:
                event.sender.permission = 2
            if event.sender.user_id in super_admin:
                event.sender.permission = 3
            log.info(
                f"[群{data['group_id']}] -> {data['sender']['nickname']}:  {msgList} "
            )
            # 插件管理器处理事件
            # 暂时未采用多进程处理事件
            flag = PluginManager.onEvent(event)
            # 判断是否继续处理事件
            if flag:
                # 开启线程调用事件处理器处理事件
                threading.Thread(target=group_eventHandler_run, args=(event,)).start()
        # 如果是好友消息
        if data["message_type"] == "private" and len(eventHandler_friend) != 0:
            # 创建事件对象
            event = FriendEvent(
                Sender(
                    data["sender"]["user_id"],
                    data["sender"]["nickname"],
                    data["sender"]["card"],
                ),
                msgList,
            )
            if event.sender.user_id in admin:
                event.sender.permission = 2
            if event.sender.user_id in super_admin:
                event.sender.permission = 3
            log.info(
                f"[好友{data['sender']['user_id']}] -> {data['sender']['nickname']}:  {msgList} "
            )
            # 插件管理器处理事件
            # 暂时未采用多进程处理事件
            flag = PluginManager.onEvent(event)
            # 判断是否继续处理事件
            if flag:
                # 开启线程调用事件处理器处理事件
                threading.Thread(target=friend_eventHandler_run, args=(event,)).start()
        # 关闭连接
        self.close(conn)

    def listen_run(self):
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        so.bind((self.host, self.port))
        so.listen(16)
        while True:
            conn, addr = so.accept()
            self.listen(conn, addr)
