from .. import loader 

import io 

 

 

@loader.tds 

class SaverMod(loader.Module): 

    strings = {"name": "Save_delPic"} 

    @loader.owner 

    async def нюcmd(self, m): 

        ".ню + реплай на самоуничтожающееся фото Чтобы сохранить" 

        reply = await m.get_reply_message() 

        if not reply or not reply.media.ttl_seconds: return await m.edit("Реплаем на самоуничтожающееся фото! ") 

        await m.edit("<b>🤫</b>")

        await m.delete() 

        new = io.BytesIO(await reply.download_media(bytes)) 

        new.name = reply.file.name 

        await m.client.send_file("me", new)
