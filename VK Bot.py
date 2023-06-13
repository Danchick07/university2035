import vk_api
from vk_api.longpoll import VkLongpoll
token = 'vk1.a.xtxt-SJ7TDAxUrFSbczFrUJ-VV9JXR-DL-umAVmeLo4VSEg-EoMdrnm96k_4FmVrfv7iWc-EXYg6IlkxSOyU2AFkz6Up7PtBcknSUSUJAHlwZj7RRI3Y5mRGbyMxX5gTTfIneVR8zssWp-BokZZKSPUuUFU8KuDeeh0DiIw8VFrT2y2Lsj0zQU-_ufnZElKk-Vs6-TnHRyz1RpWWsrDDYQ'

vk_session = vk_api.VkApi(token=token) # Подключение к сообществу

vk = vk_session.get_api() # Получили доступ к API VK

longpoll = VkLongpoll(vk_session)

while True:
    messages = vk.messages.getConversations(count=20, filter='unanswered') # выгрзука всех диалгов
    if messages['count'] >= 1:
        message_text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['random_id']
        if message_text.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Привет!!! Как твои дела?')

            import vk_api
            import requests

            token = 'vk1.a.xtxt-SJ7TDAxUrFSbczFrUJ-VV9JXR-DL-umAVmeLo4VSEg-EoMdrnm96k_4FmVrfv7iWc-EXYg6IlkxSOyU2AFkz6Up7PtBcknSUSUJAHlwZj7RRI3Y5mRGbyMxX5gTTfIneVR8zssWp-BokZZKSPUuUFU8KuDeeh0DiIw8VFrT2y2Lsj0zQU-_ufnZElKk-Vs6-TnHRyz1RpWWsrDDYQ'

            vk_session = vk_api.VkApi(token=token)  # Подключение к сообществу

            vk = vk_session.get_api()  # Получили доступ к API VK

            url = 'https://swapi.dev/api/'
            response = requests.get(url).json()
            starships_api = response['starships']


            def check_starships(url):
                for i in range(2, 11):
                    response = requests.get(url + str(i)).json()
                    print(response['name'], response['max_atmosphering_speed'])


            check_starships(starships_api)

            url = 'https://swapi.dev/api/'

            response = requests.get(url).json()

            planets_api = response['planets']


            def check_planets(url):
                for i in range(1, 6):
                    response = requests.get(url + str(i)).json()
                    print(response['name'], response['diameter'])


            check_planets(planets_api)

            while True:
                messages = vk.messages.getConversations(count=20, filter='unanswered')  # выгрзука всех диалгов
                if messages['count'] >= 1:
                    message_text = messages['items'][0]['last_message']['text']
                    user_id = messages['items'][0]['last_message']['from_id']
                    message_id = messages['items'][0]['last_message']['random_id']
                    if message_text.lower() == 'привет':
                        vk.messages.send(user_id=user_id, random_id=message_id, message='Привет!!! Как твои дела?')
                    if message_text.lower() == 'планеты':
                        vk.messages.send(user_id=user_id, random_id=message_id, message=check_planets)
                    if message_text.lower() == 'корабли':
                        vk.messages.send(user_id=user_id, random_id=message_id, message=check_starships)


#ВТОРОЕ ЗАНЯТИЕ
import vk_api
from vk_api.longpoll import VkLongPoll

token = 'vk1.a.xtxt-SJ7TDAxUrFSbczFrUJ-VV9JXR-DL-umAVmeLo4VSEg-EoMdrnm96k_4FmVrfv7iWc-EXYg6IlkxSOyU2AFkz6Up7PtBcknSUSUJAHlwZj7RRI3Y5mRGbyMxX5gTTfIneVR8zssWp-BokZZKSPUuUFU8KuDeeh0DiIw8VFrT2y2Lsj0zQU-_ufnZElKk-Vs6-TnHRyz1RpWWsrDDYQ'

vk_session = vk_api.VkApi(token=token) # Подключение к сообществу

vk = vk_session.get_api() # Получили доступ к API VK

longpoll = VkLongPoll(vk_session) # Создали длинный запрос

for event in longpoll.listen():
    if event.type == 4 and event.to_me:
        text = event.text
        user_id = event.user_id
        message_id = event.message_id
        if text.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Привет! Как твои дела?')
        else:
            vk.messages.send(user_id=user_id, random_id=message_id, message='Я не понял тебя! :(')


import vk_api
from vk_api.longpoll import VkLongPoll

token = 'vk1.a.xtxt-SJ7TDAxUrFSbczFrUJ-VV9JXR-DL-umAVmeLo4VSEg-EoMdrnm96k_4FmVrfv7iWc-EXYg6IlkxSOyU2AFkz6Up7PtBcknSUSUJAHlwZj7RRI3Y5mRGbyMxX5gTTfIneVR8zssWp-BokZZKSPUuUFU8KuDeeh0DiIw8VFrT2y2Lsj0zQU-_ufnZElKk-Vs6-TnHRyz1RpWWsrDDYQ'

vk_session = vk_api.VkApi(token=token) # Подключение к сообществу

vk = vk_session.get_api() # Получили доступ к API VK

longpoll = VkLongPoll(vk_session) # Создали длинный запрос

for event in longpoll.listen():
    if event.type == 4 and event.to_me:
        text = event.text
        user_id = event.user_id
        message_id = event.message_id
        if text.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Привет! Как твои дела?')
        elif text.lower() == 'хорошо':
            vk.messages.send(user_id=user_id, random_id=message_id, message='Я рад за тебя!!!')
        else:
            vk.messages.send(user_id=user_id, random_id=message_id, message='Я не понял тебя! :(')
