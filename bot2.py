import requests
url = "https://api.telegram.org/bot{}/"
token= '796798672:AAGbbJYA9RaQOh35bDPZsnEzFnsc6fuhnxY'
def get_updates(token):
    responce = requests.get(url.format(token))
    return resolt.json()
def get_last_message():
    data = get_updates()

	posl_object = data['result'][-1]

	update_id = posl_object['update_id']
    posl_update_id = 0
	if posl_update_id != update_id:
		posl_update_id = update_id

		chat_id = posl_object['message']['chat']['id']
		message_text = posl_object['message']['text']

		message = {'chat_id': chat_id,
					'text': message_text}
		return message
	else:
		return None
def send_message(chat_id, text='Wait a second, please...'):
	url = url + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)

	requests.get(url)
