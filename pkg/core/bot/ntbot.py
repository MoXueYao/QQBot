from pkg.core.bot.event import loopHandler_run, Handler_loop
from pkg.core.bot.message import MessageList
from pkg.core.bot.server import Listen
from pkg.tools.log import log
from pkg.tools.post import post
import threading


class NTBot:
    """
    QQ脑瘫机器人。

    Args:
        host (str): 监听地址
        port (int): 监听端口
        target_port (int): 目标端口
    """

    def __init__(self, host: str, port: int, target_port: int):
        self.listen = Listen(host, port)
        self.host = host
        self.target_port = target_port

    def upListen_run(self):
        self.listen.listen_run()

    def send_group_msg(self, group_id: int, msg: MessageList | list):
        """
        发送群消息。

        Args:
            group_id (int): 群号
            msg (MessageList | list): 消息列表
        """
        if isinstance(msg, list):
            msg = MessageList(msg)
        data = {"group_id": group_id, "message": str(msg)}
        try:
            post(self.host, self.target_port, "/send_group_msg", data)
            log.info(f"[群{group_id}] <- {msg}")
        except:
            log.error(f"[群{group_id}] <- {msg} 失败。")

    def send_friend_msg(self, user_id: int, msg: MessageList | list):
        """
        发送好友消息。

        Args:
            user_id (int): 用户id
            msg (MessageList | list): 消息
        """
        if isinstance(msg, list):
            msg = MessageList(msg)
        data = {"user_id": user_id, "message": str(msg)}
        try:
            post(self.host, self.target_port, "/send_private_msg", data)
            log.info(f"[好友{user_id}] <- {msg}")
        except:
            log.error(f"[好友{user_id}] <- {msg} 失败。")

    def group_kick(self, group_id: int, user_id: int, reject_add_request: bool = False):
        """
        群踢人。

        Args:
            group_id (int): 群号
            user_id (int): 用户id
            reject_add_request (bool): 是否拒绝此人加群请求
        """
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "reject_add_request": reject_add_request,
        }
        try:
            post(self.host, self.target_port, "/set_group_kick", data)
            log.info(f"[群{group_id}] <- 踢出{user_id}")
        except:
            log.error(f"[群{group_id}] <- 踢出{user_id} 失败。")

    def group_ban(self, group_id: int, user_id: int, duration: int = 30 * 60):
        """
        群禁言。

        Args:
            group_id (int): 群号
            user_id (int): 用户id
            duration (int): 禁言时长，单位秒
        """
        data = {"group_id": group_id, "user_id": user_id, "duration": duration}
        try:
            post(self.host, self.target_port, "/set_group_ban", data)
            log.info(f"[群{group_id}] <- 禁言{user_id}")
        except:
            log.error(f"[群{group_id}] <- 禁言{user_id} 失败。")

    def set_group_card(self, group_id: int, user_id: int, card: str):
        """
        设置群名片。

        Args:
            group_id (int): 群号
            user_id (int): 用户id
            card (str): 群名片
        """
        data = {"group_id": group_id, "user_id": user_id, "card": card}
        try:
            post(self.host, self.target_port, "/set_group_card", data)
            log.info(f"[群{group_id}] <- 设置{user_id}名片为{card}")
        except:
            log.error(f"[群{group_id}] <- 设置{user_id}名片为{card} 失败。")

    def start(self):
        """
        开始运行机器人。
        """
        log.info(f"开始监听端口{self.target_port}...")
        threading.Thread(target=self.listen.listen_run).start()
        if len(Handler_loop) > 0:
            log.info("开始运行循环事件处理程序...")
            threading.Thread(target=loopHandler_run).start()
        log.info("机器人已启动完成！")


class BotManager:
    """
    机器人管理器。
    """

    bot: NTBot = None

    def init(host: str, port: int, target_port: int) -> NTBot:
        """
        初始化机器人。
        """
        global bot
        bot = NTBot(host, port, target_port)
        return bot

    def getBot():
        """
        获取机器人。
        """
        global bot
        return bot
