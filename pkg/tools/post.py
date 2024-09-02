import socket, json
from pkg.tools.log import log


def post(host: str, port: int, path: str, data: dict) -> str | None:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        msg = json.dumps(data)
        header = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/json\r\nContent-Length: {len(msg)}\r\n\r\n"
        s.send(header.encode() + msg.encode())
        re = s.recv(1024).decode()
    except Exception as e:
        log.error(f"post error: {e}")
    return re
