# Batcueva Lambda

Lista de gastos fijos para el sistema de recordatorios automático de la batcueva

```
.
├── LICENSE
├── README.md
└── lambdas
    ├── lambda_calendario
    │   ├── README.md
    │   ├── lambda_function.py
    │   ├── murci.py
    │   └── requirements.txt
    ├── lambda_gastos
    │   ├── README.md
    │   ├── config.json
    │   ├── lambda_function.py
    │   ├── murci.py
    │   └── requirements.txt
    └── lambda_noticias
        ├── README.md
        ├── lambda_function.py
        ├── murci.py
        └── requirements.txt
```
---

## Scripts disponibles

Descripción


### Labmda gastos

Función para analizar un archivo de gastos fijos comunes y enviar un **resumen mensual de los gastos** a través de Telegram.

[:arrow_forward: Ver documentación de esta lambda](./lambdas/lambda_gastos/README.md)


### Labmda gastos semanal

Función para analizar un archivo de gastos fijos comunes y enviar un **resumen semanal de los gastos** a través de Telegram.

[:arrow_forward: Ver documentación de esta lambda](./lambdas/lambda_gastos_semanal/README.md)


### Lambda calendario

Descripción

[:arrow_forward: Ver documentación de esta lambda](./lambdas/lambda_gcalendar/README.md)


### Lambda noticias

Función para recoger noticias basadas en nuestros intereses y enviar un resumen cada dos días de las últimas 48 horas a través de Telegram.

[:arrow_forward: Ver documentación de esta lambda](./lambdas/lambda_noticias/README.md)
