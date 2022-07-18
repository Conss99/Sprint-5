schema = {
    "type": "object",
    "properties": {
        "numero": {"type": "number"},
        "nombre": {"type": "string"},
        "apellido": {"type": "string"},
        "dni": {"type": "string"},
        "tipo": {"enum": ["BLACK", "CLASSIC", "GOLD"]},
        "direccion": {
            "type": "object",
            "properties": {
                "calle": {"type": "string"},
                "numero": {"type": "string"},
                "ciudad": {"type": "string"},
                "provincia": {"type": "string"},
                "pais": {"type": "string"},
            },
            "transacciones": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "estado": {"enum": ["ACEPTADA", "RECHAZADA"]},
                        "tipo": {"enum": ["RETIRO_EFECTIVO_CAJERO_AUTOMATICO", "ALTA_TARJETA_CREDITO", "ALTA_CHEQUERA",
                                          "COMPRAR_DOLAR", "TRANSFERENCIA_ENVIADA", "TRANSFERENCIA_RECIBIDA"]},
                        "cuentaNumero": {"type": "number"},
                        "cupoDiarioRestante": {"type": "number"},
                        "cantidadExtraccionesHechas": {"type": "number"},
                        "monto": {"type": "number"},
                        "fecha": {"type": "string"},
                        "numero": {"type": "number"},
                        "saldoEnCuenta": {"type": "number"},
                        "totalTarjetasDeCreditoActualmente": {"type": "number"},
                        "totalChequerasActualmente": {"type": "number"},
                    },
                }

            },
        },
    },
}
