# Voice Chatbot UAS – STT, Gemini LLM, TTS Integration

Proyek UAS ini merupakan aplikasi chatbot berbasis suara yang memungkinkan pengguna berbicara langsung melalui antarmuka web. Sistem akan mengenali suara pengguna, mengubahnya menjadi teks (Speech-to-Text), memprosesnya menggunakan model bahasa besar (Gemini API), lalu mengubah hasil jawabannya kembali menjadi suara (Text-to-Speech).

## 📌 Fitur Utama

* 🎙️ Speech-to-Text (STT) menggunakan `whisper.cpp` dari OpenAI.
* 🧠 LLM Integration menggunakan Google Gemini API untuk menghasilkan respons dalam Bahasa Indonesia.
* 🔊 Text-to-Speech (TTS) menggunakan model Coqui TTS (Indonesian TTS).
* 🧪 Antarmuka pengguna interaktif berbasis `Gradio` untuk pengujian langsung dari browser.

## 🗂️ Struktur Proyek

```
voice_chatbot_project/
│
├── app/
│   ├── main.py            # Endpoint utama FastAPI
│   ├── llm.py             # Integrasi Gemini API
│   ├── stt.py             # Transkripsi suara (whisper.cpp)
│   ├── tts.py             # TTS dengan Coqui
│   └── whisper.cpp/       # Hasil clone whisper.cpp
│   └── coqui_utils/       # Model dan config Coqui TTS
│
├── gradio_app/
│   └── app.py             # Frontend dengan Gradio
│
├── .env                   # Menyimpan Gemini API Key
├── requirements.txt       # Daftar dependensi Python
```

## 📋 Prasyarat

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal:

1. Python 3.9 atau lebih baru
2. Whisper.cpp (termasuk model `ggml-large-v3-turbo.bin`)
3. Coqui TTS (termasuk model untuk Bahasa Indonesia)

## 🚀 Langkah Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/yourusername/voice_chatbot_project.git
   cd voice_chatbot_project
   ```

2. Instal dependensi Python:
   ```bash
   pip install -r requirements.txt
   ```

3. Clone whisper.cpp dan kompilasi:
   ```bash
   cd app
   git clone https://github.com/ggerganov/whisper.cpp.git
   cd whisper.cpp
   make
   cd ..
   ```

4. Download model Whisper:
   ```bash
   mkdir -p whisper.cpp/models
   cd whisper.cpp/models
   wget https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin
   cd ../..
   ```

5. Siapkan model TTS:
   ```bash
   mkdir -p coqui_utils
   # Download model Coqui TTS Bahasa Indonesia ke folder coqui_utils
   ```

6. Salin file `.env.example` ke `.env` dan isi dengan API key Gemini Anda:
   ```bash
   cp .env.example .env
   # Edit file .env dengan editor teks dan tambahkan API key Anda
   ```

## 🖥️ Menjalankan Aplikasi

1. Jalankan backend FastAPI:
   ```bash
   cd app
   uvicorn main:app --reload
   ```

2. Jalankan frontend Gradio (dalam terminal terpisah):
   ```bash
   cd gradio_app
   python app.py
   ```

3. Buka browser dan akses aplikasi di: http://localhost:7860

## 📚 Catatan Penggunaan

* Semua file audio menggunakan format `.wav`
* Pastikan mikrofon terhubung dan berfungsi dengan baik
* Voice Assistant dirancang untuk merespons dalam Bahasa Indonesia
* Disarankan menggunakan model Whisper: `ggml-large-v3-turbo`
* Speaker TTS: `wibowo` dari model Coqui v1.2

## 👨‍💻 Dibuat Untuk

Proyek UAS mata kuliah *Pemrosesan Bahasa Alami* — Semester Genap 2024/2025.

## 📝 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detailnya.
