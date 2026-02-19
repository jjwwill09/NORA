# NORA AI (Neural Organized Response Assistant)

NORA (Neural Organized Response Assistant) is a Python-based locally hosted AI assistant designed to listen, process, and respond to user commands in real time.
It integrates a locally hosted LLM through Ollama, wake-word detection via Picovoice, and speech-to-text processing using OpenAI’s Whisper model implementation.

The goal of NORA is to create a fully functional, open-source AI assistant capable of conversation, command execution, automation, and future hardware integration (e.g., Raspberry Pi hologram system).

---

# --- Features ---
- Wake-word activation (“Hey Nora”) using Picovoice Porcupine
- Real-time Speech-to-Text transcription (Faster-Whisper)
- Text-to-Speech responses (offline capable)
- Locally hosted LLM via Ollama (Mistral model)
- Command detection and execution (open apps, automation, scheduling)
- Self-training functionality from successful conversations
- Conversation logging system (CSV-based with timestamps)
- Cross-platform compatibility (Windows, macOS, Linux)
- Planned Raspberry Pi hardware deployment
- Future hologram projection system (Pepper’s Ghost concept)

---

# --- Technologies Used ---
- Python 3.11+
- Ollama (Local LLM hosting)
- Picovoice (Wake-word detection)
- Faster-Whisper (Speech-to-Text)
- pyttsx3 (Offline Text-to-Speech)
- PyAudio / sounddevice (Audio handling)
- NumPy (Signal processing & data handling)
- Librosa (Audio processing)
- BeautifulSoup4 + lxml (Web scraping)
- PyAutoGUI (System automation)

---

# --- How It Works ---
1. Wake Word Detection
   NORA continuously listens for the custom wake phrase using Picovoice Porcupine.
2. Speech Recognition
   Once activated, NORA records user speech and transcribes it using Faster-Whisper.
3. LLM Processing
   The transcribed text is sent to a locally hosted LLM through Ollama’s API interface.
4. Command Handling
   NORA checks if the input contains executable commands and runs them in parallel with response generation.
5. Response Output
   If no command is detected, NORA responds using text-to-speech.
6. Logging & Self-Training
   Conversations can be logged and optionally added to training data for contextual improvement.

---

# --- Installation ---

Clone the repository and install dependencies:

`git clone https://github.com/yourusername/NORA-AI.git
cd NORA-AI
pip install -r dependencies.txt`

Then install and run Ollama locally:

`ollama run mistral`

Ensure your wake-word `.ppn` file is configured properly before running the main script.

---

# --- Project Goals ---
- Fully offline AI assistant
- Modular and expandable architecture
- Raspberry Pi deployment (NORA 2.0)
- GUI implementation
- Performance optimization & profiling
- 3D printed hologram assistant enclosure

---

# --- Future Improvements ---
- Optimize Whisper model performance
- Improve response time and memory efficiency
- Add search and calendar command modules
- GUI interface for NORA 1.0
- Raspberry Pi deployment testing
- 3D animated hologram interface
- System performance analytics dashboard

---

# --- Sources ---
- Ollama – https://ollama.ai
- Picovoice – https://console.picovoice.ai
- Faster-Whisper – https://github.com/guillaumekln/faster-whisper
- pyttsx3 – https://pypi.org/project/pyttsx3/
- Librosa – https://librosa.org/
- BeautifulSoup4 – https://www.crummy.com/software/BeautifulSoup/

Schedule (Task scheduling)

Platformdirs (Cross-platform compatibility)
