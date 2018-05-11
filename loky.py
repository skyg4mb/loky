import hashlib
import sys
from os import walk


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
	LOKY - 11.05.18 - Diego A. Gamboa (skyg4mb)
------------------------------------------------------------------------------
"""

version = 1.0
directory_a = ""
directory_b = ""
files = {}

def main():
	banner()
	global directory_a 
	directory_a = raw_input("Ingrese directorio original: ")
	global directory_b 
	directory_b = raw_input("Ingrese directorio secundario: ")
	global files
	filesDir1 = ls(directory_a)
	files = {}
	filesDir2 = ls(directory_b)
	files = {}
	compareDirs(filesDir1, filesDir2)

def banner():

	global version
	b = '''
	 _        ______   _    __ __    _  
	| |      / |  | \ | |  / / \ \  | | 
	| |   _  | |  | | | |-< <   \_\_| | 
	|_|__|_| \_|__|_/ |_|  \_\  ____|_| 
                                  

	version {v} - Looking for something
	  made by Diego A Gamboa (skyg4mb)                                  
 	'''.format(v=version)
 	print(b)

def sha2256_checksum(filename, block_size=65536):
	try:
		sha256 = hashlib.sha256()
		with open(filename, 'rb') as f:
    			for block in iter(lambda: f.read(block_size), b''):
    				sha256.update(block)
			return sha256.hexdigest()
	except Exception as e:
		pass
	else:
		pass
	finally:
		pass

def compareDirs(dirOne, dirTwo):
	lost_files = 0
	new_files = 0
	mov_files = 0
	mod_files = 0
	flag = 0
	file_lost = "DeleteFiles.txt"
	file_new = "CreatedFiles.txt"
	file_mov = "MovFiles.txt"
	file_mod = "ModifiedFiles.txt"
	search_file = ""


	for key in dirOne:
		if key in dirTwo:
			if dirOne[key] == str(dirTwo[key]).replace(directory_b, directory_a):
				None
			else:
				mov_files += 1
				with open(file_mov, 'a') as file:
    					file.write(key + ";" + str(dirOne[key]) + "\n")
				
				#print("Se encontro el archivo %s pero su nombre fue modificado o movido de directorio" %(dirOne[key]))
		else:
			search_file = str(dirOne[key]).replace(directory_a, directory_b)
			for v in dirTwo.values():
				if search_file == v:
					mod_files += 1
					with open(file_mod, 'a') as file:
    						file.write(key + ";" + str(dirOne[key]) + "\n")
					flag = 1
					break
			if flag == 0:
				lost_files += 1
				with open(file_lost, 'a') as file:
    						file.write(key + ";" + str(dirOne[key]) + "\n")

			flag = 0


	for key in dirTwo:

		if key not in dirOne:
			search_file = str(dirTwo[key]).replace(directory_b, directory_a)
			for v in dirOne.values():
				if search_file == v:
					mod_files += 1
					with open(file_mod, 'a') as file:
   						file.write(key + ";" + str(dirTwo[key]) + "\n")
    				break
    		
    			if search_file not in dirOne.values():
    				new_files += 1
    				with open(file_new, 'a') as file:
    					file.write(key + ";" + str(dirTwo[key]) + "\n")


		
	print("Se movieron o renombraron %s archivos" % mov_files)
	print("Se eliminaron %s archivos" % lost_files)
	print("Se modificaron %s archivos" % mod_files)
	print("Se crearon %s archivos" % new_files)



def ls(ruta):
    dir, subdirs, archivos = next(walk(ruta))
    global files
    for archivo in archivos:
    	files[sha2256_checksum(ruta+archivo)] = ruta + archivo
    for directory in subdirs:
    	#ls(ruta+directory)
    	ls(ruta+directory+"/")

    return files

if __name__ == '__main__':
	main()

