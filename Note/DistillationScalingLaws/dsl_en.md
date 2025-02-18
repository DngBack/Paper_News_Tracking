# **Distillation Scaling Laws**

## **Introduction**

The Distillation Scaling Laws help estimate the performance of a student model after distillation. Based on the compute budget and its allocation between the teacher and student models, this law helps the research community create more capable models with lower inference and lifetime compute costs.

## **Key Findings**

### **1. Distillation Scaling Law**

- One of the key contributions of this study is a scaling law that estimates student model performance.
- This law is based on the compute budget and how it is allocated between the teacher and student models.
- It helps optimize compute to create high-performance models with lower compute costs.

### **2. Compute-Optimal Recipes**

- The paper provides specific strategies to optimize compute when using distillation.
- These strategies guide the allocation of compute resources to both teacher and student models to maximize student performance.

### **3. When Does Distillation Excel?**

Distillation is more effective than supervised pretraining under certain conditions:

#### **Multiple Students or Existing Teacher**

- If there are multiple student models to be distilled or if a suitable teacher model already exists, distillation can outperform supervised learning.
- This advantage persists up to a certain compute level, depending on student model size.

#### **Best-Case Scenario**

- In the optimal scenario, distillation outperforms supervised learning, as shown by the cross-entropy difference between the two methods.

### **4. When Is Supervised Learning Better?**

- If the goal is to train a single student model and a teacher model also needs training, supervised learning is preferable over distillation.

### **5. Role of the Teacher Model**

- The teacher's cross-entropy is the primary determinant of student cross-entropy.
- As a result, teacher size and token count may not need to be primary axes for optimization.

### **6. Fixed Compute or Token Budget**

- The paper analyzes scenarios where compute or token budgets are constrained to determine when distillation is more beneficial than supervised learning.

### **7. Compute Efficiency**

- Distillation can be more compute- and data-efficient than supervised learning when producing a desired model.

### **8. Hyperparameter Selection**

- Pure distillation with a mixing coefficient (λ) of 1 and a temperature (τ) of 1 provides robust performance across different model scales.

## **Distillation Scaling Law Formula**

The formula estimates student cross-entropy (**L_S**) based on teacher cross-entropy (**L_T**), student parameters (**N_S**), and the number of distillation tokens (**D_S**):

```math
L_S(N_S ,D_S ,L_T ) = L_T + \frac{1}{L_{c0}^T} \left(1+ \left(\frac{L_T}{\tilde{L_S}^{d1}}\right)^{\frac{1}{f1}}\right)^{-c1f1} \left(\frac{A}{N_S^{\alpha'}} + \frac{B}{D_S^{\beta'}}\right)^{\gamma'}.
```

## **Conclusion**

The "Distillation Scaling Laws" paper provides a comprehensive view of how distillation can be optimized to produce more powerful models with lower compute costs. The scaling law guides efficient compute allocation between teacher and student models, optimizing the performance of distilled models. This is a significant advancement in developing small yet effective language models for real-world applications.
