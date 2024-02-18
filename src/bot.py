import discord
import src.responses as responses

async def send_message(message, is_private):
    try:
        response = await responses.handleResponse(message, message.author.id)
        if response is not None:
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
    except Exception as e:
        print(e)
    
def get_token():
    with open("token.src", "r") as file:
        return file.read().strip()

def run_discord_bot():
    TOKEN = get_token()
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running.")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # Debug
        print(f"user: '{message.author.name}' send: '{message.content}' in channel: '{message.channel}'")
        await send_message(message, is_private=message.channel.type == discord.ChannelType.private)

    client.run(TOKEN)

run_discord_bot()
