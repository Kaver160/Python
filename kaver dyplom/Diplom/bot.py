import requests
from helper import get_weather_today
bot_token = '796798672:AAGbbJYA9RaQOh35bDPZsnEzFnsc6fuhnxY'
adress = 'https://api.telegram.org/bot{}/'
req = requests.get('https://api.telegram.org/bot{}/'.format(bot_token))
global last_update_id
last_update_id = 0
def get_updates ():
	resultat = requests.get(adress.format(bot_token)+'getupdates')
	return resultat.json()
#print (get_updates())

def get_message():

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
#print(last_messaga())
def send_messsag(text_messag):
    if type(text_messag) == str:
        send = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format(text_messag))
        return(send)
    else:
        p = type(text_messag)
        send = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format('тип сообщения ' + str(p)+' введите текстовый'))
        return(send)
#send_messsag(123123)
def funt():
    curs =requests.get('http://www.nbrb.by/API/ExRates/Rates/143')
    json_dict = curs.json()
    funt = ['Cur_OfficialRate']
    return curs.json()
def post_funt():
    getcurr=funt()
    curr_rate = getcurr['Cur_OfficialRate']
    sender = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format('Курс фунта равен ' + str(curr_rate)))
    return sender
#post_funt()
def euro():
    curs = requests.get('http://www.nbrb.by/API/ExRates/Rates/292')
    json_dict=curs.json()
    euro = ['Cur_OfficialRate']
    return curs.json()
def euro_post():
    getcurr=euro()
    curr_rate = getcurr['Cur_OfficialRate']
    sender = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format('Курс евро равен ' + str(curr_rate)))
    return sender
#euro_post()
def Rub():
    curs = requests.get('http://www.nbrb.by/API/ExRates/Rates/298')
    json_dict = curs.json()
    Rub = ['Cur_OfficialRate']
    return curs.json()
def post_rub():
    getcurr=Rub()
    curr_rate = getcurr['Cur_OfficialRate']
    sender = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format('Курс российского рубля равен ' + str(curr_rate)))
    return sender
#post_rub()
def USD ():
	curs =requests.get('http://www.nbrb.by/API/ExRates/Rates/145')
	json_dict = curs.json()
	dollar = ['Cur_OfficialRate']
	return curs.json()
def post_dollar ():
	getcurr=USD()
	curr_rate = getcurr['Cur_OfficialRate']
	sender = requests.post(adress.format(bot_token)+'sendmessage?chat_id=425899004&text={}'.format('Курс доллара равен ' + str(curr_rate)))
	return sender
post_dollar()
def main():
    while True:
        answer = get_message()
        if answer !=None:
            chat_id = answer['chat_id']
            text = answer['text']


            if text =='погода':
                send_messsag(chat_id,get_weather_today())

if __name__=='__main__':
        main()
