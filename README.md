# ¡Dale a Chat Gpt tu voz y observa cómo cobra vida este asistente personal!


![photo](840_560.jpg)
 
ChatGpt es un servicio de OpenIA que le brinda el poder de la inteligencia artificial para crear fácilmente un bot asistente personal que se encargará de cualquier tarea que se le presente!
 
Quería crear algo que realmente entusiasmara a todos, los inspirara, les hiciera la vida más fácil y los hiciera sonreír. Así que he decidido dotar a ChatGpt de superpoderes. por lo que le agregue una capa que utiliza reconocimiento de voz para comunicarse con humanos. Como si estuviera hablando con Jarvis de Iron Man.
 
### Nota:
El script no es perfecto por lo que si no hablas en un periodo de tiempo python lanza una excepción cerrando en programa

**Verifica que tu microfono este encendido**

## Ejemplo de Uso 🤖

![photo2](https://media.tenor.com/WdMAHbF-yVYAAAAM/think-about-it-reece-simpson.gif)

[ejemplos de preguntas y respuesta](https://edwight-delgado.github.io/ChatGpt-speech-recognition-/example/)

 
## Información importante: 
use la libreria [PyChatGPT](https://github.com/rawandahmad698/PyChatGPT). Es un cliente no oficial ChatGpt que genera un token de autenticación de OpenIA

También me inspiré en el video de [AVM](https://www.youtube.com/watch?v=8WKjX0dbh4E). El explica como hacer un asistente virtual basico por comandos de voz

## 🎁 Recursos:
 
### descarga el repositorio
```bash
    git clone https://github.com/edwight-delgado/ChatGpt-speech-recognition-.git
```
 
### crea un entorno virtual
```bash
    python3 -m venv venv
 ```
### activa el entorno
```bash
    source  venv/bin/activate.fish
 ```

### instalar toda las librerías necesarias
 
Para Ubuntu:
```bash
    sudo apt install portaudio19-dev python3-pyaudio ffmpeg espeak
 ```
```bash
    pip install -r requirements.txt
```

### configuración
Cambia el nombre del archivo .env.example por .env
y sustituye el email y password por defecto con los proporcionados en la cuenta de openIA

## cómo ejecutar el script
Ejecuta `chatgpt.py` y espere 2 segundos antes de iniciar la conversación. 
Por defecto el idioma esta en Español. Para cambiarlo a 
inglés solo cambia el parámetro lang=’es’ a lang=’en’

```bash
    python chatgpt.py
```

