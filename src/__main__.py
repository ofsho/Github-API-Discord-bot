import discord
from ghapi.all import GhApi
api = GhApi()
import sys

from commands import client

client.run(sys.argv[1])