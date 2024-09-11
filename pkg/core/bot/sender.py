class Sender:
    """
    发送者类。

    Args:
        user_id (int): 发送者的QQ号。
        nickname (str): 发送者的昵称。
        card (str): 发送者的群名片。
        permission (int): 默认为1,发送者的权限。\n
            1: 普通成员
            2: 管理员
            3: 超级管理员
    """

    def __init__(self, user_id: int, nickname: str, card: str, permission: int = 1):
        self.user_id = user_id
        self.nickname = nickname
        self.card = card
        self.permission = permission

    def __str__(self):
        return f"{self.user_id}"
