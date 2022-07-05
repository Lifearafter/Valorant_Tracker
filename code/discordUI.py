import os
from discord.ext import commands
from matchhistory import compMatchHistory
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')
load_dotenv()

@bot.event
async def on_ready():
  print("Bot is ready")
                       
@bot.command()
async def track(ctx,*,args):
  msg = args.split('#', 1)
  userName = msg[0]
  tag = msg[1]
  mh = compMatchHistory(userName, tag)
  await ctx.send("This is going to take a few seconds...") 
  
  if mh.getAccData() is True:
    if mh.formatAccData() is True:
      if mh.getMmrHistory() is True:
        if mh.formatMmrData() is True:
          if mh.getPrevMmr() is True:
            counter = 1
            await ctx.send('For user **{user}**: '.format(user=mh.userName))
            
            for x in mh.ranks:
              await ctx.send("> For episode 4 act {actInfo}:   `{rank}`".format(actInfo=counter, rank=x))
              counter = counter+1
            await ctx.send('\u200B\n')
            counter = 1
            for x in mh.mmrChange:
              await ctx.send('> For match {counter}:  `{mmr}`'.format(counter=counter, mmr=x))
              counter = counter+1
            await ctx.send('\u200B\n> **{user}\'s** current rank is: `{rank}`'.format(user=mh.userName, rank = mh.currentRank))
            
          else:
            await ctx.send('{status}: {error}'.format(status = mh.statusRequest, error = mh.errorMsg))
        else:
          await ctx.send('{error}'.format(error = mh.errorMsg))
      else:
        await ctx.send('{status}: {error}'.format(status = mh.statusRequest, error = mh.errorMsg))
    else:
      await ctx.send('{error}'.format(error = mh.errorMsg))
  else:
    await ctx.send('{status}: {error}'.format(status = mh.statusRequest, error = mh.errorMsg))


Token = os.getenv('TOKEN')

@bot.event 
async def on_message(message):
    if message.author is Token:
        return

    await bot.process_commands(message)

bot.run(Token)