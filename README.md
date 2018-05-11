# Loky

En algunos momentos necesitamos verificar modificaciones sobre directorios muy extensos que no disponen de una herramienta de seguimiento y control de cambios.

Loky es un herramienta que permite verificar comparar dos directorios recursivamente, el primer directorio antes del compromiso de informacion (Regularmente un backup) y el directorio actual o despues del compromiso en la informacion.

# Como funciona? 

Loky lista recursivamente todos los archivos que contienen los dos directorios, posteriormente calcula el hash en sha256 para cada uno de los archivos y crea diccionarios para cada directorio. Una vez tiene los diccionarios realiza la comparacion archivo a archivo verificando cuales fueron eliminados, cuales modificados, cuales creados y cuales renombrados o movidos.

Finalmente loky crea cuatro archivos de texto que contienen la informacion de todos los documentos modificados.

