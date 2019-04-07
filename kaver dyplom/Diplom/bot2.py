import requests
from adres import privet
from kom import usdl, rubl, eurl, uahl, eurl, plnl, weather
from time import sleep
from movie import MoviesList
URL = 'https://api.telegram.org/bot' + privet + '/'
chat_id='425899004'
global last_update_id
last_update_id = 0
def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()
print(get_updates())
def last_message():
	data = get_updates()
	last_object = data['result'][-1]
	update_id = last_object['update_id']
	global last_update_id
	if last_update_id != update_id:
		last_update_id = update_id
		chat_id = last_object['message']['chat']['id']
		message_text = last_object['message']['text']
		message = {'chat_id': chat_id,
					'text': message_text}
		return message
	return None

def send_message(chat_id, text='Wait a second, please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)
def main():
	while True:
		glavnae = last_message()
		if glavnae != None:
			chat_id = glavnae['chat_id']
			text = glavnae['text']
			if ((text == 'Курсы')|(text=='Курс')|(text == 'курсы')|(text=='курс')):
				send_message(chat_id, usdl())
				send_message(chat_id, eurl())
				send_message(chat_id, rubl())
				send_message(chat_id, uahl())
				send_message(chat_id, plnl())
			if ((text == 'Погода')|(text=='погода')):
				send_message(chat_id, weather())
			if ((text == 'Кино Сегодня')|(text=='кино сегодня')):
				send_message(chat_id, MoviesList().create_movies_list())
		else:
			continue
if __name__ == '__main__':
	main()
