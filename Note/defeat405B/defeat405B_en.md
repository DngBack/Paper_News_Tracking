# Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling

## English Version

The paper **"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"** investigates how smaller language models (LLMs) can outperform larger ones by using compute-optimal test-time scaling (TTS). TTS is a method that improves the performance of LLMs by allocating additional computation during the inference phase. The paper addresses two main questions:

1. What is the optimal way to scale test-time computation across different policy models, Process Reward Models (PRMs), and levels of problem difficulty?
2. To what extent can extended computation improve the performance of LLMs on complex tasks, and can smaller language models outperform larger ones through this approach?

### Key Concepts and Methods

- **Test-Time Scaling (TTS):** Enhances LLM reasoning by allocating more computation at inference time. There are two types of TTS:
  - **Internal TTS:** Trains LLMs to "think" slowly using long Chain-of-Thought (CoT).
  - **External TTS:** Improves reasoning via sampling or search-based methods with fixed LLMs. The challenge here is to optimally scale compute for each problem.
- **Process Reward Models (PRMs):** Guide the generation process and select the final answer, effectively scaling test-time compute. In other words, PRMs act as verifiers in the TTS process.
- **Compute-Optimal TTS:** Aims to allocate the optimal computation for each problem. The paper argues that the compute-optimal TTS strategy depends heavily on the specific policy model, PRM, and problem difficulty level.
- **Policy Models:** LLMs that generate solutions.
- **Markov Decision Process (MDP):** The reasoning problem is formulated as an MDP, defined by the tuple \(S, A, P, R, \gamma\), where \(S\) is the state space, \(A\) is the action space, \(P\) is the transition function, \(R\) is the reward function, and \(\gamma\) is the discount factor.
- **Best-of-N (BoN):** The policy model generates N responses, and scoring and voting methods are used to select the final answer.
- **Beam Search:** The policy model generates steps, and a verifier selects the top steps for subsequent search. This process repeats until the maximum depth is reached or an end-of-sequence token is generated.
- **Diverse Verifier Tree Search (DVTS):** Extends beam search by dividing the search process into subtrees, each explored independently using beam search.
- **Reward-Aware Compute-Optimal TTS:** A strategy that integrates the reward function into the compute-optimal TTS framework. This strategy ensures that compute-optimal scaling adapts to the policy model, prompt, and reward function, leading to a more general framework for practical TTS.

### Experiments and Results

The paper conducts experiments on MATH-500 and AIME24 datasets using PRMs ranging from 1.5B to 72B parameters and policy models ranging from 0.5B to 72B parameters. The key findings include:

- The compute-optimal TTS strategy is highly dependent on the choice of policy model, PRM, and problem difficulty.
- Smaller models can outperform larger models using compute-optimal TTS. For example, a 3B LLM can outperform a 405B LLM.
- The optimal TTS method depends on the PRM used. BoN outperforms other strategies when using Math-Shepherd and RLHFlow PRMs, while search-based methods perform better with Skywork and Qwen2.5-Math PRMs.
- The optimal TTS method varies with policy models. For small policy models, search-based methods outperform BoN, while for large policy models, BoN is more effective.
- The optimal TTS methods vary with different difficulty levels. For small policy models, BoN is better for easy problems, while beam search works better for harder problems.
- PRMs are biased towards the length of steps. The training data of RLHFlow-PRM-Deepseek-8B is longer than that of RLHFlow-PRM-Mistral-8B, leading to a bias towards longer outputs.
- PRMs are sensitive to voting methods. Skywork-PRM-7B works better with PRM-Vote than with PRM-Max, while Qwen2.5-Math-PRM-7B is not very sensitive to voting methods.

### Impact of Compute-Optimal TTS

- **Performance Improvement:** Llama-3.2-3B-Instruct with compute-optimal TTS outperforms Llama-3.1-405B-Instruct on MATH-500 and AIME24.
- **Efficiency:** Compute-optimal TTS can be more efficient than majority voting and can significantly improve reasoning performance over CoT.
- **Comparison with Long-CoT Methods:** TTS with Qwen2.5-7B-Instruct outperforms rStar-Math, Eurus-2, SimpleRL, and Satori on both MATH-500 and AIME24.

### Limitations

The paper identifies the following limitations and future directions:

- Extending TTS to more tasks such as coding and chemistry tasks.
- Exploring more effective methods for compute-optimal TTS.
