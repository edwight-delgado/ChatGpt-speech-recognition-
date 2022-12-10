from record import SpeechRecognizer
from speak import Talk
from pychatgpt import Chat
from dotenv import dotenv_values,load_dotenv
import csv
from datetime import datetime
import os.path

def main(lang='es'):
    current_dateTime = datetime.now()
    check = load_dotenv('.env')
    if check == True:
        env = dotenv_values(".env")
    else:
        print('no se encuentra archivo el .env')

    chat = Chat(email=env["EMAIL"], password=env["PASSWORD"])
    answer = chat.ask("hola me podrias ayudar ?")
    print(answer)

    listen = SpeechRecognizer(lang=lang)

    speak = Talk(lang)
    speak.speak(answer)

    # nombre de los campos
    fields = ['human', 'ChatGpt', 'datetime']

    file_exists = os.path.exists('dialogue.csv')
    if file_exists:
        with open('dialogue.csv', 'a') as f:
            write = csv.writer(f)
            while True:
                print("Say something!")
                message = listen.listen()
                print(f"Recognized: {message}")
                answer = chat.ask(message)

                speak.speak(answer)
                row = [message,answer,current_dateTime]
                write.writerow(row)
    else:
        with open('dialogue.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(fields)

if __name__ == "__main__":
    main(lang='es')