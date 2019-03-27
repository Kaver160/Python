import requests
def get_weather_today():
	city_id = 625144
	appid = "812e89737fcf7992cc92812abee5c137"

	res = requests.get("http://api.openweathermap.org/data/2.5/weather",
	    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()
	return ("Сегодня:", 'В минске'),	("состояние погоды:", data['weather'][0]['description']), ("Температура воздуха:", data['main']['temp']), ("минимальная температура:", data['main']['temp_min']), ("максимальная температура:", data['main']['temp_max'])
