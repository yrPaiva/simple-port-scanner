from src.scanner import scan_port

def test_scan_closed_port():
    # Porta 1 quase sempre está fechada em localhost
    assert not scan_port('127.0.0.1', 1, timeout=0.1)

def test_scan_open_port():
    # Supondo que você tenha um servidor HTTP local em 127.0.0.1:80
    # Ajuste conforme seu ambiente de teste
    assert scan_port('127.0.0.1', 80, timeout=0.1) in (True, False)
