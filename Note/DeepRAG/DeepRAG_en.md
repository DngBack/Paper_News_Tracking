### DeepRAG: Thinking Step by Step Before Retrieval for Large Language Models

The paper _"DeepRAG: Thinking to Retrieval Step by Step for Large Language Models"_ introduces a framework called **DeepRAG**, aimed at improving the reasoning and accuracy of **Large Language Models (LLMs)** in **Retrieval-Augmented Generation (RAG)**. This framework addresses the challenges of **ineffective task decomposition** and **redundant retrieval**, which can introduce noise and degrade response quality.

DeepRAG models **retrieval-augmented reasoning** as a **Markov Decision Process (MDP)**, enabling strategic and adaptive retrieval.

---

## **Key Components of DeepRAG**

### 1. Retrieval Narrative

- Ensures a structured and adaptive retrieval flow by generating **subqueries** based on previously retrieved information.
- Helps decompose complex queries into smaller, more manageable subqueries.

### 2. Atomic Decisions

- Dynamically determines whether to retrieve external knowledge or rely solely on the **parametric knowledge** of the LLM for each subquery.
- Crucial for avoiding unnecessary retrieval, which can **improve generation quality and reduce inference latency**.

---

## **How DeepRAG Works**

DeepRAG operates through a **three-step process**:

### 1. Binary Tree Search

- Constructs a **binary tree** for each subquery, **exploring** paths based on **parametric knowledge** or **external knowledge bases**.
- This method helps synthesize data for **imitation learning** and calibrate the **LLM's knowledge boundaries**.

### 2. Imitation Learning

- Extracts the **reasoning process** that leads to the correct final answer with minimal retrieval cost.
- Fine-tunes the model to **improve termination decisions, atomic decisions, query decomposition capabilities,** and **generate accurate intermediate answers**.

### 3. Chain of Calibration

- **Calibrates the LLM's internal knowledge** by optimizing each atomic decision.
- Synthesizes **preference data** to determine **when retrieval is necessary** and fine-tunes the LLM accordingly.

---

## **MDP Modeling in DeepRAG**

DeepRAG treats the reasoning process as an **MDP**, defined by the tuple **(S, A, P, R)**:

- **States (S):** Represent the **partial solution** to the original question at each step.
- **Actions (A):** Consist of two sub-decisions:
  - **Termination decision** (whether to continue or finalize the answer).
  - **Atomic decision** (whether to retrieve external knowledge or rely on parametric knowledge).
- **Transitions (P):** Update the state based on the action taken (generating the next subquery or finalizing the answer).
- **Rewards (R):** Evaluate **answer correctness** and **retrieval cost**, applied only after generating the final answer.

---

## **Experiments and Results**

DeepRAG was validated on **five open-domain question-answering datasets**:

- **HotpotQA, 2WikiMultihopQA, PopQA, CAG**, and **WebQuestions**.

Experimental results demonstrated that DeepRAG **outperforms existing methods**, achieving a **21.99% higher answer accuracy** while improving **retrieval efficiency**.

Further analysis showed a stronger correlation between retrieval decisions and **LLM's parametric knowledge**, indicating **more effective knowledge boundary calibration**.

---

## **Adaptive Retrieval-Augmented Generation**

DeepRAG falls under the category of **adaptive RAG approaches**, which aim to optimize **retrieval efficiency and accuracy**.

Existing methods include:

- **Classifier-based methods**
- **Confidence-based methods**
- **LLM-based methods**

DeepRAG **distinguishes itself** by leveraging **the inherent generative capabilities** of LLMs to **explore knowledge boundaries**, eliminating the need for **additional parameters** or **unreliable uncertainty metrics**.

---

## **Reasoning in Retrieval-Augmented Generation**

DeepRAG contributes to the growing focus on incorporating **reasoning capabilities** into RAG.

Unlike other approaches that rely heavily on **extensive retrieval operations** or **large reasoning models**, DeepRAG provides an **end-to-end method** that enables **any model to think through retrieval step by step as needed**.

---

## **Knowledge Boundary**

LLMs struggle to accurately distinguish **what they know** from **what they don’t know**.

DeepRAG addresses this challenge by **exploring knowledge boundaries** in RAG settings, enhancing the LLM's ability to **recognize its limitations** and **make informed retrieval decisions**.

---

### DeepRAG: Suy nghĩ từng bước trước khi truy xuất cho các mô hình ngôn ngữ lớn

Bài báo _"DeepRAG: Thinking to Retrieval Step by Step for Large Language Models"_ giới thiệu một framework có tên **DeepRAG**, nhằm cải thiện khả năng suy luận và độ chính xác của **các mô hình ngôn ngữ lớn (LLMs)** trong **truy xuất kết hợp sinh văn bản (Retrieval-Augmented Generation - RAG)**. Framework này giải quyết các thách thức về **phân rã nhiệm vụ kém hiệu quả** và **truy xuất dư thừa**, vốn có thể tạo ra nhiễu và làm giảm chất lượng phản hồi.

DeepRAG mô hình hóa **quá trình suy luận có hỗ trợ truy xuất** như một **Quá trình Quyết định Markov (MDP)**, cho phép truy xuất một cách chiến lược và thích ứng.
