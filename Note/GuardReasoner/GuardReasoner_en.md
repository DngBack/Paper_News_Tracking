# GuardReasoner: Towards Reasoning-based LLM Safeguards

GuardReasoner is a novel safeguard designed to enhance the safety of Large Language Models (LLMs) by equipping them with reasoning capabilities. As LLMs are increasingly deployed in safety-critical applications, ensuring their reliability and trustworthiness becomes paramount. Traditional guardrails often lack the ability to reason through complex scenarios, which can limit their effectiveness. GuardReasoner addresses this limitation by guiding the guard model to learn to reason, thereby improving performance, explainability, and generalizability.
ARXIV.ORG

How GuardReasoner Works:

Dataset Creation: The process begins with the development of the GuardReasonerTrain dataset, comprising approximately 127,000 samples and 460,000 detailed reasoning steps. This dataset is synthesized using advanced models like GPT-4o to generate comprehensive reasoning processes.
ARXIV.ORG

Reasoning Supervised Fine-Tuning (R-SFT): With the dataset in place, the guard model undergoes Reasoning Supervised Fine-Tuning. This stage aims to unlock the model's basic reasoning capabilities by training it on the synthesized reasoning data. The process is applied to base models of varying sizes, such as LLaMA 3.2 1B, 3B, and LLaMA 3.1 8B, to cater to different application needs.
ARXIV.ORG

Hard Sample Direct Preference Optimization (HS-DPO): To further enhance the model's reasoning ability, GuardReasoner employs HS-DPO. In this stage, the fine-tuned model generates multiple outputs with reasoning steps for each input. Correct outputs and their reasoning are treated as positive examples, while incorrect ones serve as negative examples. This approach focuses the model's learning on challenging cases, thereby strengthening its reasoning skills.
ARXIV.ORG

Through these stages, GuardReasoner not only improves the performance of LLMs in safety-critical tasks but also enhances their explainability by providing clear reasoning for decisions. Moreover, by focusing on complex and nuanced cases during training, the model achieves better generalization, making it more adaptable to a wide range of scenarios.
ARXIV.ORG

Extensive experiments on 13 benchmarks across three guardrail tasks have demonstrated the superiority of GuardReasoner. Notably, the 8B version of GuardReasoner outperformed GPT-4o+CoT by 5.74% and LLaMA Guard 3 8B by 20.84% in F1 score on average, highlighting its effectiveness in enhancing LLM safety.
ARXIV.ORG

For those interested in exploring or utilizing GuardReasoner, the data, code, and models (including 1B, 3B, and 8B versions) have been made publicly available on GitHub.
