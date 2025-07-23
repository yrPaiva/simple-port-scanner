import socket
from typing import Iterator, Tuple

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Tenta conectar em (host, port). Retorna True se aberta.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def scan_ports(host: str, ports: Iterator[int], timeout: float = 1.0
              ) -> Iterator[Tuple[int, bool]]:
    """
    Varre uma sequência de portas, yield (porta, está_aberta).
    """
    for port in ports:
        status = scan_port(host, port, timeout)
        yield port, status
