# 🚀 Local AI Engineer Roadmap

A complete hands-on journey from running local LLMs to building production-ready AI applications.

## Current Progress

### Phase 1: Local LLM Deployment ✅

* Installed Ollama
* Downloaded and ran Llama 3
* Connected Python to Ollama
* Generated responses locally

### Phase 2: FastAPI AI Backend ✅

* Built REST APIs using FastAPI
* Connected API endpoints to Llama 3
* Implemented JSON request/response handling
* Tested endpoints through Swagger UI

## Technologies

* Python
* Ollama
* Llama 3
* FastAPI
* Uvicorn

## Upcoming Phases

* RAG with ChromaDB
* Embeddings
* LangChain
* Tool Calling
* AI Agents
* Multi-Agent Systems

## Project Architecture
## 🏗️ Architecture

```text
User
 │
 ▼
FastAPI
 │
 ▼
Python Backend
 │
 ▼
Ollama
 │
 ▼
Llama 3
```

## 📍 Progress Tracker

- [x] Phase 1 - Local LLM Deployment
- [x] Phase 2 - FastAPI AI Backend
- [x] Phase 3 - Conversation Memory
- [x] Phase 4 - RAG with ChromaDB and Embeddings
- [x] Phase 5 - Tool Calling
- [ ] Phase 6 - AI Agents
- [ ] Phase 7 - Multi-Agent System
- [ ] Phase 8 - Docker Deployment

## 📸 Screenshots

### FastAPI Swagger UI

![Swagger](screenshots/fastapi-docs.png)

### Chat Endpoint

![Chat](screenshots/chat-endpoint1.png)
![Chat](screenshots/chat-endpoint2.png)

# Phase 3 - Conversation Memory

## Objective

Implement conversation history and multi-turn chat support.

## Concepts Learned

- Stateful AI Systems
- Conversation History
- Context Windows
- Multi-Turn Interactions

## Example

User: My name is Parth

User: What is my name?

AI: Your name is Parth

# Phase 4 - Retrieval-Augmented Generation (RAG)

## Objective

Build a document-aware AI assistant capable of answering questions using custom knowledge sources.

## Technologies

* Ollama
* Llama 3
* ChromaDB
* Sentence Transformers
* FastAPI
* LangChain

## Architecture

PDF
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Semantic Search
↓
Llama 3
↓
Answer

## Features

* PDF Ingestion
* Semantic Search
* Vector Database Storage
* Retrieval-Augmented Generation
* Resume Question Answering

## Example Questions

* What projects are mentioned in the resume?
* What technical skills are listed?
* What is the final year project?

# Phase 5 - Tool Calling

## Objective

Enable AI systems to interact with external tools.

## Tools Implemented

- Current Time
- Calculator

## Concepts Learned

- Function Calling
- Tool Invocation
- External Actions
- AI Workflows

## Author

Parth Sarthi
