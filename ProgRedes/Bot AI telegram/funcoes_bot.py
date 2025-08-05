import os, requests
from pynput import keyboard

dir_app = os.path.dirname(__file__)
dir_img = f'{dir_app}/imagens'
dir_arq = f'{dir_app}/arquivos'

def getKey(key):
    if key == keyboard.Key.f10:
        print("\n<F10> precionado. Desligando bot.")
        return False

def showHelp() -> str:
    return "\nComandos disponíveis:\n\t/? - Exibe os comandos\n\t/fat:n - Calcula o fatorial de n\n\t/fib:n - Exibe os n primeiros elementos da sequência de Fibonacci\n\t/img:nome_arquivo - Envia o arquivo [nome_arquivo] do servidor para o Telegram"

def welcome() -> str:
    return "Olá! Bem-vindo ao bot.\nUse /? para ver os comandos disponíveis."

def sendImage(nome_arquivo: str, chat_id: int, URL_send_image: str, logger) -> str:
    try:
        if not os.path.exists(dir_img):
            return f"Erro: O diretório de imagens {dir_img} não foi encontrado"
        
        nome_arquivo_str = f"{dir_img}/{nome_arquivo}"
        
        if not os.path.exists(nome_arquivo_str):
            return f"Erro: Arquivo {nome_arquivo} não encontrado"
        
        with open(nome_arquivo_str, 'rb') as file:
            files = {'photo': file}
            data = {'chat_id': chat_id}
            reply = requests.post(URL_send_image, files=files, data=data)
        
        if reply.status_code == 200:
            return f"Aviso: Arquivo {nome_arquivo} enviado com sucesso!"
        else:
            msg_erro_str = f"Erro: Falha ao enviar o arquivo. Código de retorno: {reply.status_code}\nResposta: {reply.text}"
            logger.error(msg_erro_str)
            return msg_erro_str
    except Exception as e:
        msg_erro_str = f"Erro: Erro ao enviar imagem: {e}"
        logger.error(msg_erro_str)
        return msg_erro_str

def processMessage(message, URL_send_message: str, URL_send_image: str, logger):
    try:
        comando_str = message.get('text', '')
        chat_id_int = message['chat']['id']

        if comando_str.startwith('/'):
            partes_lst = comando_str.split(':')
            comando_str = partes_lst[0]
            parametro_str = partes_lst[1] if len(partes_lst) > 1 else None

            if comando_str in comando_dict.keys():
                if parametro_str:
                    if comando == '/img':
                        reply_msg_str = f'BOT: {comando_dict[comando_str](parametro_str, chat_id_int, URL_send_image, logger)}\nUsuário: {chat_id_int}'
                    else:
                        reply_msg_str = f'BOT: {comando_dict[comando_str](parametro_str)}\nUsuário: {chat_id_int}'
                else:
                    reply_msg_str = f'BOT: {comando_dict[comando_str](parametro_str)}\n:Usuário: {chat_id_int}'
            else:
                reply_msg_str = f'BOT: Comando não reconhecido\nUsuário:{chat_id_int}'
        else:
            reply_msg_str = f'BOT: comandos devem começar com [/]\nUsuário: {chat_id_int}'
        
        dados_dict = {'chat_id': chat_id_int, 'text': reply_msg_str}
        reqURL = requests.post(URL_send_message, data=dados_dict)

        if not reqURL.status_code == 200:
            logger.error(f'Erro: Erro ao enviar mensagem: {reqURL.status_code}')
    except Exception as e:
        logger.error(f'Erro: Erro ao processar mensagem: {e}')

comando_dict = {
    '/?' : showHelp,
    '/img': lambda n, chat_id, URL_send_image, logger: sendImage(n, chat_id, URL_send_image, logger)
}
