# Many Of You May Not Know That You Can Customize Your Bot A Lot(without editing Code).

The following config vars can be used to do so.


1. IMDB_TEMPLATE - To Customize (https://t.me/TeamEvamaria/9) imdb data.


2. SUPPORT_CHAT - Add your own chat as a support chat instead of @EvamariaSupport.


3. P_TTI_SHOW_OFF - (Use True or False) - Users will be redirected to send /start to Bot PM if set to True else files will be sent directly to users PM.


4. IMDB - (Use True or False) - To disable or enable imdb data.


5. SINGLE_BUTTON - (Use True or False) - If set True, file name and files size will be shown in a single button instead of two separate button.


6. CUSTOM_FILE_CAPTION - Same as IMDB template , you can customize the caption for files (available keys , file_name, file_size, file_caption )

 Example: <b>Join [Here](https://t.me/teamevamaria)</b> 


FILE : <code>{file_name}</code> 

Size : <i>{file_size}</i>

CAPTION: {file_caption}


7. LONG_IMDB_DESCRIPTION - (Use True or False) Long IMDB story line will be used if enabled.


8. SPELL_CHECK_REPLY - (Use True or False) - if enabled, bot will be suggesting related movies if keyword not found in database.


9. MAX_LIST_ELM - long lists like long casts list can be shortened using this value. list will be shortened to first n elements where n is the value for this config var. For example if 4 is used list will be shortened to foist 4 elements.


10. AUTH_CHANNEL - To enable force subscribe. Delete this var if you do not need fsub.


11. AUTH_USERS - To restrict the use of inline queries to specified users.


12. UPSTREAM_REPO - If you want to use a customized fork of Evamaria (https://github.com/EvamariaTG/EvaMaria), You can fill this config with github url of your fork.


13. BATCH_FILE_CAPTION - Same as CUSTOM_FILE_CAPTION , use in case you want separate captions for batch files.


14. MELCOW_NEW_USERS - Use False if you want the bot to not to welcome new users in groups.


15. PROTECT_CONTANT = Use True / False . If set to true files from bot cannot be forwarded to any chat.


16. PUBLIC_FILE_STORE = Use False if you don't want your bot to be used as a filestore bot by others.
