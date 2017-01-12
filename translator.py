#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:06:56 2017

@author: soren
"""

from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

language_translator = LanguageTranslator(
    username='d85d616c-fd18-47b7-914f-2f7b701c5b81',
    password='q1CN4N6Wkydm')

input_str = input("Enter a string:")
while(input_str):
    language = language_translator.identify(input_str)
    predicted_language = language['languages'][0]['language']
    if(predicted_language == 'en'):
        print("This is English, I speak English")
    else:
        print("This is " + predicted_language)
        translation = language_translator.translate(
                                                    text=input_str,
                                                    source=predicted_language,
                                                    target='en')
        print(translation)
    input_str = input("Enter a string:")