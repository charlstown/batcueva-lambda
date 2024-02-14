#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------

# Libraries
import yaml
from newsdataapi import NewsDataApiClient
import time

# Code
class NewsAPI:
    """_summary_
    """
    def __init__(self) -> None:
        """_summary_
        """
        # Global vars
        self.api = NewsDataApiClient(apikey="pub_38105c6a8f6f914b499927ebf5f16ff8168a9")
        self.config_news = self.read_config_file()
        self.n_news = self.config_news['noticias_por_categoria']

    def get_news(self):
        """_summary_

        :return: _description_
        """
        news_results = list()
        for noticia in self.config_news['noticias']:
            news_type = noticia['name']
            news_category = self.format_category(noticia['category'])
            news_keywords = self.format_words(noticia['keywords'])

            news_results += self.request_news(api=self.api,
                                              type = news_type,
                                              n_news=self.n_news,
                                              filter=news_category,
                                              keywords=news_keywords)
            time.sleep(0.5)
        return news_results
            

    def request_news(self, api, type: str, n_news: int, filter: str, keywords: str):
        """_summary_

        :param api: _description_
        :param type: _description_
        :param n_news: _description_
        :param filter: _description_
        :param keywords: _description_
        :return: _description_
        """
        # Request news with configuration
        response = api.news_api(
            size=10,
            q=keywords,
            category=filter,
            country='es',
            language='es')
        if response['status'] == "success":
            print(f"Successfully extracted {response['totalResults']} news for {type}.")
        
        # Get results
        results = response['results']
        if len(results) == 0:
            return list()

        # Get main info
        main_info = list()
        check_duplicates = []
        for result in results:
            # Check number of news
            if len(main_info) == n_news:
                break

            # check duplicates
            if result['title'] in check_duplicates:
                continue
            else:
                check_duplicates.append(result['title'])

            # Add news
            final_result = dict()
            final_result['category'] = type
            final_result['title'] = result['title']
            final_result['description'] = result['description'][:150] + "..."
            final_result['date'] = result['pubDate'].split()[0]
            final_result['link'] = result['link']
            main_info.append(final_result)

        return main_info

    @staticmethod
    def read_config_file(file_name:str = 'config.yml'):
        """_summary_

        :param file_name: _description_, defaults to 'config.yml'
        :return: _description_
        """
        with open(file_name, 'r') as file:
            parameters = yaml.safe_load(file)
        return parameters
    
    @staticmethod
    def format_category(categories):
        f_categories = ','.join(categories)
        return f_categories

    @staticmethod
    def format_words(words):
        f_string = ' OR '.join(words)
        return f_string