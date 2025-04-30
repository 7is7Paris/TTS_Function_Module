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
