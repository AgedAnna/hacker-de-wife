import subprocess


def obter_senha_wifi(nome_rede):
    try:
        # executar o comando para obter as informações da rede Wi-Fi
        output = subprocess.check_output(["netsh", "wlan", "show", "profile", "name=" + nome_rede, "key=clear"],
                                         shell=True)
        output = output.decode("utf-8")

        # encontrar a senha na saída do comando
        for linha in output.split('\n'):
            if "Conteúdo da Chave" in linha:
                pos = linha.find(":")
                senha = linha[pos + 2:].strip()
                return senha

        # se a senha não foi encontrada, retornar None
        return None

    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando: ", e.output)


# Chame a função para obter a senha da rede Wi-Fi especificada
senha = obter_senha_wifi("DTEL_MELO_2.4")

# Verifique se a senha foi obtida corretamente
if senha:
    print("A senha da rede Wi-Fi é:", senha)
else:
    print("Não foi possível obter a senha da rede Wi-Fi.")