# Friday – Your Personal AI Assistant 🤖

**Friday** is a Python-based AI assistant inspired by Tony Stark's AI. It can generate intelligent responses, handle structured prompts, and is designed with modularity and extensibility in mind.

## 🚀 Features

- Prompt-based response generation
- Asynchronous processing using `async/await`
- Secure environment config via `.env`
- Clean, modular folder structure
- Token server integration support (e.g., LiveKit)

## 📁 Project Structure

Friday/
├── friday_app/             # Main logic  
├── agent.py                # Entry point script  
├── token_server.py         # Handles token generation  
├── prompts.py              # Prompt templates  
├── tools.py                # Utility functions  
├── requirements.txt        # Python dependencies  
├── .env                    # Environment variables (not shared)  
└── README.md               # Project description (this file)  

## ⚙️ Installation

```bash
git clone https://github.com/Aaqil1306/my_projects_repo.git
cd my_projects_repo
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
