# Sprint-5

  El archivo segmentacion_clientes.py hay que ejecutarlo desde una termina ly trabaja con 2 argumentos, el primero como habitualmente es seria el nombre del .py y el segundo el nombre del json, ej. segmentacion_clientes.py eventos_black.json.

  Requerimientos:
- Python 3.9.x
- Modulos a importar: json, msilib, sys, jsonschema

## Como importar los modulos:
Desde la terminar escribir los siguientes comandos:
python -m venv env
python -m pip install [nombre_modulo]

Nota sobre el diagrama de clases:
-Eliminamos las clases: cuenta, classic, gold, black y razon. A continuacion el porque.
  -Cuenta. la vimos innecesaria porque no se realizaba ninguna accion con la misma.
  -Classic, Gold, Black: Se entiende por como se planteo la problematica a resolver que el json solo traeria la informacion de un cliente y por lo tanto se tendra que correr el programa por cada reporte, al solo trabajar con un cliente la herencia estaria de mas, por lo tanto solo trabajamos con la clase Cliente.
  -Razon: Agregamos una clase transaccion donde se guardara cada transaccion, al mismo tiempo esta problematica de añadir una razon la resolvimos con un metodo en la clase Cliente que añadira la razon a la transaccion dependiendo unas validaciones.
  

 
