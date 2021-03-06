import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


#=======================[commands]============================

@Client.on_message(~filters.channel & filters.command(["font"]))
async def style_buttons(c, m, cb=False):
    mm = m.text.split('/font')[1]
    buttons = [[
        InlineKeyboardButton('๐๐ข๐๐๐ ๐๐๐๐๐', callback_data='style+typewriter'),
        InlineKeyboardButton('๐๐ฆ๐ฅ๐๐๐๐', callback_data='style+outline'),
        InlineKeyboardButton('๐๐๐ซ๐ข๐', callback_data='style+serif'),

        ],[

        InlineKeyboardButton('๐บ๐๐๐๐', callback_data='style+bold_cool'),
        InlineKeyboardButton('๐๐๐๐๐', callback_data='style+cool'),
        InlineKeyboardButton('Sแดแดสส Cแดแดs', callback_data='style+small_cap'),

        ],[

        InlineKeyboardButton('๐๐ธ๐๐พ๐๐', callback_data='style+script'),
        InlineKeyboardButton('๐ผ๐ฌ๐ป๐ฒ๐น๐ฝ', callback_data='style+script_bolt'),
        InlineKeyboardButton('แตโฑโฟสธ', callback_data='style+tiny'),

        ],[

        InlineKeyboardButton('Uอnอdอeอrอlอiอnอeอ', callback_data='style+underline'),
        InlineKeyboardButton('๐ฆ๐ฎ๐ป๐', callback_data='style+sans'),
        InlineKeyboardButton('๐๐๐ฃ๐จ', callback_data='style+slant_sans'),

        ],[

        InlineKeyboardButton('๐๐ข๐ฏ๐ด', callback_data='style+slant'),
        InlineKeyboardButton('๐ฒ๐บ๐๐', callback_data='style+sim'),
        InlineKeyboardButton('โธ๏ธโพ๏ธโ๏ธโธ๏ธโ๏ธโบ๏ธโ๏ธ', callback_data='style+circles'),

        ],[

        InlineKeyboardButton('๐๏ธ๐๏ธ๐ก๏ธ๐๏ธ๐๏ธ๐๏ธ๐ข๏ธ', callback_data='style+circle_dark'),
        InlineKeyboardButton('๐๐ฌ๐ฑ๐ฅ๐ฆ๐ ', callback_data='style+gothic'),
        InlineKeyboardButton('๐ฒ๐๐๐๐๐', callback_data='style+gothic_bolt'),

        ],[

        InlineKeyboardButton('๐๐๐๐ฐ๐๐ด๐', callback_data='style+squares'),
        InlineKeyboardButton('๐๏ธ๐๏ธ๐๏ธ๐ฐ๏ธ๐๏ธ๐ด๏ธ๐๏ธ', callback_data='style+squares_bold'),
        InlineKeyboardButton('Sฬฬaฬฬdฬฬ', callback_data='style+sad'),

        ],[

        InlineKeyboardButton('Next โก๏ธ', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(mm, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('๐ธโ๐ตโ๐ชโ๐จโ๐ฎโ๐ฆโ๐ฑโ', callback_data='style+special'),
            InlineKeyboardButton('Cอกอlอกอoอกอuอกอdอกอsอกอ', callback_data='style+cloud'),
            InlineKeyboardButton('Hฬฬaฬฬpฬฬpฬฬyฬฬ', callback_data='style+happy'),
            ],[
            InlineKeyboardButton('๊ช๊ชแฆ๊ช๊ชถ๊ชแฅด๐ฒ๊ช', callback_data='style+andalucia'),
            InlineKeyboardButton('็ชๅๅ แๅ', callback_data='style+manga'),
            InlineKeyboardButton('Sฬพtฬพiฬพnฬพkฬพyฬพ', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('Bอฆฬฅuอฆฬฅbอฆฬฅbอฆฬฅlอฆฬฅeอฆฬฅsอฆฬฅ', callback_data='style+bubbles'),
            InlineKeyboardButton('แOแฐIแ', callback_data='style+comic'),
            InlineKeyboardButton('๊๊๊ท๊ฉ๊๊๊', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('Rาaาyาsา', callback_data='style+rays'),
            InlineKeyboardButton('Bาiาrาdาsา', callback_data='style+birds'),
            InlineKeyboardButton('Sฬธlฬธaฬธsฬธhฬธ', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('sโ tโ oโ pโ ', callback_data='style+stop'),
            InlineKeyboardButton('Sอฬบkอฬบyอฬบlอฬบiอฬบnอฬบeอฬบ', callback_data='style+skyline'),
            InlineKeyboardButton('Aอrอrอoอwอsอ', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('แชแแญแฟแ', callback_data='style+qvnes'),
            InlineKeyboardButton('Sฬถtฬถrฬถiฬถkฬถeฬถ', callback_data='style+strike'),
            InlineKeyboardButton('Fเผrเผoเผzเผeเผnเผ', callback_data='style+frozen')
            ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
    except:
        pass


#=============================[Fonts]================================

class Fonts:
    def typewriter(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐',
            'd': '๐',
            'e': '๐',
            'f': '๐',
            'g': '๐',
            'h': '๐',
            'i': '๐',
            'j': '๐',
            'k': '๐',
            'l': '๐',
            'm': '๐',
            'n': '๐',
            'o': '๐',
            'p': '๐',
            'q': '๐',
            'r': '๐',
            's': '๐',
            't': '๐',
            'u': '๐',
            'v': '๐',
            'w': '๐ ',
            'x': '๐ก',
            'y': '๐ข',
            'z': '๐ฃ',
            'A': '๐ฐ',
            'B': '๐ฑ',
            'C': '๐ฒ',
            'D': '๐ณ',
            'E': '๐ด',
            'F': '๐ต',
            'G': '๐ถ',
            'H': '๐ท',
            'I': '๐ธ',
            'J': '๐น',
            'K': '๐บ',
            'L': '๐ป',
            'M': '๐ผ',
            'N': '๐ฝ',
            'O': '๐พ',
            'P': '๐ฟ',
            'Q': '๐',
            'R': '๐',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': '๐'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def outline(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐',
            'd': '๐',
            'e': '๐',
            'f': '๐',
            'g': '๐',
            'h': '๐',
            'i': '๐',
            'j': '๐',
            'k': '๐',
            'l': '๐',
            'm': '๐',
            'n': '๐',
            'o': '๐ ',
            'p': '๐ก',
            'q': '๐ข',
            'r': '๐ฃ',
            's': '๐ค',
            't': '๐ฅ',
            'u': '๐ฆ',
            'v': '๐ง',
            'w': '๐จ',
            'x': '๐ฉ',
            'y': '๐ช',
            'z': '๐ซ',
            'A': '๐ธ',
            'B': '๐น',
            'C': 'โ',
            'D': '๐ป',
            'E': '๐ผ',
            'F': '๐ฝ',
            'G': '๐พ',
            'H': 'โ',
            'I': '๐',
            'J': '๐',
            'K': '๐',
            'L': '๐',
            'M': '๐',
            'N': 'โ',
            'O': '๐',
            'P': 'โ',
            'Q': 'โ',
            'R': 'โ',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': 'โค',
            '0': '๐',
            '1': '๐',
            '2': '๐',
            '3': '๐',
            '4': '๐',
            '5': '๐',
            '6': '๐',
            '7': '๐',
            '8': '๐ ',
            '9': '๐ก'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def serief(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐',
            'd': '๐',
            'e': '๐',
            'f': '๐',
            'g': '๐ ',
            'h': '๐ก',
            'i': '๐ข',
            'j': '๐ฃ',
            'k': '๐ค',
            'l': '๐ฅ',
            'm': '๐ฆ',
            'n': '๐ง',
            'o': '๐จ',
            'p': '๐ฉ',
            'q': '๐ช',
            'r': '๐ซ',
            's': '๐ฌ',
            't': '๐ญ',
            'u': '๐ฎ',
            'v': '๐ฏ',
            'w': '๐ฐ',
            'x': '๐ฑ',
            'y': '๐ฒ',
            'z': '๐ณ',
            'A': '๐',
            'B': '๐',
            'C': '๐',
            'D': '๐',
            'E': '๐',
            'F': '๐',
            'G': '๐',
            'H': '๐',
            'I': '๐',
            'J': '๐',
            'K': '๐',
            'L': '๐',
            'M': '๐',
            'N': '๐',
            'O': '๐',
            'P': '๐',
            'Q': '๐',
            'R': '๐',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': '๐',
            '0': '๐',
            '1': '๐',
            '2': '๐',
            '3': '๐',
            '4': '๐',
            '5': '๐',
            '6': '๐',
            '7': '๐',
            '8': '๐',
            '9': '๐'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def bold_cool(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐',
            'd': '๐',
            'e': '๐',
            'f': '๐',
            'g': '๐',
            'h': '๐',
            'i': '๐',
            'j': '๐',
            'k': '๐',
            'l': '๐',
            'm': '๐',
            'n': '๐',
            'o': '๐',
            'p': '๐',
            'q': '๐',
            'r': '๐',
            's': '๐',
            't': '๐',
            'u': '๐',
            'v': '๐',
            'w': '๐',
            'x': '๐',
            'y': '๐',
            'z': '๐',
            'A': '๐จ',
            'B': '๐ฉ',
            'C': '๐ช',
            'D': '๐ซ',
            'E': '๐ฌ',
            'F': '๐ญ',
            'G': '๐ฎ',
            'H': '๐ฏ',
            'I': '๐ฐ',
            'J': '๐ฑ',
            'K': '๐ฒ',
            'L': '๐ณ',
            'M': '๐ด',
            'N': '๐ต',
            'O': '๐ถ',
            'P': '๐ท',
            'Q': '๐ธ',
            'R': '๐น',
            'S': '๐บ',
            'T': '๐ป',
            'U': '๐ผ',
            'V': '๐ฝ',
            'W': '๐พ',
            'X': '๐ฟ',
            'Y': '๐',
            'Z': '๐'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def cool(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐',
            'd': '๐',
            'e': '๐',
            'f': '๐',
            'g': '๐',
            'h': 'โ',
            'i': '๐',
            'j': '๐',
            'k': '๐',
            'l': '๐',
            'm': '๐',
            'n': '๐',
            'o': '๐',
            'p': '๐',
            'q': '๐',
            'r': '๐',
            's': '๐ ',
            't': '๐ก',
            'u': '๐ข',
            'v': '๐ฃ',
            'w': '๐ค',
            'x': '๐ฅ',
            'y': '๐ฆ',
            'z': '๐ง',
            'A': '๐ด',
            'B': '๐ต',
            'C': '๐ถ',
            'D': '๐ท',
            'E': '๐ธ',
            'F': '๐น',
            'G': '๐บ',
            'H': '๐ป',
            'I': '๐ผ',
            'J': '๐ฝ',
            'K': '๐พ',
            'L': '๐ฟ',
            'M': '๐',
            'N': '๐',
            'O': '๐',
            'P': '๐',
            'Q': '๐',
            'R': '๐',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': '๐'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def smallcap(text):
        style = {
            'a': 'แด',
            'b': 'ส',
            'c': 'แด',
            'd': 'แด',
            'e': 'แด',
            'f': 'า',
            'g': 'ษข',
            'h': 'ส',
            'i': 'ษช',
            'j': 'ษช',
            'k': 'แด',
            'l': 'ส',
            'm': 'แด',
            'n': 'ษด',
            'o': 'แด',
            'p': 'แด',
            'q': 'วซ',
            'r': 'ส',
            's': 's',
            't': 'แด',
            'u': 'แด',
            'v': 'แด ',
            'w': 'แดก',
            'x': 'x',
            'y': 'ส',
            'z': 'แดข',
            'A': 'A',
            'B': 'B',
            'C': 'C',
            'D': 'D',
            'E': 'E',
            'F': 'F',
            'G': 'G',
            'H': 'H',
            'I': 'I',
            'J': 'J',
            'K': 'K',
            'L': 'L',
            'M': 'M',
            'N': 'N',
            'O': 'O',
            'P': 'P',
            'Q': 'Q',
            'R': 'R',
            'S': 'S',
            'T': 'T',
            'U': 'U',
            'V': 'V',
            'W': 'W',
            'X': 'X',
            'Y': 'Y',
            'Z': 'Z',
            '0': '๐ถ',
            '1': '๐ท',
            '2': '๐ธ',
            '3': '๐น',
            '4': '๐บ',
            '5': '๐ป',
            '6': '๐ผ',
            '7': '๐ฝ',
            '8': '๐พ',
            '9': '๐ฟ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def script(text):
        style = {
            'a': '๐ถ',
            'b': '๐ท',
            'c': '๐ธ',
            'd': '๐น',
            'e': 'โฏ',
            'f': '๐ป',
            'g': 'โ',
            'h': '๐ฝ',
            'i': '๐พ',
            'j': '๐ฟ',
            'k': '๐',
            'l': '๐',
            'm': '๐',
            'n': '๐',
            'o': 'โด',
            'p': '๐',
            'q': '๐',
            'r': '๐',
            's': '๐',
            't': '๐',
            'u': '๐',
            'v': '๐',
            'w': '๐',
            'x': '๐',
            'y': '๐',
            'z': '๐',
            'A': '๐',
            'B': 'โฌ',
            'C': '๐',
            'D': '๐',
            'E': 'โฐ',
            'F': 'โฑ',
            'G': '๐ข',
            'H': 'โ',
            'I': 'โ',
            'J': '๐ฅ',
            'K': '๐ฆ',
            'L': 'โ',
            'M': 'โณ',
            'N': '๐ฉ',
            'O': '๐ช',
            'P': '๐ซ',
            'Q': '๐ฌ',
            'R': 'โ',
            'S': '๐ฎ',
            'T': '๐ฏ',
            'U': '๐ฐ',
            'V': '๐ฑ',
            'W': '๐ฒ',
            'X': '๐ณ',
            'Y': '๐ด',
            'Z': '๐ต'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def bold_script(text):
        style = {
            'a': '๐ช',
            'b': '๐ซ',
            'c': '๐ฌ',
            'd': '๐ญ',
            'e': '๐ฎ',
            'f': '๐ฏ',
            'g': '๐ฐ',
            'h': '๐ฑ',
            'i': '๐ฒ',
            'j': '๐ณ',
            'k': '๐ด',
            'l': '๐ต',
            'm': '๐ถ',
            'n': '๐ท',
            'o': '๐ธ',
            'p': '๐น',
            'q': '๐บ',
            'r': '๐ป',
            's': '๐ผ',
            't': '๐ฝ',
            'u': '๐พ',
            'v': '๐ฟ',
            'w': '๐',
            'x': '๐',
            'y': '๐',
            'z': '๐',
            'A': '๐',
            'B': '๐',
            'C': '๐',
            'D': '๐',
            'E': '๐',
            'F': '๐',
            'G': '๐',
            'H': '๐',
            'I': '๐',
            'J': '๐',
            'K': '๐',
            'L': '๐',
            'M': '๐',
            'N': '๐',
            'O': '๐',
            'P': '๐',
            'Q': '๐ ',
            'R': '๐ก',
            'S': '๐ข',
            'T': '๐ฃ',
            'U': '๐ค',
            'V': '๐ฅ',
            'W': '๐ฆ',
            'X': '๐ง',
            'Y': '๐จ',
            'Z': '๐ฉ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def tiny(text):
        style = {
            'a': 'แต',
            'b': 'แต',
            'c': 'แถ',
            'd': 'แต',
            'e': 'แต',
            'f': 'แถ ',
            'g': 'แต',
            'h': 'สฐ',
            'i': 'โฑ',
            'j': 'สฒ',
            'k': 'แต',
            'l': 'หก',
            'm': 'แต',
            'n': 'โฟ',
            'o': 'แต',
            'p': 'แต',
            'q': 'แต ',
            'r': 'สณ',
            's': 'หข',
            't': 'แต',
            'u': 'แต',
            'v': 'แต',
            'w': 'สท',
            'x': 'หฃ',
            'y': 'สธ',
            'z': 'แถป',
            'A': 'แต',
            'B': 'แต',
            'C': 'แถ',
            'D': 'แต',
            'E': 'แต',
            'F': 'แถ ',
            'G': 'แต',
            'H': 'สฐ',
            'I': 'โฑ',
            'J': 'สฒ',
            'K': 'แต',
            'L': 'หก',
            'M': 'แต',
            'N': 'โฟ',
            'O': 'แต',
            'P': 'แต',
            'Q': 'แต ',
            'R': 'สณ',
            'S': 'หข',
            'T': 'แต',
            'U': 'แต',
            'V': 'แต',
            'W': 'สท',
            'X': 'หฃ',
            'Y': 'สธ',
            'Z': 'แถป'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def comic(text):
        style = {
            'a': 'แฉ',
            'b': 'แท',
            'c': 'แ',
            'd': 'แช',
            'e': 'แด',
            'f': 'แด',
            'g': 'แ',
            'h': 'แผ',
            'i': 'I',
            'j': 'แ',
            'k': 'K',
            'l': 'แช',
            'm': 'แฐ',
            'n': 'แ',
            'o': 'O',
            'p': 'แญ',
            'q': 'แซ',
            'r': 'แ',
            's': 'ี',
            't': 'T',
            'u': 'แ',
            'v': 'แฏ',
            'w': 'แฏ',
            'x': 'แญ',
            'y': 'Y',
            'z': 'แ',
            'A': 'แฉ',
            'B': 'แท',
            'C': 'แ',
            'D': 'แช',
            'E': 'แด',
            'F': 'แด',
            'G': 'แ',
            'H': 'แผ',
            'I': 'I',
            'J': 'แ',
            'K': 'K',
            'L': 'แช',
            'M': 'แฐ',
            'N': 'แ',
            'O': 'O',
            'P': 'แญ',
            'Q': 'แซ',
            'R': 'แ',
            'S': 'ี',
            'T': 'T',
            'U': 'แ',
            'V': 'แฏ',
            'W': 'แฏ',
            'X': 'แญ',
            'Y': 'Y',
            'Z': 'แ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def san(text):
        style = {
            'a': '๐ฎ',
            'b': '๐ฏ',
            'c': '๐ฐ',
            'd': '๐ฑ',
            'e': '๐ฒ',
            'f': '๐ณ',
            'g': '๐ด',
            'h': '๐ต',
            'i': '๐ถ',
            'j': '๐ท',
            'k': '๐ธ',
            'l': '๐น',
            'm': '๐บ',
            'n': '๐ป',
            'o': '๐ผ',
            'p': '๐ฝ',
            'q': '๐พ',
            'r': '๐ฟ',
            's': '๐',
            't': '๐',
            'u': '๐',
            'v': '๐',
            'w': '๐',
            'x': '๐',
            'y': '๐',
            'z': '๐',
            'A': '๐',
            'B': '๐',
            'C': '๐',
            'D': '๐',
            'E': '๐',
            'F': '๐',
            'G': '๐',
            'H': '๐',
            'I': '๐',
            'J': '๐',
            'K': '๐',
            'L': '๐',
            'M': '๐ ',
            'N': '๐ก',
            'O': '๐ข',
            'P': '๐ฃ',
            'Q': '๐ค',
            'R': '๐ฅ',
            'S': '๐ฆ',
            'T': '๐ง',
            'U': '๐จ',
            'V': '๐ฉ',
            'W': '๐ช',
            'X': '๐ซ',
            'Y': '๐ฌ',
            'Z': '๐ญ',
            '0': '๐ฌ',
            '1': '๐ญ',
            '2': '๐ฎ',
            '3': '๐ฏ',
            '4': '๐ฐ',
            '5': '๐ฑ',
            '6': '๐ฒ',
            '7': '๐ณ',
            '8': '๐ด',
            '9': '๐ต'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def slant_san(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐',
            'd': '๐',
            'e': '๐',
            'f': '๐',
            'g': '๐',
            'h': '๐',
            'i': '๐',
            'j': '๐',
            'k': '๐ ',
            'l': '๐ก',
            'm': '๐ข',
            'n': '๐ฃ',
            'o': '๐ค',
            'p': '๐ฅ',
            'q': '๐ฆ',
            'r': '๐ง',
            's': '๐จ',
            't': '๐ฉ',
            'u': '๐ช',
            'v': '๐ซ',
            'w': '๐ฌ',
            'x': '๐ญ',
            'y': '๐ฎ',
            'z': '๐ฏ',
            'A': '๐ผ',
            'B': '๐ฝ',
            'C': '๐พ',
            'D': '๐ฟ',
            'E': '๐',
            'F': '๐',
            'G': '๐',
            'H': '๐',
            'I': '๐',
            'J': '๐',
            'K': '๐',
            'L': '๐',
            'M': '๐',
            'N': '๐',
            'O': '๐',
            'P': '๐',
            'Q': '๐',
            'R': '๐',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': '๐'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def slant(text):
        style = {
            'a': '๐ข',
            'b': '๐ฃ',
            'c': '๐ค',
            'd': '๐ฅ',
            'e': '๐ฆ',
            'f': '๐ง',
            'g': '๐จ',
            'h': '๐ฉ',
            'i': '๐ช',
            'j': '๐ซ',
            'k': '๐ฌ',
            'l': '๐ญ',
            'm': '๐ฎ',
            'n': '๐ฏ',
            'o': '๐ฐ',
            'p': '๐ฑ',
            'q': '๐ฒ',
            'r': '๐ณ',
            's': '๐ด',
            't': '๐ต',
            'u': '๐ถ',
            'v': '๐ท',
            'w': '๐ธ',
            'x': '๐น',
            'y': '๐บ',
            'z': '๐ป',
            'A': '๐',
            'B': '๐',
            'C': '๐',
            'D': '๐',
            'E': '๐',
            'F': '๐',
            'G': '๐',
            'H': '๐',
            'I': '๐',
            'J': '๐',
            'K': '๐',
            'L': '๐',
            'M': '๐',
            'N': '๐',
            'O': '๐',
            'P': '๐',
            'Q': '๐',
            'R': '๐',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐ ',
            'Z': '๐ก'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def sim(text):
        style = {
            'a': '๐บ',
            'b': '๐ป',
            'c': '๐ผ',
            'd': '๐ฝ',
            'e': '๐พ',
            'f': '๐ฟ',
            'g': '๐',
            'h': '๐',
            'i': '๐',
            'j': '๐',
            'k': '๐',
            'l': '๐',
            'm': '๐',
            'n': '๐',
            'o': '๐',
            'p': '๐',
            'q': '๐',
            'r': '๐',
            's': '๐',
            't': '๐',
            'u': '๐',
            'v': '๐',
            'w': '๐',
            'x': '๐',
            'y': '๐',
            'z': '๐',
            'A': '๐ ',
            'B': '๐ก',
            'C': '๐ข',
            'D': '๐ฃ',
            'E': '๐ค',
            'F': '๐ฅ',
            'G': '๐ฆ',
            'H': '๐ง',
            'I': '๐จ',
            'J': '๐ฉ',
            'K': '๐ช',
            'L': '๐ซ',
            'M': '๐ฌ',
            'N': '๐ญ',
            'O': '๐ฎ',
            'P': '๐ฏ',
            'Q': '๐ฐ',
            'R': '๐ฑ',
            'S': '๐ฒ',
            'T': '๐ณ',
            'U': '๐ด',
            'V': '๐ต',
            'W': '๐ถ',
            'X': '๐ท',
            'Y': '๐ธ',
            'Z': '๐น'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def circles(text):
        style = {
            'a': 'โถ๏ธ',
            'b': 'โท๏ธ',
            'c': 'โธ๏ธ',
            'd': 'โน๏ธ',
            'e': 'โบ๏ธ',
            'f': 'โป๏ธ',
            'g': 'โผ๏ธ',
            'h': 'โฝ๏ธ',
            'i': 'โพ๏ธ',
            'j': 'โฟ๏ธ',
            'k': 'โ๏ธ',
            'l': 'โ๏ธ',
            'm': 'โ๏ธ',
            'n': 'โ๏ธ',
            'o': 'โ๏ธ',
            'p': 'โ๏ธ',
            'q': 'โ๏ธ',
            'r': 'โ๏ธ',
            's': 'โ๏ธ',
            't': 'โ๏ธ',
            'u': 'โ๏ธ',
            'v': 'โ๏ธ',
            'w': 'โ๏ธ',
            'x': 'โ๏ธ',
            'y': 'โ๏ธ',
            'z': 'โ๏ธ',
            'A': 'โถ๏ธ',
            'B': 'โท๏ธ',
            'C': 'โธ๏ธ',
            'D': 'โน๏ธ',
            'E': 'โบ๏ธ',
            'F': 'โป๏ธ',
            'G': 'โผ๏ธ',
            'H': 'โฝ๏ธ',
            'I': 'โพ๏ธ',
            'J': 'โฟ๏ธ',
            'K': 'โ๏ธ',
            'L': 'โ๏ธ',
            'M': 'โ๏ธ',
            'N': 'โ๏ธ',
            'O': 'โ๏ธ',
            'P': 'โ๏ธ',
            'Q': 'โ๏ธ',
            'R': 'โ๏ธ',
            'S': 'โ๏ธ',
            'T': 'โ๏ธ',
            'U': 'โ๏ธ',
            'V': 'โ๏ธ',
            'W': 'โ๏ธ',
            'X': 'โ๏ธ',
            'Y': 'โ๏ธ',
            'Z': 'โ๏ธ',
            '0': 'โช',
            '1': 'โ ',
            '2': 'โก',
            '3': 'โข',
            '4': 'โฃ',
            '5': 'โค',
            '6': 'โฅ',
            '7': 'โฆ',
            '8': 'โง',
            '9': 'โจ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def dark_circle(text):
        style = {
            'a': '๐๏ธ',
            'b': '๐๏ธ',
            'c': '๐๏ธ',
            'd': '๐๏ธ',
            'e': '๐๏ธ',
            'f': '๐๏ธ',
            'g': '๐๏ธ',
            'h': '๐๏ธ',
            'i': '๐๏ธ',
            'j': '๐๏ธ',
            'k': '๐๏ธ',
            'l': '๐๏ธ',
            'm': '๐๏ธ',
            'n': '๐๏ธ',
            'o': '๐๏ธ',
            'p': '๐๏ธ',
            'q': '๐ ๏ธ',
            'r': '๐ก๏ธ',
            's': '๐ข๏ธ',
            't': '๐ฃ๏ธ',
            'u': '๐ค๏ธ',
            'v': '๐ฅ๏ธ',
            'w': '๐ฆ๏ธ',
            'x': '๐ง๏ธ',
            'y': '๐จ๏ธ',
            'z': '๐ฉ๏ธ',
            'A': '๐๏ธ',
            'B': '๐๏ธ',
            'C': '๐๏ธ',
            'D': '๐๏ธ',
            'E': '๐๏ธ',
            'F': '๐๏ธ',
            'G': '๐๏ธ',
            'H': '๐๏ธ',
            'I': '๐๏ธ',
            'J': '๐๏ธ',
            'K': '๐๏ธ',
            'L': '๐๏ธ',
            'M': '๐๏ธ',
            'N': '๐๏ธ',
            'O': '๐๏ธ',
            'P': '๐๏ธ',
            'Q': '๐ ๏ธ',
            'R': '๐ก๏ธ',
            'S': '๐ข๏ธ',
            'T': '๐ฃ๏ธ',
            'U': '๐ค๏ธ',
            'V': '๐ฅ๏ธ',
            'W': '๐ฆ๏ธ',
            'X': '๐ง๏ธ',
            'Y': '๐จ๏ธ',
            'Z': '๐ฉ',
            '0': 'โฟ',
            '1': 'โ',
            '2': 'โ',
            '3': 'โ',
            '4': 'โ',
            '5': 'โ',
            '6': 'โ',
            '7': 'โ',
            '8': 'โ',
            '9': 'โ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def gothic(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐ ',
            'd': '๐ก',
            'e': '๐ข',
            'f': '๐ฃ',
            'g': '๐ค',
            'h': '๐ฅ',
            'i': '๐ฆ',
            'j': '๐ง',
            'k': '๐จ',
            'l': '๐ฉ',
            'm': '๐ช',
            'n': '๐ซ',
            'o': '๐ฌ',
            'p': '๐ญ',
            'q': '๐ฎ',
            'r': '๐ฏ',
            's': '๐ฐ',
            't': '๐ฑ',
            'u': '๐ฒ',
            'v': '๐ณ',
            'w': '๐ด',
            'x': '๐ต',
            'y': '๐ถ',
            'z': '๐ท',
            'A': '๐',
            'B': '๐',
            'C': 'โญ',
            'D': '๐',
            'E': '๐',
            'F': '๐',
            'G': '๐',
            'H': 'โ',
            'I': 'โ',
            'J': '๐',
            'K': '๐',
            'L': '๐',
            'M': '๐',
            'N': '๐',
            'O': '๐',
            'P': '๐',
            'Q': '๐',
            'R': 'โ',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': 'โจ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text


    def bold_gothic(text):
        style = {
            'a': '๐',
            'b': '๐',
            'c': '๐',
            'd': '๐',
            'e': '๐',
            'f': '๐',
            'g': '๐',
            'h': '๐',
            'i': '๐',
            'j': '๐',
            'k': '๐',
            'l': '๐',
            'm': '๐',
            'n': '๐',
            'o': '๐',
            'p': '๐',
            'q': '๐',
            'r': '๐',
            's': '๐',
            't': '๐',
            'u': '๐',
            'v': '๐',
            'w': '๐',
            'x': '๐',
            'y': '๐',
            'z': '๐',
            'A': '๐ฌ',
            'B': '๐ญ',
            'C': '๐ฎ',
            'D': '๐บ',
            'E': '๐ฐ',
            'F': '๐ฑ',
            'G': '๐ฒ',
            'H': '๐ณ',
            'I': '๐ด',
            'J': '๐ต',
            'K': '๐ถ',
            'L': '๐ท',
            'M': '๐ธ',
            'N': '๐น',
            'O': '๐บ',
            'P': '๐ป',
            'Q': '๐ผ',
            'R': '๐ฝ',
            'S': '๐พ',
            'T': '๐ฟ',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': '๐'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def cloud(text):
        style = {
            'a': 'aอกอ',
            'b': 'bอกอ',
            'c': 'cอกอ',
            'd': 'dอกอ',
            'e': 'eอกอ',
            'f': 'fอกอ',
            'g': 'gอกอ',
            'h': 'hอกอ',
            'i': 'iอกอ',
            'j': 'jอกอ',
            'k': 'kอกอ',
            'l': 'lอกอ',
            'm': 'mอกอ',
            'n': 'nอกอ',
            'o': 'oอกอ',
            'p': 'pอกอ',
            'q': 'qอกอ',
            'r': 'rอกอ',
            's': 'sอกอ',
            't': 'tอกอ',
            'u': 'uอกอ',
            'v': 'vอกอ',
            'w': 'wอกอ',
            'x': 'xอกอ',
            'y': 'yอกอ',
            'z': 'zอกอ',
            'A': 'Aอกอ',
            'B': 'Bอกอ',
            'C': 'Cอกอ',
            'D': 'Dอกอ',
            'E': 'Eอกอ',
            'F': 'Fอกอ',
            'G': 'Gอกอ',
            'H': 'Hอกอ',
            'I': 'Iอกอ',
            'J': 'Jอกอ',
            'K': 'Kอกอ',
            'L': 'Lอกอ',
            'M': 'Mอกอ',
            'N': 'Nอกอ',
            'O': 'Oอกอ',
            'P': 'Pอกอ',
            'Q': 'Qอกอ',
            'R': 'Rอกอ',
            'S': 'Sอกอ',
            'T': 'Tอกอ',
            'U': 'Uอกอ',
            'V': 'Vอกอ',
            'W': 'Wอกอ',
            'X': 'Xอกอ',
            'Y': 'Yอกอ',
            'Z': 'Zอกอ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def happy(text):
        style = {
            'a': 'aฬฬ',
            'b': 'bฬฬ',
            'c': 'cฬฬ',
            'd': 'dฬฬ',
            'e': 'eฬฬ',
            'f': 'fฬฬ',
            'g': 'gฬฬ',
            'h': 'hฬฬ',
            'i': 'iฬฬ',
            'j': 'jฬฬ',
            'k': 'kฬฬ',
            'l': 'lฬฬ',
            'm': 'mฬฬ',
            'n': 'nฬฬ',
            'o': 'oฬฬ',
            'p': 'pฬฬ',
            'q': 'qฬฬ',
            'r': 'rฬฬ',
            's': 'sฬฬ',
            't': 'tฬฬ',
            'u': 'uฬฬ',
            'v': 'vฬฬ',
            'w': 'wฬฬ',
            'x': 'xฬฬ',
            'y': 'yฬฬ',
            'z': 'zฬฬ',
            'A': 'Aฬฬ',
            'B': 'Bฬฬ',
            'C': 'Cฬฬ',
            'D': 'Dฬฬ',
            'E': 'Eฬฬ',
            'F': 'Fฬฬ',
            'G': 'Gฬฬ',
            'H': 'Hฬฬ',
            'I': 'Iฬฬ',
            'J': 'Jฬฬ',
            'K': 'Kฬฬ',
            'L': 'Lฬฬ',
            'M': 'Mฬฬ',
            'N': 'Nฬฬ',
            'O': 'Oฬฬ',
            'P': 'Pฬฬ',
            'Q': 'Qฬฬ',
            'R': 'Rฬฬ',
            'S': 'Sฬฬ',
            'T': 'Tฬฬ',
            'U': 'Uฬฬ',
            'V': 'Vฬฬ',
            'W': 'Wฬฬ',
            'X': 'Xฬฬ',
            'Y': 'Yฬฬ',
            'Z': 'Zฬฬ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def sad(text):
        style = {
            'a': 'aฬฬ',
            'b': 'bฬฬ',
            'c': 'cฬฬ',
            'd': 'dฬฬ',
            'e': 'eฬฬ',
            'f': 'fฬฬ',
            'g': 'gฬฬ',
            'h': 'hฬฬ',
            'i': 'iฬฬ',
            'j': 'jฬฬ',
            'k': 'kฬฬ',
            'l': 'lฬฬ',
            'm': 'mฬฬ',
            'n': 'nฬฬ',
            'o': 'oฬฬ',
            'p': 'pฬฬ',
            'q': 'qฬฬ',
            'r': 'rฬฬ',
            's': 'sฬฬ',
            't': 'tฬฬ',
            'u': 'uฬฬ',
            'v': 'vฬฬ',
            'w': 'wฬฬ',
            'x': 'xฬฬ',
            'y': 'yฬฬ',
            'z': 'zฬฬ',
            'A': 'Aฬฬ',
            'B': 'Bฬฬ',
            'C': 'Cฬฬ',
            'D': 'Dฬฬ',
            'E': 'Eฬฬ',
            'F': 'Fฬฬ',
            'G': 'Gฬฬ',
            'H': 'Hฬฬ',
            'I': 'Iฬฬ',
            'J': 'Jฬฬ',
            'K': 'Kฬฬ',
            'L': 'Lฬฬ',
            'M': 'Mฬฬ',
            'N': 'Nฬฬ',
            'O': 'Oฬฬ',
            'P': 'Pฬฬ',
            'Q': 'Qฬฬ',
            'R': 'Rฬฬ',
            'S': 'Sฬฬ',
            'T': 'Tฬฬ',
            'U': 'Uฬฬ',
            'V': 'Vฬฬ',
            'W': 'Wฬฬ',
            'X': 'Xฬฬ',
            'Y': 'Yฬฬ',
            'Z': 'Zฬฬ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def special(text):
        style = {
            'a': '๐ฆโ',
            'b': '๐งโ',
            'c': '๐จโ',
            'd': '๐ฉโ',
            'e': '๐ชโ',
            'f': '๐ซโ',
            'g': '๐ฌโ',
            'h': '๐ญโ',
            'i': '๐ฎโ',
            'j': '๐ฏโ',
            'k': '๐ฐโ',
            'l': '๐ฑโ',
            'm': '๐ฒโ',
            'n': '๐ณโ',
            'o': '๐ดโ',
            'p': '๐ตโ',
            'q': '๐ถโ',
            'r': '๐ทโ',
            's': '๐ธโ',
            't': '๐นโ',
            'u': '๐บโ',
            'v': '๐ปโ',
            'w': '๐ผโ',
            'x': '๐ฝโ',
            'y': '๐พโ',
            'z': '๐ฟโ',
            'A': '๐ฆโ',
            'B': '๐งโ',
            'C': '๐จโ',
            'D': '๐ฉโ',
            'E': '๐ชโ',
            'F': '๐ซโ',
            'G': '๐ฌโ',
            'H': '๐ญโ',
            'I': '๐ฎโ',
            'J': '๐ฏโ',
            'K': '๐ฐโ',
            'L': '๐ฑโ',
            'M': '๐ฒโ',
            'N': '๐ณโ',
            'O': '๐ดโ',
            'P': '๐ตโ',
            'Q': '๐ถโ',
            'R': '๐ทโ',
            'S': '๐ธโ',
            'T': '๐นโ',
            'U': '๐บโ',
            'V': '๐ปโ',
            'W': '๐ผโ',
            'X': '๐ฝโ',
            'Y': '๐พโ',
            'Z': '๐ฟโ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def square(text):
        style = {
            'a': '๐ฐ',
            'b': '๐ฑ',
            'c': '๐ฒ',
            'd': '๐ณ',
            'e': '๐ด',
            'f': '๐ต',
            'g': '๐ถ',
            'h': '๐ท',
            'i': '๐ธ',
            'j': '๐น',
            'k': '๐บ',
            'l': '๐ป',
            'm': '๐ผ',
            'n': '๐ฝ',
            'o': '๐พ',
            'p': '๐ฟ',
            'q': '๐',
            'r': '๐',
            's': '๐',
            't': '๐',
            'u': '๐',
            'v': '๐',
            'w': '๐',
            'x': '๐',
            'y': '๐',
            'z': '๐',
            'A': '๐ฐ',
            'B': '๐ฑ',
            'C': '๐ฒ',
            'D': '๐ณ',
            'E': '๐ด',
            'F': '๐ต',
            'G': '๐ถ',
            'H': '๐ท',
            'I': '๐ธ',
            'J': '๐น',
            'K': '๐บ',
            'L': '๐ป',
            'M': '๐ผ',
            'N': '๐ฝ',
            'O': '๐พ',
            'P': '๐ฟ',
            'Q': '๐',
            'R': '๐',
            'S': '๐',
            'T': '๐',
            'U': '๐',
            'V': '๐',
            'W': '๐',
            'X': '๐',
            'Y': '๐',
            'Z': '๐'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def dark_square(text):
        style = {
            'a': '๐ฐ๏ธ',
            'b': '๐ฑ๏ธ',
            'c': '๐ฒ๏ธ',
            'd': '๐ณ๏ธ',
            'e': '๐ด๏ธ',
            'f': '๐ต๏ธ',
            'g': '๐ถ๏ธ',
            'h': '๐ท๏ธ',
            'i': '๐ธ๏ธ',
            'j': '๐น๏ธ',
            'k': '๐บ๏ธ',
            'l': '๐ป๏ธ',
            'm': '๐ผ๏ธ',
            'n': '๐ฝ๏ธ',
            'o': '๐พ๏ธ',
            'p': '๐ฟ๏ธ',
            'q': '๐๏ธ',
            'r': '๐๏ธ',
            's': '๐๏ธ',
            't': '๐๏ธ',
            'u': '๐๏ธ',
            'v': '๐๏ธ',
            'w': '๐๏ธ',
            'x': '๐๏ธ',
            'y': '๐๏ธ',
            'z': '๐๏ธ',
            'A': '๐ฐ๏ธ',
            'B': '๐ฑ๏ธ',
            'C': '๐ฒ๏ธ',
            'D': '๐ณ๏ธ',
            'E': '๐ด๏ธ',
            'F': '๐ต๏ธ',
            'G': '๐ถ๏ธ',
            'H': '๐ท๏ธ',
            'I': '๐ธ๏ธ',
            'J': '๐น๏ธ',
            'K': '๐บ๏ธ',
            'L': '๐ป๏ธ',
            'M': '๐ผ๏ธ',
            'N': '๐ฝ๏ธ',
            'O': '๐พ๏ธ',
            'P': '๐ฟ๏ธ',
            'Q': '๐๏ธ',
            'R': '๐๏ธ',
            'S': '๐๏ธ',
            'T': '๐๏ธ',
            'U': '๐๏ธ',
            'V': '๐๏ธ',
            'W': '๐๏ธ',
            'X': '๐๏ธ',
            'Y': '๐๏ธ',
            'Z': '๐๏ธ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def andalucia(text):
        style = {
            'a': '๊ช',
            'b': 'แฅ',
            'c': 'แฅด',
            'd': 'แฆ',
            'e': '๊ซ',
            'f': 'แ ป',
            'g': 'แง',
            'h': '๊ซ',
            'i': '๐ฒ',
            'j': '๐ณ',
            'k': '๐ฌ',
            'l': '๊ชถ',
            'm': '๊ช',
            'n': '๊ช',
            'o': '๊ชฎ',
            'p': 'ฯ',
            'q': '๐ฒ',
            'r': '๐ณ',
            's': '๐ด',
            't': '๐ฝ',
            'u': '๊ช',
            'v': '๊ช',
            'w': 'แญ',
            'x': 'แฅ',
            'y': '๊ช',
            'z': 'ษ',
            'A': '๊ช',
            'B': 'แฅ',
            'C': 'แฅด',
            'D': 'แฆ',
            'E': '๊ซ',
            'F': 'แ ป',
            'G': 'แง',
            'H': '๊ซ',
            'I': '๐ฒ',
            'J': '๐ณ',
            'K': '๐ฌ',
            'L': '๊ชถ',
            'M': '๊ช',
            'N': '๊ช',
            'O': '๊ชฎ',
            'P': 'ฯ',
            'Q': '๐ฒ',
            'R': '๐ณ',
            'S': '๐ด',
            'T': '๐ฝ',
            'U': '๊ช',
            'V': '๊ช',
            'W': 'แญ',
            'X': 'แฅ',
            'Y': '๊ช',
            'Z': 'ษ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def manga(text):
        style = {
            'a': 'ๅ',
            'b': 'ไน',
            'c': 'ๅ',
            'd': 'แช',
            'e': 'ไน',
            'f': 'ๅ',
            'g': 'แ',
            'h': 'ๅ',
            'i': '|',
            'j': '๏พ',
            'k': 'า',
            'l': 'ใฅ',
            'm': '็ช',
            'n': 'ๅ ',
            'o': 'ใ',
            'p': 'ๅฉ',
            'q': 'าจ',
            'r': 'ๅฐบ',
            's': 'ไธ',
            't': 'ใ',
            'u': 'ใฉ',
            'v': 'แฏ',
            'w': 'ๅฑฑ',
            'x': 'ไน',
            'y': 'ใ',
            'z': 'ไน',
            'A': 'ๅ',
            'B': 'ไน',
            'C': 'ๅ',
            'D': 'แช',
            'E': 'ไน',
            'F': 'ๅ',
            'G': 'แ',
            'H': 'ๅ',
            'I': '|',
            'J': '๏พ',
            'K': 'า',
            'L': 'ใฅ',
            'M': '็ช',
            'N': 'ๅ ',
            'O': 'ใ',
            'P': 'ๅฉ',
            'Q': 'าจ',
            'R': 'ๅฐบ',
            'S': 'ไธ',
            'T': 'ใ',
            'U': 'ใฉ',
            'V': 'แฏ',
            'W': 'ๅฑฑ',
            'X': 'ไน',
            'Y': 'ใ',
            'Z': 'ไน'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def stinky(text):
        style = {
            'a': 'aฬพ',
            'b': 'bฬพ',
            'c': 'cฬพ',
            'd': 'dฬพ',
            'e': 'eฬพ',
            'f': 'fฬพ',
            'g': 'gฬพ',
            'h': 'hฬพ',
            'i': 'iฬพ',
            'j': 'jฬพ',
            'k': 'kฬพ',
            'l': 'lฬพ',
            'm': 'mฬพ',
            'n': 'nฬพ',
            'o': 'oฬพ',
            'p': 'pฬพ',
            'q': 'qฬพ',
            'r': 'rฬพ',
            's': 'sฬพ',
            't': 'tฬพ',
            'u': 'uฬพ',
            'v': 'vฬพ',
            'w': 'wฬพ',
            'x': 'xฬพ',
            'y': 'yฬพ',
            'z': 'zฬพ',
            'A': 'Aฬพ',
            'B': 'Bฬพ',
            'C': 'Cฬพ',
            'D': 'Dฬพ',
            'E': 'Eฬพ',
            'F': 'Fฬพ',
            'G': 'Gฬพ',
            'H': 'Hฬพ',
            'I': 'Iฬพ',
            'J': 'Jฬพ',
            'K': 'Kฬพ',
            'L': 'Lฬพ',
            'M': 'Mฬพ',
            'N': 'Nฬพ',
            'O': 'Oฬพ',
            'P': 'Pฬพ',
            'Q': 'Qฬพ',
            'R': 'Rฬพ',
            'S': 'Sฬพ',
            'T': 'Tฬพ',
            'U': 'Uฬพ',
            'V': 'Vฬพ',
            'W': 'Wฬพ',
            'X': 'Xฬพ',
            'Y': 'Yฬพ',
            'Z': 'Zฬพ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def bubbles(text):
        style = {
            'a': 'aอฆฬฅ',
            'b': 'bอฆฬฅ',
            'c': 'cอฆฬฅ',
            'd': 'dอฆฬฅ',
            'e': 'eอฆฬฅ',
            'f': 'fอฆฬฅ',
            'g': 'gอฆฬฅ',
            'h': 'hอฆฬฅ',
            'i': 'iอฆฬฅ',
            'j': 'jอฆฬฅ',
            'k': 'kอฆฬฅ',
            'l': 'lอฆฬฅ',
            'm': 'mอฆฬฅ',
            'n': 'nอฆฬฅ',
            'o': 'oอฆฬฅ',
            'p': 'pอฆฬฅ',
            'q': 'qอฆฬฅ',
            'r': 'rอฆฬฅ',
            's': 'sอฆฬฅ',
            't': 'tอฆฬฅ',
            'u': 'uอฆฬฅ',
            'v': 'vอฆฬฅ',
            'w': 'wอฆฬฅ',
            'x': 'xอฆฬฅ',
            'y': 'yอฆฬฅ',
            'z': 'zอฆฬฅ',
            'A': 'Aอฆฬฅ',
            'B': 'Bอฆฬฅ',
            'C': 'Cอฆฬฅ',
            'D': 'Dอฆฬฅ',
            'E': 'Eอฆฬฅ',
            'F': 'Fอฆฬฅ',
            'G': 'Gอฆฬฅ',
            'H': 'Hอฆฬฅ',
            'I': 'Iอฆฬฅ',
            'J': 'Jอฆฬฅ',
            'K': 'Kอฆฬฅ',
            'L': 'Lอฆฬฅ',
            'M': 'Mอฆฬฅ',
            'N': 'Nอฆฬฅ',
            'O': 'Oอฆฬฅ',
            'P': 'Pอฆฬฅ',
            'Q': 'Qอฆฬฅ',
            'R': 'Rอฆฬฅ',
            'S': 'Sอฆฬฅ',
            'T': 'Tอฆฬฅ',
            'U': 'Uอฆฬฅ',
            'V': 'Vอฆฬฅ',
            'W': 'Wอฆฬฅ',
            'X': 'Xอฆฬฅ',
            'Y': 'Yอฆฬฅ',
            'Z': 'Zอฆฬฅ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def underline(text):
        style = {
            'a': 'aอ',
            'b': 'bอ',
            'c': 'cอ',
            'd': 'dอ',
            'e': 'eอ',
            'f': 'fอ',
            'g': 'gอ',
            'h': 'hอ',
            'i': 'iอ',
            'j': 'jอ',
            'k': 'kอ',
            'l': 'lอ',
            'm': 'mอ',
            'n': 'nอ',
            'o': 'oอ',
            'p': 'pอ',
            'q': 'qอ',
            'r': 'rอ',
            's': 'sอ',
            't': 'tอ',
            'u': 'uอ',
            'v': 'vอ',
            'w': 'wอ',
            'x': 'xอ',
            'y': 'yอ',
            'z': 'zอ',
            'A': 'Aอ',
            'B': 'Bอ',
            'C': 'Cอ',
            'D': 'Dอ',
            'E': 'Eอ',
            'F': 'Fอ',
            'G': 'Gอ',
            'H': 'Hอ',
            'I': 'Iอ',
            'J': 'Jอ',
            'K': 'Kอ',
            'L': 'Lอ',
            'M': 'Mอ',
            'N': 'Nอ',
            'O': 'Oอ',
            'P': 'Pอ',
            'Q': 'Qอ',
            'R': 'Rอ',
            'S': 'Sอ',
            'T': 'Tอ',
            'U': 'Uอ',
            'V': 'Vอ',
            'W': 'Wอ',
            'X': 'Xอ',
            'Y': 'Yอ',
            'Z': 'Zอ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def ladybug(text):
        style = {
            'a': '๊',
            'b': '๊',
            'c': '๊ณ',
            'd': '๊ท',
            'e': '๊',
            'f': '๊',
            'g': '๊',
            'h': '๊',
            'i': '๊ค',
            'j': '๊ป',
            'k': '๊',
            'l': '๊',
            'm': '๊ญ',
            'n': '๊ค',
            'o': '๊ฆ',
            'p': 'แ',
            'q': '๊ฐ',
            'r': '๊ช',
            's': '๊',
            't': '๊',
            'u': '๊',
            'v': '๊ฆ',
            'w': '๊',
            'x': '๊ง',
            'y': '๊ฉ',
            'z': '๊ด',
            'A': '๊',
            'B': '๊',
            'C': '๊ณ',
            'D': '๊ท',
            'E': '๊',
            'F': '๊',
            'G': '๊',
            'H': '๊',
            'I': '๊ค',
            'J': '๊ป',
            'K': '๊',
            'L': '๊',
            'M': '๊ญ',
            'N': '๊ค',
            'O': '๊ฆ',
            'P': 'แ',
            'Q': '๊ฐ',
            'R': '๊ช',
            'S': '๊',
            'T': '๊',
            'U': '๊',
            'V': '๊ฆ',
            'W': '๊',
            'X': '๊ง',
            'Y': '๊ฉ',
            'Z': '๊ด'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def rays(text):
        style = {
            'a': 'aา',
            'b': 'bา',
            'c': 'cา',
            'd': 'dา',
            'e': 'eา',
            'f': 'fา',
            'g': 'gา',
            'h': 'hา',
            'i': 'iา',
            'j': 'jา',
            'k': 'kา',
            'l': 'lา',
            'm': 'mา',
            'n': 'nา',
            'o': 'oา',
            'p': 'pา',
            'q': 'qา',
            'r': 'rา',
            's': 'sา',
            't': 'tา',
            'u': 'uา',
            'v': 'vา',
            'w': 'wา',
            'x': 'xา',
            'y': 'yา',
            'z': 'zา',
            'A': 'Aา',
            'B': 'Bา',
            'C': 'Cา',
            'D': 'Dา',
            'E': 'Eา',
            'F': 'Fา',
            'G': 'Gา',
            'H': 'Hา',
            'I': 'Iา',
            'J': 'Jา',
            'K': 'Kา',
            'L': 'Lา',
            'M': 'Mา',
            'N': 'Nา',
            'O': 'Oา',
            'P': 'Pา',
            'Q': 'Qา',
            'R': 'Rา',
            'S': 'Sา',
            'T': 'Tา',
            'U': 'Uา',
            'V': 'Vา',
            'W': 'Wา',
            'X': 'Xา',
            'Y': 'Yา',
            'Z': 'Zา'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def birds(text):
        style = {
            'a': 'aา',
            'b': 'bา',
            'c': 'cา',
            'd': 'dา',
            'e': 'eา',
            'f': 'fา',
            'g': 'gา',
            'h': 'hา',
            'i': 'iา',
            'j': 'jา',
            'k': 'kา',
            'l': 'lา',
            'm': 'mา',
            'n': 'nา',
            'o': 'oา',
            'p': 'pา',
            'q': 'qา',
            'r': 'rา',
            's': 'sา',
            't': 'tา',
            'u': 'uา',
            'v': 'vา',
            'w': 'wา',
            'x': 'xา',
            'y': 'yา',
            'z': 'zา',
            'A': 'Aา',
            'B': 'Bา',
            'C': 'Cา',
            'D': 'Dา',
            'E': 'Eา',
            'F': 'Fา',
            'G': 'Gา',
            'H': 'Hา',
            'I': 'Iา',
            'J': 'Jา',
            'K': 'Kา',
            'L': 'Lา',
            'M': 'Mา',
            'N': 'Nา',
            'O': 'Oา',
            'P': 'Pา',
            'Q': 'Qา',
            'R': 'Rา',
            'S': 'Sา',
            'T': 'Tา',
            'U': 'Uา',
            'V': 'Vา',
            'W': 'Wา',
            'X': 'Xา',
            'Y': 'Yา',
            'Z': 'Zา'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def slash(text):
        style = {
            'a': 'aฬธ',
            'b': 'bฬธ',
            'c': 'cฬธ',
            'd': 'dฬธ',
            'e': 'eฬธ',
            'f': 'fฬธ',
            'g': 'gฬธ',
            'h': 'hฬธ',
            'i': 'iฬธ',
            'j': 'jฬธ',
            'k': 'kฬธ',
            'l': 'lฬธ',
            'm': 'mฬธ',
            'n': 'nฬธ',
            'o': 'oฬธ',
            'p': 'pฬธ',
            'q': 'qฬธ',
            'r': 'rฬธ',
            's': 'sฬธ',
            't': 'tฬธ',
            'u': 'uฬธ',
            'v': 'vฬธ',
            'w': 'wฬธ',
            'x': 'xฬธ',
            'y': 'yฬธ',
            'z': 'zฬธ',
            'A': 'Aฬธ',
            'B': 'Bฬธ',
            'C': 'Cฬธ',
            'D': 'Dฬธ',
            'E': 'Eฬธ',
            'F': 'Fฬธ',
            'G': 'Gฬธ',
            'H': 'Hฬธ',
            'I': 'Iฬธ',
            'J': 'Jฬธ',
            'K': 'Kฬธ',
            'L': 'Lฬธ',
            'M': 'Mฬธ',
            'N': 'Nฬธ',
            'O': 'Oฬธ',
            'P': 'Pฬธ',
            'Q': 'Qฬธ',
            'R': 'Rฬธ',
            'S': 'Sฬธ',
            'T': 'Tฬธ',
            'U': 'Uฬธ',
            'V': 'Vฬธ',
            'W': 'Wฬธ',
            'X': 'Xฬธ',
            'Y': 'Yฬธ',
            'Z': 'Zฬธ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def stop(text):
        style = {
            'a': 'aโ ',
            'b': 'bโ ',
            'c': 'cโ ',
            'd': 'dโ ',
            'e': 'eโ ',
            'f': 'fโ ',
            'g': 'gโ ',
            'h': 'hโ ',
            'i': 'iโ ',
            'j': 'jโ ',
            'k': 'kโ ',
            'l': 'lโ ',
            'm': 'mโ ',
            'n': 'nโ ',
            'o': 'oโ ',
            'p': 'pโ ',
            'q': 'qโ ',
            'r': 'rโ ',
            's': 'sโ ',
            't': 'tโ ',
            'u': 'uโ ',
            'v': 'vโ ',
            'w': 'wโ ',
            'x': 'xโ ',
            'y': 'yโ ',
            'z': 'zโ ',
            'A': 'Aโ ',
            'B': 'Bโ ',
            'C': 'Cโ ',
            'D': 'Dโ ',
            'E': 'Eโ ',
            'F': 'Fโ ',
            'G': 'Gโ ',
            'H': 'Hโ ',
            'I': 'Iโ ',
            'J': 'Jโ ',
            'K': 'Kโ ',
            'L': 'Lโ ',
            'M': 'Mโ ',
            'N': 'Nโ ',
            'O': 'Oโ ',
            'P': 'Pโ ',
            'Q': 'Qโ ',
            'R': 'Rโ ',
            'S': 'Sโ ',
            'T': 'Tโ ',
            'U': 'Uโ ',
            'V': 'Vโ ',
            'W': 'Wโ ',
            'X': 'Xโ ',
            'Y': 'Yโ ',
            'Z': 'Zโ '
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def skyline(text):
        style = {
            'a': 'aอฬบ',
            'b': 'bอฬบ',
            'c': 'cอฬบ',
            'd': 'dอฬบ',
            'e': 'eอฬบ',
            'f': 'fอฬบ',
            'g': 'gอฬบ',
            'h': 'hอฬบ',
            'i': 'iอฬบ',
            'j': 'jอฬบ',
            'k': 'kอฬบ',
            'l': 'lอฬบ',
            'm': 'mอฬบ',
            'n': 'nอฬบ',
            'o': 'oอฬบ',
            'p': 'pอฬบ',
            'q': 'qอฬบ',
            'r': 'rอฬบ',
            's': 'sอฬบ',
            't': 'tอฬบ',
            'u': 'uอฬบ',
            'v': 'vอฬบ',
            'w': 'wอฬบ',
            'x': 'xอฬบ',
            'y': 'yอฬบ',
            'z': 'zอฬบ',
            'A': 'Aอฬบ',
            'B': 'Bอฬบ',
            'C': 'Cอฬบ',
            'D': 'Dอฬบ',
            'E': 'Eอฬบ',
            'F': 'Fอฬบ',
            'G': 'Gอฬบ',
            'H': 'Hอฬบ',
            'I': 'Iอฬบ',
            'J': 'Jอฬบ',
            'K': 'Kอฬบ',
            'L': 'Lอฬบ',
            'M': 'Mอฬบ',
            'N': 'Nอฬบ',
            'O': 'Oอฬบ',
            'P': 'Pอฬบ',
            'Q': 'Qอฬบ',
            'R': 'Rอฬบ',
            'S': 'Sอฬบ',
            'T': 'Tอฬบ',
            'U': 'Uอฬบ',
            'V': 'Vอฬบ',
            'W': 'Wอฬบ',
            'X': 'Xอฬบ',
            'Y': 'Yอฬบ',
            'Z': 'Zอฬบ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def arrows(text):
        style = {
            'a': 'aอ',
            'b': 'bอ',
            'c': 'cอ',
            'd': 'dอ',
            'e': 'eอ',
            'f': 'fอ',
            'g': 'gอ',
            'h': 'hอ',
            'i': 'iอ',
            'j': 'jอ',
            'k': 'kอ',
            'l': 'lอ',
            'm': 'mอ',
            'n': 'nอ',
            'o': 'oอ',
            'p': 'pอ',
            'q': 'qอ',
            'r': 'rอ',
            's': 'sอ',
            't': 'tอ',
            'u': 'uอ',
            'v': 'vอ',
            'w': 'wอ',
            'x': 'xอ',
            'y': 'yอ',
            'z': 'zอ',
            'A': 'Aอ',
            'B': 'Bอ',
            'C': 'Cอ',
            'D': 'Dอ',
            'E': 'Eอ',
            'F': 'Fอ',
            'G': 'Gอ',
            'H': 'Hอ',
            'I': 'Iอ',
            'J': 'Jอ',
            'K': 'Kอ',
            'L': 'Lอ',
            'M': 'Mอ',
            'N': 'Nอ',
            'O': 'Oอ',
            'P': 'Pอ',
            'Q': 'Qอ',
            'R': 'Rอ',
            'S': 'Sอ',
            'T': 'Tอ',
            'U': 'Uอ',
            'V': 'Vอ',
            'W': 'Wอ',
            'X': 'Xอ',
            'Y': 'Yอ',
            'Z': 'Zอ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def rvnes(text):
        style = {
            'a': 'แ',
            'b': 'แ',
            'c': 'แญ',
            'd': 'แ',
            'e': 'แฟ',
            'f': 'แป',
            'g': 'แ',
            'h': 'แ',
            'i': 'แ',
            'j': 'แ',
            'k': 'แ',
            'l': 'แจ',
            'm': 'แ ',
            'n': 'แญ',
            'o': 'แ',
            'p': 'แจ',
            'q': 'แ',
            'r': 'แช',
            's': 'แ',
            't': 'แ',
            'u': 'แ',
            'v': 'แ',
            'w': 'แ ',
            'x': 'แธ',
            'y': 'แ',
            'z': 'แ',
            'A': 'แ',
            'B': 'แ',
            'C': 'แญ',
            'D': 'แ',
            'E': 'แฟ',
            'F': 'แป',
            'G': 'แ',
            'H': 'แ',
            'I': 'แ',
            'J': 'แ',
            'K': 'แ',
            'L': 'แจ',
            'M': 'แ ',
            'N': 'แญ',
            'O': 'แ',
            'P': 'แจ',
            'Q': 'แ',
            'R': 'แช',
            'S': 'แ',
            'T': 'แ',
            'U': 'แ',
            'V': 'แ',
            'W': 'แ ',
            'X': 'แธ',
            'Y': 'แ',
            'Z': 'แ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def strike(text):
        style = {
            'a': 'aฬถ',
            'b': 'bฬถ',
            'c': 'cฬถ',
            'd': 'dฬถ',
            'e': 'eฬถ',
            'f': 'fฬถ',
            'g': 'gฬถ',
            'h': 'hฬถ',
            'i': 'iฬถ',
            'j': 'jฬถ',
            'k': 'kฬถ',
            'l': 'lฬถ',
            'm': 'mฬถ',
            'n': 'nฬถ',
            'o': 'oฬถ',
            'p': 'pฬถ',
            'q': 'qฬถ',
            'r': 'rฬถ',
            's': 'sฬถ',
            't': 'tฬถ',
            'u': 'uฬถ',
            'v': 'vฬถ',
            'w': 'wฬถ',
            'x': 'xฬถ',
            'y': 'yฬถ',
            'z': 'zฬถ',
            'A': 'Aฬถ',
            'B': 'Bฬถ',
            'C': 'Cฬถ',
            'D': 'Dฬถ',
            'E': 'Eฬถ',
            'F': 'Fฬถ',
            'G': 'Gฬถ',
            'H': 'Hฬถ',
            'I': 'Iฬถ',
            'J': 'Jฬถ',
            'K': 'Kฬถ',
            'L': 'Lฬถ',
            'M': 'Mฬถ',
            'N': 'Nฬถ',
            'O': 'Oฬถ',
            'P': 'Pฬถ',
            'Q': 'Qฬถ',
            'R': 'Rฬถ',
            'S': 'Sฬถ',
            'T': 'Tฬถ',
            'U': 'Uฬถ',
            'V': 'Vฬถ',
            'W': 'Wฬถ',
            'X': 'Xฬถ',
            'Y': 'Yฬถ',
            'Z': 'Zฬถ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def frozen(text):
        style = {
            'a': 'aเผ',
            'b': 'bเผ',
            'c': 'cเผ',
            'd': 'dเผ',
            'e': 'eเผ',
            'f': 'fเผ',
            'g': 'gเผ',
            'h': 'hเผ',
            'i': 'iเผ',
            'j': 'jเผ',
            'k': 'kเผ',
            'l': 'lเผ',
            'm': 'mเผ',
            'n': 'nเผ',
            'o': 'oเผ',
            'p': 'pเผ',
            'q': 'qเผ',
            'r': 'rเผ',
            's': 'sเผ',
            't': 'tเผ',
            'u': 'uเผ',
            'v': 'vเผ',
            'w': 'wเผ',
            'x': 'xเผ',
            'y': 'yเผ',
            'z': 'zเผ',
            'A': 'Aเผ',
            'B': 'Bเผ',
            'C': 'Cเผ',
            'D': 'Dเผ',
            'E': 'Eเผ',
            'F': 'Fเผ',
            'G': 'Gเผ',
            'H': 'Hเผ',
            'I': 'Iเผ',
            'J': 'Jเผ',
            'K': 'Kเผ',
            'L': 'Lเผ',
            'M': 'Mเผ',
            'N': 'Nเผ',
            'O': 'Oเผ',
            'P': 'Pเผ',
            'Q': 'Qเผ',
            'R': 'Rเผ',
            'S': 'Sเผ',
            'T': 'Tเผ',
            'U': 'Uเผ',
            'V': 'Vเผ',
            'W': 'Wเผ',
            'X': 'Xเผ',
            'Y': 'Yเผ',
            'Z': 'Zเผ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text
