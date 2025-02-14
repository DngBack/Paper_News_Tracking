### s1: Simple Test-Time Scaling

The paper _"s1: Simple Test-Time Scaling"_ introduces a method for improving the reasoning performance of **language models (LMs)** by increasing computation at test time. The authors, **Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, and Emmanuel Candès**, focus on achieving both strong reasoning performance and clear test-time scaling behavior.

The core idea involves training a **language model** on a small, carefully curated dataset and then employing a technique called **"budget forcing"** to control the amount of computation the model uses at test time.

---

## **Key Components of s1**

### 1. Dataset Curation

- The authors created **s1K**, a dataset of **1,000 questions** paired with reasoning traces.
- The selection of these questions was guided by **three principles**: **quality, difficulty, and diversity**.
- They started with **59,029 questions from 16 diverse sources**, including **NuminaMATH, historical AIME problems, OlympicArena, OmniMath, and AGIEval**.
- The authors also created **two original datasets: s1-prob and s1-teasers**.
- The dataset was filtered down to **1,000 samples** based on quality, difficulty, and diversity. Questions with **API errors or formatting issues** were removed.
- Each question was classified into **specific domains** using **Claude 3.5 Sonnet** based on the **Mathematics Subject Classification (MSC) system**.

### 2. Budget Forcing

- **Controls test-time compute** by **terminating** or **lengthening** the model’s reasoning process.
- If the model generates more **thinking tokens** than a desired limit, an **end-of-thinking token delimiter** is appended, prompting the model to provide an answer.
- To **encourage longer reasoning**, the **end-of-thinking token delimiter** is suppressed, and **"Wait"** is appended to the model’s current reasoning trace, encouraging further reasoning.

### 3. Model Training and Evaluation

- The **Qwen2.5-32B-Instruct** model was **fine-tuned** on the **s1K dataset**.
- Evaluated on **three reasoning benchmarks**: **AIME24, MATH500, and GPQA Diamond**.
  - **AIME24**: 2024 American Invitational Mathematics Examination problems.
  - **MATH500**: Competition-level math problems.
  - **GPQA Diamond**: PhD-level science questions.
- The model, **s1-32B**, was trained using **supervised fine-tuning (SFT)**, taking **26 minutes on 16 NVIDIA H100 GPUs**.

---

## **Findings and Limitations**

- **Sample-Efficient Reasoning**: The **s1-32B model** achieves competitive performance with **closed-source models like OpenAI’s o1-preview**, despite being trained on only **1,000 samples**.
- **Pretraining & Fine-Tuning**: The authors argue that **pretraining on vast data** gives models **latent reasoning ability**, which can be **activated through fine-tuning** on a **small, high-quality dataset**.
- **Test-Time Scaling Limitations**: Budget forcing eventually **flattens out** due to:
  - The **context window constraint** of LMs.
  - Diminishing returns in extended reasoning.
- **Proposed Solutions**:
  - **Parallel Scaling Methods**, such as **majority voting** and **tree search**.
  - Classification of **test-time scaling methods** into **sequential and parallel**.
  - **Budget forcing is a sequential method**, meaning later computations depend on earlier ones, which may **scale better** than parallel methods.
