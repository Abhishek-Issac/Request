import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
SESSION = environ.get("SESSION")
CHANNELS = "-1001885651550"         
AuthChat = filters.chat(CHANNELS) if CHANNELS else (filters.group | filters.channel)         
UB_Client = Client(session_name="my_session", api_id=20268776, api_hash="1048dbd34139b86a39122bd95d49bd63", session_string=SESSION)


@UB_Client.on_message(filters.command(["run", "approve", "start"], [".", "/"]) & AuthChat)                     
async def approve(client: User, message: Message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq 🙃
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await asyncio.sleep(3)
    await msg.delete()


logging.info("Bot Started....")
UB_Client.run()







