import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from main import client


async def body(message):
    advice = random.randint(0, 6)
    if (advice == 0):
        await client.send_message(message.channel, "Depends, do you have fava beans?")
    if (advice == 1):
        await client.send_message(message.channel, "Bathtub, Sulfuric acid, or lye, read a book, done.")
    if (advice == 2):
        await client.send_message(message.channel, "Oil Field")
    if (advice == 3):
        await client.send_message(message.channel, "*sigh* I'll take care of it....")
    if (advice == 4):
        await client.send_message(message.channel, "Why hide what's useful? Frame the butler. Or the Ex.")
    if (advice == 5):
        await client.send_message(message.channel, "Dumpster.")
    if (advice == 6):
        await client.send_message(message.channel, "Fire. See Michael.")