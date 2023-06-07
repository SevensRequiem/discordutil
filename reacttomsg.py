import selfcord
import colorama
from datetime import datetime

# Set up colorama
colorama.init()

# Set up the client
client = selfcord.Client()

# Set up the user ID, server ID, and emoji
user_ids = [12312312312312, 123123123123123, 123123123123]
server_id = 123123123123123123
emoji = ":name:53425234522"

# Get the channel IDs
channel_ids = [12413412, 245245245245, 243523452345235243] # Add more channel IDs here

# Define the on_ready event
@client.event
async def on_ready():
    print(f"Logged in as {client.user}.")
    # Get the server
    server = client.get_guild(int(server_id))
    # Get the users
    global users
    users = [server.get_member(int(user_id)) for user_id in user_ids]
    # Get the channels
    channels = [selfcord.utils.get(server.channels, id=channel_id) for channel_id in channel_ids]

# Define the on_message event
@client.event
async def on_message(message):
    if message.guild and message.guild.id == server_id and message.channel.id in channel_ids:
        print(f"{colorama.Fore.RED}User ID: {colorama.Fore.YELLOW}{message.author.id}{colorama.Fore.RED} | {colorama.Fore.YELLOW}{message.author.name}{colorama.Fore.RED} | {colorama.Fore.YELLOW}{message.content}")
    if message.author.id in user_ids and message.guild and message.guild.id == server_id and message.channel.id in channel_ids:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{colorama.Style.RESET_ALL}[{colorama.Fore.GREEN}{message.author.name}{colorama.Style.RESET_ALL}]: {message.content} {colorama.Fore.YELLOW}[{time}]{colorama.Style.RESET_ALL}")
            await message.add_reaction(emoji)
# Run the client
client.run("YOUR_USER_TOKEN")
