# AutoStream Conversational AI Agent

An end-to-end **Conversational AI Agent** built as part of the **Machine Learning Intern Assignment (ServiceHive – Inflx)**.
This agent simulates a real-world **social-to-lead workflow**, converting user conversations into qualified leads for a fictional SaaS product called **AutoStream**.

---

## 🚀 Project Overview

**AutoStream** is a SaaS platform that provides **automated video editing tools** for content creators.
This conversational agent is designed to:

* Understand user intent (greeting, inquiry, high-intent lead)
* Answer product and pricing questions using **RAG (Retrieval-Augmented Generation)**
* Detect high-intent users
* Collect lead details (name, email, platform)
* Trigger a backend lead-capture action using a mock API

This is **not a simple chatbot** — it demonstrates reasoning, state management, and tool execution.

---

## 🧠 Agent Capabilities

### 1️⃣ Intent Identification

The agent classifies user intent into:

* Casual greeting
* Product / pricing inquiry
* High-intent lead (ready to sign up)

Intent detection is rule-assisted and context-aware.

---

### 2️⃣ RAG-Powered Knowledge Retrieval

The agent answers questions strictly using a **local knowledge base** stored in JSON.

**Knowledge Base Includes:**

**Pricing & Features**

* **Basic Plan**: $29/month

  * 10 videos/month
  * 720p resolution

* **Pro Plan**: $79/month

  * Unlimited videos
  * 4K resolution
  * AI captions

**Company Policies**

* No refunds after 7 days
* 24/7 support available only on Pro plan

---

### 3️⃣ Lead Capture Tool Execution

When high intent is detected, the agent:

1. Asks for **Name**
2. Asks for **Email**
3. Asks for **Creator Platform**

Only after collecting all three fields does it trigger the mock API:

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

Tool execution is **strictly controlled** and never triggered prematurely.

---

## 🏗️ Architecture

### Framework Choice: LangGraph

LangGraph was chosen because:

* It provides explicit **state management**
* Allows clear separation of nodes (intent, RAG, lead capture)
* Mimics real-world agent workflows

### State Management

Conversation state is maintained using a structured `AgentState` object:

* Conversation history
* Current intent
* Collected lead fields (name, email, platform)

This allows the agent to retain memory across **multiple conversation turns (5–6+)**.

---

## 📁 Project Structure

```
autostream-agent/
│
├── agent/
│   ├── graph.py        # LangGraph workflow
│   ├── intents.py      # Intent detection logic
│   ├── rag.py          # RAG pipeline
│   ├── state.py        # Agent state schema
│   └── tools.py        # Mock lead capture tool
│
├── data/
│   └── knowledge_base.json
│
├── main.py             # Entry point
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/USERNAME/autostream-agent.git
cd autostream-agent
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Agent

```bash
python main.py
```

---

## 🎥 Demo Video

The demo video showcases:

1. Pricing question answered via RAG
2. High-intent detection
3. Lead detail collection
4. Successful mock lead capture

*(Video included in submission)*

---

## 📲 WhatsApp Deployment (Conceptual)

To integrate this agent with WhatsApp:

1. Use **WhatsApp Business API** (via Meta or Twilio)
2. Incoming messages hit a **Webhook endpoint**
3. Webhook forwards message to the LangGraph agent
4. Agent response is sent back via WhatsApp API
5. State can be stored using Redis or a database keyed by phone number

This allows real-time, scalable deployment with persistent conversation memory.

---

## ✅ Evaluation Alignment

This project demonstrates:

* Agent reasoning & intent detection
* Correct RAG usage
* Clean state management
* Safe tool execution
* Production-ready architecture

---

## 👤 Author

**Bhaskar Parihar**
Machine Learning Intern Applicant
