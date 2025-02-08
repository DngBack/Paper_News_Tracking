# ThinkSmarternotHarder: AdaptiveReasoningwith Inference AwareOptimization

The paper addresses several problems related to reasoning in large language models (LLMs):

- Uni-modal behavior of long reasoning-chain models: Advanced long reasoning-chain models tend to use unnecessarily long reasoning traces even for trivial questions. This leads to higher inference costs and increased carbon footprints.
- Need for query-adaptive reasoning length: The paper aims to enable multi-modal behavior in reasoning models, where the length of reasoning traces is automatically adjusted based on the difficulty of the queries.
- Balancing accuracy gain and token overhead: The paper seeks to improve token efficiency, which means achieving better accuracy with less token overhead.
- Resource allocation: The paper addresses the challenge of controlling how responses of different lengths are distributed, with the goal of optimizing inference efficiency.
- Constraint satisfaction and budget allocation: The paper aims to enable models to adhere to inference budget constraints and dynamically allocate the budget to harder problems.

- Algorithm Design: Formulates the problem as a constrained RL problem with resource allocation constraints and presents the derivation of the IBPO algorithm from an optimization perspective, resulting in a weighted iterative SFT update.
- Practical Implementation: Provides details on the practical implementation of the IBPO algorithm, including the choice of the base algorithm (Constraint Generative Policy Optimization - CGPO) and the design of the reward function. The reward function is defined as the reward margin, which is the reward advantage of a group G against all other groups.
- Acronyms, Naïve Construction G+ & Training Pipelines: Explains the construction of extended length responses, including Sequential Voting (SV) and Adaptive Sequential Voting (ASV). SV generates only responses in G+, while ASV outputs a mixture of responses of y ∈ G◦ and y ∈ G+. The section details the datasets and training pipelines used for the experiments.
- Evaluation of IBPO w/ OPTIuB: Presents the empirical results of the IBPO algorithm, demonstrating its ability to adhere to constraints and dynamically allocate the inference budget. The evaluation includes absolute improvement, efficiency, constraint following, and budget allocation.
- Conclusion & Discussions: Summarizes the IBPO framework and its benefits, including adherence to constraints and dynamic allocation of the inference budget. It also discusses limitations, broader applications, and future directions.
  The paper also includes the following appendices:
- Sample Responses: Shows example responses of ASV-IuB-50%, including voting and non-voting examples.
- Batch Accumulation: Provides a batch accumulation implementation of Algorithm 1 to mitigate the issue of limited computational resources.
- MILP Solving: Discusses the use of the SciPy MILP solver for solving the in-batch integer linear programming optimizations.
- Data Construction: Elaborates on the details of the datasets used, including Qsdpo, Agolden sdpo, Qmath, and Asample math.
- Hyperparameters: Lists the hyperparameters used for the experiments.
- Further Discussions: Includes further discussion on budget constraints and CGPO on Drl w/ LLaMA.
  The paper concludes that the IBPO framework enables models to adhere to constraints and dynamically allocate the inference budget, which can lead to improved performance and efficiency in mathematical problem-solving.
