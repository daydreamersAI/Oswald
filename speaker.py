# !pip install git+https://github.com/suno-ai/bark.git

from bark import SAMPLE_RATE, generate_audio, preload_models
import sounddevice as sd

# Check if running in IPython environment
try:
    get_ipython
    from IPython.display import Audio
    in_ipython = True
except NameError:
    in_ipython = False

class TextToAudioConverter:
    def __init__(self):
        preload_models()

    def convert_text_to_audio(self, text_prompt):
        audio_array = generate_audio(text_prompt)
        return audio_array, SAMPLE_RATE

# Example usage:
if __name__ == "__main__":
    text_converter = TextToAudioConverter()

    text_prompt = """
        Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
        But I also have other interests such as playing tic tac toe.
    """

    audio_array, sample_rate = text_converter.convert_text_to_audio(text_prompt)

    if in_ipython:
        # If in IPython, use IPython.display.Audio for playback
        from IPython.display import Audio
        audio_output = Audio(audio_array, rate=SAMPLE_RATE)
        audio_output
    else:
        # If not in IPython, use sounddevice for playback
        sd.play(audio_array, sample_rate, blocking=True)