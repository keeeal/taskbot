import asyncio, discord
from tasks import get_task

BOT_SIGN = '💌'

def main():
    with open('token.txt') as f:
        token = f.readline()[:-1]

    client = discord.Client()

    @client.event
    async def on_ready():
        print('\nLogged in as', client.user.name, '\n')

    @client.event
    async def on_message(message):
        if message.content.startswith(BOT_SIGN):
            command = message.content[len(BOT_SIGN):].strip()
            reply = 'Unknown command: \"' + command + '\"'

            if command == '':
                reply = get_task()

            await client.send_message(message.channel,
                embed=discord.Embed(description=reply))

    while True:
        try:
            client.run(token)
        except KeyboardInterrupt:
            raise
        except:
            pass

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    main(**vars(parser.parse_args()))
