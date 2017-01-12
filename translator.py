#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:06:56 2017

@author: soren
"""
import json
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

#%%
language_translator = LanguageTranslator(
    username='d85d616c-fd18-47b7-914f-2f7b701c5b81',
    password='q1CN4N6Wkydm')
#%%
text_to_speech = TextToSpeechV1(
    username='ca31b7e7-7e8c-437b-9678-6cdeea6b18d7',
    password='AkzcUaUFERup',
    x_watson_learning_opt_out=True) 
#%%
#print(json.dumps(text_to_speech.voices(), indent=2))
#%%
voice_db = {'en': 'en-US_AllisonVoice', 'es': 'es-ES_LauraVoice', 'fr':'fr-FR_ReneeVoice'}
lang_db = {'en': 'English', 'es': 'Spanish', 'fr':'French' }
#%%
input_str = input("Enter a string to be translated:")
language = language_translator.identify(input_str)
pred_lang = language['languages'][0]['language']
text1 = ''
text2 = ''
if(pred_lang == 'en'):
    text1 = input_str
    text2 = ' is already English.'
else:
    text1 = input_str
    translation = language_translator.translate(
                                                text=input_str,
                                                source=pred_lang,
                                                target='en')
    text2 = ' is ' + lang_db[pred_lang] + '. In english this would be - ' + translation
    
#%%

with open(join(dirname(__file__), 'output.wav'),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(text1, accept='audio/wav',
                                  voice=voice_db[pred_lang]))
    audio_file.write(
        text_to_speech.synthesize(text2, accept='audio/wav',
                                  voice= 'en-US_MichaelVoice' ))
    
print("The output was successfully written to output.wav")

"""
Un hombre va al circo en busca de empleo.
El director le pregunta: Y usted qué sabe hacer?
El director responde, bueno... creo que no nos interesa, gracias.
... y el hombre se fue volando.
"""