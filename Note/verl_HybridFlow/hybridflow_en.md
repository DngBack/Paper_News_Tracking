# HybridFlow: A New Framework for Reinforcement Learning from Human Feedback (RLHF)

This paper introduces **HybridFlow**, a new framework designed to improve the **flexibility** and **efficiency** of RLHF dataflows.

## Key Aspects of HybridFlow

### Hybrid Programming Model

- Combines **single-controller** and **multi-controller** paradigms for flexible and efficient RLHF dataflow execution.
- Uses a **hierarchical API** to decouple computation and data dependencies.
- Enables **efficient operation orchestration** and flexible mapping to various devices.

### 3D-HybridEngine

- Designed for **efficient actor model training and generation**.
- Introduces **zero memory redundancy**.
- Reduces **communication overhead** during model parameter resharding between training and generation stages.

### Auto-Mapping Algorithm

- Automatically identifies **optimized GPU allocation** and **placement** for each model in the RLHF dataflow.

## Performance

- Experiments show **1.53x to 20.57x** throughput improvement compared to state-of-the-art baselines.

## Key Features

### Flexibility

- Easily represents and executes **diverse RLHF dataflows**.
- Supports different RLHF algorithms with **modular API design**, allowing adjustments in numerical computations.

### Efficiency

- **3D-HybridEngine** improves computational efficiency with:
  - **Zero memory redundancy**.
  - **Reduced communication overhead** in model parameter resharding.
- **Single-controller design** efficiently coordinates:
  - **Data transfer**.
  - **Execution order**.
  - **Resource virtualization** across distributed models.

### Heterogeneous Model Support

- Handles different model types in RLHF:
  - **Actor**
  - **Critic**
  - **Reference**
  - **Reward**
- Adapts to varying workloads, memory footprints, and computational demands.

### Ease of Use

- Abstracts away **distributed computing complexities**.
- Enables RLHF implementation with just **a few lines of code**.
- Runs RLHF through a **single process** in the single-controller design.

## Conclusion

**HybridFlow** simplifies the implementation and optimization of RLHF workflows, offering a balance between **flexibility**, **efficiency**, and **ease of use**.
