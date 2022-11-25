from flask import Flask, Blueprint, render_template, request, url_for, current_app, flash
from flask_login import login_required, current_user
import pprint
import gspread
from datetime import date, datetime,timedelta
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import csv
from ..conexion import *
# CODE
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

filename = open('Project/materias_itam.csv', 'r')
file = csv.DictReader(filename)
materias = []
for col in file:
    materias.append(col["Materias"])

Booking = Blueprint('quieroSerAsesor', __name__, template_folder='templates/Booking', static_folder='static/Booking')

@Booking.route('/',methods=['POST','GET'])
@login_required
def booking():
  materia = request.form.get("materias")
  nombre=request.form.get("nombre")
  apellido = request.form.get("apellido")
  clave_unica = request.form.get("cu")
  telefono = request.form.get("telefono")
  correo = request.form.get("correo")
  precio = request.form.get("tarifa")
  
  if request.method=="POST":
  
    print(nombre, apellido,clave_unica, materia, telefono, correo, precio)
    agregar_candidato_asesor(materia,nombre,apellido,clave_unica,telefono,correo,precio)
    
  return render_template('booking.html', materias = materias)
