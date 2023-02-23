import speech_recognition as sr
from pydub import AudioSegment

# convert mp3 file to wav  
src=(r"audio/2.mp3")
sound = AudioSegment.from_mp3(src)
sound.export("audio_transcription/2.wav", format="wav")

file_audio = sr.AudioFile(r"C:\Users\Andrew\Podcast.wav")

# use the audio file as the audio source                                        
r = sr.Recognizer()
with file_audio as source:
    audio_text = r.record(source)

print(type(audio_text))
print(r.recognize_google(audio_text))