import logging
import azure.functions as func
import azure.cognitiveservices.speech as speechsdk
import os
import uuid
import json

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
        items = req_body.get("Output", [])
        voice = req_body.get("Voice", "en-US-JennyNeural")

        audio_urls = []

        for i, entry in enumerate(items):
            sentence = entry.get("sentence")
            timestamp = entry.get("timestamp").replace(":", "_")
            filename = f"audio_{timestamp}.mp3"

            output_path = f"/tmp/{filename}"  # Azure Linux compatible
            result = text_to_speech(sentence, output_path, voice)
            
            # For now, only return local paths — optionally you can add upload to Azure Blob later
            audio_urls.append({
                "timestamp": entry.get("timestamp"),
                "audio_file": output_path  # You can replace with blob URL after upload
            })

        return func.HttpResponse(
            body=json.dumps({"audios": audio_urls}, indent=2),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error in TTS function: {str(e)}")
        return func.HttpResponse(f"Internal Server Error: {str(e)}", status_code=500)