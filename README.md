<h1 align="center">
  <b>𝐶𝐼𝑁𝐸𝑀𝐴𝐻𝑈𝐵 𝑣𝑒𝑟𝑠𝑖𝑜𝑚 𝑜𝑓 𝐸𝑣𝑎𝑀𝑎𝑟𝑖𝑎 𝐵𝑜𝑡</b>
</h1>


## A fully functional Group Management Bot with Auto Filter and File store Feature.

  [![Size](https://img.shields.io/github/repo-size/soymadip/EVA_Cinehub?style=flat-square&color=green)](https://github.com/soymadip/EVA_Cinehub.git) [![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/soymadip/EVA_Cinehub.git)
  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgjbae1212%2Fhit-counter&count_bg=%23FF9008&title_bg=%23555555&icon=probot.svg&icon_color=%23E7E7E7&title=EVA&edge_flat=false)](https://github.com/soymadip/EVA_Cinehub)

## Features--

> [!WARNING]
> Development stopped

✗ STOCK:-
- [x] Filter (Manual & Auto)
- [x] IMDB poster search
- [x] Admin Commands
- [x] Broadcast
- [x] IMDB search
- [x] Inline Search (ADMINS Exclusive).
- [x] Random pics
- [x] ids and User info 
- [x] File Store
- [x] Individual Settings for each groups

✗ CINEHUB FEATURES:-
- [x] MAINTENANCE MODE : When enabled, bot will tell everyone that maintenance is going on.
- [x] Auto delete autofilter results to avoid copyright.
- [x] Manual filter now supports fillings.
- [x] Blocking (tmute, mute, kick)
- [x] Group Management (pin, purge, kick etc..) 
- [x] telegraph
- [x] sharable link 
- [x] link shortner
- [x] Text to speech
- [x] Url Shortner
- [x] Log of files taken by users.
- [x] logs of pending requests 
- [x] Improved spellCheck A.I, Now it's more practical.
- [x] PM guide.
- [x] Users who banned bot, will be deleted automatically from db.
- [x] Added forward with quote support. use /qbroadcast to.....
- [ ] FUTURE PLAN : Improve PM guide to enable or disable PM result.
- [ ] ~~Many others coming.....~~

## Read [this](https://graph.org/Many-Of-You-May-Not-Be-Knowing-That-You-Can-Customize-Your-Bot-A-Lot-02-03) before you start messing up with <b>stock codes</b>.

### Variables--
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). 
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel. 
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* `SUPPORT_CHAT` - Add your own chat as a support chat
* `P_TTI_SHOW_OFF` - (Use True or False) - Users will be redirected to send /start to Bot PM if set to True else files will be sent directly to users PM

## Deploy--

<b>𝕺𝖊𝖕𝖑𝖔𝖞 𝕿𝖔 𝕳𝖊𝖗𝖔𝖐𝖚</b>:-
<p>
<a href="https://heroku.com/deploy?template=https://github.com/soymadip/EVA_Cinehub.git">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>




<b>Deploy to VPS</b>:-
<p>
<pre>
git clone https://github.com/soymadip/EVA_Cinehub.git
# Install Packages
pip3 install -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>


## Commands--
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
* /imdb - fetch info from imdb.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
* /enable - re-enable chat.
• /ban_user  - to ban a user.
• /unban  - to unban a user.
• /channels - to get list of total connected channels
• /broadcast - to broadcast a message to all users (without quote).
• /qbroadcast - to broadcast a message to all users (with quote).
• /batch - to create link for multiple posts.
• /links - to create link for one post.
• /telegraph - upload media less than 5 MB to telegraph.
• /share - get shareable link of any text or link.
• /tmute <time> - temporarily mute user .
```

## Thanks to- 
 - First of all thanks to [Eva Maria](https://github.com/EvamariaTG/EvaMaria) Devs.
 - Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)
 - Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0254/Media-Search-bot)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)



## Disclaimer--
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    

Selling The Codes To Other People For Money Is *Strictly Prohibited*.
