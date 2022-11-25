from google.cloud.bigquery import table
from google.cloud import bigquery
from google.oauth2 import service_account
import os
import json

credentials_path = 'Project/asesoriasonline-ead83ac573f6.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=credentials_path

client=bigquery.Client()
table_asesor_id='asesoriasonline.asesorias_online.asesor'
table_documentos_id='asesoriasonline.asesorias_online.documentos'
table_usuario_id='asesoriasonline.asesorias_online.usuario'
table_candidato_asesor_id='asesoriasonline.asesorias_online.candidatos_asesores'

def agregar_documento(materia, titulo, archivo):
    archivo=[{u'materia':materia, u'titulo':titulo, u'archivo':archivo}]
    error = client.insert_rows_json(table_documentos_id, archivo)
    if error==[]:
        resp = True
    else:
        resp = False
    return resp
    
def agregar_usuario(nombre,apellido,correo,contra):
  usuario=[{ u'nombre':nombre, u'apellido':apellido, u'correo':correo, u'contrasena':contra}]
  error=client.insert_rows_json(table_usuario_id,usuario)
  if error==[]:
    resp=True
  else:
    resp=False
  return resp

def agregar_candidato_asesor(materia, nombre, apellido, clave_unica, telefono, correo, precio):
  usuario=[{u'materia':materia, u'nombre':nombre, u'apellido':apellido, u'clave_unica':clave_unica,u'telefono':telefono,u'correo':correo, u'precio':precio}]
  error=client.insert_rows_json(table_candidato_asesor_id,usuario)
  if error==[]:
    resp=True
  else:
    resp=False
  return resp

def agregar_asesor(materia, nombre, apellido, clave_unica, telefono, correo, precio):
  usuario=[{u'materia':materia, u'nombre':nombre, u'apellido':apellido, u'clave_unica':clave_unica,u'telefono':telefono,u'correo':correo, u'precio':precio}]
  error=client.insert_rows_json(table_asesor_id,usuario)
  if error==[]:
    resp=True
  else:
    resp=False
  return resp

def validar_correo_contraseña(correo, contraseña):
    query= """ select correo, contrasena from `asesorias_online.usuario` where correo="{}" and contrasena="{}" """.format(correo,contraseña)
    docs=client.query(query)
    results = docs.result()
    correo_resultado =""
    contraseña_resultado=""

    for i in results:
        correo_resultado = i[0]
        contraseña_resultado = i[1]
    
    if correo == correo_resultado and contraseña == contraseña_resultado:
        res = True
    else:
        res = False 
    
    return res

def extraer_asesores(materia):
  query= """ select * from `asesoriasonline.asesorias_online.candidatos_asesores` """
  docs=client.query(query)
  records = [dict(row) for row in docs]
  list = []
  
  for i in range(len(records)):
    if records[i]['materia'] == materia:
      list.append(records[i])
  
  print(list)
  return list

def extraer_materiales(materia):
  query= """ select * from `asesoriasonline.asesorias_online.documentos` """
  docs=client.query(query)
  records = [dict(row) for row in docs]
  list = []
  
  for i in range(len(records)):
    if records[i]['materia'] == materia:
      list.append(records[i])
  
  print(list)
  return list

#extraer_asesores("CALCULO ACTUARIAL 1")

#resp1 = agregar_usuario('Israel','Cabrera','cabreraportillaisrael@gmail.com','Israel2069231')
#print(resp1)
#resp = validar_correo_contraseña("cabreraportillaisrael@gmail.com","Israel2069231")
#print(resp)