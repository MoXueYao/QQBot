from pkg.core.bot.event import loopHandler_run, Handler_loop
from pkg.core.bot.message import MessageList, NodeList
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

    def send_group_msg(self, group_id: int, msg: MessageList | list | NodeList):
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

    def send_friend_msg(self, user_id: int, msg: MessageList | list | NodeList):
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

    def send_group_forward_msg(self, group_id: int, msgs: NodeList):
        """
        发送群聊自定义合并转发。

        Args:
            group_id (int): 群号
            msgs (NodeList): 合并消息
        """
        data = {"group_id": group_id, "messages": str(msgs)}
        try:
            post(self.host, self.target_port, "/send_group_forward_msg", data)
            log.info(f"[群{group_id}] <- 发送合并转发")
        except:
            log.error(f"[群{group_id}] <- 发送合并转发失败。")

    def send_private_forward_msg(self, user_id: int, msgs: NodeList):
        """
        发送好友自定义合并转发。

        Args:
            user_id (int): 用户id
            msgs (NodeList): 合并消息
        """
        data = {"user_id": user_id, "messages": str(msgs)}
        try:
            post(self.host, self.target_port, "/send_private_forward_msg", data)
            log.info(f"[好友{user_id}] <- 发送合并转发")
        except:
            log.error(f"[好友{user_id}] <- 发送合并转发失败。")

    def upload_private_file(self, user_id: int, file: str, name: str):
        """
        发送好友文件。

        Args:
            user_id (int): 用户id
            file (str): 本地文件路径(绝对路径)
            name (str): 发送时所用文件名称
        """
        data = {"user_id": user_id, "file": file, "name": name}
        try:
            a = post(self.host, self.target_port, "/upload_private_file", data)
            log.info(f"[好友{user_id}] <- 从{file}发送文件{name}成功")
        except:
            log.error(f"[好友{user_id}] <- 从{file}发送文件{name}失败")

    def send_like(self, user_id: int, times: int):
        """
        个人名片点赞

        Args:
            user_id (int): 用户id
            times (int): 点赞次数
        """
        data = {"user_id": user_id, "times": times}
        try:
            post(self.host, self.target_port, "/send_like", data)
            log.info(f"[用户{user_id}] <- 为{user_id}点了{times}个赞")
        except:
            log.error(f"[用户{user_id}] <- 为{user_id}点了{times}个赞失败")

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

    def set_qq_avatar(self, file: str):
        """
        设置个人头像

        Args:
            file (str): 头像图片绝对路径, 支持 http, base64
        """
        data = {"file": f"file://{str(file)}"}
        try:
            post(self.host, self.target_port, "/set_qq_avatar", data)
            log.info(f"设置[{file}]的文件为头像, 成功")
        except:
            log.error(f"设置[{file}]的文件为头像, 失败")

    def set_qq_profile(self, nickname: str, company: str = "", email: str = "", college: str = "", personal_note: str = ""):
        """
        设置个人信息

        Args:
            nickname (str): 昵称
            company (str): 公司,默认为空
            email (str): 邮箱,默认为空
            college (str): 学校,默认为空
            personal_note (str): 个人说明,默认为空
        """
        data = {"nickname": str(nickname), "company": str(company), "email": str(email), "college": str(college), "personal_note": str(personal_note)}
        try:
            post(self.host, self.target_port, "/set_qq_profile", data)
            log.info(f"设置昵称为[{nickname}],公司为[{company}],邮箱为[{email}],学校为[{college}],个性签名为[{personal_note}], 成功")
        except:
            log.error(f"设置昵称为[{nickname}],公司为[{company}],邮箱为[{email}],学校为[{college}],个性签名为[{personal_note}], 失败")

    def start(self):
        """
        开始运行机器人。
        """
        log.info(f"开始监听端口{self.listen.port}...")
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
