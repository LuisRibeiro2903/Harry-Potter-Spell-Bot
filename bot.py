import discord, json, random, datetime
from discord.ext import commands


def run_discord_bot():
  TOKEN = '' #Token is put manually 
  intents = discord.Intents.all()
  client = commands.Bot(command_prefix = "hp!", intents = intents)
  links = json.load(open("gifs.json"))

  @client.event
  async def on_ready():
    print(f'{client.user} is now running!')

  @client.command()
  async def hi(ctx):
    username = ctx.message.author.mention
    await ctx.send("Hello there " + username)

  @client.command(name = "expel", aliases=["EXPELLIARMUS", "Expelliarmus", "expelliarmus"])
  async def Time_out(ctx, member:discord.Member):
    await ctx.send(random.choice(links["expel"]))
    username = member.mention
    seconds = random.randint(10,120)
    time = datetime.timedelta(seconds = seconds)
    await ctx.send("" + username + " was hit by ***Expelliarmus*** and is unable to cast magic for " + str(seconds) + " seconds")
    await member.edit(timed_out_until=discord.utils.utcnow() + time)

  @client.command(name = "fin", aliases = ["Finite", "finite", "FINITE"])
  async def End_TO(ctx, member:discord.Member):
    username = member.mention
    if not member.is_timed_out():
      await ctx.send("Fortunately, " + username + "is not affected by any spell")
    else:
      await ctx.send(links["fin"])
      await ctx.send("Marvelous, " + ctx.message.author.mention + " saved " + username + "! What a generous soul")
      await member.edit(timed_out_until = None)
    
  client.run(TOKEN)
    
