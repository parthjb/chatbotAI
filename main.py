# This example requires the 'message_content' intent.
#Application ID : 1153045765204217988
#Public key : 509865564b5c0f28264e2a7f969be455640de9bcff6b7d013c3be18a9e361b29
# import os
# import discord
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
# token = os.getenv("SECRET_KEY")

# class MyClient(discord.Client):
  
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')
      
#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')
#         print(message.mentions)
      
#         if self.user!= message.author:
#           if self.user in message.mentions:
#             response = openai.Completion.create(
#               model="text-davinci-003",
#               prompt= message.content,
#               temperature=1,
#               max_tokens=256,
#               top_p=1,
#               frequency_penalty=0,
#               presence_penalty=0
#               )
#             channel = message.channel
#             messageToSend = response.choices[0].text
#             await channel.send(messageToSend)
      
# intents = discord.Intents.default()
# intents.message_content = True

# client = MyClient(intents=intents)
# client.run(token)

# import discord
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
# token = os.getenv("SECRET_KEY")

# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     print(f'Logged on as {client.user}!')

# @client.event
# async def on_message(message):
#     try:
#         if client.user != message.author:
#             if client.user in message.mentions:
#                 channel = message.channel
#                 response = openai.Completion.create(
#                     model="text-davinci-003",
#                     prompt=message.content,
#                     temperature=1,
#                     max_tokens=256,
#                     top_p=1,
#                     frequency_penalty=0,
#                     presence_penalty=0
#                 )
#                 messageToSend = response.choices[0].text
#                 await channel.send(messageToSend)
#     except Exception as e:
#         print(f"An error occurred: {e}")

# client.run(token)

import discord
import os
import openai
import logging

# Load configuration from a JSON file or environment variables
# Ensure you have a valid config file or .env setup
# config = load_config()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Command Prefix
command_prefix = "!"

@client.event
async def on_ready():
    logger.info(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Avoid responding to the bot's own messages

    if message.content.startswith(command_prefix):
        # Handle bot commands here
        pass
    else:
        try:
            # Handle non-command messages by generating a response
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.content,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            messageToSend = response.choices[0].text
            await message.channel.send(messageToSend)
        except openai.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")

# Run the bot with your Discord token
client.run(os.getenv("SECRET_KEY"))
