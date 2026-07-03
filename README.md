End to end AI system for real-time speech understanding, context-aware response generation &  natural voice interaction. In other terms, a system that listens to your voice, understands what you mean, generates intelligent answers, and responds back naturally in speech.


Project flow - 

┌────────────────────┐
│   User Speaks 🎤   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Speech-to-Text     │
│ (Whisper)          │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Query Processing   │
│ Intent Extraction  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Semantic Retrieval │
│ (Embeddings+FAISS) │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Context Building   │
│ + User Memory      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Response Generation│
│ (LLM)              │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Text-to-Speech     │
│ (TTS Model)        │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Voice Response 🔊  │
└────────────────────┘

 
