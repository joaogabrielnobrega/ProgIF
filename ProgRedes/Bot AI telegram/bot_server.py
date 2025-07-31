import os, sys, requests, platform, logging
from pynput import keyboard
#from funcoes_bot import funcoes
#from bot_token import token

logging.basicConfig(level=logging.info, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler('bot_ai_telegram.log')])

logger = logging.getLogger(__name__)

URL_base = f'https://api.telegram.org/bot{token_api}'
URL_get_updates = f'{URL_base}/getUpdate'
URL_send_message = f'{URL_base}/sendMessage'
URL_send_image = f'{URL_base}/sendPhoto'

