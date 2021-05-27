# Python Keylogger

Este script en Python es un keylogger que envía a un chat de Telegram todo lo que se escribe por teclado.

## Configuración

Es necesaria la creación de un fichero **config.py** con los siguientes datos:

```
TELEGRAM_TOKEN = "AAAA"
TELEGRAM_GROUP_ID = 12345
REPORT_EVERY = 20
```

### Aclaración

Descripción de cada parámetro de la configuración:

- TELEGRAM_TOKEN --> Token del bot telegram
- TELEGRAM_GROUP_ID --> Token del chat/grupo al que quieres mandar mensajes.
- REPORT_EVERY --> Cada cuanto tiempo envía reporte a Telegram

## Uso
Build docker image:
```
docker image build -t py_keylogger .
```

Using docker:
```
docker container run --rm -it py_keylogger
```