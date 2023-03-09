import discord, json, random, datetime
from discord.ext import commands


def run_discord_bot():
  TOKEN = 'MTA3ODc2MDc5OTQwMjczMzYyOQ.G3vBY5.YqmLXZvAfgWeL_RoQ8oyCuNBk1bKdLC9Zwsn2U' #Token is put manually 
  intents = discord.Intents.all()
  client = commands.Bot(command_prefix = ".", intents = intents)
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
    percem = random.randint(1,10)
    username = member.mention
    if percem <= 7:
      await ctx.send(random.choice(links["expel"]))
      seconds = random.randint(10,120)
      time = datetime.timedelta(seconds = seconds)
      await ctx.send(username + " was hit by ***Expelliarmus*** and is unable to cast magic for " + str(seconds) + " seconds")
      await member.edit(timed_out_until=discord.utils.utcnow() + time)
    else:
      await ctx.send(ctx.message.author.mention + " tried to use ***Expelliarmus*** on " + username + ", but it missed!")

  @client.command(name = "fin", aliases = ["Finite", "finite", "FINITE"])
  async def End_TO(ctx, member:discord.Member):
    username = member.mention
    if not member.is_timed_out():
      await ctx.send("Fortunately, " + username + "is not affected by any spell")
    else:
      await ctx.send(links["fin"])
      await ctx.send("Marvelous, " + ctx.message.author.mention + " saved " + username + "! What a generous soul")
      await member.edit(timed_out_until = None)

  @client.command(name = "kill", aliases = ["AVADA_KEDAVRA"])
  @commands.has_any_role(543905846510354442, 1079186787257307228)
  async def kick(ctx, member:discord.Member):
    percem = random.randint(1,10)
    if percem <= 2:
      await ctx.send(random.choice(links["kill"]))
      username = member.mention
      await ctx.send("It can't be. " + ctx.message.author.mention + " used the killing curse :fearful: Poor " + username)
      await member.kick(reason="AVADA KEDAVRA")
    else:
      await ctx.send(ctx.message.author.mention + " tried to use ***Avada Kedavra*** on " + username + ", but it missed!")
  client.run(TOKEN)
    
