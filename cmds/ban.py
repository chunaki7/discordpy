def ban(client, discord):
    @client.command()
    async def ban(ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} banned from the server.")