import requests

bot_token = '796798672:AAGbbJYA9RaQOh35bDPZsnEzFnsc6fuhnxY'
adress = 'https://api.telegram.org/bot{}/'

def get_updates ():
	resultat = requests.get(adress.format(bot_token)+'getupdates')
	return resultat.json()
#print (get_updates())

def last_messaga ():
	updates = get_updates()
	chat_id = updates['result'][-1]
	text = chat_id['message']['text']
	return text

#print  (last_messaga())

def post_messsag (text_messag):
	send = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format(text_messag))
	return text_messag
#post_messsag('123bot')
def USD ():
	curs =requests.get('http://www.nbrb.by/API/ExRates/Rates/145')
	json_dict = curs.json()
	dollar = ['Cur_OfficialRate']
	return curs.json()

def post_dollar ():
	getcurr=USD()
	curr_rate = getcurr['Cur_OfficialRate']

	sender = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format(curr_rate))
	return sender
post_dollar()
