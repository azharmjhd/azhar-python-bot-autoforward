from telethon import TelegramClient, events, sync

# Ganti dengan informasi API_ID, API_HASH, dan BOT_TOKEN Anda
api_id = 'your_api_id'
api_hash = 'your_api_hash'
bot_token = 'your_bot_token'

chat_id_grafana_bot = '@usernamebot'  # atau ID bot
chat_id_group_sitamaid = -10012  # Ganti dengan chat ID grup

# Inisialisasi TelegramClient
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(from_users=chat_id_grafana_bot))
async def forward_message(event):
    await event.message.forward_to(chat_id_group_sitamaid)
    print(f'Pesan dari Bot Alert diteruskan ke grup : {event.message.text}')

def main():
    with client:
        client.run_until_disconnected()

if __name__ == '__main__':
    main()
