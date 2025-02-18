# Satori: A 7B LLM with Enhanced Reasoning Capabilities

Satori is a **7B Large Language Model (LLM)** that enhances reasoning abilities through **autoregressive searching**. It utilizes the **Chain-of-Action-Thought (COAT)** mechanism, which allows it to perform various meta-actions during problem-solving, such as **reflecting on previous steps or exploring alternative solutions**.

## 🔹 Key Features of Satori:

- **🧠 Training Paradigm:**  
  Satori follows a **two-stage training paradigm**:

  1. **Format Tuning (FT):** Helps internalize the COAT reasoning format.
  2. **Self-Improvement with Reinforcement Learning (RL):** Enhances reasoning through self-optimization.

- **⚡ Efficiency:**  
  Satori is a **single LLM capable of autoregressive search** without external guidance, achieving this with **minimal supervision** and **large-scale self-improvement**.

- **📈 Effectiveness:**  
  It demonstrates **strong performance on mathematical reasoning tasks**, **outperforming instruct models** built on the same base model.

- **🌍 Generalizability:**

  - **Transfers well** to out-of-domain tasks.
  - Exhibits **self-reflection** and **self-exploration** capabilities.

- **🔗 COAT Reasoning:**

  - Trained with the **COAT reasoning format**.
  - **Outperforms Chain-of-Thought (CoT) trained models**.

- **🔄 Self-Correction:**

  - **Stronger self-correction abilities** compared to models that lack RL training.

- **📊 Test-Time Scaling Behavior:**

  - Through RL training, Satori **improves reasoning performance** by allocating **more time to reasoning**.

- **♻️ Iterative Self-Improvement:**
  - Achieves **continuous performance gains** through **iterative self-improvement**.

---

## 🔹 Satori’s Training Framework:

### 🔧 1. **Format Tuning (FT)**

- A small-scale fine-tuning phase adjusts a **pre-trained LLM** on a **small dataset** of demonstrated reasoning trajectories.
- Helps the model **familiarize itself with meta-action tokens**.

### 🤖 2. **Multi-Agent Data Synthesis**

A multi-agent data synthesis framework leverages **three LLMs** to construct high-quality reasoning demonstrations:

1. **Generator**
   - Generates multiple reasoning paths for a given input problem.
2. **Critic**
   - Evaluates the correctness of the reasoning paths and provides feedback.
3. **Reward Model**
   - Assigns scores and selects **the most effective** reasoning path.

### 🔄 3. **Restart and Explore (RAE)**

- Inspired by **Go-Explore**, allowing the model to:
  - **Restart from intermediate steps**, including failed reasoning attempts.
  - **Focus on error correction** instead of starting over.
  - **Encourage deeper exploration** through exploration bonuses.

### 🎯 4. **Reward Design**

Satori uses **correctness as the primary reward** while introducing additional reward bonuses:

- **🏆 Rule-Based Reward**
  - Evaluates **the correctness of the final answer**.
- **📊 Preference Bonuses**
  - An **Outcome Reward Model (ORM)** is trained using the **Bradley-Terry (BT) framework** to evaluate reasoning trajectories, assigning **higher values to correct ones**.

### 🚀 5. **Iterative Self-Improvement**

- After each **RL training round**, the optimized reasoning policy is **distilled into the base model** through **supervised fine-tuning (SFT)**.

---

## 📊 **Experimental Performance of Satori**

- Achieves **state-of-the-art performance** on **mathematical reasoning benchmarks**.
- Exhibits **strong generalization** to **out-of-domain tasks**.
- **Outperforms** `Qwen-2.5-Math-7B-Instruct`, a math-specialized model built on the same base, **despite requiring less supervision**.

---
