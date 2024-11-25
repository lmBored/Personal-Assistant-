# Personal Assistant - Python

No problem! Here is a personal assistant application written in Python that uses computer vision and various APIs to interact with the user by recognizing faces, providing weather updates, and managing a to-do list.

## Features
- **Face Recognition**: Uses the `face_recognition` library for identifying known faces.
- **Weather Updates**: Fetches the latest weather information using the OpenWeather API.
- **To-Do List Management**: Integrates with Todoist API to fetch and read out the to-do list items.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- gTTS (`gtts`)
- playsound
- requests
- face_recognition
- Todoist API

## Setup
1. **Clone the repository**:
    ```bash
    git clone https://github.com/lmBored/Personal-Assistant-.git
    cd Personal-Assistant-
    ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
- **OpenWeather API**: Replace `YOUR_OPENWEATHER_API_KEY` and `YOUR_CITY_NAME` in `Personal_Assistant.py` with your OpenWeather API key and city name.
- **Todoist API**: Replace `YOUR_TODOIST_API_KEY` and `YOUR_PROJECT_ID` in `Personal_Assistant.py` with your Todoist API key and project ID.
- **Face Image**: Replace `FACE.jpg` with the image of the face you want to recognize.

## Usage
Run the personal assistant script:
```bash
python Personal_Assistant.py
```

## License
This project is licensed under the MIT License.
