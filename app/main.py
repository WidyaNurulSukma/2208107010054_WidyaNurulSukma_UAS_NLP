import os
import tempfile
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uvicorn
from app.stt import transcribe_speech_to_text
from app.llm import generate_response
from app.tts import transcribe_text_to_speech

app = FastAPI(title="Voice Chatbot API")

@app.post("/voice-chat")
async def voice_chat_endpoint(file: UploadFile = File(...)):
    """
    Endpoint untuk menerima file audio dari pengguna, memproses melalui
    STT, LLM, dan TTS, lalu mengembalikan file audio respons.
    """
    # Baca file audio yang diunggah
    file_content = await file.read()
    file_extension = os.path.splitext(file.filename)[1]
    
    # Step 1: Speech-to-Text (STT)
    transcript = transcribe_speech_to_text(file_content, file_extension)
    print(f"[STT] Transcript: {transcript}")
    
    # Step 2: Proses menggunakan LLM (Gemini)
    if transcript.startswith("[ERROR]"):
        response_text = "Maaf, terjadi kesalahan saat mengenali suara Anda."
    else:
        response_text = generate_response(transcript)
    print(f"[LLM] Response: {response_text}")
    
    # Step 3: Text-to-Speech (TTS)
    if response_text.startswith("[ERROR]"):
        # Fallback jika LLM error
        response_text = "Maaf, terjadi kesalahan dalam memproses pertanyaan Anda."
    
    audio_path = transcribe_text_to_speech(response_text)
    print(f"[TTS] Audio response path: {audio_path}")
    
    # Kirim file audio sebagai respons
    if audio_path.startswith("[ERROR]"):
        # Fallback jika TTS error
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.close()
            return FileResponse(f.name, media_type="audio/wav")
    
    return FileResponse(audio_path, media_type="audio/wav")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)