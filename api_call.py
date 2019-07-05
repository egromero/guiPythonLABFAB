import requests
import json
from credentials import *


def get_data(uid):

	url_tarjeta_uc = 'https://api-lib.uc.cl/tarjetauc/v1/user/{0}?buscar=mifare'.format(uid)
	uc_card = requests.get(url_tarjeta_uc, headers = tarjeta_uc_credential).json()
	print('request', uc_card)
	data_tarjeta = uc_card['tarjetauc']['data']

	if isinstance(data_tarjeta, str):
		return data_tarjeta

	run = data_tarjeta['run']
	url_personas_uc = 'https://api-lib.uc.cl/personauc/v1/user/{0}'.format(run)
	persona_uc  = requests.get(url_personas_uc, headers = persona_uc_credential).json()
	data = persona_uc['datos_personales']['data']

	return {'rfid':  data['tarjetauc']['data']['cod_mifare'],
			'nombre': data['tarjetauc']['data']['nombre_titular'],
			'correo': data['login']+'@uc.cl',
			'rut': data['run'][:-1]+'-'+data['run'][-1],
			'sit_academica': data['rol'][0]['estado']}
	
