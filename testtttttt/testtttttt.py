import discord
from discord.ext import commands
import asyncio
import json
import aiohttp

class testtttttt(commands.Cog):
    def __init__(self, bot):
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        self.bot = bot
        self.numbers = {'1': ':one:',
                        '2': ':two:',
                        '3': ':three:',
                        '4': ':four:',
                        '5': ':five:',
                        '6': ':six:',
                        '7': ':seven:',
                        '8': ':eight:',
                        '9': ':nine:',
                        '0': ':zero:'}
        self.sub_count = 0
        self.confirm = True
        self.double_instance = False
        self.interval = 10

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)

    @commands.command()
    async def startsubs(self, ctx):
        if not self.double_instance:
            await self.bot.send('Instance started.')
            while True:
                self.double_instance = True
                parameters = {"id": "UCnFHsZfaCwgBzbmt89Nmj3A",
                              "key": "AIzaSyCssyjjfIcJpvl4CYoD20LbKcWIxQPNvw8",
                              "part": "statistics",
                              "fields": "items/statistics/subscriberCount"}
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://www.googleapis.com/youtube/v3/channels", params=parameters) as r:
                            json_data = await r.json()
                sub_count = json_data['items'][0]['statistics']['subscriberCount']
                if sub_count != self.sub_count:
                    self.sub_count = sub_count
                    text = ''.join([self.numbers[x] for x in sub_count if x in self.numbers.keys()])
                    await self.bot.edit_channel(ctx.message.channel, topic=' **Total Subscribers** __**MaGe Clan**__ : {} __**bit.ly/MaGeClan**__<:xd:312128955467431936>'.format(text))
                if not self.confirm:
                    await self.bot.send('Done')
                    break
                await asyncio.sleep(self.interval)
        elif self.double_instance:
            await self.bot.send('An instance of the live subscriber counter is already running.')

def setup(bot):
    bot.add_cog(testtttttt(bot))
