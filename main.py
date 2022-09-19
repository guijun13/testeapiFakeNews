import pandas as pd
import json
import flask
from flask import Flask, request,jsonify, render_template
from flask_cors import CORS
import os
import pickle
import newspaper
from newspaper import Article
import urllib
import nltk

  
#Loading Flask and assigning the model variable
app = Flask(__name__)
CORS(app)

app=flask.Flask(__name__,template_folder='templates')


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/text')
def text():
   text= pd.read_csv('preprocessed05.csv')
   text_fake = text_falso['label'].sum()
   text_true = text_verdadeiro['label'].sum()
   resposta = {'text_verdadeiro': text_verdadeiro}
   resposta = {'text_falso': text_falso}
   return jsonify (resposta)
      

#Receiving the input text from the user
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        keywords= ['coronavirus','covid','covid19','virus','vacina','variola do macaco','guerra','COVID19','COVID-19',
        'ucrânia','eleições','variola','eleições 2022','pandemia','rússia','Covid', 'lava jato', 'Moro', 'Lula', 'Bolsonaro', 'Simonte Tebet', 'Ciro', 'Espionagem', 'Espião', 'Fome', 'Agronegócio', 'Meio Ambiente','Democracia', 'Politica', 'EUA','Energia', 'Europa', 'Brasil']
        keywords = request.get_data(as_text=True)[8:]
        keywords = urllib.parse.unquote(keywords)
  
       
        text=Article(str(url),language="pt")
        text.download()
        text.parse()
                #nltk.download('punkt')
        text.nlp()
        a = text.title
        title=""
        count=0
        for i in a:
          if(i.isspace()):
              count=count+1
          if count==9:
                  break
          else:
                title+=i
                print(title)
                b = text.keywords
                print(b)
                c = text.text
                print(c)
                summary=text.summary
                if any(x in b for x in keywords):
                    print(summary)
                    # Predicting the input
                    pred = model.predict([summary])
                    return render_template('pred.text', prediction_text='Esse texto é {}.'.format(pred[0]), title=title,text=c,leno=len(c),active=1, keywords=b,summary=summary, lenk=len(keywords))
                for prediction_text in text:
                  if prediction_text ('Falso'):
                    print("Texto com conteúdo falso")
                    return render_template('pred.text', message='Falso', activ
            else prediction_text in text_true:
              elif text ('Verdadeiro'):
                    print("Texto com conteúdo verdadeiro")
                    return render_template('pred.text', message='Verdadeiro', active=1)

            elif(len(url) < 100):
                print(url)
                if any(x in url for x in keywords):
                    pred = model.predict([text])
                    return render_template('pred.text', prediction_text='Esse texto é {}.'.format(pred[0]), active=1)
                else:
                    return render_template('pred.text', message='Esse texto não está relacionado. Não encontramos resultados para sua busca', active=1)

            else:
                return render_template('pred.text', message='As informações são insuficientes. Seu texto precisa conter no minimo 100 caracteres', active=1)

        except:
            print("Invalid")
            return render_template('pred.text', text='Texto invalido. Por favor, digite o texto, não cole o endereço da página.', active=1)
    return render_template('pred.text')



    
app.run(host='0.0.0.0')