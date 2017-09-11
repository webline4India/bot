import sys
import time
import telepot
from telepot.loop import MessageLoop
# import splinter
import os
import sys


class BotFunction(object):

    def __init__(self, command):
        self.command = command
        self.command_list = [
            '/start',
            '/createevent',
            '/mergeevent',
            '/quit'
        ]

    def isValidFunction(self, command):
        return command in self.command_list

    def executeCommand(self, command):
        if self.isValidFunction():
            if command == '/start':
                bot.sendMessage(chat_id, "Beep. You can start chatting with me now, or ask me to do stuff. :)")
        else:
            bot.sendMessage(chat_id, 'Command not found!')