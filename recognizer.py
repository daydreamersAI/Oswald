import speech_recognition as sr

def recognize_audio(filename):
    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)  # Record the audio file

        try:
            text = recognizer.recognize_google(audio_data)
            print("Recognized Text: ", text)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    audio_file_path = "recorded_audio.wav"  # Replace with your audio file path
    recognize_audio(audio_file_path)