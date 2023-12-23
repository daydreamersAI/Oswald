
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def record_audio_wav(filename, duration=5, sample_rate=44100, channels=2):
    print(f"Recording for {duration} seconds...")

    # Start recorder with the given values
    recording = sd.rec(int(duration * sample_rate),
                       samplerate=sample_rate, channels=channels, dtype='int16')

    # Record audio for the given number of seconds
    sd.wait()

    # Save the recorded audio as a WAV file using scipy.io.wavfile.write
    write(filename, sample_rate, recording)

    # Alternatively, save the recorded audio using wavio
    wv.write(filename, recording, sample_rate, sampwidth=2)

    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    output_filename = "recorded_audio.wav"
    recording_duration = 6  # Set the desired recording duration in seconds

    record_audio_wav(output_filename, recording_duration)

# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv
# import keyboard

# def record_audio_wav(filename, duration=5, sample_rate=44100, channels=2):
#     print(f"Recording for {duration} seconds... Press 'Esc' to stop.")

#     # Initialize an empty array to store the recorded audio
#     recording = []

#     def callback(indata, frames, time, status):
#         if status:
#             print(f"Error in recording: {status}")
#         else:
#             # Append the recorded audio data to the array
#             recording.extend(indata.copy())

#     # Start recorder with the given values
#     with sd.InputStream(callback=callback, channels=channels, samplerate=sample_rate):
#         start_time = sd.get_stream().time
#         while sd.get_stream().time - start_time < duration and not keyboard.is_pressed('esc'):
#             pass  # Continue recording until the specified duration or 'Esc' key press

#     # Save the recorded audio as a WAV file using scipy.io.wavfile.write
#     write(filename, sample_rate, recording)

#     # Alternatively, save the recorded audio using wavio
#     wv.write(filename, recording, sample_rate, sampwidth=2)

#     print(f"Recording saved as {filename}")

# if __name__ == "__main__":
#     output_filename = "recorded_audio.wav"

#     record_audio_wav(output_filename)
