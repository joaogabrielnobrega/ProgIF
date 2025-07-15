import os
from funcoes import *

# --------------------------------------------------------------------------------
host_server_ip    = getLocalIP()
host_port         = 40000

page_code         = 'utf-8'
buffer_size       = 512

server_img_dir   = os.path.dirname(__file__) + '\\server_files\\'
client_img_dir   = os.path.dirname(__file__) + '\\client_files\\'
# --------------------------------------------------------------------------------