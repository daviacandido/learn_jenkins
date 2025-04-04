import os
import subprocess
import sys


def criar_ambiente_virtual(diretorio_projeto):
    if not os.path.exists(diretorio_projeto):
        print(f"O diretório '{diretorio_projeto}' não existe.")
        return

    venv_path = os.path.join(diretorio_projeto, 'venv')

    if os.path.exists(venv_path):
        print("O ambiente virtual já existe.")
        return

    try:
        subprocess.run(['virtualenv', venv_path], check=True)
        print("Ambiente virtual criado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o ambiente virtual: {e}")


def instalar_dependencias(diretorio_projeto, requirements_file):

    if not os.path.exists(requirements_file):
        print(f"O arquivo '{requirements_file}' não existe.")
        return

    venv_path = os.path.join(diretorio_projeto, 'venv', 'bin', 'activate')

    subprocess.run(['source', venv_path], shell=True)

    try:
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
        print("Dependências instaladas com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar as dependências: {e}")


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 nome.py /caminho/do/diretorio")
        sys.exit(1)

    diretorio_projeto = sys.argv[1]
    
    requirements_file = os.path.join(diretorio_projeto, 'requirements.txt')
    
    criar_ambiente_virtual(diretorio_projeto)
    
    instalar_dependencias(diretorio_projeto, requirements_file)


if __name__ == "__main__":
    main()

