from flask import Flask, Blueprint, render_template, request, url_for, current_app, flash
from flask_login import login_required, current_user
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
pd.options.mode.chained_assignment = None
import csv
from ..conexion import *

# FLASK
filename = open('Project/materias_itam.csv', 'r')
file = csv.DictReader(filename)
materias = []
for col in file:
    materias.append(col["Materias"])


userPnL = Blueprint('buscarAsesorias', __name__, template_folder='templates/userPnL', static_folder='static/userPnL')

@userPnL.route('/',methods=['POST','GET'])
@login_required
def user_PnL():
    
    list = []    
    materia = request.form.get("materias")
    
    if request.method=="POST":
        list = extraer_asesores(materia)
    
    return render_template('user_pnl.html', materias = materias, informacion=list)


