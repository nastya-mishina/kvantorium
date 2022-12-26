import telebot

bot = telebot.TeleBot('5560452845:AAFsQwiG60h4USEQ8SzKpLrA52AObnFU1rg')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Расписание занятий', 'Работа в праздничные дни')
    keyboard.row('Бесплатные мероприятия', 'Платные услуги')
    keyboard.row('Свободные места', 'Информация о квантумах')
    keyboard.row('Информация о преподавателях', 'Правила кванторианца')
    keyboard.row('Контакты')

    bot.send_message(message.chat.id, 'Здравствуйте, уважаемые родители! Этот чат-бот поможет Вам узнать ответы на '
                                      'часто задаваемые вопросы. Если Вы не нашли ответ на свой вопрос - '
                                      'позвоните администратору по номеру *+7(910)875-20-54*.', reply_markup=keyboard,
                     parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def choose_a_category(message):
    directions_for_timetable = telebot.types.InlineKeyboardMarkup()
    directions_for_timetable.add(telebot.types.InlineKeyboardButton(text='IT - квантум',
                                                                    callback_data='IT_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Data - квантум',
                                                                    callback_data='Data_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='VR/AR - квантум',
                                                                    callback_data='VR/AR_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Промробоквантум',
                                                                    callback_data='Robo_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Хайтек',
                                                                    callback_data='Haytek_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Геоквантум',
                                                                    callback_data='Geo_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Медиаквантум',
                                                                    callback_data='Media_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Квантошахматы',
                                                                    callback_data='Quaintness_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Математика',
                                                                    callback_data='Math_for_timetable'),
                                 telebot.types.InlineKeyboardButton(text='Английский язык',
                                                                    callback_data='English_for_timetable'))

    directions_for_free_places = telebot.types.InlineKeyboardMarkup()
    directions_for_free_places.add(telebot.types.InlineKeyboardButton(text='IT - квантум',
                                                                      callback_data='IT_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Data - квантум',
                                                                      callback_data='Data_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='VR/AR - квантум',
                                                                      callback_data='VR/AR_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Промробоквантум',
                                                                      callback_data='Robo_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Хайтек',
                                                                      callback_data='Haytek_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Геоквантум',
                                                                      callback_data='Geo_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Медиаквантум',
                                                                      callback_data='Media_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Квантошахматы',
                                                                      callback_data='Quaintness_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Математика',
                                                                      callback_data='Math_for_free_places'),
                                   telebot.types.InlineKeyboardButton(text='Английский язык',
                                                                      callback_data='English_for_free_places'))

    directions_for_kvantum = telebot.types.InlineKeyboardMarkup()
    directions_for_kvantum.add(telebot.types.InlineKeyboardButton(text='IT - квантум',
                                                                  callback_data='IT_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Data - квантум',
                                                                  callback_data='Data_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='VR/AR - квантум',
                                                                  callback_data='VR/AR_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Промробоквантум',
                                                                  callback_data='Robo_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Хайтек',
                                                                  callback_data='Haytek_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Геоквантум',
                                                                  callback_data='Geo_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Медиаквантум',
                                                                  callback_data='Media_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Квантошахматы',
                                                                  callback_data='Quaintness_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Математика',
                                                                  callback_data='Math_for_kvantum'),
                               telebot.types.InlineKeyboardButton(text='Английский язык',
                                                                  callback_data='English_for_kvantum'))

    master_class_categories = telebot.types.InlineKeyboardMarkup()
    master_class_categories.add(telebot.types.InlineKeyboardButton(text='IT-квантум', callback_data='it_mk'),
                                telebot.types.InlineKeyboardButton(text='Data-квантум', callback_data='data_mk'),
                                telebot.types.InlineKeyboardButton(text='VR/AR-квантум', callback_data='vr_mk'),
                                telebot.types.InlineKeyboardButton(text='Промробоквантум', callback_data='robo_mk'),
                                telebot.types.InlineKeyboardButton(text='Хайтек', callback_data='haytek_mk'),
                                telebot.types.InlineKeyboardButton(text='Геоквантум', callback_data='geo_mk'),
                                telebot.types.InlineKeyboardButton(text='Семейные мастер классы',
                                                                   callback_data='family_mk'),
                                telebot.types.InlineKeyboardButton(text='Творческие мастер классы',
                                                                   callback_data='creative_mk'))

    directions_for_mentors = telebot.types.InlineKeyboardMarkup()
    directions_for_mentors.add(telebot.types.InlineKeyboardButton(text='IT - квантум',
                                                                  callback_data='IT_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Data - квантум',
                                                                  callback_data='Data_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='VR/AR - квантум',
                                                                  callback_data='VR/AR_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Промробоквантум',
                                                                  callback_data='Robo_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Хайтек',
                                                                  callback_data='Haytek_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Геоквантум',
                                                                  callback_data='Geo_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Медиаквантум',
                                                                  callback_data='Media_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Квантошахматы',
                                                                  callback_data='Quaintness_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Математика',
                                                                  callback_data='Math_for_mentors'),
                               telebot.types.InlineKeyboardButton(text='Английский язык',
                                                                  callback_data='English_for_mentors'))

    if message.text == 'Расписание занятий':
        bot.send_message(message.chat.id, text='❓ Уточните пожалуйста, расписание какого направления Вы хотите узнать?',
                         reply_markup=directions_for_timetable)
    elif message.text == 'Работа в праздничные дни':
        bot.send_message(message.chat.id, text='*❓ Вопрос: *\nРабота в праздничные дни\n\n*💡 Ответ:*\nМы не '
                                               'работаем:\n▪️31 декабря - 8 января\n▪️23 февраля\n▪️8 '
                                               'марта\n▪️1 мая\n▪️9 мая\n▪️12 июня\n▪️4 ноября', parse_mode='Markdown')
    elif message.text == 'Бесплатные мероприятия':
        bot.send_message(message.chat.id, text='*❓ Вопрос: *\nБесплатные мероприятия\n\n*💡 Ответ:*\nПриглашаем Вас '
                                               'посетить серию предновогодних мастер классов 💫\n\n*8 декабря, '
                                               '14:40*\n🎄 Мастер класс "Новогодняя игрушка"\n[Записаться]('
                                               'https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/activity/2479/?date'
                                               '=2022-12-08)\n\n*9 декабря, 14:40*\n🎥 Кинопоказ "Гринч"\n[Записаться]('
                                               'https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/activity/2481/?date'
                                               '=2022-12-09)\n\n*12 декабря, 16:30*\n🪐 Астроклуб\n[Записаться]('
                                               'https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/activity/2474/?date'
                                               '=2022-12-12)\n\n*13 декабря, 16:30*\n🧩 Научный квиз – «Важнейшие '
                                               'открытия»\n[Записаться](https://xn--52-kmc.xn--80aafey1amqq.xn'
                                               '--d1acj3b/activity/2477/?date=2022-12-13)\n\n*14 декабря, 16:30*\n💻 '
                                               'Технологический диктант\n[Записаться]('
                                               'https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/activity/2478/?date'
                                               '=2022-12-14)', parse_mode='Markdown')
    elif message.text == 'Платные услуги':
        bot.send_message(message.chat.id, text='*❓ Вопрос: *\nПлатные услуги\n\n*💡 Ответ:*\nПредлагаем организацию '
                                               'мастер классов для школьников и родителей на базе детского технопарка '
                                               '"Кванториум Саров"✨\n\n*📝 Как записаться:\n*Для участия необходимо '
                                               'оставить заявку (сообщить школу, класс, количество участников, '
                                               'удобную дату, контакт лица, ответственного за организацию), '
                                               'связавшись с администратором детского технопарка по телефону: '
                                               '*+79108752054*\n\n*Стоимость мастер классов указана с учетом '
                                               'проведения в марте - мае 2022 года, в связи с колебанием цен на '
                                               'расходные материалы, стоимость может изменяться*\n\n❗️Трансфер до ДТ '
                                               '"Кванториум Саров" и обратно организуется *направляющей* '
                                               'стороной.\n\nВыберите категорию мастер классов, чтобы узнать о них '
                                               'подробнее', reply_markup=master_class_categories, parse_mode='Markdown')
    elif message.text == 'Свободные места':
        bot.send_message(message.chat.id, text='Выберите направление', reply_markup=directions_for_free_places)
    elif message.text == 'Информация о квантумах':
        bot.send_message(message.chat.id, text='Выберите направление', reply_markup=directions_for_kvantum)
    elif message.text == 'Информация о преподавателях':
        bot.send_message(message.chat.id, text='Выберите направление', reply_markup=directions_for_mentors)
    elif message.text == 'Правила кванторианца':
        bot.send_message(message.chat.id, text='*Чтобы всем жителям нашего КВАНТОдома было радостно и комфортно, '
                                               'каждый кванторианец соблюдает СЕМЬ ПРОСТЫХ ПРАВИЛ:*\n\n1️⃣ Уважать '
                                               'честь и достоинство обучающихся и работников Кванториума.\n2️⃣ Не '
                                               'опаздывать и не пропускать занятия без уважительной причины. В случае '
                                               'пропуска предупредить наставника о своем отсутствии.\n3️⃣ Приходить в '
                                               'опрятной одежде, предназначенной для занятий, иметь сменную обувь с '
                                               'белой подошвой.\n4️⃣ Соблюдать чистоту в квантумах, на территории '
                                               'технопарка и вокруг него. Не пить и не есть в квантумах и на рабочих '
                                               'местах.\n5️⃣ Беречь оборудование и помещение Кванториума.\n6️⃣ '
                                               'Экономно расходовать электроэнергию и воду.\n7️⃣ Уделять должное '
                                               'внимание своему здоровью и здоровью окружающих.\n\nДобро пожаловать в '
                                               'мир увлеченных!❤️',
                         parse_mode='Markdown')
    elif message.text == 'Контакты':
        bot.send_message(message.chat.id, text='Вы можете связаться с нами:\n\n☎️ По телефону: *+7('
                                               '910)875-20-54*\n\n📩  По электронной почте '
                                               '*infosarov@kvantorium52.ru*\n\n📍 Наш адрес: '
                                               '*Парковая улица, 3, Саров*', parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: True)
def all_information(call):
    group_for_it = telebot.types.InlineKeyboardMarkup()
    group_for_it.add(
        telebot.types.InlineKeyboardButton(text='ДВ-15', callback_data='DV-15'),
        telebot.types.InlineKeyboardButton(text='ЕД-16 АСШ-1', callback_data='ED-16'),
        telebot.types.InlineKeyboardButton(text='ДГ-13', callback_data='DG-13'),
        telebot.types.InlineKeyboardButton(text='ДГ-18', callback_data='DG-18'))

    group_for_data = telebot.types.InlineKeyboardMarkup()
    group_for_data.add(
        telebot.types.InlineKeyboardButton(text='МА-23', callback_data='MA-23'),
        telebot.types.InlineKeyboardButton(text='МА-25', callback_data='MA-25'))

    group_for_vr = telebot.types.InlineKeyboardMarkup()
    group_for_vr.add(
        telebot.types.InlineKeyboardButton(text='ЕД-8', callback_data='ED-8'),
        telebot.types.InlineKeyboardButton(text='ЕД-12', callback_data='ED-12'),
        telebot.types.InlineKeyboardButton(text='ЗВ-9', callback_data='ZV-9'),
        telebot.types.InlineKeyboardButton(text='ЗВ-14', callback_data='ZV-14'),
        telebot.types.InlineKeyboardButton(text='НА-11', callback_data='NA-11'))

    group_for_robo = telebot.types.InlineKeyboardMarkup()
    group_for_robo.add(
        telebot.types.InlineKeyboardButton(text='КМ-1 Дивеево', callback_data='KM-1'),
        telebot.types.InlineKeyboardButton(text='КМ-4', callback_data='KM-4'),
        telebot.types.InlineKeyboardButton(text='КМ-5', callback_data='KM-5'),
        telebot.types.InlineKeyboardButton(text='КМ-6', callback_data='KM-6'),
        telebot.types.InlineKeyboardButton(text='АИ-2 Сатис', callback_data='AI-2'),
        telebot.types.InlineKeyboardButton(text='АИ-3', callback_data='AI-3'),
        telebot.types.InlineKeyboardButton(text='ДВ-7', callback_data='DV-7'))

    group_for_haytek = telebot.types.InlineKeyboardMarkup()
    group_for_haytek.add(
        telebot.types.InlineKeyboardButton(text='БВ-26 Дивеево', callback_data='BV-26'),
        telebot.types.InlineKeyboardButton(text='БВ-27', callback_data='BV-27'),
        telebot.types.InlineKeyboardButton(text='БВ-28', callback_data='BV-28'),
        telebot.types.InlineKeyboardButton(text='БВ-29 Полх-Майдан', callback_data='BV-29'),
        telebot.types.InlineKeyboardButton(text='ЛЮ-30 Ард. р-н', callback_data='LU-30'),
        telebot.types.InlineKeyboardButton(text='ЛЮ-31', callback_data='LU-31'),
        telebot.types.InlineKeyboardButton(text='ПИ-32 Первомайск', callback_data='PI-32'))

    group_for_geo = telebot.types.InlineKeyboardMarkup()
    group_for_geo.add(
        telebot.types.InlineKeyboardButton(text='НД-19 Елизарьево', callback_data='ND-19'),
        telebot.types.InlineKeyboardButton(text='НД-20', callback_data='ND-20'),
        telebot.types.InlineKeyboardButton(text='АИ-21 Вознесенск', callback_data='AI-21'),
        telebot.types.InlineKeyboardButton(text='АИ-22', callback_data='AI-22'))

    group_for_media = telebot.types.InlineKeyboardMarkup()
    group_for_media.add(
        telebot.types.InlineKeyboardButton(text='КА-33', callback_data='KA-33'),
        telebot.types.InlineKeyboardButton(text='КА-34', callback_data='KA-34'))

    group_for_cheese = telebot.types.InlineKeyboardMarkup()
    group_for_cheese.add(
        telebot.types.InlineKeyboardButton(text='ПС-44', callback_data='PS-44'),
        telebot.types.InlineKeyboardButton(text='ПС-45', callback_data='PS-45'),
        telebot.types.InlineKeyboardButton(text='ПС-46', callback_data='PS-46'),
        telebot.types.InlineKeyboardButton(text='ПС-47', callback_data='PS-47'))

    group_for_math = telebot.types.InlineKeyboardMarkup()
    group_for_math.add(
        telebot.types.InlineKeyboardButton(text='АА-35', callback_data='AA-35'),
        telebot.types.InlineKeyboardButton(text='АА-36', callback_data='AA-36'))

    group_for_english = telebot.types.InlineKeyboardMarkup()
    group_for_english.add(
        telebot.types.InlineKeyboardButton(text='БЕ-37', callback_data='BE-37'),
        telebot.types.InlineKeyboardButton(text='БЕ-38', callback_data='BE-38'),
        telebot.types.InlineKeyboardButton(text='БЕ-39', callback_data='BE-39'),
        telebot.types.InlineKeyboardButton(text='БВ-40', callback_data='BV-40'),
        telebot.types.InlineKeyboardButton(text='БВ-41', callback_data='BV-41'),
        telebot.types.InlineKeyboardButton(text='БВ-42', callback_data='BV-42'),
        telebot.types.InlineKeyboardButton(text='БВ-43', callback_data='BV-43'))

    if call.data == 'IT_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_it, parse_mode='Markdown')
    elif call.data == 'DV-15':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ДВ-15*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n18:20 - 20:00', parse_mode='Markdown')
    elif call.data == 'ED-16':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ЕД-16 АСШ-1*\n\n*💡 '
                                               'Ответ:*\nВторник, четверг\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'DG-13':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ДГ-13*\n\n*💡 '
                                               'Ответ:*\nПятница\n16:30 - 18:10\nСуббота\n10:40 - 12:10',
                         parse_mode='Markdown')
    elif call.data == 'DG-18':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ДГ-18*\n\n*💡 '
                                               'Ответ:*\nПятница\n14:40 - 16:20\nСуббота\n12:20 - 13:50',
                         parse_mode='Markdown')

    if call.data == 'Data_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_data,
                         parse_mode='Markdown')
    elif call.data == 'MA-23':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *МА-23*\n\n*💡 '
                                               'Ответ:*\nПонедельник, пятница\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'MA-25':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *МА-25*\n\n*💡 '
                                               'Ответ:*\nВторник, четверг \n 16:30 - 18:10', parse_mode='Markdown')

    if call.data == 'VR/AR_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_vr, parse_mode='Markdown')
    elif call.data == 'ED-8':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ЕД-8*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'ED-12':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ЕД-12*\n\n*💡 '
                                               'Ответ:*\nВторник, среда\n 18:20 - 20:00', parse_mode='Markdown')
    elif call.data == 'ZV-9':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ЗВ-9*\n\n*💡 '
                                               'Ответ:*\nПонедельник, пятница\n 18:20 - 20:00', parse_mode='Markdown')
    elif call.data == 'ZV-14':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ЗВ-14*\n\n*💡 '
                                               'Ответ:*\nЧетверг\n18:20 - 20:00\nПятница\n16:30 - 18:10',
                         parse_mode='Markdown')
    elif call.data == 'NA-11':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *НА-11*\n\n*💡 '
                                               'Ответ:*\nВторник, четверг\n16:30 - 18:10', parse_mode='Markdown')

    if call.data == 'Robo_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_robo,
                         parse_mode='Markdown')
    elif call.data == 'KM-1':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *КМ-1 Дивеево*\n\n*💡 '
                                               'Ответ:*\nПонедельник, четверг\n14:40 - 16:20', parse_mode='Markdown')
    elif call.data == 'KM-4':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *КМ-4*\n\n*💡 '
                                               'Ответ:*\nВторник, четверг\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'KM-5':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *КМ-5*\n\n*💡 '
                                               'Ответ:*\nВторник, четверг\n18:10 - 20:00', parse_mode='Markdown')
    elif call.data == 'KM-6':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *КМ-6*\n\n*💡 '
                                               'Ответ:*\nПятница\n16:30 - 18:10\nСуббота\n12:20 - 13:50',
                         parse_mode='Markdown')
    elif call.data == 'AI-2':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *АИ-2 Сатис*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'AI-3':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *АИ-3*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n18:20 - 20:00', parse_mode='Markdown')
    elif call.data == 'DV-7':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ДВ-7*\n\n*💡 '
                                               'Ответ:*\nПятница\n18:20 - 20:00\nСуббота\n10:40 - 12:10',
                         parse_mode='Markdown')

    if call.data == 'Haytek_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_haytek,
                         parse_mode='Markdown')
    elif call.data == 'BV-26':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-26 Дивеево*\n\n*💡 '
                                               'Ответ:*\nПонедельник, четверг\n14:40 - 16:20', parse_mode='Markdown')
    elif call.data == 'BV-27':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-27*\n\n*💡 '
                                               'Ответ:*\nПонедельник\n16:30 - 18:10\nПятница\n18:20 - 20:00',
                         parse_mode='Markdown')
    elif call.data == 'BV-28':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-28*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n18:20 - 20:00', parse_mode='Markdown')
    elif call.data == 'BV-29':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-29 Полх-Майдан*\n\n*💡 '
                                               'Ответ:*\nСуббота\n9:00 - 10:30\n10:40 - 12:10', parse_mode='Markdown')
    elif call.data == 'LU-30':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ЛЮ-30 Ард. р-н*\n\n*💡 '
                                               'Ответ:*\nВторник, четверг\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'LU-31':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ЛЮ-31*\n\n*💡 '
                                               'Ответ:*\nВторник, четверг\n18:20 - 20:00', parse_mode='Markdown')
    elif call.data == 'PI-32':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ПИ-32 Первомайск*\n\n*💡 '
                                               'Ответ:*\nСреда, пятница\n16:30 - 18:10', parse_mode='Markdown')

    if call.data == 'Geo_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_geo, parse_mode='Markdown')
    elif call.data == 'ND-19':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *НД-19 Елизарьево*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n14:40 - 16:20', parse_mode='Markdown')
    elif call.data == 'ND-20':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *НД-20*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'AI-21':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *АИ-21 Вознесенск*\n\n*💡 '
                                               'Ответ:*\nСуббота\n9:00 - 10:30\n10:40 - 12:10', parse_mode='Markdown')
    elif call.data == 'AI-22':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *АИ-22*\n\n*💡 '
                                               'Ответ:*\nВторник\n16:30 - 18:10\n18:20 - 20:00', parse_mode='Markdown')

    if call.data == 'Media_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_media,
                         parse_mode='Markdown')
    elif call.data == 'KA-33':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *КА-33*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n16:30 - 18:10', parse_mode='Markdown')
    elif call.data == 'KA-34':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *КА-34*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n18:20 - 20:00', parse_mode='Markdown')

    if call.data == 'Quaintness_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_cheese,
                         parse_mode='Markdown')
    elif call.data == 'PS-44':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ПС-44*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n15:35 - 16:20', parse_mode='Markdown')
    elif call.data == 'PS-45':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ПС-45*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n16:30 - 17:15', parse_mode='Markdown')
    elif call.data == 'PS-46':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ПС-46*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n17:25 - 18:10', parse_mode='Markdown')
    elif call.data == 'PS-47':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *ПС-47*\n\n*💡 '
                                               'Ответ:*\nПонедельник, среда\n18:20 - 19:05', parse_mode='Markdown')

    if call.data == 'Math_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_math,
                         parse_mode='Markdown')
    elif call.data == 'AA-35':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *АА-35*\n\n*💡 '
                                               'Ответ:*\nСреда\n16:30 - 18:10\nПятница\n14:40 - 16:20',
                         parse_mode='Markdown')
    elif call.data == 'AA-36':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *АА-36*\n\n*💡 '
                                               'Ответ:*\nСреда\n18:20 - 20:00\nПятница\n16:30 - 18:10',
                         parse_mode='Markdown')

    if call.data == 'English_for_timetable':
        bot.send_message(call.message.chat.id, '*Выберите группу: *', reply_markup=group_for_english,
                         parse_mode='Markdown')
    elif call.data == 'BE-37':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БЕ-37*\n\n*💡 '
                                               'Ответ:*\nПонедельник, четверг\n14:40 - 15:25', parse_mode='Markdown')
    elif call.data == 'BE-38':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БЕ-38*\n\n*💡 '
                                               'Ответ:*\nПонедельник, четверг\n15:35 - 16:20', parse_mode='Markdown')
    elif call.data == 'BE-39':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БЕ-39*\n\n*💡 '
                                               'Ответ:*\nПонедельник\n16:30 - 17:15\n17:25 - 18:10\nЧетверг\n16:30 - '
                                               '17:15\n17:25 - 18:10', parse_mode='Markdown')
    elif call.data == 'BV-40':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-40*\n\n*💡 '
                                               'Ответ:*\nСреда, пятница\n16:30 - 17:15', parse_mode='Markdown')
    elif call.data == 'BV-41':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-41*\n\n*💡 '
                                               'Ответ:*\nСреда, пятница\n17:25 - 18:10', parse_mode='Markdown')
    elif call.data == 'BV-42':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-42*\n\n*💡 '
                                               'Ответ:*\nПонедельник, четверг\n18:20 - 19:05', parse_mode='Markdown')
    elif call.data == 'BV-43':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nРасписание занятий в группе *БВ-43*\n\n*💡 '
                                               'Ответ:*\nСреда, пятница\n18:20 - 19:05', parse_mode='Markdown')

    if call.data == 'it_mk':
        bot.send_message(call.message.chat.id, '🎮 *СОЗДАНИЕ ИГРЫ НА SCRATCH*\nПопробуем себя в роли разработчиков '
                                               'игр, погрузимся в мир GAMEDEV. Создадим свою первую '
                                               'кликер-игру.\n\n▪️*Возраст*: 10-12 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 300 руб.\n\n\n💻 *СОЗДАНИЕ МОБИЛЬНОГО ПРИЛОЖЕНИЯ '
                                               'В MITAPPINVENTOR*\nСоздадим собственные мобильные приложения для '
                                               '-устройств.\n\n▪️*Возраст*: 12-17 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 300 руб.', parse_mode='Markdown')
    elif call.data == 'data_mk':
        bot.send_message(call.message.chat.id, '🌐 *ПРОТИВОДЕЙСТВИЕ ИНТЕРНЕТ-УГРОЗАМ*\nНаучимся избегать манипуляций '
                                               'собственным сознанием в интернете, потренируемся различать '
                                               'вредоносные и безопасные воздействия, рассмотрим работу фишинговых '
                                               'сайтов. Мастер-класс сформирует у детей грамотное и безопасное '
                                               'поведение в интернете, даст представление о цифровом '
                                               'этикете.\n\n▪️*Возраст*: 9-12 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 300 руб.\n\n\n🖥 *СЧИТАЕМ С PYTHON*\nНаучимся '
                                               'проводить математические вычисления с помощью языка программирования '
                                               'Python. Под руководством наставника создадим программу "калькулятор" '
                                               'с различными функциями и наборами инструментов.\n\n▪️*Возраст*: 12-15 '
                                               'лет\n▪️*Длительность*: 45 минут\n▪️*Стоимость*: 300 руб.',
                         parse_mode='Markdown')
    elif call.data == 'vr_mk':
        bot.send_message(call.message.chat.id, '✨ *3D-ФИГУРКА ИЗ MINECRAFT В '
                                               'BLENDER*\nСоздадим 3D модель овечки, изучив основные инструменты '
                                               'Blender, научимся пользоваться референсом.\n\n▪️*Возраст*: 9-12 '
                                               'лет\n▪️*Длительность*: 45 минут\n▪️*Стоимость*: 350 руб.\n\n\n😎 *НАБОР '
                                               'СТИКЕРОВ В TELEGRAM*\nСоздадим уникальный набор стикеров для '
                                               'Telegram. Основой для наклеек могут послужить любимые персонажи или '
                                               'фотографии.\n\n▪️*Возраст*: 12-15 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 400 руб.', parse_mode='Markdown')
    elif call.data == 'robo_mk':
        bot.send_message(call.message.chat.id, '🤖 *WORKSHOP ПО РОБОТОТЕХНИКЕ*\nНаучимся '
                                               'конструировать и программировать роботов из деталей конструктора LEGO '
                                               'Education Mindstorms EV3, производить тестовый запуск, '
                                               'отладку работы. Организуем увлекательные соревнования '
                                               'роботов.\n\n▪️*Возраст*: 10-12 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 350 руб.\n\n\n🤖 *WORKSHOP ПО РОБОТОТЕХНИКЕ '
                                               '2*\nПознакомимся с микроконтроллерной платформой Arduino IDE. Освоим '
                                               'основные принципы построения схем, поработаем с компонентами комлекта '
                                               'Эвольвектор, создадим собственные проекты с датчиками, кнопками или '
                                               'светодиодами, научимся управлять ими при помощи программы '
                                               'Arduino.\n\n▪️*Возраст*: 14-15 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 350 руб.', parse_mode='Markdown')
    elif call.data == 'haytek_mk':
        bot.send_message(call.message.chat.id, '🚲 *ВЕЛОСИПЕД С ДВИЖУЩИМИСЯ ЭЛЕМЕНТАМИ*\nИспользуя '
                                               'программу CorelDraw, а также лазерный гравер, научимся изготавливать '
                                               'экологически чистый конструктор, развивающий мелкую моторику рук, '
                                               'воображение, пространственное мышление, логику и предметное '
                                               'моделирование.\n\n▪️*Возраст*: 9-17 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 550 руб.\n\n\n🖨 *БРЕЛОК НА 3D-ПРИНТЕРЕ*\nОсвоив '
                                               'азы прототипирования с помощью программы "Компас 3D", создадим свой '
                                               'собственный брелок на 3D-принтере.\n\n▪️*Возраст*: 12-17 '
                                               'лет\n▪️*Длительность*: 45 минут\n▪️*Стоимость*: 350 руб.',
                         parse_mode='Markdown')
    elif call.data == 'geo_mk':
        bot.send_message(call.message.chat.id, '🚦 *ГОНКИ НА КВАДРОКОПТЕРАХ*\nПознакомимся с оборудованием '
                                               'Геоквантума, научимся управлять гоночным квадрокоптером '
                                               'DJITello.\n\n▪️*Возраст*: 14-17 лет\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 300 руб.\n\n\n🎞 *СОЗДАНИЕ ВИДЕОТУРА В GOOGLE '
                                               'EARTH PRO*\nИзучим основные инструменты программы GoogleEarthPro, '
                                               'создадим собственные уникальные проекты.\n\n▪️*Возраст*: 9-12 '
                                               'лет\n▪️*Длительность*: 45 минут\n▪️*Стоимость*: 300 руб.',
                         parse_mode='Markdown')
    elif call.data == 'family_mk':
        bot.send_message(call.message.chat.id, '🤖 *СЕМЕЙНЫЕ РОБОГОНКИ*\nНа базе конструктора LEGO '
                                               'EducationMindstormsEV3! У вас есть уникальная возможность вместе с '
                                               'детьми погрузиться в мир роботов, собрать своего и устроить '
                                               'гонки.\n\n▪️*Возраст*: 12+ и взрослые\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 300 руб.\n\n\n🕶 *3D-ОЧКИ ДЛЯ ДОЧКИ И '
                                               'СЫНОЧКА*\nИзготовим с помощью 3D-ручек стильные очки и отправимся '
                                               'прямиком в кинотеатр, чтобы всей семьей протестировать '
                                               'изобретение.n\n▪️*Возраст*: 9+ и взрослые\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 350 руб.\n\n\n🗺 *КАРТА СЕМЕЙНОГО ПУТЕШЕСТВИЯ*\nС '
                                               'помощью программы Google Планета Земля создадим мини-маршрут по '
                                               'достопримечательностям любой местности. Найдем данные о каждом '
                                               'объекте и заполним их карточки.n\n▪️*Возраст*: 12+ и '
                                               'взрослые\n▪️*Длительность*: 45 минут\n▪️*Стоимость*: 300 руб.\n\n\n💫 '
                                               '*3D-КОНСТРУКТОР "ЭЙФЕЛЕВА БАШНЯ", "ДИРИЖАБЛЬ"*\nС помощью программы '
                                               'CorelDraw и лазерного гравера вы создадите семейный шедевр, '
                                               'который будет отличным подарком или украшением '
                                               'интерьера.\n▪️*Возраст*: 12+ и взрослые\n▪️*Длительность*: 45 '
                                               'минут\n▪️*Стоимость*: 700 руб.',
                         parse_mode='Markdown')
    elif call.data == 'creative_mk':
        bot.send_message(call.message.chat.id, '😎 *КВЕСТ "ДЕЛО №56*\nОГО! Ребята превратились в агентов, которые '
                                               'расследуют киберпреступления. И вот очередное дело. Похищен '
                                               'суперкомпьютер. За раскрытое дело обещают щедрое вознаграждение! '
                                               'Собирайте улики, исследуйте место преступления. За дело, '
                                               'друзья!\n▪️*Возраст*: 10-17 лет\n▪️*Длительность*: 1 '
                                               'час\n▪️*Стоимость*: 250 руб.\n\n\n🌏 *КВЕСТ "МИР ИНЖЕНЕРНЫХ '
                                               'ПРОФЕССИЙ*\nЭтот квест познакомит участников со всеми направлениями '
                                               'ДТ "Кванториум Саров". Добро пожаловать к нам на классный час или '
                                               'профориентационный урок! Отличный формат взаимодействия со школами '
                                               'города.\n▪️*Возраст*: 9+ и взрослые\n▪️*Длительность*: 1 час 15 '
                                               'минут\n▪️*Стоимость*: 250 руб.\n\n\n☀️*СОЗДАЙ ЗНАЧОК*\nЗначок - это '
                                               'предмет искусства и коллекционирования. Создадим уникальные авторские '
                                               'изделия, которые станут отличным подарком или придадут '
                                               'индивидуальности участникам мастер-класса.\n▪️*Возраст*: 10-17 '
                                               'лет\n▪️*Длительность*: 45 минут\n▪️*Стоимость*: 550 руб.\n\n\n💫 '
                                               '*ВЫХОДНОЙ ДЕНЬ В КВАНТОРИУМЕ*\nПроведи выходной день с пользой в '
                                               'Кванториуме! Тебя ждут экскурсия, увлекательный квест и множество '
                                               'технических мастер-классов. 3D-ручка, очки виртуальной реальности, '
                                               'лазерный гравёр и многое другое! (_количество и виды мастер-классов '
                                               'согласуются с менеджером технопарка_)\n▪️*Возраст*: 10-17 '
                                               'лет\n▪️*Длительность*: 2 часа\n▪️*Стоимость*: 700 руб.\n\n\n✏️*ОСНОВЫ '
                                               'SKETCHINGA*\nСкетчинг - это замечательный навык, помогающий '
                                               'максимально быстро, эффективно, красиво и здорово передавать свою '
                                               'идею из головы на бумагу. На мастер-классе мы разберем виды '
                                               'sketchinga, попрактикуемся в создании зарисовок.\n▪️*Возраст*: 12-17 '
                                               'лет\n▪️*Длительность*: 1 час\n▪️*Стоимость*: 500 руб.',
                         parse_mode='Markdown')

    if call.data == 'IT_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nОткрыт набор в группы '
                                               'для школьников от 10 до 17 лет.\nСтарт обучения - *в январе*\n\n📌 '
                                               'ГР-48\n📆 *Расписание*: вторник, четверг в 18:20\n\n📌 ГР-49\n📆 '
                                               '*Расписание*: пятница в 18:20 и суббота в 9:00\n\n[Записаться на '
                                               'обучение](https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program'
                                               '/27816-kvantorium-sarov-aiti-kvantum)', parse_mode='Markdown')
    elif call.data == 'Data_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nК сожалению, свободных '
                                               'мест нет.', parse_mode='Markdown')
    elif call.data == 'VR/AR_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nК сожалению, свободных '
                                               'мест нет.', parse_mode='Markdown')
    elif call.data == 'Robo_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nОткрыт набор в группы '
                                               'для школьников 7 - 9 лет. Старт обучения - *в январе*\n\n⚡️МИР ИГР '
                                               'ROBLOX\nНа занятиях ребята знакомятся с теорией и практикой в области '
                                               'создания игр, освоят среду RobloxStudio, получат опыт '
                                               'программирования.\n\n📆 *Расписание*: четверг, пятница в 16:15 (2 '
                                               'занятия в неделю по 45 минут).\n▪️*Стоимость обучения* (36 часов, '
                                               '4 месяца) - 7800 руб.\nВозможно внесение оплаты двумя платежами.\n'
                                               '[Записаться](https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program'
                                               '/36012-mir-igr-roblox)\n\n\n🤖 ЗАНИМАТЕЛЬНАЯ РОБОТОТЕХНИКА\nНа '
                                               'занятиях ребята освоят основы робототехники, научатся самостоятельно '
                                               'конструировать и программировать роботов, освоят работу в команде, '
                                               'проявят фантазию и воображение.\n\n📆 *Расписание*: суббота 12:20 - '
                                               '13:50 (два занятия по 45 минут с перерывом, динамической '
                                               'паузой)\n▪️*Стоимость обучения* (36 часов, 4 месяца) - 7800 '
                                               'руб.\nВозможно внесение оплаты двумя платежами.\n[Записаться]('
                                               'https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program/36838'
                                               '-kvantorium-sarov-zanimatelnaya-robototekhnika)',
                         parse_mode='Markdown')
    elif call.data == 'Haytek_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nК сожалению, свободных '
                                               'мест нет.', parse_mode='Markdown')
    elif call.data == 'Geo_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nК сожалению, свободных '
                                               'мест нет.', parse_mode='Markdown')
    elif call.data == 'Media_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nК сожалению, свободных '
                                               'мест нет.', parse_mode='Markdown')
    elif call.data == 'Quaintness_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nК сожалению, свободных '
                                               'мест нет.', parse_mode='Markdown')
    elif call.data == 'Math_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nК сожалению, свободных '
                                               'мест нет.', parse_mode='Markdown')
    elif call.data == 'English_for_free_places':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nСвободные места\n\n*💡 Ответ:*\nОткрыт набор в '
                                               'группы:\n📌 БЕ-37 (8 - 9 лет)\n📆 *Расписание*: понедельник, четверг '
                                               'в 14:40\n\n📌 БЕ-38(9 - 10 лет)\n📆 *Расписание*: понедельник, '
                                               'четверг в 15:35\n\n📌 БЕ-39(12 - 17 лет)\n📆 *Расписание*: '
                                               'понедельник, четвергв 16:30\n\n[Записаться на базовый английский]('
                                               'https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program/34229'
                                               '-kvantorium-sarov-bazovyi-angliiskii-yazyk)\n[Записаться на '
                                               'технический английский]('
                                               'https://xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program/28356'
                                               '-tekhnicheskii-angliiskii-osnova-tolko-dlya-kvantoriantsev)',
                         parse_mode='Markdown')

    if call.data == 'IT_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*IT-квантум - *'
                                               'это углубленное изучение высокоуровневых языков программирования и '
                                               'сетевых технологий. Ребята научатся таким современным языкам '
                                               'программирования как Python, C/C++, JavaScript.', parse_mode='Markdown')
    elif call.data == 'Data_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Data-квантум - *'
                                               'это разработка программ для сбора, визуализации, моделирования и '
                                               'анализа данных. Это работа с имитационными моделями, а также работа с '
                                               'базами данных. Ребята научатся программировать на таких языках, '
                                               'как Python, SQL, Lava. получат навыки по аналитики, статистике и '
                                               'математике, необходимые для выявления закономерностей в собранных '
                                               'данных. Научатся создавать имитационные модели в программе AnyLogic, '
                                               'анализировать их и при необходимости оптимизировать.',
                         parse_mode='Markdown')
    elif call.data == 'VR/AR_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Виртуальная и '
                                               'дополненная реальность (VR и AR) - *это современные и быстро '
                                               'развивающиеся технологии. Их цель - расширение физического '
                                               'пространства жизни человека объектами, созданными с помощью цифровых '
                                               'устройств и программ.', parse_mode='Markdown')
    elif call.data == 'Robo_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Промышленная '
                                               'робототехника - *это создание роботов, изучение передовых технологий в '
                                               'области электроники, мехатроники и программирования для автоматизации '
                                               'производственных процессов.', parse_mode='Markdown')
    elif call.data == 'Haytek_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Хайтек - *это '
                                               'высокотехнологичная лаборатория для изготовления любой нужной детали, '
                                               'устройства. Хайтек-цех оснащен по последнему слову техники. Юные '
                                               'изобретатели и инженеры научатся работать на современном высокоточном '
                                               'оборудовании. 3D-принтеры, плоттеры, станки с ЧПУ, аэрограф, '
                                               '3D ручки, лазерный гравер, паяльные станции, ручной инструмент '
                                               'позволят создать проект мечты!', parse_mode='Markdown')
    elif call.data == 'Geo_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Геоквантум – '
                                               '*это работа с дистанционным зондированием Земли, картографией, '
                                               'проектирование виртуальных карт местности. Сфера применения '
                                               'полученных знаний очень широка – она позволит решать различные задачи '
                                               'в транспортных системах, геологоразведке и добыче полезных '
                                               'ископаемых, в сельском хозяйстве, ЖКХ, землеустройстве, '
                                               'градостроительстве, обороне и безопасности.', parse_mode='Markdown')
    elif call.data == 'Media_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Медиа.* '
                                               'Кванторианцы изучат жанры современной журналистики и применят их для '
                                               'реализации своих идей – видеоблога, новостных репортажей, '
                                               'интернет-статей. Ребята попробуют себя в создании собственного '
                                               'контента: съемках события, монтаже, публикации в информационных '
                                               'ресурсах, а также научатся безопасному поведению в интернете.',
                         parse_mode='Markdown')
    elif call.data == 'Quaintness_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Шахматы – '
                                               '*универсальный интеллектуальный тренажер. В процессе занятий '
                                               'кванторианцы учатся не только игре, но и взаимодействию, '
                                               'коммуникациям, развивают креативность и критическое мышление.',
                         parse_mode='Markdown')
    elif call.data == 'Math_for_kvantum':
        bot.send_message(call.message.chat.id, "*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Математика.* "
                                               "Программа предназначена для ознакомления учащихся с применением "
                                               "математики в инженерии, получения базовых навыков для дальнейших "
                                               "исследований. Программа познакомит обучающихся с такими базовыми "
                                               "математическими объектами, как графы, множества, геометрические "
                                               "фигуры, системы координат, с понятиями вероятность и статистика, "
                                               "а также с таким фундаментальным разделом математики, "
                                               "как математическая логика.", parse_mode='Markdown')
    elif call.data == 'English_for_kvantum':
        bot.send_message(call.message.chat.id, '*❓ Вопрос: *\nИнформация о квантумах\n\n*💡 Ответ:*\n*Программа '
                                               '«Английский язык»* поможет исправить пробелы в знаниях обучающихся, '
                                               'обучит юных кванторианцев технической лексике и расскажет о культуре '
                                               'англоговорящих стран. Интерактивные задания, игры и уроки-дискуссии '
                                               'помогут применять английский язык не только на занятиях, '
                                               'но и в обычной жизни.', parse_mode='Markdown')

    if call.data == 'IT_for_mentors':
        gleb = open('mentors/gleb.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=gleb,
            caption='*Дерюгин Глеб Сергеевич*\n\n▪️*Преподаваемая дополнительная общеобразовательная программа:* '
                    'IT-квантум\n\n ▪️*Общий стаж работы:* с 2020\n*Стаж работы по специальности:* с 2020\n\n'
                    '▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n*Направление подготовки:* "Вычислительные '
                    'технологии" \n\n▪️*Повышение квалификации:*\n1) "Программирование на Python", 2021 г.\n2) '
                    'Академия Яндекса "Введение в программирование (C++)", 2021 г.\n3) Академия Яндекса "Безопасность '
                    'в интернете", 2021 г.\n4) Онлайн-университет "Нетология". Программа "Основы верстки сайта", '
                    '2021 г.\n5) Stepik. Курс "Веб-разработка для начинающих: HTML и CSS", 2021 г.\n6) Нетология. '
                    'Python. Разработка для начинающих, 2021 г.\n\n▪️*О себе:*\nУвлекаюсь программированием. Основные '
                    'языки программирования: Python и JavaScript. Знания ООП Python. Фреймворков Django и Flask. '
                    'Управление DOM структурой на JS. React и немного Vue.js. Знания управлениями БД и языка SQL. '
                    'Знания HTML/CSS, адаптивной верстки. Сейчас продолжаю учиться в магистратуре СарФТИ.',
            parse_mode='Markdown'
        )

        vova = open('mentors/vova.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=vova,
            caption='*Добровольский Владимир Андреевич*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* IT-квантум, Промробоквантум\n\n▪️*Общий стаж работы:* с 2019\n*Стаж работы по '
                    'специальности:* с 2019\n\n▪️*Образование:* среднее профессиональное\n1)Политехникум Сарфти НИЯУ '
                    'МИФИ\n*Направление подготовки:* «Программирование компьютерных систем»\n\n▪️*О себе:*\nМогу '
                    'научить программировать контроллеры разной сложности.\nМогу научить делать слаботочную проводку '
                    'и обвязку вокруг сложных иформационных систем.\nМогу научить паять, лудить платы и ремонтировать '
                    'оборудование.\nМогу научить варить метал, и делать металлические конструкции.\nМогу научить '
                    'работать на ЧПУ станках в том числе и 3D принтеры, а так же промышленном манипулятора '
                    'KUKA.\nМогу показать и рассказать и научить как работать в Компас 3D, SprutCAM, Blockbench.\n\nВ '
                    'общем, зовите меня "Инспектор Гаджет" 😎 ', parse_mode='Markdown'
        )

        dima = open('mentors/dima.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=dima,
            caption='*Ермолаев Дмитрий Александрович*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* IT-квантум, VR/AR-квантум\n\n▪️*Общий стаж работы:* с 2022\n*Стаж работы по '
                    'специальности:* с 2022\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n*Квалификация:* '
                    'Специалист\n*Направление:* "Электроника и автоматика физических установок"\n\n▪️*О '
                    'себе:*\nХарды: преподаю VR/AR и IT, пишем код на языке Python, создаем VR и AR приложения\n'
                    'Общительный, тактичный, активный', parse_mode='Markdown'
        )
    elif call.data == 'Data_for_mentors':
        nastya = open('mentors/nastya.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=nastya,
            caption='*Мишина Анастасия Алексеевна*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Data-квантум\n\n▪️*Общий стаж работы:* с 2019\n*Стаж работы по '
                    'специальности:* с 2021\n\n▪️*Образование:* среднее-профессиональное, высшее неоконченное\n1) '
                    'СарФТИ НИЯУ МИФИ\n*Направление:* "Технология машиностроения"\n*Квалификация:* техник\n2) '
                    'Ульяновский государственный университет\n*Направление:* "Информационные системы и '
                    'технологии\n▪️Повышение квалификации:\n1) Профессиональная переподготовка '
                    '"Яндекс.Практикум"\nФакультет backend разработки\n\n▪️*О себе:*\nПодбираю индивидуальный подход '
                    'к каждому ученику.\nСоздаем интересные творческие проекты, такие как:\n- Чат-бот на платформе '
                    'Telegram для "Миллион роз"\n- Социальная сеть для ДТ "Кванториум Саров"\n- Система электронного '
                    'документооборота\n-Имитационное моделирование дорожной ситуации на перекрестке и ее '
                    'оптимизация\nи многое другое', parse_mode='Markdown'
        )
    elif call.data == 'VR/AR_for_mentors':
        albina = open('mentors/albina.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=albina,
            caption='*Нестерова Альбина Андреевна*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* VR/AR-квантум\n\n▪️*Общий стаж работы:* с 2021\n*Стаж работы по '
                    'специальности:* с 2021\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n*Квалификация:* Бакалавр\n'
                    '*Направление подготовки:* "Информационные системы и технологии"', parse_mode='Markdown'
        )

        dima = open('mentors/dima.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=dima,
            caption='*Ермолаев Дмитрий Александрович*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* IT-квантум, VR/AR-квантум\n\n▪️*Общий стаж работы:* с 2022\n*Стаж работы по '
                    'специальности:* с 2022\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n*Квалификация:* '
                    'Специалист\n*Направление:* "Электроника и автоматика физических установок"\n\n▪️*О '
                    'себе:*\nХарды: преподаю VR/AR и IT, пишем код на языке Python, создаем VR и AR приложения\n'
                    'Общительный, тактичный, активный', parse_mode='Markdown'
        )

        viktor = open('mentors/viktor.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=viktor,
            caption='*Завадский Виктор Станиславович*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* VR/AR-квантум\n\n▪️*Общий стаж работы:* с 2022\n*Стаж работы по '
                    'специальности:* с 2022\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n'
                    '*Направление:* "Автоматика и электроника физических установок"\n\n▪️*О себе:*\nИмею профессию '
                    'воспитатель - вожатый. Легко нахожу общий язык с детьми. Занятия проходят в лёгкой и '
                    'непринужденной обстановке', parse_mode='Markdown'
        )
    elif call.data == 'Robo_for_mentors':
        maksim = open('mentors/maksim.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=maksim,
            caption='*Ключников Максим Алексеевич*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Промробоквантум\n\n▪️*Общий стаж работы:* с 2022\n*Стаж работы по '
                    'специальности:* с 2022\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n'
                    '*Направление:* "Автоматика и электроника физических установок"\n\n▪️*О себе:*\nНаучу ваших детей '
                    'собирать и программировать сложные модели роботов', parse_mode='Markdown'
        )

        ilya_afonin = open('mentors/ilya_afonin.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=ilya_afonin,
            caption='*Афонин Илья Дмитриевич*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Промробоквантум, Геоквантум\n\n▪️*Общий стаж работы:* с 2018\n*Стаж работы по '
                    'специальности:* с 2021\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n'
                    '*Направление:* "Электроника физических установок"\n*Квалификация:* специалист\n▪️*Повышение '
                    'квалификации:*\n1) Курс на площадке "Mirapolis LMS"\n\n▪️*О себе:*\nЛояльность '
                    'организации\nСпособность развивать других\nСпособность выстраивать отношения с '
                    'окружающими\nОтветственность\nНацеленность на результат\nУмение мотивировать '
                    'других\nАвторитетность', parse_mode='Markdown'
        )

        vova = open('mentors/vova.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=vova,
            caption='*Добровольский Владимир Андреевич*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* IT-квантум, Промробоквантум\n\n▪️*Общий стаж работы:* с 2019\n*Стаж работы по '
                    'специальности:* с 2019\n\n▪️*Образование:* среднее профессиональное\n1)Политехникум Сарфти НИЯУ '
                    'МИФИ\n*Направление подготовки:* «Программирование компьютерных систем»\n\n▪️*О себе:*\nМогу '
                    'научить программировать контроллеры разной сложности.\nМогу научить делать слаботочную проводку '
                    'и обвязку вокруг сложных иформационных систем.\nМогу научить паять, лудить платы и ремонтировать '
                    'оборудование.\nМогу научить варить метал, и делать металлические конструкции.\nМогу научить '
                    'работать на ЧПУ станках в том числе и 3D принтеры, а так же промышленном манипулятора '
                    'KUKA.\nМогу показать и рассказать и научить как работать в Компас 3D, SprutCAM, Blockbench.\n\nВ '
                    'общем, зовите меня "Инспектор Гаджет" 😎 ', parse_mode='Markdown'
        )
    elif call.data == 'Haytek_for_mentors':
        slava = open('mentors/slava.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=slava,
            caption='*Бурлаков Вячеслав Андреевич*\n\n▪️Инженер-преподаватель квантума Хайтек\n\n▪️*Общий стаж '
                    'работы:* с 2021\n*Стаж работы по специальности:* с 2022\n\n▪️*Образование:* высшее\n*Направление '
                    'подготовки:* "Электроника и наноэлектроника"\n\n▪️*О себе:*\nЕще с детства я увлекался различными '
                    'самоделками, а недавно понял что хочу еще и обучать своим навыкам детей. Поэтому я с радостью '
                    'передаю свои навыки, привнося немного знаний из сферы электроники, которую я изучал в институте. '
                    'Как по мне, занятия получаются весёлыми и познавательными.', parse_mode='Markdown'
        )

        yulya = open('mentors/yulya.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=yulya,
            caption='*Лукьянова Юлия Андреевна*\n\n▪️Инженер-преподаватель квантума Хайтек\n\n▪️*Образование:* '
                    'высшее\n1) СарФТИ НИЯУ МИФИ\n*Направление:* "Технологическое обеспечение машиностроительных '
                    'производств"\n\n▪️*О себе:*\nХорошо знаю материаловедение и программу Компас-3D. Аддитивные и '
                    'лазерные технологии - это моя темочка.\nНа занятиях учу пользоваться инженерно-графическими '
                    'программами, строим эскизы, чертежи и трехмерные модели. Также учимся пользоваться '
                    'высокотехнологичным оборудованием, например, лазерным гравером, сверлильным станком, торцовочный '
                    'пилами и многим другим.\nНаучу настраивать 3д-принтер и печатать на нем все, что угодно😉\nКо '
                    'всем проектам подходим с творческой точки зрения🎨', parse_mode='Markdown'
        )

        ilya_podolyak = open('mentors/ilya_podolyak.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=ilya_podolyak,
            caption='*Подоляк Илья Сергеевич*\n\n▪️Инженер-преподаватель квантума Хайтек\n\n▪️*Общий стаж работы:* '
                    'с 2022\nС*таж работы по специальности:* с 2022\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ '
                    'МИФИ\n*Направление:* "Динамика и прочность машин"', parse_mode='Markdown'
        )
    elif call.data == 'Geo_for_mentors':
        dasha = open('mentors/dasha.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=dasha
        )
        bot.send_message(call.message.chat.id,
                         '*Николаева Дарья Дмитриевна*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                         'программа:* Геоквантум\n\n▪️*Общий стаж работы:* с 2020\n*Стаж работы по специальности:* с '
                         '2020\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n*Направление:* "Вычислительные '
                         'технологии"\n*Квалификация:* бакалавр\n\n▪️*Повышение квалификации:*\n1) Digital-Центр НИЯУ '
                         'МИФИ\n- Python и его научные библиотеки (24 ак.ч.), 2021 г.\n- Основы программирования в 1С '
                         '(16 ак.ч.), 2021 г.\n\n▪️*О себе:*\nСпециальные профессиональные навыки:\nВладею языками '
                         'программирования: Python, HTML, CSS, JavaScript, Lua.\nОсвоила программы: MathCad, '
                         'Visual Studio Code, пакет программ Microsoft (Word, Excel, Access, Power Point), Sketch Up, '
                         'GoogleEarth, Tinkercad, Компас 3D, Figma, Adobe Photoshop, Adobe Illustrator, '
                         'RobloxStudio\nРасширенное понимание современного графического оборудования, геокодирования, '
                         '3D-моделирования;\nНавыки управления дронами DJI Mavic 2 Pro, DJI Tello;\nЗнание жанров игр '
                         'и принципов их создания, навыки разработки игрового интерфейса пользователя;\nВозможность '
                         'отладки и оптимизации нового и существующего кода\n\nДополнительные качества\nСпособность к '
                         'обучению, готовность к профессиональному самосовершенствованию, способность сосредоточить в '
                         'течение достаточного периода времени внимание на одном предмете, умение выбрать из большого '
                         'объема информации ту, которая необходима для решения данной задачи, способность объективно '
                         'оценивать свои достижения, силы и возможности, умение доходчиво донести слушателю свои '
                         'мысли и намерения, способность понимать подтекст речи (иронию, шутку), умение дать '
                         'объективную оценку действиям других людей, способность располагать к себе людей, вызывать у '
                         'них доверие', parse_mode='Markdown')

        ilya_afonin = open('mentors/ilya_afonin.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=ilya_afonin,
            caption='*Афонин Илья Дмитриевич*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Промробоквантум, Геоквантум\n\n▪️*Общий стаж работы:* с 2018\n*Стаж работы по '
                    'специальности:* с 2021\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n'
                    '*Направление:* "Электроника физических установок"\n*Квалификация:* специалист\n▪️*Повышение '
                    'квалификации:*\n1) Курс на площадке "Mirapolis LMS"\n\n▪️*О себе:*\nЛояльность '
                    'организации\nСпособность развивать других\nСпособность выстраивать отношения с '
                    'окружающими\nОтветственность\nНацеленность на результат\nУмение мотивировать '
                    'других\nАвторитетность', parse_mode='Markdown'
        )
    elif call.data == 'Media_for_mentors':
        alina = open('mentors/alina.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=alina,
            caption='*Кимяева Алина Ивановна*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Медиаквантум\n\n▪️*Общий стаж работы:* с 2016\n*Стаж работы по '
                    'специальности:* с 2020\n\n▪️*Образование:* высшее\n1) МГПУ (бывш. МГПИ им. Евсевьева)\n'
                    '*Направление:* "Изобразительное искусство"\n*Квалификация:* бакалавр\n▪️*Повышение '
                    'квалификации:*\n1) МГПУ (бывш. МГПИ им. Евсевьева), "Начальное образование", 2019 г.\n2) МГПУ ('
                    'бывш. МГПИ им. Евсевьева), "Дошкольное образование", 2019 г.\n3) ФГБОУ ДО ФЦДО. Программа '
                    '"Организационно-педагогическая деятельность", 2021 г.\n4) Корпоративная Академия Росатом. Курс '
                    '"7 ступеней успешной организации смены для школьников", 2021 г.', parse_mode='Markdown'
        )
    elif call.data == 'Quaintness_for_mentors':
        semen = open('mentors/semen.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=semen,
            caption='*Пухов Семен Александрович*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Квантошахматы\n\n▪️*Общий стаж работы:* с 2013\n*Стаж работы по '
                    'специальности:* с 2021\n\n▪️*Образование:* высшее\n1) СарФТИ НИЯУ МИФИ\n'
                    'Направление: "Финансы и кредит"\n▪️*Повышение квалификации:*\n1) «Проектная деятельность на основе '
                    'перспективных технологий прототипирования и обработки материалов в дополнительном образовании '
                    'детей» (Сколково)\n2) «Основы технологий работы педагогических работников, реализующих программы '
                    'детских международных русских лагерей за рубежом». (Московский психолого-социальный '
                    'университет)\n3) Корпоративная Академия Росатом. Курс "7 ступеней успешной организации смены для '
                    'школьников", 2021 г.', parse_mode='Markdown'
        )
    elif call.data == 'Math_for_mentors':
        angelina = open('mentors/angelina.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=angelina,
            caption='*Аронова Ангелина Олеговна*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Математика\n\n▪️*Общий стаж работы:* с 2022\n*Стаж работы по '
                    'специальности:* с 2022\n\n▪️*Образование:* высшее неоконченное\n1) СарФТИ НИЯУ МИФИ\n'
                    '*Направление:* "Прикладная механика"', parse_mode='Markdown'
        )
    elif call.data == 'English_for_mentors':
        liza = open('mentors/liza.webp', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=liza
        )
        bot.send_message(call.message.chat.id,
                         '*Бондарь Елизавета Дмитриевна*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                         'программа:* Английский язык\n\n▪️*Общий стаж работы:* с 2020\n*Стаж работы по '
                         'специальности:* с 2020\n\n▪️*Образование:* высшее\n1) Смоленский государственный '
                         'университет\nНаправление: "Английский язык"\n▪️Повышение квалификации:\n1) Программа '
                         'ASSECC, международная программа «Between the lines. Онлайн курсы «Write for Your '
                         'Life:Turning Trauma info stories» от University of IOWA\n2) ФГБОУ ДО ФЦДО. Программа '
                         '"Организационно-педагогическая деятельность", 2021 г.\n3) Онлайн-курс: Youth Community '
                         'Leadership Challende» от University of Maryland\n\n▪️*Профессиональные успехи:*\nРабота '
                         'мастером и вожатым на сменах в лагере благотворительного фонда реабилитации детей '
                         'перенесших тяжелые заболевания «Шередарь»\n\n▪️*О себе:*\nСмолГУ ‘Методика преподавания '
                         'английского языка’.\nМладшие группы (дети до 10 лет) изучают английский весело и интересно: '
                         'с помощью игровой деятельности, интерактивных приложений и аутентичных УМК.\nВзрослые '
                         'ребята (10-17 лет) смогут развить коммуникативные навыки, узнать технические термины, '
                         'а также подтянуть грамматику.', parse_mode='Markdown')

        vika = open('mentors/vika.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=vika,
            caption='*Быкова Виктория Александровна*\n\n▪️*Преподаваемая дополнительная общеобразовательная '
                    'программа:* Английский язык\n\n▪️*Общий стаж работы:* с 2022\n*Стаж работы по '
                    'специальности:* с 2022\n\n▪️*Образование:* высшее неоконченное\n\n▪️*О себе:*\nОрганизованность,'
                    'эффективность, точность, умение слушать и вести переговоры,умение найти подход к детям, '
                    'знания в области иностранных языков', parse_mode='Markdown'
        )


bot.polling(none_stop=True, interval=0)
