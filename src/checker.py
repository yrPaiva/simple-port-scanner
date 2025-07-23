import json
from pathlib import Path
from typing import Dict

def load_vulnerable_ports(path: str = 'data/vulnerable_ports.json'
                         ) -> Dict[int, str]:
    """
    Lê JSON e converte chaves para int.
    """
    raw = json.loads(Path(path).read_text())
    return {int(p): desc for p, desc in raw.items()}

def check_vulnerabilities(open_ports: list[int],
                          vuln_map: Dict[int, str]
                         ) -> Dict[int, str]:
    """
    Para cada porta aberta que exista em vuln_map, retorna descrição.
    """
    return {p: vuln_map[p] for p in open_ports if p in vuln_map}
