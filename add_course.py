import base64
import uuid
from gtts import gTTS
from sqlalchemy import create_engine
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from sys import path
LANG = {
    1 : 'id',
    2 : 'en'
}
USERNAME = 'root'
PASSWORD = '100300'
URL = 'localhost'
DB = 'flexy'
def pick_module_text_file(language):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    with open(filename, 'rt') as text_file:
        text = text_file.read()
        speech_from_text = gTTS(text, lang=LANG[language])
        text_file.close()
    speech_from_text.save(f'{path[0]}//temp.mp3')
    with open(f'{path[0]}//temp.mp3', 'rb') as audio_file:
        encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')
        audio_file.close()
    return text, encoded_string

def pick_course_thumbnail():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    with open(filename, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        image_file.close()
    return encoded_string

def main():
    print("Make sure the DB has been started!")
    id = str(uuid.uuid4())
    course_name = input("Insert Course Name: ")
    print("Insert your course thumbnail (Image file): ")
    course_thumbnail = pick_course_thumbnail()
    num_of_modules = int(input('How many Modules: '))
    modules = []
    for _ in range(num_of_modules):
        print('Module 1')
        while 1:
            try:
                language = int(input("What is the language for the module?\n1.Indonesia\n2.English\nInsert your number: "))
                if language!= 1 and language != 2:
                    raise ValueError
                break
            except ValueError:
                print('Check Your Output')
        text, audio = pick_module_text_file(language)
        module = (text,audio)
        modules.append(module)
    con = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{URL}/{DB}")
    conn = con.connect()
    conn.execute(f"INSERT INTO COURSE (course_id, course_name, course_thumbnail, total_modules) VALUES ('{id}', '{course_name}', '{course_thumbnail}', {num_of_modules})")
    for text,audio in modules:
        conn.execute(f"INSERT INTO course_module (course_id, texts, audio) VALUES ('{id}', '{text}', '{audio}')")

main()