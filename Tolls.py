#bin/python
# Author : Angga rismayana

# ---> Tidak Diperuntukan Untuk Di Recode <---

from lib.admin_finder import *
from lib.subdo_scaner import *
from lib.extract_link import *
from lib.quotes import *
from lib.create_sandi import *
from lib.Myip import *
from lib.iplocation import *
from lib.call import *
from lib.sms import *
from lib.short import *
from lib.infophone import *
from lib.gempa import *

UNGU = '\033[95m'
BIRU = '\033[94m'
HIJAU = '\033[92m'
KUNING = '\033[93m'
MERAH = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[97m'
LORD = '\033[1;47m'
CMIW = '\033[2;34m'
BLACK = '\033[2;30m'

_logo_hemkel = lambda: print(f"\n{CMIW}  ╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦  ╔╦╗╔═╗╔═╗╦  ╔═╗\n   ║ ║╣ ╠╦╝║║║║ ║╔╩╦╝   ║ ║ ║║ ║║  ╚═╗\n   ╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═   ╩ ╚═╝╚═╝╩═╝╚═╝\n   {LORD}\033[2;30m   By : Angga rismayana | Mafia Teknologi    {ENDC}")

class Main:

	def __init__(self):
		self._Menu()

	def _Menu(self):
		try:
			__import__('os').system('clear');_logo_hemkel()
			print(f"\n     {CMIW}01 {ENDC}Scaner Admin Finder\n     {CMIW}02 {ENDC}Subdomain Scaner\n     {CMIW}03 {ENDC}Extract Page Site\n     {CMIW}04 {ENDC}Random Quotes\n     {CMIW}05 {ENDC}Create Sandi Password\n     {CMIW}06 {ENDC}Check My Ip Address\n     {CMIW}07 {ENDC}IpLocation Tracker\n     {CMIW}08 {ENDC}Spaming Call\n     {CMIW}09 {ENDC}Spaming Sms\n     {CMIW}10 {ENDC}Short Url / Pemendek Url\n     {CMIW}11 {ENDC}Phone Number Information\n     {CMIW}12 {ENDC}Information Gempa\n     {CMIW}00 {ENDC}Exit Program\n")
			menu = input("     {}➤ {}Choose : ".format(EBLE,ENDC,BOLD))

			if menu in ("1","01"):
				Admin()
			elif menu in ("2","02"):
				Subdo()
			elif menu in ("3","03"):
				Link()
			elif menu in ("4","04"):
				quote()
			elif menu in ("5","05"):
				Sandi()
			elif menu in ("6","06"):
				My()
			elif menu in ("7","07"):
				Ip()
			elif menu in ("8","08"):
				Call()
			elif menu in ("9","09"):
				Sms()
			elif menu in("10","10"):
				Short()
			elif menu in ("11","11"):
				Phone()
			elif menu in ("12","12"):
				Gempa()
		except:
			pass

if __name__=='__main__':
	Main()
