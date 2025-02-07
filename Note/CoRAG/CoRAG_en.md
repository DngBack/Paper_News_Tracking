# CoRAG: Chain-of-Retrieval Augmented Generation

This paper introduces Chain-of-Retrieval Augmented Generation (CoRAG), a method for training models that can retrieve and reason over relevant information in multiple steps before producing a final answer. Here's a breakdown of the key aspects of the paper:
Core Problem:

- Conventional Retrieval-Augmented Generation (RAG) systems typically perform a single retrieval step before generating a response. This can be limiting, especially for complex queries requiring multiple reasoning steps.
- Retrieval models, which use fixed-size vector representations for efficiency, may struggle with complex queries.
- It is often unclear what information should be retrieved initially for multi-hop reasoning tasks.
  Proposed Solution: CoRAG
- CoRAG allows the model to dynamically reformulate queries based on the current state of the reasoning process, retrieving information iteratively.
- The framework is designed to mimic the human problem-solving process, where information is sought iteratively.
- CoRAG is trained to explicitly retrieve information step by step, rather than relying solely on in-context learning.
  Training CoRAG:
- Rejection Sampling: The paper uses rejection sampling to automatically generate intermediate retrieval chains, which are sequences of sub-queries and sub-answers.
  - A language model (LLM) generates sub-queries based on the original query and preceding sub-queries and sub-answers.
  - A text retriever finds relevant documents for each sub-query, and an LLM generates the corresponding sub-answers.
  - The process iterates until a maximum chain length is reached or the answer matches the correct final answer.
  - The retrieval chain with the highest log-likelihood score is selected to augment the original QA-only dataset.
- Fine-tuning: Open-source language models are fine-tuned on the augmented datasets using standard next-token prediction objectives. The model is trained on three tasks: next sub-query prediction, sub-answer prediction, and final answer prediction.
  Test-Time Decoding Strategies:
- The paper explores various decoding strategies to manage the trade-off between performance and computational cost at test time. These strategies control token consumption and the frequency of retriever calls.
  - Greedy Decoding: Generates sub-queries and sub-answers sequentially using greedy decoding.
  - Best-of-N Sampling: Samples N retrieval chains and chooses the best one to generate the final answer, based on a penalty score.
  - Tree Search: Uses a breadth-first search variant with retrieval chain rollouts.
    Experimental Results:
- CoRAG significantly outperforms strong baselines in multi-hop question answering (QA) tasks.
- The model achieves new state-of-the-art performance on the KILT benchmark across diverse knowledge-intensive tasks.
- The performance of CoRAG scales with increased test-time computation (longer retrieval chains), following an approximate log-linear relationship between token consumption and model performance.
- The framework exhibits robustness against retrievers of varying quality.
- CoRAG can effectively decompose complex queries and perform flexible query reformulation to improve the quality of generated responses.
  Key Findings and Analysis:
- Iterative Training: Iterative rejection sampling, where a trained CoRAG model is used to generate new sets of retrieval chains, showed mixed results, suggesting that instruction-tuned LLMs already generate high-quality retrieval chains.
- Weak-to-strong generalization: Employing weaker LLMs for retrieval chain generation and stronger LLMs for training is a viable strategy.
- Chain-of-Retrieval: The chain-of-retrieval mechanism is most beneficial for complex multi-hop questions; for simpler questions, the gains are marginal.
- Learning to Stop: The model can learn to stop retrieving information at test time, which can save tokens at the cost of performance degradation.
- The paper also analyzes the impact of various factors like different retrievers, rejection sampling size, and sampling temperature on the model's performance.
  Overall, CoRAG is a promising approach for improving the factual accuracy and reliability of RAG systems by enabling models to reason and retrieve information iteratively.
