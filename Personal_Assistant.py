import datetime
import json

import cv2
import playsound
import requests
from gtts import gTTS
from todoist.api import TodoistAPI

import face_recognition

# Teach Face
abbas_image = face_recognition.load_image_file("FACE.jpg")
face_face_encodings = face_recognition.face_encodings(face_image)[0]
known_face_encodings = [face_face_encodings, ]
known_face_names = ["Face", ]

# Recognize Face
video_capture = cv2.VideoCapture(0)
last_time = datetime.datetime.now()


routine_played = False

# Open Weather
weather_api_key = "YOUR_OPENWEATHER_API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "YOUR_CITY_NAME"


# Todoist
api_key = "YOUR_TODOIST_API_KEY"
api = TodoistAPI(api_key)


def get_latest_weather():
    raw_response = requests.get(base_url + "appid=" + weather_api_key + "&q=" + city_name)
    data = raw_response.json()
    current_temp = round(int(data["main"]["temp"]) - 273.15)
    current_hum = round(int(data["main"]["humidity"]))
    current_cond = data["weather"][0]["description"]
    tts = gTTS(f'The current condition is {current_cond} with the temperature of {current_temp} degree celcius and current humidity at {current_hum} percent')
    tts.save("current_weather.mp3")
    playsound.playsound("current_weather.mp3")


def get_latest_todo_list():
    api.sync()
    all_data = api.projects.get_data(YOUR_PROJECT_ID)
    todo_list = [items["content"] for items in all_data["items"]]
    audio = f'''
    You have {len(todo_list)} items in your to do list
    '''
    for item in todo_list:
        audio = audio + item + ', '
    tts = gTTS(audio)
    tts.save("todo_list.mp3")
    playsound.playsound("todo_list.mp3")


def greet_user(name):
    tts = gTTS(f'Hello {name}.', lang='en')
    tts.save('greet.mp3')
    playsound.playsound('greet.mp3')


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            greet_user(name)
            get_latest_weather()
            get_latest_todo_list()

            # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
