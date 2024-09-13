class Text:
    """
    文本消息。

    Args:
        text (str): 文本内容。
    """

    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        if isinstance(other, Text):
            return Text(self.text + other.text)
        if isinstance(other, (Image, Record, Face, At)):
            return MessageList([self, other])
        raise TypeError(f"Text不能与{type(other)}相加")

    def __str__(self) -> str:
        return self.text


class Image:
    """
    图片消息。

    Args:
        image_url (str): 图片链接。
    """

    def __init__(self, image_url: str):
        self.image_url = image_url

    def __add__(self, other):
        if isinstance(other, (Text, Record, Face, At, Image)):
            return MessageList([self, other])
        raise TypeError(f"Image不能与{type(other)}相加")

    def __str__(self) -> str:
        return f"[CQ:image,file={self.image_url}]"


class Face:
    """
    表情消息。

    Args:
        face_id (str): 表情 ID。
    """

    def __init__(self, face_id: int):
        self.face_id = face_id

    def __add__(self, other):
        if isinstance(other, (Text, Record, Image, At, Face)):
            return MessageList([self, other])
        raise TypeError(f"Face不能与{type(other)}相加")

    def __str__(self) -> str:
        return f"[CQ:face,id={self.face_id}]"


class Record:
    """
    语音消息。

    Args:
        record_url (str): 语音链接。
    """

    def __init__(self, record_url: str):
        self.record_url = record_url

    def __add__(self, other):
        if isinstance(other, (Text, Image, Face, At, Record)):
            return MessageList([self, other])
        raise TypeError(f"Record不能与{type(other)}相加")

    def __str__(self) -> str:
        return f"[CQ:record,file={self.record_url}]"


class At:
    """
    @消息。

    Args:
        at_id (str): 被@的 ID。
    """

    def __init__(self, at_id: int):
        self.at_id = at_id

    def __add__(self, other):
        if isinstance(other, (Text, Image, Face, Record, At)):
            return MessageList([self, other])
        raise TypeError(f"At不能与{type(other)}相加")

    def __str__(self) -> dict:
        return f"[CQ:at,qq={self.at_id}]"


class Node:
    """
    合并消息节点。

    Args:
        name (str): 发送者显示的名字。
        uin (int): 发送者QQ 号。
        content (str): 消息内容(目前仅支持文字)。

    """

    def __init__(self, name, uin, content):
        self.name = name
        self.uin = uin
        self.content = content

    def __str__(self) -> dict:
        return f"[CQ:node,name={self.name},uin={self.uin},content={self.content}]"

    def __add__(self, other):
        if isinstance(other, Node):
            return NodeList([self, other])
        raise TypeError(f"Node不能与{type(other)}相加")


class NodeList:
    """
    合并消息。

    Args:
        array (list): 消息列表。
    """

    def __init__(self, array: list):
        self.array = array

    def __str__(self):
        return "".join([str(node) for node in self.array])


def toMessage(message: dict) -> Text | Image | Face | Record | At:
    """
    将消息转换为消息对象。
    """
    if message["type"] == "text":
        return Text(message["data"]["text"])
    if message["type"] == "image":
        return Image(message["data"]["file"])
    if message["type"] == "face":
        return Face(message["data"]["id"])
    if message["type"] == "record":
        return Record(message["data"]["file"])
    if message["type"] == "at":
        return At(int(message["data"]["qq"]))


class MessageList:
    """
    消息列表。
    """

    def __init__(self, messages: list):
        self.messages = messages

    def __add__(self, other):
        if isinstance(other, MessageList):
            return MessageList(self.messages + other.messages)
        if isinstance(other, (Text, Image, Face, Record, At)):
            return MessageList(self.messages + [other])

    def append(self, message) -> None:
        """
        将消息添加到消息列表中。
        """
        if isinstance(message, str):
            self.messages.append(Text(message))
            return
        if isinstance(message, (Text, Image, Face, Record, At)):
            self.messages.append(message)

    def __str__(self) -> str:
        return "".join([str(message) for message in self.messages])

    def __eq__(self, text: str) -> bool:
        return str(self) == str(text)

    def find(self, text: str) -> int:
        """
        在消息列表中查找指定文本。

        Args:
            text (str): 要查找的文本。
        Return:
            int | None: 如果找到，返回索引；否则返回 -1
        """
        return str(self).find(text)

    def haveImage(self) -> bool:
        """
        判断消息列表中是否有图片。
        """
        for message in self.messages:
            if isinstance(message, Image):
                return True
        return False

    def haveAt(self) -> bool:
        """
        判断消息列表中是否有@。
        """
        for message in self.messages:
            if isinstance(message, At):
                return True
        return False

    def haveFace(self) -> bool:
        """
        判断消息列表中是否有表情。
        """
        for message in self.messages:
            if isinstance(message, Face):
                return True
        return False

    def onlyText(self) -> bool:
        """
        判断消息列表中是否只有文本。
        """
        for message in self.messages:
            if not isinstance(message, Text):
                return False
        return True

    def getImage(self, index=False) -> list[Image] | list[int]:
        """
        获取消息列表中的所有图片。
        """
        images = []
        if index:
            for i in range(len(self.messages)):
                if isinstance(self.messages[i], Image):
                    images.append(i)
        else:
            for message in self.messages:
                if isinstance(message, Image):
                    images.append(message)
        return images

    def getFace(self, index=False) -> list[Face] | list[int]:
        """
        获取消息列表中的所有表情。

        Args:
            index (bool): 是否返回索引。默认为 False。
        """
        faces = []
        if index:
            for i in range(len(self.messages)):
                if isinstance(self.messages[i], Face):
                    faces.append(i)
        else:
            for message in self.messages:
                if isinstance(message, Face):
                    faces.append(message)
        return faces

    def getAt(self, index=False) -> At | int | None:
        """
        获取消息列表中的第一个@。

        Args:
            index (bool): 是否返回索引。默认为 False。
        """
        if index:
            for i in range(len(self.messages)):
                if isinstance(self.messages[i], At):
                    return i
            return None
        else:
            for message in self.messages:
                if isinstance(message, At):
                    return message

    def getMessage(self, index=0) -> Text | Image | Face | Record | At:
        """
        获取消息列表中的指定消息。

        Args:
            index (int): 获取的消息的索引。默认为 0。
        """
        return self.messages[index]

    def pop(self, index=0) -> Text | Image | Face | Record | At:
        """
        弹出消息列表中的指定消息。

        Args:
            index (int): 弹出的消息的索引。默认为 0。
        """
        return self.messages.pop(index)
