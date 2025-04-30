# TTS_Function_Module
Azure Function to convert AI-generated motivational sentences into speech using Azure TTS. Part of AI Binome project.
# AI Binome - TTS Function Module 🎧

This module is part of the **AI Binome** project, which helps users stay motivated while achieving personal goals through long-form AI-generated audio companions.

## 🔧 Function Overview

This Azure Function receives motivational text (generated from LLM) and converts it into speech using Azure TTS (Text-to-Speech). The audio can be returned to the user or stored.

## ✅ Input (POST JSON)

```json
{
  "text": "You've studied 30 minutes. Keep going!",
  "timestamp": "00_30_00",
  "voice": "en-US-JennyNeural"
}

##  🔁 Output
Returns confirmation:
Audio generated: /tmp/audio_00_30_00.wav

## 📦 Requirements
Install dependencies with:
pip install -r requirements.txt

## ▶️ Local Run
Make sure your local.settings.json contains your Azure Speech key and region:
"AZURE_SPEECH_KEY": "xxx",
"AZURE_SPEECH_REGION": "eastus"
Then start the function:
func start

## ☁️ Deployment
Use Azure CLI:
func azure functionapp publish <your-function-app-name>

## 📁 Files Description
| File | Purpose |
|------|---------|
| `tts_module/function_app.py` | Core function logic |
| `requirements.txt` | Python dependencies |
| `local.settings.json` | Local environment config (excluded from Git) |
| `.gitignore` | Files to exclude from GitHub |
| `host.json` | Azure Function host config |
| `README.md` | This file |

## ✨ Team Note
This module will integrate with other agents:
LLM Agent: breaks down goal & generates motivational sentences
Frontend Agent: collects user input & plays audio from TTS
You: the dreamer that needs encouragement 😉
