import argparse
from scanner import scan_ports
from checker import load_vulnerable_ports, check_vulnerabilities
from colorama import Fore, Style, init

def parse_args():
    p = argparse.ArgumentParser(
        description="Simple Port Scanner + Vulnerability Checker"
    )
    p.add_argument('host', help="IPv4 ou hostname alvo")
    p.add_argument(
        '-p', '--ports',
        default="1-1024",
        help="Intervalo de portas, ex: 20-80 ou lista: 22,80,443"
    )
    p.add_argument('-t', '--timeout', type=float, default=0.5)
    return p.parse_args()

def expand_ports(spec: str) -> list[int]:
    parts = spec.split(',')
    ports = []
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-', 1))
            ports += list(range(start, end+1))
        else:
            ports.append(int(part))
    return sorted(set(ports))

def main():
    init(autoreset=True)
    args = parse_args()
    ports = expand_ports(args.ports)
    print(f"Scanning {args.host} on {len(ports)} ports...")

    open_ports = []
    for port, is_open in scan_ports(args.host, ports, args.timeout):
        if is_open:
            print(f"{Fore.GREEN}[OPEN]  Port {port}{Style.RESET_ALL}")
            open_ports.append(port)

    vuln_map = load_vulnerable_ports()
    vulns = check_vulnerabilities(open_ports, vuln_map)
    if vulns:
        print(f"\n{Fore.RED}Detected potential vulnerabilities:{Style.RESET_ALL}")
        for p, desc in vulns.items():
            print(f" - Port {p}: {desc}")
    else:
        print(f"\n{Fore.CYAN}No common vulnerable services detected.{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
