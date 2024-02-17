import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handleResponse(user_message, message.author.id)
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
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f"{client.user} is running.")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # Debug console
        print("user: '" + str(client.user) + "' send: '" + str(message.content) + "' in channel: '" + str(message.channel) + "'")

        # Check if the bot is mentioned in the message
        if client.user.mentioned_in(message):
            # Extract the command after the mention
            user_message = message.content.split(maxsplit=1)[1].strip()
            
            # Pass the command to the appropriate function
            await send_message(message, user_message, is_private=message.channel.type == discord.ChannelType.private)
        else:
            await send_message(message, message.content, is_private=message.channel.type == discord.ChannelType.private)

    client.run(TOKEN)

run_discord_bot()
