# **Key Findings of the LIMO Project (Less is More for Reasoning)**

## **1. High Accuracy with Minimal Data**

- LIMO achieves **57.1%** accuracy on the **AIME** benchmark and **94.8%** on **MATH** with only **817 training samples**.
- This demonstrates that complex mathematical reasoning can be extracted with very few examples.
- LIMO uses only **1% of the training data** compared to previous methods but still achieves superior performance.

## **2. Out-of-Distribution Generalization**

- LIMO achieves **an absolute improvement of 40.5% across 10 diverse evaluation benchmarks**.
- Outperforms models trained on **100 times larger datasets**.
- Challenges the notion that supervised fine-tuning mainly leads to memorization rather than generalization.

## **3. Outperforming Larger Datasets**

- A carefully curated dataset of **817 problems** enables LIMO to achieve **72.8% accuracy**.
- Surpasses models trained on large datasets like **NuminaMath-100k** and **OpenThoughts-114k**.
- This proves that **data quality is more important than data quantity**.

## **4. Impact of Reasoning Chain Quality**

- Models trained on the highest-quality reasoning chains (_L5_) achieve the best performance on **AIME24** and **MATH500**.
- Performance decreases progressively with lower-quality reasoning chains.
- Gap between _L5_ and _L1_:
  - **15 percentage points** on AIME24.
  - **12 percentage points** on MATH500.

## **5. Impact of Question Quality**

- Training on more challenging datasets improves reasoning ability.
- Simply changing the selection of problems increases **accuracy by 16% on AIME2024**.

## **6. Importance of Pretraining Foundation**

- Choice of the pretraining model significantly affects reasoning performance.
- LIMO is built on **Qwen2.5-32B-Instruct**, outperforming its predecessor:
  - **AIME2024**: **47.1 percentage points** higher than **Qwen1.5-32B-Instruct**.
  - **MATH500**: **34.4 percentage points** higher than **Qwen1.5-32B-Instruct**.

## **7. Overall Highest Performance**

- LIMO achieves **an average of 72.1%** across all evaluation benchmarks, surpassing:
  - **OpenAI-o1-preview**: 67.8%.
  - **QwQ-32B-Preview**: 66.4%.
  - Other baseline models.

## **8. Qualitative Analysis**

- LIMO demonstrates **strong self-criticism** and **long chain-of-thought reasoning**.
- Capable of **self-verifying statements** and **checking computations**.

# **Key Contributions of the LIMO Project (Less is More for Reasoning)**

## **1. LIMO Hypothesis**

- The paper introduces and establishes the **LIMO Hypothesis**, demonstrating that **complex reasoning can be extracted with an astonishingly small amount of data** (only a few hundred examples).
- By leveraging **rich mathematical knowledge** in pretrained models and **detailed reasoning chains**, LIMO **challenges traditional scaling laws** in reasoning tasks.
- The LIMO Hypothesis suggests that **advanced reasoning capabilities can emerge in foundation models with only a small number of well-structured examples**, based on two key factors:
  - **Pretrained knowledge** already encoded in the model's parameter space.
  - **Quality of the reasoning chain**, which decomposes complex problems into detailed logical steps.

## **2. Data Efficiency**

- LIMO demonstrates that high accuracy can be achieved with minimal training data.
- Examples:
  - **57.1% accuracy on AIME**.
  - **94.8% accuracy on MATH**.
  - Uses only **817 training samples**, equivalent to **1% of the data** used by prior methods.

## **3. Out-of-Distribution Generalization**

- LIMO exhibits **strong generalization**, achieving **an absolute improvement of 40.5% across 10 different evaluation sets**.
- Outperforms models trained on **100× larger datasets**.

## **4. Identification of Critical Factors**

- The project identifies **key factors** for unlocking effective reasoning, especially:
  - **The combination of pretrained knowledge and computational expansion at inference time**.

## **5. Systematic Empirical Evidence**

- LIMO provides **systematic empirical evidence**, challenging current assumptions about **scaling laws in reasoning tasks**.
- Demonstrates that the benefits of this approach **extend beyond training data and generalize well to out-of-distribution problems**.

## **6. Open-Source Release**

- The authors release **a complete open-source toolkit**, including:
  - **Fine-tuned models**.
  - **Evaluation pipelines**.
  - **Training code**.
  - **A carefully curated dataset**.
- This facilitates **systematic research on data efficiency in complex reasoning** and ensures **result reproducibility**.

## **7. High-Quality Data Curation**

- The paper emphasizes **data quality over quantity**.
- LIMO introduces **a systematic approach** for constructing minimal datasets with questions designed to **maximize extended reasoning processes** and solutions that exhibit **clear logical progressions**.

## **8. Reasoning Chain Quality**

- Models trained on **high-quality reasoning chains** perform significantly better.

## **9. Question Quality**

- Models trained on **more challenging datasets** demonstrate **superior reasoning abilities**.

---

# **Building the LIMO Dataset and Training the Model**

## **1. Dataset Construction**

### **LIMO Hypothesis Validation**

- The dataset construction follows the **LIMO Hypothesis**, asserting that **complex reasoning can emerge through a small but well-structured set of reasoning examples** in foundation models that have comprehensive domain knowledge encoded during pretraining.
- This hypothesis is based on:
  - **The presence of prerequisite knowledge** in the model’s parameter space.
  - **The quality of the reasoning chain**, which decomposes complex problems into detailed logical steps.

### **Objective**

- Construct a **minimal yet high-quality dataset** capable of **effectively leveraging the model’s inherent reasoning abilities**.

### **Question Selection**

- **Selection Criteria**:

  - **Difficulty**: Prioritizing **high-challenge problems** requiring complex reasoning and knowledge integration.
  - **Generalization**: Preferring problems **significantly different from the model’s training data**.
  - **Knowledge Diversity**: Covering various mathematical domains and concepts.

- **Multi-Stage Filtering Process**:
  - Start with **millions of math problems** from various available datasets.
  - **Initial difficulty filtering**:
    - Use **Qwen2.5-Math-7B-Instruct** to eliminate problems solvable within **a few attempts**.
  - **Advanced filtering**:
    - Remaining problems are evaluated by **state-of-the-art reasoning models**.
    - Retain only problems where **even the strongest models struggle to solve them consistently**.
  - **Strategic selection**:
    - Ensure **balanced representation** across **math domains and complexity levels**.
    - **Avoid conceptual redundancy**.
  - **Outcome**:
    - **817 carefully curated problems**.

### **Reasoning Chain Construction**

- **Solution Selection Strategy**:
  - Collect official solutions (if available) and supplement with solutions from **human experts** and **AI experts**.
  - Use **advanced reasoning models** to generate **diverse solutions**.
  - Apply **self-distillation techniques** to refine additional responses.
  - **Filter and validate** solutions to build a **high-quality reasoning set**.

---

## **2. Model Training**

### **Foundation Model**

- **Base model**: **Qwen2.5-32B-Instruct**, fine-tuned using **Supervised Fine-Tuning (SFT)** on the LIMO dataset.

### **Training Protocol**

- Apply **full parameter fine-tuning** with **DeepSpeed ZeRO-3** and **FlashAttention-2**.
- Max token length **16,384 tokens**.
- After training on **only a few hundred SFT samples**, the model **integrates meta-reasoning tasks into a unified reasoning chain**.
