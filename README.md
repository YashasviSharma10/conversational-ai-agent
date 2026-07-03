# 🎙️ Agentic AI Voice Assistant

An intelligent conversational AI voice assistant built using **Python**, **Google Gemini**, and the **OpenAI-compatible API**. The assistant accepts voice input, performs multi-step reasoning using a structured planning workflow, invokes external tools when required, and responds naturally using text-to-speech.

The project demonstrates the core concepts behind **Agentic AI**, including structured reasoning, tool invocation, conversation memory, and voice-based interaction.

---

# ✨ Features

- 🎤 Speech-to-Text using SpeechRecognition
- 🧠 Multi-step reasoning with a START → PLAN → TOOL → OBSERVE → OUTPUT workflow
- 🤖 Conversational AI powered by Google Gemini
- 🛠 Dynamic tool invocation
- 🌦 Real-time weather lookup using an external weather API
- 💻 Execute Linux terminal commands through tool calls
- 🔊 Natural Text-to-Speech responses
- 💬 Conversation history for contextual interactions
- 📦 Modular and easy-to-maintain project structure

---

# 🏗 Project Architecture

```
User Voice
     │
     ▼
Speech Recognition
     │
     ▼
Speech → Text
     │
     ▼
Conversation History
     │
     ▼
Gemini LLM
     │
     ▼
Structured Response
(START / PLAN / TOOL / OUTPUT)
     │
     ├───────────────┐
     │               │
     ▼               ▼
Planning        Tool Execution
                     │
                     ▼
              Observation Added
                     │
                     ▼
               Gemini Re-evaluates
                     │
                     ▼
                 Final Output
                     │
                     ▼
              Text-to-Speech
                     │
                     ▼
                 Voice Response
```

---

# 📁 Project Structure

```
agentic-voice-assistant/
│
├── agent.py          # Core reasoning loop and agent workflow
├── config.py         # Gemini/OpenAI client configuration
├── main.py           # Application entry point
├── prompt.py         # System prompt for the AI agent
├── schema.py         # Pydantic schema for structured outputs
├── speech.py         # Speech-to-Text and Text-to-Speech utilities
├── tools.py          # External tools (Weather & Terminal Commands)
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# ⚙️ Technologies Used

- Python
- Google Gemini
- OpenAI Python SDK
- SpeechRecognition
- PyAudio
- Pydantic
- Requests
- AsyncIO

---

# 🧠 Agent Workflow

The assistant follows a structured reasoning workflow instead of generating an immediate response.

```
START

↓

PLAN

↓

TOOL (Optional)

↓

OBSERVE

↓

PLAN

↓

OUTPUT
```

This workflow enables the assistant to reason through a task, decide whether external information is required, execute the appropriate tool, observe the result, and then generate the final response.

---

# 🛠 Available Tools

### 🌦 Weather Tool

Retrieves real-time weather information for a specified city.

Example:

```
What is the weather in Delhi?
```

---

### 💻 Terminal Command Tool

Executes Linux terminal commands on the local machine.

Example:

```
Create a folder called Demo
```

---

# 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd agentic-voice-assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 💡 Example Queries

- What is the weather in Mumbai?
- Create a folder named AI_Project
- Make a directory called Demo
- Solve 25 * 40 + 18
- Explain Binary Search

---

# 🚀 Future Improvements

- More external tools
- File management tools
- Browser automation
- Memory persistence
- Streaming responses
- Code generation tools
- GUI interface
- Docker support

---

# 👨‍💻 Author

**Yashasvi Kumar**

B.Tech Computer Science & Engineering

Built as a learning project to explore **Agentic AI**, **Large Language Models**, **Tool Calling**, and **Voice-based AI Assistants**.