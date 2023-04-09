import subprocess


def obter_senha_wifi(nome_rede):
    # Executar o comando para obter as informações da rede Wi-Fi
    cmd_output = subprocess.run(
        ["netsh", "wlan", "show", "profile", nome_rede, "key=clear"],
        capture_output=True,
        text=True
    )

    # Verificar se o comando executou com sucesso
    if cmd_output.returncode != 0:
        return None

    # Extrair a senha da saída do comando
    for linha in cmd_output.stdout.split('\n'):
        if "Conteúdo da Chave" in linha:
            senha = linha.split(":")[1].strip()
            return senha

    # Se a senha não foi encontrada, retornar None
    return None
    print("Não foi possível obter a senha da rede Wi-Fi.")