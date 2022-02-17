from gettext import find
from posixpath import split
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
app = Client("gramsession", 14897586, "49db49b537577139a4b337f2764b70a3")
toSender = "SENDYMN"

@app.on_message()
def my_function(client, message):
    if message.chat.id != -1001159025906 and message.chat.type != "channel":
        if message.text:
            
            textUpdate = message.text
            splitText = textUpdate.split("||")        
            if '.join' == splitText[0]:
                chatJuser = app.get_chat(splitText[1])['username']
                print(app.join_chat(chatJuser))
            textUpdate = message.text
            splitText = textUpdate.split("||")
            if '.del' == splitText[0]:
                chatJuser = app.get_chat(splitText[1])['id']
                app.leave_chat(chatJuser, delete=True)



    if message.chat.id != -1001159025906 and message.chat.type == "channel":
        print( message )
        if message.photo:
            photoFileId = message.photo.file_id
            captionPhoto = message.caption
            IdSenderPhoto = message.chat.id
            app.send_photo(toSender, photoFileId, caption=f"\(idsender){IdSenderPhoto}\(idSender): {captionPhoto}")
        if message.video:
            videoFileId = message.video.file_id
            captionVideo = message.caption
            IdSenderVideo = message.chat.id
            app.send_video(toSender, videoFileId, caption=f"\(idsender){IdSenderVideo}\(idSender): {captionVideo}")
        if message.document:
            documentFileId = message.document.file_id
            captionDocument = message.caption
            IdSenderDocument = message.chat.id
            app.send_document(toSender, documentFileId, caption=f"\(idsender){IdSenderDocument}\(idSender): {captionDocument}")
        if message.audio:
            audioFileId = message.audio.file_id
            captionAudio = message.caption
            IdSenderAudio = message.chat.id
            app.send_audio(toSender, audioFileId, caption=f"\(idsender){IdSenderAudio}\(idSender): {captionAudio}")
        if message.text:
            textIsset = message.text
            IdSenderText = message.chat.id
            app.send_message(toSender, f"\(idsender){IdSenderText}\(idSender): {textIsset}")

            
        
        
my_handler = MessageHandler(my_function)

app.add_handler(my_handler)

app.run()
