from bs4 import BeautifulSoup
import requests
import string
import random
import re

import base64
import time


names = [
    "Аарон", "Аба", "Аббас", "Абд аль-Узза", "Абдуллах", "Абид", "Аботур", "Аввакум", "Август", "Авдей", "Авель", "Аверкий", "Авигдор", "Авирмэд", "Авксентий", "Авл", "Авнер", "Аврелий", "Автандил", "Автоном", "Агапит", "Агафангел", "Агафодор", "Агафон", "Аги", "Агриппа", "Адам", "Адар", "Адиль", "Адольф", "Адонирам", "Адриан", "Азамат", "Азарий", "Азат", "Азиз", "Азим", "Айварс", "Айдар", "Айрат", "Акакий", "Аквилий", "Акиф", "Акоп", "Аксель", "Алан", "Аланус", "Алек", "Александр", "Алексей", "Алемдар", "Алик", "Алим", "Алипий", "Алишер", "Алмат", "Алоиз", "Алон", "Альберик", "Альберт", "Альбин", "Альваро", "Альвиан", "Альвизе", "Альфонс", "Альфред", "Амадис", "Амвросий", "Амедей", "Амин", "Амир", "Амр", "Амфилохий", "Анания", "Анас", "Анастасий", "Анатолий", "Ангеляр", "Андокид", "Андрей", "Андроник", "Аннерс", "Анри", "Ансельм", "Антипа", "Антон", "Антоний", "Антонин", "Антуан", "Арам", "Арефа", "Арзуман", "Аристарх", "Аристон", "Ариф", "Аркадий", "Арсений", "Артём", "Артур", "Арфаксад", "Асаф", "Атанасий", "Атом", "Аттик", "Афанасий", "Афинагор", "Афиней", "Афиф", "Африкан", "Ахилл", "Ахмад", "Ахтям", "Ашот", "Бадар", "Барни", "Бартоломео", "Басир", "Бахтияр", "Баян", "Безсон", "Бен", "Беньямин", "Берт", "Бехруз", "Билял", "Богдан", "Болеслав", "Бонавентура", "Борис", "Борислав", "Боян", "Бронислав", "Брячислав", "Бурхан", "Бутрос", "Бямбасурэн", "Вадим", "Валентин", "Валентино", "Валерий", "Валерьян", "Вальдемар", "Вангьял", "Варлам", "Варнава", "Варфоломей", "Василий", "Вахтанг", "Велвел", "Венансио", "Венедикт", "Вениамин", "Венцеслав", "Вигго", "Викентий", "Виктор", "Викторин", "Вильгельм", "Винцас", "Виссарион", "Виталий", "Витаутас", "Вито", "Владимир", "Владислав", "Владлен", "Влас", "Воислав", "Володарь", "Вольфганг", "Вописк", "Всеволод", "Всеслав", "Вук", "Вукол", "Вышеслав", "Вячеслав", "Габриеле", "Гавриил", "Гай", "Галактион", "Галымжан", "Гамлет", "Гаспар", "Гафур", "Гвидо", "Гейдар", "Геласий", "Гелий", "Гельмут", "Геннадий", "Генри", "Генрих", "Георге", "Георгий", "Гераклид", "Герасим", "Герберт", "Герман", "Германн", "Геронтий", "Герхард", "Гийом", "Гильем", "Гинкмар", "Глеб", "Гней", "Гоар", "Горацио", "Гордей", "Градислав", "Григорий", "Гримоальд", "Гуго", "Гурий", "Густав", "Гьялцен", "Давид", 
    "Дамдинсурэн", "Дамир", "Даниил", "Дарий", "Демид", "Демьян", "Денеш", "Денис", "Децим", "Джаббар", "Джамиль", "Джан", "Джанер", "Джанфранко", "Джафар", "Джейкоб", "Джихангир", "Джованни", "Джон", "Джохар", "Джулиано", "Джулиус", "Дино", "Диодор", "Дитер", "Дитмар", "Дитрих", "Дмитрий", "Доминик", "Дональд", "Донат", "Дорофей", "Досифей", "Евгений", "Евграф", "Евдоким", "Еврит", "Евсей", "Евстафий", "Евтихан", "Евтихий", "Егор", "Елеазар", "Елисей", "Емельян", "Епифаний", "Ербол", "Ерванд", "Еремей", "Ермак", "Ермолай", "Ерофей", "Ефим", "Ефрем", "Жан", "Ждан", "Жером", "Жоан", "Захар", "Захария", "Збигнев", "Зденек", "Зейналабдин", "Зенон", "Зеэв", "Зигмунд", "Зинон", "Зия", "Золтан", "Зосима", "Иакинф", "Иан", "Ибрагим", "Ибрахим", "Иван", "Игнатий", "Игорь", "Иероним", "Иерофей", "Израиль", "Икрима", "Иларий", "Илия", "Илларион", "Илмари", "Ильфат", "Илья", "Имран", "Иннокентий", "Иоаким", "Иоанн", "Иоанникий", "Иоахим", "Иов", "Иоганн", "Иоганнес", "Ионафан", "Иосафат", "Ираклий", "Иржи", "Иринарх", "Ириней", "Иродион", "Иса", "Исаак", "Исаакий", "Исаия", "Исидор", "Ислам", "Исмаил", "Истислав", "Истома", "Истукарий", "Иштван", "Йюрген", "Кадваллон", "Кадир", "Казимир", "Каликст", "Калин", "Каллистрат", "Кальман", "Канат", "Карен", "Карлос", "Карп", "Картерий", "Кассиан", "Кассий", "Касторий", "Касьян", "Катберт", "Квинт", "Кехлер", "Киллиан", "Ким", "Кир", "Кириак", "Кирилл", "Клаас", "Клавдиан", "Клеоник", "Климент", "Кондрат", "Конон", "Конрад", "Константин", "Корнелиус", "Корнилий", "Коррадо", "Косьма", "Кратет", "Кратипп", "Крис", "Криспин", "Кристиан", "Кронид", "Кузьма", "Куприян", "Курбан", "Курт", "Кутлуг-Буга", "Кэлин", "Лаврентий", "Лавс", "Ладислав", "Лазарь", "Лайл", "Лампрехт", "Ландульф", "Лев", "Леви", "Ленни", "Леонид", "Леонтий", "Леонхард", "Лиам", "Линкей", "Логгин", "Лоренц", "Лоренцо", "Луи", "Луитпольд", "Лука", "Лукас", "Лукий", "Лукьян", "Луций", "Людовик", "Люцифер", "Макар", "Максим", "Максимиан", "Максимилиан", "Малик", "Малх", "Мамбет", "Маний", "Мануил", "Мануэль", "Мариан", "Мариус", "Марк", "Маркел", "Мартын", "Марчелло", "Матвей", "Матео", "Матиас", "Матфей", "Матфий", "Махмуд", "Меир", "Мелентий", "Мелитон", "Менахем-Мендель", "Месроп", "Мефодий", "Мечислав", "Мика", "Микеланджело", 
    "Микулаш", "Милорад", "Мина", "Мирко", "Мирон", "Мирослав", "Митрофан", "Михаил", "Михей", "Младан", "Модест", "Моисей", "Мордехай", "Мстислав", "Мурад", "Мухаммед", "Мэдисон", "Мэлор", "Мэлс", "Назар", "Наиль", "Насиф", "Натан", "Натаниэль", "Наум", "Нафанаил", "Нацагдорж", "Нестор", "Никандр", "Никанор", "Никита", "Никифор", "Никодим", "Николай", "Нил", "Нильс", "Ноа", "Ной", "Норд", "Нуржан", "Нурлан", "Овадья", "Оге", "Одинец", "Октав", "Октавиан", "Октавий", "Октавио", "Олаф", "Оле", "Олег", "Оливер", "Ольгерд", "Онисим", "Орест", "Осип", "Оскар", "Осман", "Отто", "Оттон", "Очирбат", "Пабло", "Павел", "Павлин", "Павсикакий", "Паисий", "Палладий", "Панкратий", "Пантелеймон", "Папа", "Паруйр", "Парфений", "Патрик", "Пафнутий", "Пахомий", "Педро", "Пётр", "Пимен", "Пинхас", "Пипин", "Питирим", "Пол", "Полидор", "Полиевкт", "Поликарп", "Поликрат", "Порфирий", "Потап", "Предраг", "Премысл", "Приск", "Прокл", "Прокопий", "Прокул", "Протасий", "Прохор", "Публий", "Рагнар", "Рагуил", "Радмир", "Радослав", "Разумник", "Раймонд", "Рамадан", "Рамазан", "Рахман", "Рашад", "Рейнхард", "Ренат", "Реститут", "Ричард", "Роберт", "Родерик", "Родион", "Рожер", "Розарио", "Роман", "Ромен", "Рон", "Ронан", "Ростислав", "Рудольф", "Руслан", "Руф", "Руфин", "Рушан", "Сабит", "Савва", "Савватий", "Савелий", "Савин", "Саддам", "Садик", "Саид", "Салават", "Салих", "Саллюстий", "Салман", "Самуил", "Сармат", "Святослав", "Севастьян", "Северин", "Секст", "Секунд", "Семён", "Септимий", "Серапион", "Сергей", "Серж", "Сигеберт", "Сильвестр", "Симеон", "Симон", "Созон", "Соломон", "Сонам", "Софрон", "Спиридон", "Срджан", "Станислав", "Степан", "Стефано", "Стивен", "Таврион", "Тавус", "Тадеуш", "Тарас", "Тарасий", "Тейс", "Тендзин", "Теофил", "Терентий", "Терри", "Тиберий", "Тигран", "Тимофей", "Тимур", "Тихомир", "Тихон", "Томас", "Томоми", "Торос", "Тофик", "Трифон", "Трофим", "Тудхалия", "Тутмос", "Тьерри", "Тьяго", "Уве", "Уильям", "Улдис", "Ульрих", "Ульф", "Умар", "Урызмаг", "Усама", "Усман", "Фавст", "Фаддей", "Файзулла", "Фарид", "Фахраддин", "Федериго", "Федосей", "Федот", "Фейсал", "Феликс", "Феоктист", "Феофан", "Феофил", "Феофилакт", "Фердинанд", "Ференц", "Фёдор", "Фидель", "Филарет", "Филат", "Филип", "Филипп", "Философ", "Филострат", 
    "Фирс", "Фока", "Фома", "Фотий", "Франц", "Франческо", "Фредерик", "Фридрих", "Фродо", "Фрол", "Фульк", "Хайме", "Ханс", "Харальд", "Харитон", "Харри", "Харрисон", "Хасан", "Хетаг", "Хильдерик", "Хирам", "Хлодвиг", "Хокон", "Хорив", "Хоселито", "Хосрой", "Хрисанф", "Христофор", "Хуан", "Цэрэндорж", "Чеслав", "Шалом", "Шамиль", "Шамсуддин", "Шапур", "Шарль", "Шейх-Хайдар", "Шон", "Эберхард", "Эдмунд", "Эдна", "Эдуард", "Элбэгдорж", "Элджернон", "Элиас", "Эллиот", "Эмиль", "Энрик", "Энрико", "Энтони", "Эразм", "Эраст", "Эрик", "Эрнст", "Эсекьель", "Эстебан", "Этьен", "Ювеналий", "Юлиан", "Юлий", "Юлиус", "Юрий", "Юстас", "Юстин", "Яков", "Якуб", "Якун", "Ян", "Яни", "Януарий", "Яромир", "Ярополк", "Ярослав"
]


surnames = [
    "Абабков", "Абаимов", "Абакишин", "Абакулин", "Абакулов", "Абакумкин", "Абакумов", "Абакушин", "Абакшин", "Абалакин", "Абалаков", "Абалдуев", "Абалкин", "Абатурин", "Абатуров", "Абашев", "Абашеев", "Абашенко", "Абашин", "Абашичев", "Абашкин", "Абашков", "Абашуров", "Абаянцев", "Аббакумов", "Абдулин", "Абдулла", "Абдулов", "Аблакатов", "Аблеухов", "Абоимов", "Аборин", "Абраменко", "Абраменков", "Абрамкин", "Абрамов", "Абрамович", "Абрамсон", "Абрамуш", "Абрамцев", "Абрамчик", "Абрамчук", "Абрамычев", "Абрахин", "Абрашин", "Абрашкин", "Абрикосов", "Абросимов", "Абросинов", "Аброськин", "Аброшин", "Абухов", "Абухович", "Авакин", "Аваков", "Авакумов", "Аванесов", "Аввакумов", "Августинович", "Августович", "Авдаев", "Авдаков", "Авдевичев", "Авдеев", "Авдеенко", "Авдеенков", "Авдеичев", "Авдейкин", "Авдиев", "Авдин", "Авдонин", "Авдонкин", "Авдонов", "Авдонюшкин", "Авдосев", "Авдотъин", "Авдотьев", "Авдотьин", "Авдохин", "Авдошин", "Авдулов", "Авдусин", "Авдушев", "Авдыев", "Авдышев", "Авдюков", "Авдюнин", "Авдюничев", "Авдюхов", "Авдюшин", "Авениров", "Аверин", "Аверинцев", "Аверихин", "Аверичев", "Аверичкин", "Аверкиев", "Аверкин", "Аверков", "Аверченко", "Аверченков", "Авершин", "Авершьев", "Аверьянов", "Авиафин", "Авилин", "Авилкин", "Авилов", "Авиловичев", "Авксентьев", "Авлампиев", "Авлашкин", "Авлов", "Авлуков", "Авнатамов", "Авнатомов", "Авр", "Авраамов", "Авраменко", "Аврамец", "Аврамов", "Аврамчик", "Аврасин", "Аврашин", "Аврашко", "Аврашков", "Аврашов", "Аврелин", "Аврорин", "Авроров", "Авросимов", "Авросинов", "Авсеев", "Авсеенко", "Авсейкин", "Австрийский", "Авсюков", "Автаев", "Автайкин", "Автоманов", "Автомонов", "Автономов", "Автухов", "Авчинников", "Авчухов", "Агаев", "Агальцов", "Агапеев", "Агапитов", "Агапов", "Агапьев", "Агарков", "Агафонкин", "Агафонов", "Агашин", "Агашкин", "Агашков", "Аггеев", "Агдавлетов", "Агеев", "Агеенко", "Агеенков", "Агейкин", "Агейчев", "Агейчик", "Агибалов", "Агиевич", "Агин", "Агишев", "Агишин", "Агищев", "Аглинцев", "Агопов", "Агранов", "Аграновский", "Агренев", "Агрененко", "Агриколянский", "Агуреев", "Агушев", "Адаев", "Адаменко", "Адамов", "Адамович", "Адамчук", "Адашев", "Адвокатов", "Адельфинский", "Адинец", "Адонисов", "Адоратский", "Адриянов", "Адуев", "Адыбаев", "Аедоницкий", 
    "Ажгибесов", "Азамов", "Азанов", "Азанчевский", "Азанчеев", "Азарин", "Азаров", "Азарьев", "Азегов", "Азерников", "Азизов", "Азимов", "Азин", "Азначеев", "Азов", "Азовцев", "Азянов", "Аипов", "Айвазов", "Айвазовский", "Айдаров", "Акаткин", "Акатов", "Акатьев", "Акашев", "Акашин", "Акбаров", "Акберов", "Аквилев", "Акдавлетов", "Акентьев", "Акилин", "Акилов", "Акимакин", "Акименко", "Акимихин", "Акимичев", "Акимкин", "Акимов", "Акимочев", "Акимочкин", "Акимушкин", "Акимчев", "Акимчин", "Акимычев", "Акиндинов", "Акинин", "Акинишин", "Акинфиев", "Акинфов", "Акинфьев", "Акинчев", "Акиншин", "Акиньшин", "Акифьев", "Акишев", "Акишин", "Аккузин", "Акопов", "Аксаков", "Аксанов", "Аксененко", "Аксененков", "Аксенов", "Аксентьев", "Аксенцев", "Аксенцов", "Аксенюшкин", "Аксинин", "Аксюков", "Аксюта", "Аксютенок", "Аксютин", "Аксянов", "Акуленко", "Акуленок", "Акулин", "Акулинин", "Акулиничев", "Акулинский", "Акулич", "Акулов", "Акулышин", "Акульшин", "Акуляков", "Акундинов", "Акустьев", "Акушев", "Акциперов", "Акципетров", "Акчурин", "Алабердиев", "Алабин", "Алабушев", "Алабышев", "Аладышкин", "Аладьин", "Алаев", "Алайкин", "Алалыкин", "Алампиев", "Алаторцев", "Алатырев", "Алатырцев", "Алачев", "Алачеев", "Алашеев", "Алдаков", "Алдашин", "Алдонин", "Алдохин", "Алдошин", "Алдошкин", "Алдушин", "Алдушкин", "Алдущенков", "Алебастров", "Алеев", "Алейник", "Алейников", "Александренков", "Александрийский", "Александрикин", "Александров", "Александровский", "Александрук", "Александрюк", "Алексанин", "Алексанкин", "Алексанов", "Алексахин", "Алексашин", "Алексеев", "Алексеевский", "Алексеенко", "Алексеенков", "Алексеичев", "Алексейчик", "Алексин", "Алексинский", "Алексов", "Алексутин", "Алекторов", "Алемасов", "Алемпиев", "Аленев", "Алеников", "Аленин", "Аленичев", "Аленкин", "Аленников", "Аленов", "Алентов", "Алентьев", "Аленчев", "Аленчиков", "Аленшев", "Алесин", "Алесов", "Алеутский", "Алеханов", "Алехин", "Алехов", "Алешейкин", "Алешечкин", "Алешин", "Алешинцев", "Алешихин", "Алешкевич", "Алешкин", "Алешков", "Алешников", "Алешонков", "Алиев", "Алимгулов", "Алимов", "Алимпиев", "Алин", "Алипанов", "Алипов", "Алипьев", "Алисейко", "Алисов", "Алистратов", "Алифанов", "Алифонов", "Аллавердиев", "Аллавердов", "Аллилуев", "Алмагестов", "Алмагестров", 
    "Алмазов", "Алмин", "Алов", "Алпаров", "Алпатов", "Алпин", "Алтунин", "Алтуфьев", "Алтухов", "Алтынин", "Алтынов", "Алфеев", "Алферов", "Алферьев", "Алфимов", "Алхимов", "Алымбеков", "Алымов", "Алынбеков", "Альбертов", "Альбицкий", "Альбов", "Альбовский", "Альтов", "Альтовский", "Альхименко", "Альхимович", "Альшанников", "Альшевский", "Алютин", "Алюхин", "Алюшин", "Алюшников", "Алябин", "Алябушев", "Алябышев", "Алябьев", "Алявдин", "Аляев", "Алякринский", "Аляпин", "Амбалов", "Амброс", "Амбросий", "Амбросимов", "Амвросимов", "Амвросов", "Амвросьев", "Амеленко", "Амелехин", "Амелин", "Амеличев", "Амелишко", "Амелькин", "Амельчев", "Амельченко", "Амельченков", "Амельянов", "Амелюшкин", "Амелякин", "Американцев", "Аметистов", "Аминов", "Амирев", "Амиров", "Аморский", "Амосов", "Ампелогов", "Ампилов", "Амплеев", "Амстиславский", "Амусин", "Амусов", "Амфилохов", "Амфитеатров", "Амчанинов", "Амченцев", "Амчиславский", "Анаксагоров", "Ананенков", "Ананич", "Ананичев", "Ананкин", "Ананко", "Ананский", "Ананченко", "Ананченков", "Ананьев", "Ананьевский", "Ананьин", "Анастасов", "Анастасьев", "Анаткин", "Анахин", "Анахов", "Анашкин", "Ангарщиков", "Ангелин", "Ангелов", "Ангельский", "Анджиевский", "Андреев", "Андреевский", "Андреенко", "Андреещев", "Андреищев", "Андрейкин", "Андрейцев", "Андрейченко", "Андрейчик", "Андрейчиков", "Андрейчук", "Андренко", "Андреянов", "Андрианов", "Андриановский", "Андриашин", "Андриевский", "Андриенко", "Андрийчак", "Андрийчук", "Андрионов", "Андриянов", "Андрияш", "Андрияшев", "Андрияшкин", "Андроников", "Андронников", "Андронов", "Андропов", "Андросенко", "Андросик", "Андросов", "Андрощенко", "Андрощук", "Андрунец", "Андрунин", "Андрусенко", "Андрусив", "Андрусик", "Андрусишин", "Андрускив", "Андрусов", "Андрусский", "Андрусяк", "Андрухненко", "Андрухович", "Андруша", "Андрушакевич", "Андрушевич", "Андрущакевич", "Андрущенко", "Андрюк", "Андрюков", "Андрюнин", "Андрюхин", "Андрюцкий", "Андрюшечкин", "Андрюшин", "Андрющенко", "Анемхуров", "Аниканов", "Аникеев", "Аникеенко", "Аникикевич", "Аникин", "Аникичев", "Аникушин", "Аникушкин", "Анин", "Анисим", "Анисимков", "Анисимов", "Анисимцев", "Анисин", "Анисифоров", "Анискевич", "Анискин", "Анисковец", "Анискович", "Анисов", "Анисович", "Анистратов", "Аниськин", 
    "Аниськов", "Анихнов", "Аничев", "Аниченко", "Аничкин", "Аничков", "Анищенко", "Анищенков", "Анкидинов", "Анкин", "Анкиндинов", "Анкудимов", "Анкудинов", "Анненков", "Анненский", "Аннин", "Аннинский", "Аннич", "Анничкин", "Аннушкин", "Аннщенкский", "Аннщенский", "Анокин", "Аносков", "Аносов", "Анохин", "Аношечкин", "Аношин", "Аношкин", "Анпилов", "Ансеров", "Антипенко", "Антипенков", "Антипин", "Антипичев", "Антипкин", "Антипов", "Антипьев", "Антифеев", "Антифьев", "Антокольский", "Антоманов", "Антоневич", "Антоненко", "Антоненков", "Антонец", "Антоник", "Антоников", "Антонич", "Антонишин", "Антонников", "Антонов", "Антонович", "Антоновский", "Антонцев", "Антончик", "Антонычев", "Антоньев", "Антонюк", "Антоняк", "Антохи", "Антохин", "Антошин", "Антошкин", "Антошко", "Антощук", "Антропенко", "Антропов", "Антрохин", "Антрошин", "Антрощенко", "Антрушев", "Антрушин", "Антук", "Антуфьев", "Антушев", "Антушевич", "Антыпко", "Антышев", "Антюфеев", "Антюхин", "Антюхов", "Анурин", "Ануров", "Анурьев", "Ануфриев", "Анучин", "Анучкин", "Анушкин", "Анфилатов", "Анфилов", "Анфилодьев", "Анфилофьев", "Анфимкин", "Анфимов", "Анфиногенов", "Анфиногентов", "Анфудимов", "Анфудинов", "Анхим", "Анхимов", "Анцев", "Анцибор", "Анциборенко", "Анциборов", "Анциперов", "Анциферов", "Анцифиров", "Анцишкин", "Анцуп", "Анцупов", "Анцыферов", "Анцыфиров", "Анцышкин", "Анютин", "Апанасенко", "Апашев", "Аплетин", "Аплечеев", "Аполитов", "Аполлонов", "Аполлонский", "Аппаков", "Апраксин", "Апрелиев", "Апрелов", "Апсеитов", "Апухтин", "Аракин", "Аракчеев", "Аралин", "Арамилев", "Арапкин", "Арапов", "Арасланов", "Арбузов", "Аргамаков", "Аргентовский", "Аргунов", "Аргушкин", "Ардабьев", "Ардаев", "Ардалионов", "Ардасенов", "Ардатов", "Ардашев", "Ардашников", "Ардеев", "Аредаков", "Аренов", "Аренский", "Арепьев", "Арестов", "Аретинский", "Арефин", "Арефов", "Арефьев", "Аржавитин", "Аржавитинов", "Аржаев", "Аржаников", "Аржанников", "Аржанов", "Аржанухин", "Аржаных", "Арзамасцев", "Арзубов", "Аринин", "Аринич", "Аринкин", "Аринушкин", "Аринчев", "Аристархов", "Аристов", "Аристовский", "Аристотелев", "Аричков", "Аришин", "Аришкин", "Арищев", "Аркадов", "Аркадьев", "Аркадьин", "Арканников", "Аркашин", "Арнаутов", "Арнольдов", "Аронов", "Арсеев", "Арсеенков", "Арсенин", 
    "Арсеничев", "Арсенков", "Арсенов", "Арсенович", "Арсентьев", "Арсеньев", "Арсенюк", "Арскии", "Арсланов", "Артаков", "Артамонов", "Артамонычев", "Артамохин", "Артамошин", "Артанов", "Артеев", "Артеменко", "Артеменков", "Артемин", "Артемичев", "Артемкин", "Артемов", "Артемчук", "Артемьев", "Артищев", "Артищенко", "Артоболевский", "Артыбашев", "Артыков", "Артюгов", "Артюков", "Артюх", "Артюхин", "Артюхов", "Артюшенко", "Артюшин", "Артюшкевич", "Артюшков", "Артяев", "Арутюнов", "Арутюнян", "Архангельский", "Архаров", "Архип", "Архипенко", "Архипенков", "Архипкин", "Архипов", "Архиповский", "Архипцев", "Архипычев", "Архипьев", "Архиреев", "Арцыбашев", "Арцыбушев", "Аршавский", "Аршанинов", "Аршинников", "Аршинов", "Арысланов", "Асадов", "Асадулин", "Асадуллин", "Асанов", "Асатов", "Асауленко", "Асаулов", "Асаульченко", "Асафов", "Асафьев", "Асеев", "Асейкин", "Асенин", "Асин", "Асинкритов", "Асипенко", "Аскеров", "Асланов", "Асманов", "Асмус", "Асонов", "Ассанов", "Ассанович", "Ассонов", "Астанин", "Астанкин", "Астанков", "Астанов", "Астапенко", "Астапенков", "Астапеня", "Астапкин", "Астапов", "Астапович", "Астапченок", "Астапчук", "Астафимов", "Астафичев", "Астафуров", "Астафьев", "Астахин", "Астахов", "Асташев", "Асташевский", "Асташенко", "Асташенков", "Асташин", "Асташкин", "Асташков", "Асташов", "Астров", "Атаманенко", "Атаманов", "Атаманченко", "Атаманчук", "Атаманюк", "Атиков", "Атласов", "Атраментов", "Атрохин", "Атрохов", "Атрошкин", "Атрошков", "Атрощенко", "Атучин", "Аулов", "Аушев", "Афанасенко", "Афанасенков", "Афанаскин", "Афанасов", "Афанасьев", "Афанаськин", "Афинин", "Афинов", "Афиногенов", "Афиногентов", "Афинский", "Афонасьев", "Афонин", "Афоничев", "Афонов", "Афончиков", "Афончин", "Афонышев", "Афонькин", "Афонюшин", "Афонюшкин", "Африканов", "Африкантов", "Афродитин", "Афродитов", "Афросимов", "Афросинов", "Афрунин", "Ахвердов", "Ахмадулин", "Ахматов", "Ахматулин", "Ахмедов", "Ахмедулов", "Ахметов", "Ахметшин", "Ахов", "Ахрамеев", "Ахраменко", "Ахременко", "Ахромеев", "Ахромов", "Ахросимов", "Ахряпов", "Ахтырцев", "Ахунов", "Ачкасов", "Ачугин", "Ашарин", "Ашитков", "Ашкенази", "Ашмарин", "Ашпин", "Ашукин", "Ашурков", "Ашуров", "Ащеулов", "Аяцков"
]


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'passport.yandex.ru',
    'Origin': 'https://passport.yandex.ru',
    'Referer': 'https://passport.yandex.ru/registration/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def regexp(text, pattern):
    if not text:
        return None

    found = re.search(pattern, text)

    return found.group(1) if found else None


class Init:

    def __init__(self, user_name = None, password = None, RUCAPTCHA_KEY = None, text_file = 'ready.txt'):
        self.user_name = user_name
        self.password = password

        self.RUCAPTCHA_KEY = RUCAPTCHA_KEY

        self.name = self.generate_name()
        self.surname = self.generate_surname()
        self.answer = self.generate_name() + "_" + self.generate_surname()
        self.session = requests.session()
        self.codes = self.track_id_and_csrf()

        if self.user_name == None:
            self.generate_user_name()
        else:
            if not self.user_name_valid():
                print('Замена логина потому что он занят')

                self.generate_user_name()

        if self.password == None:
            self.generate_password()
        else:
            if not self.password_valid():
                print('Изменение пароля потому что он не подходит под условия от яндекса')

                self.generate_password()

        self.registred = False
        self.text_file = text_file


    def get_captcha(self):
        while True:
            captcha = self.session.post(
                'https://passport.yandex.ru/registration-validations/textcaptcha', 
                data = {
                    "track_id": self.codes['track_id'],
                    "csrf_token": self.codes['csrf'],
                    'language': 'ru',
                    'ocr': True,
                },
                headers = headers,
            )

            captcha = captcha.json()

            print(captcha['image_url'])
            
            if self.RUCAPTCHA_KEY:
                print('solving... wait.')

                for _ in range(10):
                    a = requests.post(
                        'https://rucaptcha.com/in.php',
                         data= {
                            'key': self.RUCAPTCHA_KEY,
                            'method': 'base64',
                            'body': base64.b64encode(requests.get(captcha['image_url']).content),
                        }
                    ).text.split('|')

                    if a[0] == 'OK':
                        break
                    else:
                        print(a[0])

                for _ in range(10):
                    res = requests.post(
                        'https://rucaptcha.com/res.php', 
                        data={
                            'key': self.RUCAPTCHA_KEY,
                            'action':'get',
                            'id': a[1],
                        }
                    ).text.split('|')

                    if res[0] == 'OK':
                        resolved_captcha = res[1]

                        break
                    else:
                        print(res[0])

                        time.sleep(4)

            else:
                resolved_captcha = input('Captcha: ')

            result_resolve = self.session.post(
                'https://passport.yandex.ru/registration-validations/checkHuman', 
                data = {
                    "track_id": self.codes['track_id'],
                    "csrf_token": self.codes['csrf'],
                    'answer': resolved_captcha,
                },
                headers = headers,
            ).json()

            if result_resolve['status'] == 'ok':
                print("Капча успешно решена!")

                break

        return result_resolve

    def generate_password(self, nums = 4, letters = 8):
        while True:
            data = [random.choice(string.ascii_letters) for x in range(letters)]

            data += [random.choice(string.digits) for x in range(nums)]

            random.shuffle(data)

            self.password = "".join(data)

            if self.password_valid():
                break

        return self.password


    def generate_name(self):
        return random.choice(names)


    def generate_surname(self):
        return random.choice(surnames)


    def generate_user_name(self, min_symbols = 8, max_symbols = 12):
        while True:
            self.user_name = "".join(
                random.choice(string.ascii_letters + string.digits) for x in range(random.randint(min_symbols, max_symbols))
            )

            if self.user_name_valid():
                break

        return self.user_name


    def track_id_and_csrf(self):
        get_first = self.session.get('https://passport.yandex.ru/registration/')

        soup = BeautifulSoup(get_first.text, 'html.parser')

        track = soup.find('input', attrs= {'name': 'track_id'})['value']
        csrf = regexp(get_first.text, r'"csrf":"([\w\W]+:[\d]+)"')

        return {
            "track_id": track,
            "csrf": csrf,
        }

    
    def password_valid(self):
        res = self.session.post(
            'https://passport.yandex.ru/registration-validations/password',
            data = {
                "track_id": self.codes['track_id'],
                "csrf_token": self.codes['csrf'],
                "password": self.password,
            },
            headers = headers,
        ).json()

        return (type(res) is dict and not type(res.get('validation_errors', None)) is list)


    def user_name_valid(self):
        res = self.session.post(
            'https://passport.yandex.ru/registration-validations/login',
            data = {
                "track_id": self.codes['track_id'],
                "csrf_token": self.codes['csrf'],
                "login": self.user_name,
            },
            headers = headers,
        ).json()

        return (type(res) is dict and res.get('status') == 'ok')


    def return_data(self, txt_writing = False):
        if self.registred == False:
            return 'Аккаунт не зарегистрирован'

        data = '%s:%s:%s:%s:%s' % (
            self.user_name,
            self.password,
            self.answer,
            self.name,
            self.surname,
        )

        if txt_writing:
            with open(self.text_file, 'a+') as f:
                f.write(data + "\n")

        return data

    
    def register_account(self):
        result = self.session.post(
            'https://passport.yandex.ru/registration-validations/registration-alternative', 
            data = {
                "track_id": self.codes['track_id'],
                "csrf_token": self.codes['csrf'],
                'firstname': self.name,
                'lastname': self.surname,
                'surname': '',
                'login': self.user_name,
                'password': self.password,
                'password_confirm': self.password,
                'hint_question_id': '12',
                'hint_question': 'Фамилия вашего любимого музыканта',
                'hint_question_custom': '',
                'hint_answer': 'Курт',
                'captcha': self.get_captcha(),
                'phone': '',
                'phoneCode': '',
                'human-confirmation': 'captcha',
                'from': 'mail',
                'eula_accepted': 'on',
                'type': 'alternative'
            },
            headers = headers,
        )

        try:
            result_answer = result.json()

            if result_answer.get('status') == 'ok':
                self.registred = True
        
        except Exception:
            pass
        
        print(self.return_data())
