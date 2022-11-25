from flask import Flask, Blueprint, render_template, request, url_for, current_app, flash
from flask_login import login_required, current_user
import requests
import gspread 
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from pprint import pprint
from datetime import datetime
import re
from gspread.exceptions import WorksheetNotFound
from gspread.utils import finditem
from gspread.models import Worksheet
from gspread.exceptions import APIError
import requests
import time
import traceback
import csv
from ..conexion import *

# CODE
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


#---- Leyendo datos del csv ------ 
filename = open('Project/materias_itam.csv', 'r')
file = csv.DictReader(filename)
materias = []
for col in file:
    materias.append(col["Materias"])
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# FLASK
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
autoBook = Blueprint('buscarDocumentos', __name__, template_folder='templates/autoBook', static_folder='static/autoBook')

@autoBook.route('/', methods=['POST','GET'])
@login_required
def autobook():
    
  documento = []  
  materia = str(request.form.get("materias"))
  if request.method == 'POST':
   
    print(materia)

    documento = extraer_materiales(materia)

  return render_template('autobook.html', materias=materias, documentos=documento)

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-


