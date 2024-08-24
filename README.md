# Criando um Chatbot com a API do Google Gemini

# Considerações:
* Segurança: Não compartilhar sua API Key publicamente.

## Tecnologias utilizadas: Google Colab, Google Gemini API, Python.

## Pré-requisitos:
* Conta Google: É necessário ter uma conta Google para utilizar o Google Colab e a API do Google Gemini.
* Conhecimento básico de Python: Entender conceitos básicos de programação em Python.
* Acesso ao Google Colab: Saber como utilizar a plataforma Google Colab.

## Importa as bibliotecas necessárias
* import google.generativeai as genai
* from google.colab import userdata

## Obtém a API Key do usuário
* GOOGLE_GEMINI_API_KEY = userdata.get('GOOGLE_GEMINI_API_KEY')
* genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

## Lista os modelos disponíveis
### for m in genai.list_models():
 ### if 'generateContent' in m.supported_generation_methods:
 ##  print(m.name)

## Escolhe um modelo (ex: Gemini 1.5 Pro)
### model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

## Inicia um chat e cria um loop de conversação
### chat = model.start_chat(history=[])

### while True:
      prompt = input("Você: ")
      if prompt.lower() == 'sair':
        break
      response = chat.send_message(prompt)
      print("Chatbot:", response.text)
