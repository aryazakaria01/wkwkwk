""" Userbot module Memes tmoji"""

import asyncio

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.tmoji$")
async def tmoji(tmoji):
    """ Basically it's .tmoji command """
    await tmoji.edit(f"š")
    await asyncio.sleep(2)
    await tmoji.edit(f"š")
    await asyncio.sleep(2)
    await tmoji.edit(f"š¤£")
    await asyncio.sleep(2)
    await tmoji.edit(f"š")


CMD_HELP.update({
    "tmoji":
    "š **Cmd** : `.tmoji`\
    \nš **Descriptions** : Cek Aja sendiri :v."
})
