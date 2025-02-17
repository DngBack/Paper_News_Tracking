# **RSD (Reward-Guided Speculative Decoding)**

**RSD improves LLM inference efficiency by combining a lightweight draft model with a more powerful target model, using a reward function to guide output selection at each step.**

## **1. Draft and Target Models**

RSD leverages two models:

- **Draft Model:** A small, fast model that generates candidate steps.
- **Target Model:** A larger, more reliable model used for verification and refinement.

## **2. Reward Function**

- The reward function \( r(y*i | z_i) \) evaluates the quality of each generated step \( y_i \) within the sequence \( y*{1:i} \) given the prompt \( x \).
- A higher reward indicates a greater likelihood that the model output aligns with the desired response.

## **3. Adaptive Selection**

- Unlike **traditional speculative decoding**, which enforces strict unbiasedness, RSD uses reward signals to **adaptively select high-value draft outputs** rather than discarding mismatched tokens outright.

## **4. RSD Algorithm Steps**

1. **Generate Draft Step:** The draft model generates a candidate step \( \hat{y}\_i \).
2. **Compute Reward:** The reward function \( r(y_i | z_i) \) evaluates the step’s quality.
3. **Apply Acceptance Criterion:**
   - If \( r*i \) meets the criterion \( A*\omega(r_i) \), \( \hat{y}\_i \) is accepted.
   - Otherwise, the target model \( M \) generates a new step.
4. **Sample from Mixture Distribution:**
   - Accepted steps come from \( P_m \) (draft model).
   - Rejected steps come from \( P_M \) (target model).
5. **Repeat Until Termination:** The process continues until the end-of-sequence (EOS) token appears or the sequence reaches a maximum length \( N \).

## **5. Dynamic Mixing with Weighting Functions**

RSD defines a distribution \( P\_{RSD} \) as a **dynamic mixture** of the draft model (\( P_m \)) and the target model (\( P_M \)):

\[
P\_{RSD}(y_i | z_i) = w(y_i | z_i) P_m(y_i | z_i) + v(y_i | z_i) P_M(y_i | z_i)
\]

Where:

- **\( w(\cdot) \) and \( v(\cdot) \)** are weighting functions that dynamically adjust based on the quality of the output \( y_i | z_i \).
- **\( v(y_i | z_i) = \nu \)** where \( \nu \) is a constant, ensuring that the target model always acts as a fallback.
- **\( w(y_i | z_i) = \omega r(y_i | z_i) = \omega(r(y_i | z_i)) \)**, where \( \omega(\cdot) \) maps the reward into a confidence score for \( P_m \).

## **6. Weighting Function Behavior**

- **When \( r(y_i | z_i) \) is high:**
  - \( \omega(r(y_i | z_i)) \to 1 \), so \( P_m \) dominates the mixture.
  - The system trusts the draft model to generate efficient outputs.
- **When \( r(y_i | z_i) \) is low:**
  - \( \omega(r(y_i | z_i)) \to 0 \), so \( P_M \) dominates the mixture.
  - The target model ensures robustness by handling low-quality outputs.

## **7. Optimal Weighting**

The optimal weighting function for maximizing reward under a constrained sampling budget is a **binary step function**:

\[
\omega*r(y|z) =
\begin{cases}
1, & \text{if } r(y|z) \geq \delta*\gamma(z) \\  
0, & \text{if } r(y|z) < \delta\_\gamma(z)
\end{cases}
\]

Where \( \delta\_\gamma(z) \) is the largest possible threshold that satisfies the constraint.

## **8. Process Reward Models (PRMs)**

- RSD employs **Skywork-o1-Open-PRM** as the **Process Reward Model (PRM)**.
- The reward score ranges from 0 to 1, with higher scores being better.
- The PRM is invoked at each reasoning step to rate the quality of the step.

## **9. Summary**

RSD dynamically adjusts when to invoke the larger model, **significantly reducing unnecessary computations while maintaining or surpassing traditional inference quality**.

This balance between **cost and quality** is particularly important in large-scale applications where **both efficiency and performance** are critical.
