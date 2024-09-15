state: list = [True, True]
# state[0] 事件传递状态


def setEventTransmit(value: bool) -> None:
    state[0] = value


def getEventTransmit() -> bool:
    return state[0]
