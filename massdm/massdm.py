import re
import asyncio
import datetime
import discord
from discord.ext import commands


class Massdm(commands.Cog):

    """Send a direct message to all members of the specified Role."""

    def __init__(self, ctx):
        self.bot = bot

    def _member_has_role(self, ctx):
        return role in member.roles

    def _get_users_with_role(self, ctx): -> List[discord.User]:
        roled = []
        for member in server.members:
            if self._member_has_role(member, role):
                roled.append(member)
        return roled

    
    
    
    @commands.command()
    async def mdm(self, ctx):
        """Sends a DM to all Members with the given Role.
        Allows for the following customizations:
        {0} is the member being messaged.
        {1} is the role they are being message through.
        {2} is the person sending the message.
        """

        server = ctx.message.server
        sender = ctx.message.author

        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass

        dm_these = self._get_users_with_role(server, role)

        for user in dm_these:
            try:
                await self.bot.send_message(user,
                                            message.format(user, role, sender))
            except (discord.Forbidden, discord.HTTPException):
                continue


def setup(bot):
    bot.add_cog(Massdm(bot))
