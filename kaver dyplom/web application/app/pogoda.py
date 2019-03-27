import requests


def weather():

	city_name = "в Минске"
	city_id = 625144
	appid = "812e89737fcf7992cc92812abee5c137"

	res = requests.get("http://api.openweathermap.org/data/2.5/weather",
	    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()

	weather = [str(city_name)+': '+str(data['weather'][0]['description'])+',   '+ 'Скорость ветра:'+' '+str(data['wind']['speed'])+' '+'м/с'+',   '+"направление:"+' '+str(data['wind']['deg'])+',   '+"Температура воздуха"+': '+str(data['main']['temp']) +',   '+ "минимальная температура:"+' '+ str(data['main']['temp_min']) +',   '+ "максимальная температура:"+' '+str(data['main']['temp_max'])+',   '+"восход:"+' '+str(data['sys']['sunrise'])+',   '+"закат:"+' '+str(data['sys']['sunset'])]
	return weather
print(weather())
