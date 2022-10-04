from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/envia", methods=['GET','POST'])
def envia():
  dados = request.json
  #variavel = request.form['variavel']
  with open("dados.csv","a") as arquivo :
    arquivo.write("01"+","+str(dados["valor"])+'\n')
    arquivo.close
    return dados

@app.route("/busca", methods=['GET'])
def busca():
  df = pd.read_csv("dados.csv")
  tam = len(df.index)
  return {"Dados": tam}
  
# rodar a api
app.run(host='0.0.0.0')