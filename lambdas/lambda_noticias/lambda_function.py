#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Project: lambda_noticias
# Author/s: charlstown
# -----------------------------------------------------

# Libraries
import json
from newsdataapi import NewsDataApiClient
from murci import Murci

# Import classes
from news_api import NewsAPI

# Main code
def lambda_handler(event, context):

    print("Iniciando Lambda para la publicación de noticias")

    # Instanciate classes
    news_api = NewsAPI()
    murci = Murci()
    
    # request news
    news = news_api.get_news()
    print(news)
    print('------\n')

    # Generate message
    message = "Hola amiguis os traigo el resumen de noticias de las últimas 48h:\n"

    category = ""
    for item in news:
        if item['category'] != category:
            message += "\n────\n"
            message += f"__SOBRE {item['category']}__\n".upper()

        message += f"- {item['title']:}\n"

        message += f"_Fecha de publicación: {item['date']}_\n"

        f_link = item['link'].replace('_', '\_')

        message += f"[📰 Leer la noticia]({f_link})\n"

        category = item['category']


    print(message)
    murci.send_message(message)
    


    
    #print(sources)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    # Local test
    lambda_handler(None, None)