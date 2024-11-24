#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Project: lambda_gastos
# Author/s: charlstown
# -----------------------------------------------------
import os
import telebot

class Murci:
    """
    Class to run the different actions from the bot
    """
    def __init__(self):
        """
        Constructor from Murci class to initialize the global and shared variables
        """
        
        # Global vars
        self.token = os.environ.get('BOT_TOKEN')
        self.chat_id = os.environ.get('CHAT_ID')
    
    
    def send_message(self, message: str):
        """
        Function to send messages to the telegram bot
        
        :param message: string with the message you want to send
        :return: None
        """
        
        bot = telebot.TeleBot(token=self.token)
        
        bot.send_message(chat_id=self.chat_id, text=message, parse_mode='MARKDOWN')