import os
import discord
import reponses as my_responses

async def send_message(message, user_message, is_private):
    """Send a message."""
    try:
        response = my_responses.handle_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as exc:
        print(exc)


def get_private_token() -> str:
    """Get the private token either from env or a file."""
    private_token = os.environ.get("DISCORD_BOT_TOKEN")
    if not private_token:
        with open("private_token", "rb") as token_file:
            private_token = token_file.readline().decode("utf-8")
    return private_token

def run_discord_bot():
    """Run the bot."""
    TOKEN = get_private_token()

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"The {client.user} is now running.")

    @client.event
    async def on_message(message: discord.message.Message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(
            f"username: {username} in channel ({channel}):\n{user_message}")
        
        if user_message[0] in ["?", "%", "$"]:
            user_message = user_message[1:]
            await send_message(message, user_message[1:], is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)