# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from itertools import groupby

GROUP_ID = 210137294

api = ""
vk_session = vk_api.VkApi(token=api)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vip = ['-210137294','61789896','632240112','555657232','322346076']


def sender(id, text):
    vk_session.method('messages.send', {'peer_id': id, 'message': text, 'random_id': 0})


def get_members(group_id, peer_id):
    result = vk_session.method('messages.getConversationMembers',
                                   {'peer_id': id,
                                    'group_id': group_id})  # максимально 200
    user_ids = [item["member_id"] for item in result["items"]]
    return user_ids

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        id = event.object.message["peer_id"]
        msg = event.object.message["text"].lower()
        text = event.object["message"]["text"].lower()   #получаем текст сообщения для дальнейшей записи
        u_id = event.object["message"]["from_id"]
        # print(msg)
        # print(id)

        # date = datetime.now()
        # # print(date)
        #
        # with open("meassage.txt", "a+") as file:
        #     file.write("{0},{1},{2},{3} \n".format(date, text, "id", u_id))

        with open("id_deys.txt", "a+") as file:
            file.write("{}\n".format(u_id))


        if "action" in event.object.message:
            dey = event.object.message["action"]['type']
            invite_id = event.object.message["action"]['member_id']
            if dey == 'chat_invite_user':
                sender(id, f'добро пожаловать,@id{invite_id}, '
                           f'Добро пожаловать в секту коллекционеров снаряги и военных вещей.'
                           f'1. Запрещено переходить на личности и оскорбление родных.'
                           f'2. Продажа и обмен снаряжения приветствуются ( администрация не несет ответственности и не выступает гарантом)'
                           f'3. Делится фотографиями, видео коллекций категорически приветствуется.'
                           f'4. Запрещено использовать команду . @.all. Исключения админы и крайне важные сообщения.'
                           f'5. Розжиг межнациональной розни, призывы к терроризму или другим радикальным и незаконным поступкам.'
                           f'6. Наказание на усмотрение администрации.'
                           f'7. Общение исключительно на Русском и Русском матерном языках.'
                           f'8. Запрещена продажа огнестрельного и холодного оружия в беседе и группе.'
                           f'1. Предупреждение.'
                           f'2. Кик из беседы на временной или постоянной основе.'
                           f'3. Внесения в черный список группы и сообщества, и всеобщее порицание.'
                           f'Друзья, вы сами пришли в беседу, и зайдя согласились с правилами'
                           f'.Наша беседа создана объединить людей с общими интересами со всего мира.Слава снаряге.'
                           f'1. Не бывает плохой снаряге, бывают далбаебы.'
                           f'2. Пуговица китель бережет.'
                           f'3. Собирай все, собирай много'
                           f'Хэштеги.'
                           f'#продажа_снаряги'
                           f'#куплю'
                           f'#обменяю'
                           f'#крафт'
                           f'#интересное'
                           f'#моя_снаряга'
                           f'#ищу#вопросы#предложения')
        else:
            if msg == 'привет':
                sender(id, 'Слава снаряге!)')
            if msg == 'all_ids':
                members_id = get_members(GROUP_ID, id)
                sender(id, "\n".join(map(str, members_id)))
            if msg == 'gnevimperatora':
                members_id = list(get_members(GROUP_ID, id))#получаем все ид беседы
                with open('id_deys.txt') as f:
                    content = f.readlines()
                content = [x.strip() for x in content] #получаем ид всех кто писал из файла
                content = content + vip
                sor = sorted(content)#сортировка по порядку
                message_day = [el for el, _ in groupby(sor)]#
                a = tuple(map(str, members_id))#преобразует members_id в вид ['id']
                spis_del = list(set(a) - set(message_day))#
                print(spis_del)#
                for x in spis_del:#проход по списку на удаление
                    print(x)
                    vk_session.method("messages.removeChatUser",
                              {
                                  "chat_id": 5,
                                  "user_id": x
                              }
                              )


