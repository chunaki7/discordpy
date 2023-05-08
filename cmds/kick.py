def kick(client, discord):
    @client.command()
    async def kick(ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} kicked from the server.")