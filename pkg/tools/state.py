state: dict = {"event_transmit": True}  # 事件传递的状态


def setEventTransmit(value: bool) -> None:
    state["event_transmit"] = value
