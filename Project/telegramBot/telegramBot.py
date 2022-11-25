from flask import Flask, Blueprint, render_template, request, url_for, current_app
from flask_login import login_required, current_user
import pandas as pd
import requests
from urllib.request import urlopen
import os
from datetime import datetime
import time
import gspread
from werkzeug import *
import gspread 
from gspread.exceptions import WorksheetNotFound
from gspread.utils import finditem
from gspread.models import Worksheet
from gspread.exceptions import APIError
from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import bigquery
from google.oauth2 import service_account
from googleapiclient.http import *
import os
import pandas as pd
from googleapiclient.discovery import build
import csv
from ..google_cloud import *
from ..conexion import * 

#UPLOAD_FOLDER = "Project/telegramBot/static/telegramBot"
#uploadDocument = Blueprint('uploadDocument', __name__, template_folder='templates/uploadDocument',)

#current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPLOAD_FOLDER = "Project/telegramBot/static/telegramBot"
telegramBot = Blueprint('subirDocumento', __name__, template_folder='templates/telegramBot', static_folder='static/telegramBot')

current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
@telegramBot.route('/', methods=["GET", "POST"])
@login_required
def subir_documentos():
    #---- Leyendo datos del csv ------ 
    filename = open('Project/materias_itam.csv', 'r')
    file = csv.DictReader(filename)
    materias = []
    for col in file:
        materias.append(col["Materias"])

    if request.method == 'POST':
        materia = str(request.form.get("materias"))
        titulo = str(request.form.get("titulo"))
        print(materia)
        print(titulo)
        
        
        if request.files['file1']:
            
            #Se hace el request en caso de que el usuario haya subido un documento 
            f = request.files['file1']
            print(f)
            filename = f.filename
            f.save(filename) 
            
            response = upload_to_bucket(titulo, filename , 'bucket-docs-ing-software')
            print(response)
            
            url = 'https://storage.cloud.google.com/{}/{}'.format('bucket-docs-ing-software', titulo)
            
            agregar_documento(materia,titulo,url)
  
            print("subi el archivo perrote")
            
    return render_template('telegram_bot.html', materias = materias)

