import asyncio
from collections import deque
from . import *


#befor any command use ^ this. If U dont want to add command handler before command then use ^ this it will work without command handler.
@bot.on(admin_cmd(pattern=r"^🤬", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^🤬", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "𝙸 𝚊𝚖 𝚊𝚗𝚐𝚛𝚢 ")
    deq = deque(list("😡🔥🤬🔥😡🔥🤬🔥😡🔥"))
    for _ in range(30):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)
        

@bot.on(admin_cmd(pattern=r"^🤣", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^🤣", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Lots Of Laugh")
    deq = deque(list("🤣😂🤣😂🤣😂🤣😂"))
    for _ in range(50):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)
  
@bot.on(admin_cmd(pattern=r"^✅", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^✅", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Choose What U like😂")
    deq = deque(list("✅❌✅❌✅❌✅❌✅❌"))
    for _ in range(10):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)
      
CmdHelp("angry").add_command(
  "^🤬", None, "υѕє it also it describes all about ur felling that u r angry - 🤬"
).add_command(
  "^🤣", None, "funny command use it and see it"
).add_command(
  "^✅", "<Reply To User>", "Use this to make person Confused"
).add_type(
  "Addons"
).add_info(
  "Its Very Useful Module this module explains all about your fellings like (🤬) for ur angry(🤣)friends message is funny "
).add_warning(
  "Harmless Module✅"
).add()

