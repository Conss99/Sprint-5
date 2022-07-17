import json
from msilib.schema import Class
import sys
# import validacion_json
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("paquete"),
    autoescape=select_autoescape()
)

class Direccion:

    def __init__(self,calle,numero,ciudad,provincia,pais ):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self. pais = pais
    
    def __str__(self):
        return '{} {}, {}, {} {}.'.format(self.calle,self.numero,self.ciudad,self.provincia,self.pais)

class Transaccion:
    def __init__(self, estado,tipo_transaccion,cuentaNumero,cupoDiarioRestante,monto,fecha,numero,saldo_en_cuenta,tarjeras_credito,chequeras):
        self.estado = estado
        self.tipo_transaccion=tipo_transaccion
        self.cuenta_Numero= cuentaNumero
        self.cupo_diario_restante= cupoDiarioRestante
        self.monto= monto
        self.fecha= fecha
        self.numero_transaccion = numero
        self.saldo_en_cuenta = saldo_en_cuenta
        self.tarjetas_credito= tarjeras_credito
        self.chequeras = chequeras
        self.razon=''

    def __str__(self):
        return 'Numero: {}   Fecha: {}   Estado: {}   Tipo: {}   Cuenta Numero: {}  \nCupo Diario Restante: {}   Monto: {}   Saldo En Cuenta: {}    \nTotal Tarjetas De Credito Actualmente: {} \nTotal Chequeras Actualmente: {} \nRazon: {}'.format(self.numero_transaccion,self.fecha,self.estado,self.tipo_transaccion,self.cuenta_Numero,self.cupo_diario_restante,self.monto,self.saldo_en_cuenta,self.tarjetas_credito,self.chequeras,self.razon)
    
   
class Cliente:
    def __init__(self,tipo_cliente,numero_Cliente,nombre,apellido,dni,calle,numero,ciudad,provincia,pais):
        self.tipo_cliente = tipo_cliente
        self.numero_Cliente = numero_Cliente
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = Direccion(calle,numero,ciudad,provincia,pais)
        self.transacciones = []

    def __str__(self):
        v = 'Cliente {}  -   Numero de cliente: {}   Nombre y Apellido: {} {}   DNI: {} \nDireccion: {} \n  \n\tTransacciones: '.format(self.tipo_cliente,self.numero_Cliente,self.nombre,self.apellido,self.dni,self.direccion) 
        
        c = 0
        for i in self.transacciones:
            v += '\n\n{}'.format(self.transacciones[c])
            c+=1
        return v



    def puede_crear_chequera(self, cant_chequeras):
        band = False
        if (self.tipo_cliente.lower() == 'gold' and cant_chequeras == 0) or (self.tipo_cliente.lower() == 'black' and cant_chequeras <= 1):
            band = True
        return band

    def puede_crear_tarjeta_credito(self, cant_tarjetas):
        band = False
        if (self.tipo_cliente.lower() == 'gold' and cant_tarjetas == 0) or (self.tipo_cliente.lower() == 'black' and cant_tarjetas<= 4):
            band = True
        return band

    def puede_comprar_dolar(self):
        band = False
        if (self.tipo_cliente.lower() == 'gold' or self.tipo_cliente.lower() == 'black' ):
            band = True
        return band

    def añadir_transacciones(self, una_transaccion):

        if una_transaccion.estado.lower() == 'rechazada':
            if una_transaccion.tipo_transaccion == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                    if self.tipo_cliente.lower() == 'classic':
                        if (una_transaccion.monto > una_transaccion.saldo_en_cuenta):
                            una_transaccion.razon = 'El monto que quiso extraer es mayor que el saldo disponible en la cuenta'
                        elif una_transaccion.monto > una_transaccion.cupo_diario_restante:
                            una_transaccion.razon = 'El monto que quiso extraer es mayor que el cupo diario restante para extraer de la cuenta'
                        else:
                            una_transaccion.razon = 'El monto que quiso extraer es mayor que el cupo diario restante para extraer y el saldo disponible de la cuenta'
                    else:
                        if una_transaccion.saldo_en_cuenta>= -10000:
                            if (una_transaccion.monto > una_transaccion.saldo_en_cuenta):
                                una_transaccion.razon = 'El monto que quiso extraer es mayor que el saldo disponible en la cuenta'
                            elif una_transaccion.monto > una_transaccion.cupo_diario_restante:
                                una_transaccion.razon = 'El monto que quiso extraer es mayor que el cupo diario restante para extraer de la cuenta'
                            else:
                                una_transaccion.razon = 'El monto que quiso extraer es mayor que el cupo diario restante para extraer y el saldo disponible de la cuenta'
            elif una_transaccion.tipo_transaccion == 'ALTA_TARJETA_CREDITO':
                    if self.tipo_cliente.lower() == 'classic':
                        una_transaccion.razon = 'El tipo de cliente no puede tener una tarjeta de credito'
                    else:
                        if not self.puede_crear_tarjeta_credito(una_transaccion.tarjetas_credito):
                            una_transaccion.razon = 'Cantidad maxima de tarjetas de credito posibles'

            elif una_transaccion.tipo_transaccion == 'ALTA_CHEQUERA':
                if self.tipo_cliente.lower() == 'classic':
                        una_transaccion.razon = 'El tipo de cliente no puede tener una chequera'
                else:
                        if not self.puede_crear_chequera(una_transaccion.chequeras):
                            una_transaccion.razon = 'Cantidad maxima de tarjetas de credito posibles'
            elif una_transaccion.tipo_transaccion == 'COMPRA_DOLAR':
                if not self.puede_comprar_dolar():
                        una_transaccion.razon = 'El tipo de cliente no puede comprar dolares'
                
                else:
                        
                        if (una_transaccion.monto > una_transaccion.saldo_en_cuenta):
                            una_transaccion.razon = 'El monto que quiso comprar es mayor que el saldo disponible en la cuenta'
                        elif una_transaccion.monto > una_transaccion.cupo_diario_restante:
                            una_transaccion.razon = 'El monto que quiso comprar es mayor que el cupo diario restante para comprar de la cuenta'
            elif una_transaccion.tipo_transaccion == 'TRANSFERENCIA_ENVIADA':
                if self.tipo_cliente.lower() == 'black':
                    una_transaccion.razon = 'El monto de la transferencia supera el monto disponible en la cuenta' 
                else:
                    una_transaccion.razon = 'El monto de la transferencia supera o iguala el monto disponible en la cuenta por lo tanto no puede pagar la comision por transaccion'
            elif una_transaccion.tipo_transaccion == 'TRANSFERENCIA_RECIBIDA':
                una_transaccion.razon = 'La transferencia supera el monto de transferencia recibida sin autorizacion previa'
                  
                  
        self.transacciones.append(una_transaccion)


argumen = sys.argv

# validacion_json.json_validator(argumen[1])

with open(argumen[1], 'r') as j:
     contents = json.loads(j.read())

template = env.get_template("template.html")
with open('reporte.html', 'w') as file:
    file.write(template.render())

direccion = contents['direccion']

cliente = Cliente(contents['tipo'],contents['numero'],contents['nombre'],contents['apellido'],contents['dni'],direccion['calle'],direccion['numero'],direccion['ciudad'],direccion['provincia'],direccion['pais'])

for i in contents['transacciones']:
    v = Transaccion(i['estado'],i['tipo'],i['cuentaNumero'],i['cupoDiarioRestante'],i['monto'],i['fecha'],i['numero'],i['saldoEnCuenta'],i['totalTarjetasDeCreditoActualmente'],i['totalChequerasActualmente'])
    cliente.añadir_transacciones(v)


