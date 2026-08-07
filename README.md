# 🌍 TravelMate AI – Intelligent Travel Planner for India

TravelMate AI is an Agentic AI-powered travel planning assistant that helps users explore destinations across India, generate personalized travel itineraries, and manage their travel preferences using function calling and tool-based workflows.

This project demonstrates how Large Language Models (LLMs) can interact with Python tools to perform real-world tasks instead of only generating text.

---

## ✨ Features

- 🇮🇳 Travel planning across multiple Indian destinations
- 📍 Destination recommendation based on user interests
- 📖 Detailed destination information retrieval
- 💾 Save travel itineraries
- 👤 Save user travel preferences
- 🔎 Keyword-based destination search
- 📂 Retrieve previously saved trips
- 🤖 Gemini Function Calling / Tool Calling
- 💬 Interactive Gradio interface

---

## 🏗️ Project Structure

```
AI Travel Planner Agent
│
├── app.py                 # Gradio Interface
├── agent.py               # LLM + Tool Calling Logic
├── context.py             # System Prompt
├── knowledge.py           # Loads Destination Knowledge
├── tools.py               # Python Tool Functions
├── styles.py              # UI Styling
│
├── data
│   ├── destinations       # Destination Knowledge (.txt files)
│   ├── saved_trips.json
│   └── user_preferences.json
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tools Implemented

### 1. Save Trip Plan

Stores user travel itineraries for future retrieval.

Example:

- Destination
- Duration
- Budget
- Notes

---

### 2. Save User Preference

Stores travel preferences such as:

- Budget
- Traveller Type
- Travel Style
- Food Preference

---

### 3. Search Destinations

Searches the destination knowledge base using keywords such as:

- Beach
- Hill Station
- Temple
- Wildlife
- Shopping
- Adventure
- Honeymoon

Returns matching destinations.

---

### 4. Recommend Destination

Retrieves complete travel information for a selected destination.

Includes:

- Attractions
- Best Season
- Food
- Transport
- Budget
- Suggested Itinerary
- Safety Tips

---

### 5. Get Saved Trip

Retrieves a previously saved itinerary.

---

## 🧠 Agent Workflow

```
User
      │
      ▼
Gemini LLM
      │
      ▼
Function Calling
      │
      ▼
Python Tools
      │
      ▼
Knowledge Base / JSON Storage
      │
      ▼
Final Response
```

---

## 📚 Knowledge Base

The travel knowledge is stored as individual text files.

Example:

```
data/
    destinations/
        Goa.txt
        Jaipur.txt
        Ooty.txt
        Kerala.txt
        ...
```

This makes it easy to extend the system by simply adding new destination files.

---

## 🚀 Technologies Used

- Python
- Google Gemini API
- OpenAI Compatible SDK
- Gradio
- JSON
- pathlib
- dotenv

---

## 💡 Future Improvements

- Multi-day itinerary optimization
- Live Weather API integration
- Google Maps integration
- Hotel recommendations
- Flight recommendations
- Budget estimation
- PDF itinerary generation
- User authentication
- Persistent user memory

---

## 🎯 Learning Objectives

This project was built to understand:

- Agentic AI concepts
- Function Calling
- Tool Calling
- Knowledge-Augmented Generation
- LLM orchestration
- Python backend development
- Gradio application development

---

## 📌 Note

This project currently works with a curated travel knowledge base and does not access live internet data. Recommendations are generated only from the provided destination information.

---

## 👨‍💻 Author
**S.VENIKALAXMI**
Integrated MTech Software Engineering , VIT VELLORE.

Developed as part of an Agentic AI learning journey to explore tool-using LLM applications and real-world AI software engineering.
