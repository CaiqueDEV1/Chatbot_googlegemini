# -*- coding: utf-8 -*-
"""UtilizandoGoogleGEMINICHATBOT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CniBDSvuJOiaCQkTJV9_A-Py3ayWXolp
"""

!pip install google-generativeai

import google.generativeai as genai

from google.colab import userdata

GOOGLE_GEMINI_API_KEY = userdata.get('GOOGLE_GEMINI_API_KEY')

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

response = model.generate_content('Você é muito inteligente')
response.text

chat = model.start_chat(history=[])

prompt = input('Esperando prompt: ')

while prompt != 'fim':
  response = chat.send_message(prompt)
  print(response.text)
  prompt = input('Esperando prompt: ')