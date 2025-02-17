# Critique Fine-Tuning (CFT) – Training Strategy for Critiquing Noisy Responses

**Critique Fine-Tuning (CFT)** is a training strategy for language models that focuses on learning to critique noisy responses rather than simply imitating correct ones. This approach is inspired by human learning processes, which emphasize critical thinking and deeper analysis.

## Key Aspects of CFT

- The model learns to provide critiques for noisy responses, including **identifying flaws, suggesting improvements, and verifying correctness**.
- CFT involves training the model to critique a given query-response pair, **maximizing the probability** $P(c|[x; y])$, where **c** is the critique assigned to the query-response pair **[x; y]**.
- CFT has shown **consistent improvements** over **Supervised Fine-Tuning (SFT)** on math benchmarks with different base models. **CFT can outperform SFT models by an average of 4–10 absolute points**.
- CFT can **match the performance of reinforcement learning (RL) methods** while **requiring fewer computational resources**.
- **Ablation studies** show that CFT is **robust to the source of noisy responses and the teacher critique model**.

## Experimental Methodology

To validate the effectiveness of CFT, the authors constructed a **50,000-sample dataset** from **WebInstruct**, using **GPT-4o** to generate critiques in the form of:

\[
([query; noisy response], critique)
\]

The datasets used for CFT **cover a broader range of topics but are smaller in size**, highlighting their **efficiency in boosting LLMs' reasoning abilities**.  
The training objective involves **concatenating the question $x$ and noisy response $y$ as input**, then optimizing the model parameters to generate the critique $c$.

## Experimental Results

Experiments compared **CFT with various SFT methods** on **three 7B-scale base models** using mathematical reasoning benchmarks.  
**Results:**

✅ CFT **consistently outperforms** all SFT baselines across different models.  
✅ CFT demonstrates **faster convergence** with **less training data**.
