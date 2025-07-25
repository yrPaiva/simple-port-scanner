# Simple Port Scanner & Vulnerability Checker

Projeto em Python para varrer portas TCP e identificar serviços potencialmente vulneráveis.


## Pré‑requisitos
- Python 3.8+  
- (opcional) Git, pytest

## Como usar

1. Clone o repositório e entre na pasta:
   ```bash
   git clone https://github.com/yrPaiva/simple-port-scanner.git
   cd simple-port-scanner

3. Crie o ambiente virtual:
    ```bash
    python -m venv .venv

4. Ative o ambiente virtual
    ```bash
    PowerShell:
        .\.venv\Scripts\Activate.ps1

    CMD:
        .venv\Scripts\activate

    Bash / WSL / macOS / Linux:
        source .venv/bin/activate

5. Instale as dependências: 
    ```bash
    pip install -r requirements.txt

6. Execute o script principal:
    ```bash
    python src/main.py <host> -p 1-1024 -t 0.3

        <host>: IP ou domínio a ser escaneado
        -p: portas (ex.: 22,80,443 ou 1-1000)
        -t: timeout de conexão (segundos)

7. Executar testes (opicional):
    ```bash
    pytest
