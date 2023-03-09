import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes, ImageAnalysis
from msrest.authentication import CognitiveServicesCredentials
import requests
import json
import os
import wave
import ffmpeg

speech_key = os.environ['']   # Setup Azure Speech Service
speech_region = os.environ['']


vision_key = os.environ['']
vision_endpoint = os.environ['']   # Setup Azure Computer Vision
credentials = CognitiveServicesCredentials(vision_key)
client = ComputerVisionClient(vision_endpoint, credentials)


gpt3_key = os.environ['']   # Setup OpenAI GPT-3
gpt3_endpoint = 'https://api.openai.com/v1/'

video_url = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_5mb.mp4"
video_stream = requests.get(video_url, stream=True).raw

with wave.open('temp_audio.wav', 'wb') as wave_file:
    audio_stream = ffmpeg.input(video_stream).audio
    audio_data = ffmpeg.output(audio_stream, 'pipe:', format='wav')
    audio_data = ffmpeg.run(audio_data, capture_stdout=True)
    wave_file.setnchannels(1)
    wave_file.setsampwidth(2)
    wave_file.setframerate(16000)
    wave_file.writeframes(audio_data)

audio_config = speechsdk.audio.AudioConfig(filename='temp_audio.wav')
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
result = speech_recognizer.recognize_once()

image_url = "https://i.postimg.cc/pLNL97j3/test.jpg"
image_analysis = client.analyze_image(image_url, visual_features=[VisualFeatureTypes.objects, VisualFeatureTypes.tags])

prompt = f"Hey GPT-3, what is happening in the scene? I see {', '.join(tag.name for tag in image_analysis.tags)}. The video is about {result.text}."
response_length = 50  
completion_endpoint = gpt3_endpoint + "completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {gpt3_key}"
}
payload = {
    "prompt": prompt,
    "max_tokens": response_length
}
response = requests.post(completion_endpoint, headers=headers, json=payload)
response_text = json.loads(response.text)['choices'][0]['text']

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
result = speech_synthesizer.speak_text_async(response_text).get()

os.remove('temp_audio.wav')
