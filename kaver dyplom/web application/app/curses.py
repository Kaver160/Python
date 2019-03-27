
import requests


def curses():
	usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
	res_u = requests.get(usd).json()
	name_u = res_u['Cur_Name']
	price_u = res_u['Cur_OfficialRate']
	u = str(name_u) +' : '+ str(price_u)
	eur = 'http://www.nbrb.by/API/ExRates/Rates/292'
	res_e = requests.get(eur).json()
	name_e = res_e['Cur_Name']
	price_e = res_e['Cur_OfficialRate']
	e = str(name_e) +' : '+ str(price_e)
	rub = 'http://www.nbrb.by/API/ExRates/Rates/298'
	res_r = requests.get(rub).json()
	name_r = res_r['Cur_Name']
	price_r = res_r['Cur_OfficialRate']
	r =str(name_r) +' : '+ str(price_r)
	funt = 'http://www.nbrb.by/API/ExRates/Rates/143'
	res_uh = requests.get(funt).json()
	name_uh = res_uh['Cur_Name']
	price_uh = res_uh['Cur_OfficialRate']
	fu =str(name_uh) +' : '+ str(price_uh)
	pln = 'http://www.nbrb.by/API/ExRates/Rates/293'
	res_p = requests.get(pln).json()
	name_p = res_p['Cur_Name']
	price_p = res_p['Cur_OfficialRate']
	p = str(name_p) +' : '+ str(price_p)


	curses = [str(u)+ ';  '+str(e)+';  '+str(r)+';    '+str(fu)+'; '+str(p)]

	return curses
