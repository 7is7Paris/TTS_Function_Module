import logging
import azure.functions as func
import azure.cognitiveservices.speech as speechsdk
import os
import json
import uuid

def text_to_speech(text, filename, voice="en-US-JennyNeural"):
    speech_key = os.getenv("AZURE_SPEECH_KEY")
    service_region = os.getenv("AZURE_SPEECH_REGION")

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = voice

    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async(text).get()
    return result

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('TTS Function triggered.')

    try:
        req_body = req.get_json()
        text = req_body.get("text")
        voice = req_body.get("voice", "en-US-JennyNeural")

        if not text:
            return func.HttpResponse("Missing 'text' in request body.", status_code=400)

        filename = f"/
