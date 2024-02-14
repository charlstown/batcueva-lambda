# Lambda gastos

Este proyecto utiliza una función Lambda en AWS para analizar un archivo de gastos fijos comunes y enviar un **resumen mensual de los gastos** a través de Telegram. Automatiza el proceso de seguimiento de gastos y facilita la gestión financiera.


## 1. Estructura de archivos

La estructura de archivos incluye un archivo principal llamado **lambda_function.py**, que contiene el código al que llama AWS cuando se levanta la función Lambda.

```
.
├── README.md           # Documentación de la lambda
├── config.json         # Fichero con los gastos fijos a procesar
├── lambda_function.py  # Fichero principal para la ejecución
├── murci.py            # Clase para enviar mensajes a telegram
└── requirements.txt    # Librerías necesarias para ejecutar el código
```


## 2. Configuración

Puedes añadir nuevos gastos al fichero de configuración config.json siguiendo el formato proporcionado. Simplemente agrega una nueva entrada con el nombre del gasto, el importe, y la frecuencia de pago en formato cron.

```
{
    "gasto_luz": {
        "nombre": "Nombre",
        "importe": xx,
        "frecuencia": "* * * * *"
    },
    ...
}
```

- nombre: Es el nombre descriptivo del gasto. Debe ser una cadena de texto que identifique de manera clara y concisa el tipo de gasto.

- importe: Representa el valor numérico del gasto. Se refiere a la cantidad de dinero que se destina al gasto especificado.

- frecuencia: Especifica la frecuencia con la que se realiza el pago del gasto. Se utiliza el formato cron unix para definir esta frecuencia.


## 3. Ejecución en local

- Instala las librerías necesarias
```
pip install -r requirements.txt
```

- Añade los siguientes secretos a las variables de tu entorno de desarrollo

```
export BOT_TOKEN="add-secret"
export CHAT_ID="add-secret"
```

- Ejecuta el código llamando al archivo 'lambda_function.py'
```
python lambda_function.py
```
