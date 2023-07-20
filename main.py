import discord
import os
import openai
import sys

client = discord.Client(intents=discord.Intents.all())

try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
  sys.stderr.write("""
  You haven't set up your API key yet.
  """)
  exit(1)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()

  if "domino" in msg and "bot" in msg:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": message.content}
    ]
)
    await message.channel.send(response.choices[0].message.content)

client.run(os.getenv("TOKEN"))