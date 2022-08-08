import discord

ALLOWED_CHANNELS = [1004837501350985868]
ALLOWED_GUILDS = [778411794996789278]
BANNED_USERS = [1006004286460797019]


access_token = None
client = discord.Client()

@client.event
async def on_ready():
    print("Login successful")

@client.event
async def on_message(message):
    try:
        if (not (message.guild.id in ALLOWED_GUILDS)) or (not (message.channel.id in ALLOWED_CHANNELS) or 
            (message.author.id in BANNED_USERS)):
            return
        await log_message(message)
        await message.edit(suppress=True)
    except:
        await message.reply(content="This caused an exception. (In other words, you crashed the bot!)")


#a logging function for received messages
async def log_message(message):
    print("----------------------------\nCONTENT:" + message.content)
    print("AUTHOR:" + str(message.author.id))
    print("GUILD:" + str(message.guild.id))
    print("CHANNEL:" + str(message.channel.id) + "\n----------------------------")

def main():
    print("Starting Remove Embeds Bot...")

    #read the access token
    try:
        acf = open("access_token", "r")
        access_token = acf.readline()
        acf.close()
    except:
        print("Fatal error: could not open access_file\n")
        return

    client.run(access_token)
    print("\nLeft main()")

if __name__ == '__main__':
    main()