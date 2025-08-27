# KERALATRAVELCHATBOT
An AI-powered chatbot that helps travelers explore Kerala, India 🇮🇳 — also known as “God’s Own Country”.
This project uses LangChain, Hugging Face embeddings, Pinecone, and Groq LLMs to provide travel recommendations, itineraries, cultural insights, and authentic Kerala experiences.



# ✨ Features

🏞️ Destination Guide – Suggests popular & hidden gems across Kerala.

🍲 Food & Culture – Recommends Kerala cuisine, festivals, and traditions.

🛶 Travel Planning – Creates itineraries (1-day, 3-day, 7-day trips).

🚍 Transport Help – Information on routes, local transport, and best travel seasons.

💬 Interactive Chat UI – Clean, modern chat interface with user & bot messages.






# 🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

AI/ML:

Hugging Face Embeddings (for semantic search)

Pinecone (for vector storage & retrieval)

Groq LLM (LLaMA 3) (for natural language generation)

Others: LangChain, dotenv



KERALA-TRAVELBOT/
│── app.py              # Flask backend  
│── store_index.py      # Loads data into Pinecone  
│── helper.py           # PDF/document loader & embedding functions  
│── template.py         # System prompt setup  
│── templates/          # HTML frontend  
│── static/             # CSS, JS, Images  
│── requirements.txt    # Project dependencies  
│── .env                # API keys (ignored in git)  
│── README.md           # Project documentation  



# How to run
Clone the repository
project repo:
STEP 01- Create a conda environment after opening the repository
conda create -n project_env python-3.10 -y
conda activate project_env
STEP 02 install the requirements
pip install -r requirements.txt
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
python store_index.py
python run app.py


