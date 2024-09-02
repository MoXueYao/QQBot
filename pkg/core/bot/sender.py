class Sender:
    """
    发送者类。

    Args:
        user_id (int): 发送者的QQ号。
        nickname (str): 发送者的昵称。
        card (str): 发送者的群名片。
    """

    def __init__(self, user_id: int, nickname: str, card: str):
        self.user_id = user_id
        self.nickname = nickname
        self.card = card

    def __str__(self):
        return f"{self.user_id}"
