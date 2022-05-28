

from pyrogram import (
    Client,
    __version__
)

from info import (
    API_HASH,
    API_ID,
    TG_USER_SESSION
)

class User(Client):
    def __init__(self):
        super().__init__(
            TG_USER_SESSION,
            api_hash=API_HASH,
            api_id=API_ID,
            workers=4
        )
 
 
