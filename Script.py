class script(object):
    START_TXT = """ℍ𝔼𝕃𝕃𝕆 {}\n\n 𝕀 𝔸𝕄 <a href=https://t.me/{}>{}</a>\n 𝕀 𝔻𝔼𝕃𝕀𝕍𝕀𝔼ℝ ℝ𝔼ℚ𝕌𝔼𝕊𝕋𝔼𝔻 𝕄𝔼𝔻𝕀𝔸 𝕋𝕆 ℙ𝔼𝕆ℙ𝕃𝔼.\n𝔻𝕆ℕ𝕋 𝔽𝕆ℝ𝔾𝔼𝕋 𝕋𝕆 𝔽𝕆𝕃𝕃𝕆𝕎 𝕄𝕐 𝕌𝕆𝔻𝔸𝕋𝔼𝕊 ℂℍ𝔸ℕℕ𝔼𝕃 𝔹𝔼𝔽𝕆ℝ𝔼 𝕌𝕊𝕀ℕ𝔾 𝕄𝔼."""
    HELP_TXT = """𝙷𝙴𝚈 {}
ℍ𝔼ℝ𝔼 𝕀𝕊 𝕄𝕐 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href= https://t.me/anonymous7205>🆂🅾️🆄🅼🅰️🅳🅸🅿️</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳: v1.0.1 [ ℂ𝕀ℕ𝔼ℍ𝕌𝔹 𝕍𝔼ℝ𝕊𝕀𝕆ℕ ]"""
    SOURCE_TXT = """<b>SOURCE:</b> 
- THIS PIECE OF SOFTWARE IS TOTALY PRVATE.\nALTHOUGH IF YOU WANT MY CODE THEN PLEASE CONTACT MY <b>DEV</b>.\n
<b>   𝔻𝔼𝕍:-</b> <a href= https://t.me/anonymous7205>🆂🅾️🆄🅼🅰️🅳🅸🅿️</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- 𝔽𝕚𝕝𝕥𝕖𝕣 𝕚𝕤 𝕥𝕙𝕖 𝕗𝕖𝕒𝕥𝕦𝕣𝕖 𝕨𝕖𝕣𝕖 𝕦𝕤𝕖𝕣𝕤 𝕔𝕒𝕟 𝕤𝕖𝕥 𝕒𝕦𝕥𝕠𝕞𝕒𝕥𝕖𝕕 𝕣𝕖𝕡𝕝𝕚𝕖𝕤 𝕗𝕠𝕣 𝕒 𝕡𝕒𝕣𝕥𝕚𝕔𝕦𝕝𝕒𝕣 𝕜𝕖𝕪𝕨𝕠𝕣𝕕 𝕒𝕟𝕕 𝔼𝕧𝕒𝕄𝕒𝕣𝕚𝕒 𝕨𝕚𝕝𝕝 𝕣𝕖𝕤𝕡𝕠𝕟𝕕 𝕨𝕙𝕖𝕟𝕖𝕧𝕖𝕣 𝕒 𝕜𝕖𝕪𝕨𝕠𝕣𝕕 𝕚𝕤 𝕗𝕠𝕦𝕟𝕕 𝕥𝕙𝕖 𝕞𝕖𝕤𝕤𝕒𝕘𝕖.
<b>NOTE:</b>
1. 𝕒𝕝𝕖𝕣𝕥 𝕓𝕦𝕥𝕥𝕠𝕟𝕤 𝕙𝕒𝕧𝕖 𝕒 𝕝𝕚𝕞𝕚𝕥 𝕠𝕗 𝟞𝟜 𝕔𝕙𝕒𝕣𝕒𝕔𝕥𝕖𝕣𝕤.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- ME Supports both url and alert inline buttons.
<b>NOTE:</b>
1. 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝑤𝑖𝑙𝑙 𝑛𝑜𝑡 𝑎𝑙𝑙𝑜𝑤𝑠 𝑦𝑜𝑢 𝑡𝑜 𝑠𝑒𝑛𝑑 𝑏𝑢𝑡𝑡𝑜𝑛𝑠 𝑤𝑖𝑡ℎ𝑜𝑢𝑡 𝑎𝑛𝑦 𝑐𝑜𝑛𝑡𝑒𝑛𝑡, 𝑠𝑜 𝑐𝑜𝑛𝑡𝑒𝑛𝑡 𝑖𝑠 𝑚𝑎𝑛𝑑𝑎𝑡𝑜𝑟𝑦.
2. 𝑀𝐸 𝑠𝑢𝑝𝑝𝑜𝑟𝑡𝑠 𝑏𝑢𝑡𝑡𝑜𝑛𝑠 𝑤𝑖𝑡ℎ 𝑎𝑛𝑦 𝑡𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝑚𝑒𝑑𝑖𝑎 𝑡𝑦𝑝𝑒.
3. 𝐵𝑢𝑡𝑡𝑜𝑛𝑠 𝑠ℎ𝑜𝑢𝑙𝑑 𝑏𝑒 𝑝𝑟𝑜𝑝𝑒𝑟𝑙𝑦 𝑝𝑎𝑟𝑠𝑒𝑑 𝑎𝑠 𝑚𝑎𝑟𝑘𝑑𝑜𝑤𝑛 𝑓𝑜𝑟𝑚𝑎𝑡
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Eva)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. 𝑀𝑎𝑘𝑒 𝑚𝑒 𝑡ℎ𝑒 𝑎𝑑𝑚𝑖𝑛 𝑜𝑓 𝑦𝑜𝑢𝑟 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 𝑖𝑓 𝑖𝑡'𝑠 𝑝𝑟𝑖𝑣𝑎𝑡𝑒.
2. 𝑚𝑎𝑘𝑒 𝑠𝑢𝑟𝑒 𝑡ℎ𝑎𝑡 𝑦𝑜𝑢𝑟 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 𝑑𝑜𝑒𝑠 𝑛𝑜𝑡 𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑠 𝑐𝑎𝑚𝑟𝑖𝑝𝑠, 𝑝𝑜𝑟𝑛 𝑎𝑛𝑑 𝑓𝑎𝑘𝑒 𝑓𝑖𝑙𝑒𝑠.
3. 𝐹𝑜𝑟𝑤𝑎𝑟𝑑 𝑡ℎ𝑒 𝑙𝑎𝑠𝑡 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑡𝑜 𝑚𝑒 𝑤𝑖𝑡ℎ 𝑞𝑢𝑜𝑡𝑒𝑠.
 𝐼'𝑙𝑙 𝑎𝑑𝑑 𝑎𝑙𝑙 𝑡ℎ𝑒 𝑓𝑖𝑙𝑒𝑠 𝑖𝑛 𝑡ℎ𝑎𝑡 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 𝑡𝑜 𝑚𝑦 𝑑𝑏."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- �𝑠𝑒𝑑 𝑡𝑜 𝑐𝑜𝑛𝑛𝑒𝑐𝑡 𝑏𝑜𝑡 𝑡𝑜 𝑃𝑀 𝑓𝑜𝑟 𝑚𝑎𝑛𝑎𝑔𝑖𝑛𝑔 𝑓𝑖𝑙𝑡𝑒𝑟𝑠 
- 𝑖𝑡 ℎ𝑒𝑙𝑝𝑠 𝑡𝑜 𝑎𝑣𝑜𝑖𝑑 𝑠𝑝𝑎𝑚𝑚𝑖𝑛𝑔 𝑖𝑛 𝑔𝑟𝑜𝑢𝑝𝑠.
<b>NOTE:</b>
1. 1. 𝓞𝓷𝓵𝔂 𝓪𝓭𝓶𝓲𝓷𝓼 𝓬𝓪𝓷 𝓪𝓭𝓭 𝓪 𝓬𝓸𝓷𝓷𝓮𝓬𝓽𝓲𝓸𝓷.
2. 𝑆𝑒𝑛𝑑 <code>/connect</code> 𝑓𝑜𝑟 𝑐𝑜𝑛𝑛𝑒𝑐𝑡𝑖𝑛𝑔 𝑚𝑒 𝑡𝑜 𝑢𝑟 𝑃𝑀
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of ME
<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
𝑇ℎ𝑖𝑠 𝑚𝑜𝑑𝑢𝑙𝑒 𝑜𝑛𝑙𝑦 𝑤𝑜𝑟𝑘𝑠 𝑓𝑜𝑟 𝑚𝑦 𝑎𝑑�"""
    STATUS_TXT = """✗ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
✗ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
✗ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
✗ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code>
✗ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """🅽🅴🆆 🆄🆂🅴🆁
🅘🅓 - <code>{}</code>
ⓃⒶⓂ️Ⓔ - {}
"""