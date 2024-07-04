from telethon import TelegramClient, events, sync

# Ganti dengan informasi API_ID, API_HASH, dan BOT_TOKEN Anda
api_id = 'your_api_id'
api_hash = 'your_api_hash'
bot_token = 'your_bot_token'

# Ganti dengan chat_id bot Grafana Alert dan grup Telegram yang dituju
chat_id_grafana_bot = 'test'  # atau ID bot Grafana Alert
chat_id_group_sitamaid = -10012  # Ganti dengan chat ID grup sitamaid

# Inisialisasi TelegramClient
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(from_users=chat_id_grafana_bot))
async def forward_message(event):
    await event.message.forward_to(chat_id_group_sitamaid)
    print(f'Pesan dari bot Grafana Alert diteruskan ke grup sitamaid: {event.message.text}')

def main():
    with client:
        client.run_until_disconnected()

if __name__ == '__main__':
    main()
