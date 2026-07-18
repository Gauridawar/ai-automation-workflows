# AI Automation Workflows
Built by Gauri Dawar — Full Stack Developer & AI Automation Engineer

## Projects

### 1. AI Email Classifier n8n and Make.com
Webhook → Groq LLM → Google Sheets  
Classifies incoming emails as urgent/normal/spam automatically.
Demonstrates cross-platform automation skills.

### 2. AI Lead Qualifier  
Webhook → Groq LLM (scoring) → Groq LLM (email draft) → Google Sheets → Telegram alert  
Scores leads as Hot/Warm/Cold and drafts personalized follow-up emails.

### 3. AI Customer Support Ticket Router
Webhook → Groq AI → IF nodes → Google Sheets (x3) + Telegram alerts
Receives support tickets, classifies them as billing/technical/general using AI, 
routes each to a separate Google Sheet, and sends real-time Telegram notifications.

### 4. AI Social Media Content Scheduler
Webhook → Groq AI → Code Node → Google Sheets → Telegram
Takes any topic as input, generates 3 LinkedIn post variations using AI, 
saves all 3 to Google Sheets, and sends the best one to Telegram for approval.

### 5. AI Resume Reader (RAG Pipeline)
PDF → PyPDF Loader → ChromaDB (vector store) → Groq LLM → Answer
Upload any PDF and ask questions about it in natural language. 
The system retrieves relevant sections using semantic search and answers accurately using only the document content.

## Tech Stack
- n8n (self-hosted)
- Make.com
- Groq API (LLaMA 3)
- Google Sheets API + OAuth2
- Webhooks
- Postman for testing
- LangChain
- ChromaDB (vector database)
- Sentence Transformers (embeddings)
- Python

## Skills Demonstrated
- AI workflow engineering
- LLM API integration
- Event-driven automation
- OAuth2 authentication
- Dynamic data mapping
- REST API design
- IF/Switch node branching and conditional routing
- Structured JSON prompting for multiple AI outputs
- RAG (Retrieval Augmented Generation) pipeline
- Vector embeddings and semantic search
- PDF processing and text chunking

## Contact
- LinkedIn:https://www.linkedin.com/in/gauri-dawar/
