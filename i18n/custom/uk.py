# -*- coding: utf-8 -*-

# Translated by Yuri Chornoivan (Юрій Чорноіван)

# FAO Translators:
# First of all thank you for your interest in translating this game,
# I will be grateful if you could share it with the community -
# if possible please send it back to my email, and I'll add it to the next version.

# The translation does not have to be exact as long as it makes sense and fits in its location
# (if it doesn't I'll try to either make the font smaller or make the area wider - where possible).
# The colour names in other languages than English are already in smaller font.

d = dict()  # messages for display
dp = dict()  # messages with pronunciation exceptions - this dictionary will override entries in a copy of d

numbers = ["один", "два", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять", "десять", "одинадцять",
           "дванадцять", "тринадцять", "чотирнадцять", "п’ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять",
           "дев'ятнадцять", "двадцять", "двадцять один", "двадцять два", "двадцять три", "двадцять чотири",
           "двадцять п’ять", "двадцять шість", "двадцять сім", "двадцять вісім", "двадцять дев’ять"]
numbers2090 = ["тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"]

d['abc_flashcards_word_sequence'] = ['<1>А<2>втобус', '<1>Б<2>анан', '<1>В<2>иноград', '<1>Г<2>ітара', '<1>Ґ<2>удзик',
                                     '<1>Д<2>ельфін', '<1>Е<2>кран', '<1>Є<2>нот', '<1>Ж<2>ираф', '<1>З<2>ебра',
                                     '<2>М<1>и<2>ша', '<1>І<2>глу', '<1>Ї<2>жак', '<1>Й<2>огурт', '<1>К<2>ач<1>к<2>а',
                                     '<1>Л<2>ев', '<1>М<2>ураха', '<1>Н<2>отатки', '<1>О<2>чі', '<1>П<2>арасолька',
                                     '<1>Р<2>иба', '<1>С<2>онце', '<1>Т<2>елефон', '<1>У<2>збережжя',
                                     '<1>Ф<2>ортепіано', '<1>Х<2>ліб', '<1>Ц<2>ап', '<1>Ч<2>айник', '<1>Ш<2>импанзе',
                                     '<1>Щ<2>ука', '<2>Кін<1>ь', '<1>Ю<2>рист', '<1>Я<2>блуко']
d['abc_flashcards_frame_sequence'] = [77, 71, 6, 28, 86, 59, 40, 87, 30, 25, 12, 8, 29, 73, 3, 11, 0, 13, 75, 20, 5, 18,
                                      79, 82, 34, 35, 70, 19, 37, 38, 45, 85, 42]

# d['abc_flashcards_frame_sequence'] = [77, 71, 6, 28, 86, 59, 40, 87, 30, 25, 12', 8, 29, 73, 3, 11, 0, 13, 75, 20, 5, 18, 79, 82, 34, 35, 70, 19, 37, 38, 45, 85, 42]

# alphabet uk: - 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
alphabet_uc = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
               'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']
alphabet_lc = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
               'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
# correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['-']
accents_uc = []


def n2txt(n, twoliner=False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbers[n - 1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090[(n // 10) - 2]
        if m == 0:
            return tens
        elif m > 0:
            ones = numbers[m - 1]
            if twoliner:
                return [tens, ones]
            else:
                return tens + " " + ones
    elif n == 0:
        return "нуль"
    elif n == 100:
        return "сто"
    return ""


# TIME FOR DISPLAY
mt1 = ["одна", "дві", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять", "десять", "одинадцять",
       "дванадцять", "тринадцять", "чотирнадцять", "п’ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять",
       "дев’ятнадцять", "двадцять", "двадцять одна", "двадцять две", "двадцять три", "двадцять чотири",
       "двадцять п’ять", "двадцять шість", "двадцять сім", "двадцять вісім", "двадцять дев’ять", "тридцять",
       "тридцять одна", "тридцять дві", "тридцять три", "тридцять чотири", "тридцять п’ять", "тридцять шість",
       "тридцять сім", "тридцять вісім", "тридцять дев’ять"]
mt2 = ["одну", "дві", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять", "десять", "одинадцять",
       "дванадцять", "тринадцять", "чотирнадцять", "п’ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять",
       "дев’ятнадцять", "двадцять", "двадцять одну", "двадцять дві", "двадцять три", "двадцять чотири",
       "двадцять п’ять", "двадцять шість", "двядцать сім", "двадцять вісім", "двадцять дев’ять"]

ht1 = ["перша", "друга", "третя", "четверта", "п’ята", "шоста", "сьома", "восьма", "дев’ята", "десята", "одинадцята",
       "дванадцята"]
ht2 = ["на першу", "на другу", "на третю", "на четверту", "на п’яту", "на шосту", "на сьому", "на восьму", "на дев’яту",
       "на десяту", "на одинадцяту", "на дванадцяту"]

def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 0:
        if h == 12:
            h = 1
        else:
            h += 1

    if m == 0:
        if h == 1:
            return "перша година"
        elif h < 5:
            return "%s години" % ht1[h - 1]
        else:
            return "%s годин" % ht1[h - 1]
    elif m == 15:
        return "чверть %s" % ht2[h - 1]
    elif m == 20:
        return "%s хвилин %s" % (mt1[m - 1], ht2[h - 1])
    elif m in [1, 21]:
        return "%s хвилина %s" % (mt1[m - 1], ht2[h - 1])
    elif m in [2, 3, 4, 22, 23, 24]:
        return "%s хвилини %s" % (mt1[m - 1], ht2[h - 1])
    elif m < 30:
        return "%s хвилин %s" % (mt1[m - 1], ht2[h - 1])
    elif m == 30:
        return "о пів %s" % ht2[h - 1]
    elif m == 39:
        return "за двадцять одну хвилину %s" % ht1[h - 1]
    elif m == 40:
        return "за %s хвилин %s" % (mt2[60 - m - 1], ht1[h - 1])
    elif m == 45:
        return "за чверть %s" % ht1[h - 1]
    elif m == 59:
        return "за одну хвилину %s" % ht1[h - 1]
    elif m > 30:
        return "за %s хвилин %s" % (mt2[60 - m - 1], ht1[h - 1])
    return ""

# only if this is used in Ukrainian
def time2officialstr(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. six fifty five - for 6:55'

    # get the right "suffix" for hour
    if h == 1:
        sf = "година"
    elif h < 5:
        sf = "години"
    else:
        sf = "годин"

    if m == 0:
        return "%s %s" % (numbers[h - 1], sf)
    elif m == 1:
        return "%s %s одна хвилина" % (numbers[h - 1], sf)
    elif m in [21, 31, 41, 51]:
        return "%s %s %s одна хвилина" % (numbers[h - 1], sf, n2txt(m - 1))
    elif m == 2:
        return "%s %s дві хвилини" % (numbers[h - 1], sf)
    elif m in [22, 32, 42, 52]:
        return "%s %s %s дві хвилини" % (numbers[h - 1], sf, n2txt(m - 2))
    elif m in [3, 4, 23, 24, 33, 34, 43, 44, 53, 54]:
        return "%s %s %s хвилини" % (numbers[h - 1], sf, n2txt(m))
    else:
        return "%s %s %s хвилин" % (numbers[h - 1], sf, n2txt(m))

#write a fraction in words
numerators = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
d_singular = ['', 'half', 'third', 'quarter', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
d_plural = ['', 'halves', 'thirds', 'quarters', 'fifths', 'sixths', 'sevenths', 'eighths', 'ninths', 'tenths', 'elevenths', 'twelfths']

def fract2str(n, d):
    if n == 1:
        return numerators[0] + " " + d_singular[d-1]
    else:
        return numerators[n-1] + " " + d_plural[d-1]

# The following 12 categories will be used to activate the 12 Word Builder Games in Ukrainian, bear in mind it's 589 words to translate. Possibly the best way to do it would be to use google translate and correct wrong translations.
d["a4a_animals"] = ["корова", "індичка", "креветка", "вовк", "пантера", "панда", "сорока", "молюск", "поні", "миша",
                    "мопс", "коала", "жаба", "сонечко", "горила", "лама", "стерв’ятник", "хом’як", "пташка",
                    "морська зірка", "ворона", "довгохвостий папуга", "гусінь", "тигр", "колібрі", "піранья", "свиня",
                    "скорпіон", "лисиця", "леопард", "ігуана", "дельфін", "летюча миша", "курча", "краб", "курка",
                    "оса", "хамелеон", "кит", "їжак", "оленятко", "лось", "бджола", "гадюка", "сорокопуд", "віслюк",
                    "морська свинка", "лінивець", "кінь", "пінгвін", "видра", "ведмідь", "зебра", "страус", "верблюд",
                    "антилопа", "лемур", "голуб", "лама", "кріт", "скат", "баран", "скунс", "медуза", "вівця", "акула",
                    "кошеня", "олень", "равлик", "фламінго", "кролик", "устриця", "бобер", "горобець", "голубка",
                    "орел", "жук", "бегемот", "сова", "кобра", "саламандра", "гусак", "кенгуру", "бабка", "жабка",
                    "пелікан", "кальмар", "левеня", "ягуар", "качка", "ящірка", "носоріг", "гієна", "бик", "павич",
                    "папуга", "лось", "крокодил", "мураха", "козел", "кроленя", "лев", "білка", "опосум", "шимпанзе",
                    "оленя", "ховрах", "слон", "жирафа", "павук", "щеня", "сойка", "тюлень", "півень", "черепаха",
                    "бик", "кіт", "щур", "слимак", "бізон", "чорний дрізд", "лебідь", "омар", "собака",
                    "москіт", "змія", "круча", "мурахоїд"]
d["a4a_sport"] = ["дзюдо", "плавання", "велогонка", "розтяжка", "шолом", "ковзани", "ходьба", "біг", "пірнання",
                  "батут", "піший туризм", "бокс", "хокей", "забіг", "кидок", "скейт", "перемога", "присідання", "лижі",
                  "гольф", "свисток", "факел", "яхта", "стійка", "теніс", "стрибок", "веслування", "біг підтюпцем",
                  "скакалка"]
d["a4a_body"] = ["зуб", "щока", "кісточка", "коліно", "п’ята", "мускул", "рот", "ступня", "рука", "лікоть", "волосся",
                 "вія", "борода", "пупок", "великий палець", "груди", "ніздря", "ніс", "поперек", "рука", "брова",
                 "кулак", "шия", "зап’ясток", "горло", "око", "нога", "спина", "вухо", "палець", "ступня", "борода",
                 "лице", "спина", "підборіддя", "сідниці", "стегно", "живіт"]
d["a4a_people"] = ["дівчина", "хлопець", "син", "однокласники", "друзі", "немовля", "дитя", "татусь", "матуся",
                   "двійнята", "брати", "чоловік", "мати", "дідусь", "сім’я", "дівчина", "жінка", "чоловік",
                   "нареченна", "тітонька", "бабуся", "закохані", "хлопчина", "двійнята", "дикуни", "хлопчик", "сестри",
                   "жінка", "леді"]
d["a4a_food"] = ["цукерка", "сосиска", "гамбургер", "стейк", "помадка", "пончик", "кокос", "рис", "морозиво", "желе",
                 "йогурт", "десерт", "крендель", "арахіс", "варення", "курка", "крекер", "бекон", "спеції", "кава",
                 "пиріг", "лимонад", "шоколад", "пляшка з водою", "обід", "лід", "цукор", "кетчуп", "суп", "сік",
                 "чіпси", "торт", "пюре", "чай", "булка", "сир", "відбивна", "бутерброд", "шматочки", "присипка",
                 "піца", "борошно", "жувальна різинка", "спагеті", "печеня", "напій", "тушковане м’ясо", "намащування",
                 "м’ясо", "молоко", "страва", "кукурудза", "хліб", "горіх", "яйце", "гот-доґ", "шинка"]
d["a4a_clothes_n_accessories"] = ["прикраси", "шкарпетка", "піджак", "шпилька", "пляма", "шорти", "кишеня", "намисто",
                                  "спортивний светр", "уніформа", "плащ", "штани", "сонячні окуляри", "куртка", "светр",
                                  "блузка", "сандалі", "костюм", "піжама", "спідниця", "блискавка", "туфлі", "камінь",
                                  "краватка", "шльопанці", "рукавички", "капелюх", "рукав", "кепка", "купальний костюм",
                                  "кросівок", "жилет", "окуляри", "шнурок", "латка", "шарф", "черевик", "ґудзик",
                                  "плаття", "пояс", "підошви", "мантія", "труси", "кімоно", "комбінезон"]
d["a4a_actions"] = ["лизати", "закидати", "молити", "падати", "дряпати", "торкати", "нюхати", "дивитися", "дертися",
                    "копати", "вити", "спати", "досліджувати", "малювати", "обнімати", "навчати", "куняти", "ліпити",
                    "ловити", "плескати", "плакати", "співати", "зустрічатися", "продавати", "дзьобати", "вдарити",
                    "ставати на коліна", "знайти", "танцювати", "кахикати", "різати", "думати", "гавкати", "говорити",
                    "веселити", "куховарити", "писати", "бити", "бренькати", "навчатися", "орати", "мріяти",
                    "надсилати", "пірнати", "шепотіти", "ридати", "трясти", "годувати", "повзти", "отаборитися",
                    "розливати", "митися", "кричати", "рвати", "плавати", "тягти", "поїсти", "цілувати", "сидіти",
                    "вилуплюватися", "блимати", "слухати", "цілуватися", "грати", "мити", "балакати", "вести", "пити",
                    "літати", "жонглювати", "кусати", "мести", "роздивлятися", "в’язати", "піднімати", "тримати",
                    "читати", "квакати", "витріщитися", "їсти"]
d["a4a_construction"] = ["маяк", "двері", "цирк", "церква", "буда", "храм", "дим", "димар", "цегла", "колодязь",
                         "вулиця", "замок", "крамниця", "сходи", "школа", "ферма", "місток", "гребля", "піраміда",
                         "комора", "млин", "вікно", "хатка", "сходинка", "магазин", "сарай", "дах", "дзвіниця", "гараж",
                         "мечеть", "шпиталь", "намет", "будинок", "стіна", "банк", "віконниця", "хижа"]
d["a4a_nature"] = ["суходіл", "круча", "пагорб", "каньйон", "камінь", "море", "озеро", "пляж", "узбережжя", "гора",
                   "ставок", "вершина", "лава", "печера", "дюна", "острів", "ліс", "пустеля", "айсберг"]
d["a4a_jobs"] = ["клоун", "інженер", "священник", "ветеринар", "суддя", "повар", "атлет", "бібліотекарка", "жонглер",
                 "поліцейський", "водопровідник", "нагорода", "королева", "фермер", "фокусник", "рицар", "доктор",
                 "муляр", "прибиральниця", "вчителька", "мисливець", "солдат", "музикант", "юрист", "рибалка",
                 "принцеса", "пожежник", "черниця", "пірат", "ковбой", "електрик", "нянька", "король",
                 "президент", "клерк", "тесляр", "жокей", "робітник", "механік", "пілот", "актор", "кухар", "студент",
                 "м’ясник", "бухгалтер", "принц", "папа", "моряк", "боксер", "балерина", "тренер", "астронавт",
                 "художник", "анестезіолог", "учений"]
d["a4a_fruit_n_veg"] = ["морква", "ведмежина", "селера", "редька", "какао", "персик", "диня", "грейпфрут", "броколі",
                        "виноград", "шпинат", "фіга", "кісточка", "редиска", "помідор", "ківі", "спаржа", "оливки",
                        "огірки", "боби", "полуниця", "перці", "малина", "абрикос", "картопля", "горох", "капуста",
                        "вишня", "гарбузи", "ожина", "груша", "апельсин", "гарбуз", "авокадо", "часник", "цибуля",
                        "яблуко", "лайм", "цвітна капуста", "манго", "салат", "лимон", "баклажан", "артишоки", "сливи",
                        "цибуля", "банани", "папая"]
d["a4a_transport"] = ["яхта", "таксі", "автомобіль", "велосипед", "пліт", "педаль", "автобус", "кермо", "човен",
                      "пікап", "сани", "килим", "потоцикл", "потяг", "корабель", "фургон", "каное", "ракета", "мачта",
                      "санчата", "велосипед"]
