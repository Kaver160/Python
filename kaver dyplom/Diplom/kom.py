import requests
def weather():
	city_id = 625144
	appid = "812e89737fcf7992cc92812abee5c137"
	res = requests.get("http://api.openweathermap.org/data/2.5/weather",
	    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()
	return (),	('состояние погоды,сегодня в Минске:', data['weather'][0]['description']), ('Температура воздуха:', data['main']['temp']), ('минимальная температура:', data['main']['temp_min']), ('максимальная температура:', data['main']['temp_max'])
def usdl():

	usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
	response = requests.get(usd).json()
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(name), str(price)
def rubl():
	rub = 'http://www.nbrb.by/API/ExRates/Rates/298'
	response = requests.get(rub).json()
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(name),str(price)
def uahl():
	funt = 'http://www.nbrb.by/API/ExRates/Rates/143'
	response = requests.get(funt).json()
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(name),str(price)
def eurl():
	eur = 'http://www.nbrb.by/API/ExRates/Rates/292'
	response = requests.get(eur).json()
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(name),str(price)
def plnl():
	pln = 'http://www.nbrb.by/API/ExRates/Rates/293'
	response = requests.get(pln).json()
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(name),str(price)
