# **Benders Decomposition for the Stochastic Capacitated Facility Location Problem (CFLP)**  

This project provides a **Python implementation of Benders decomposition** to efficiently solve the **Stochastic Capacitated Facility Location Problem (CFLP)** using the **Gurobi Optimizer**. The code demonstrates an effective approach to **modeling the CFLP as a Mixed Integer Program (MIP)** and solving it efficiently through **Benders decomposition**, leveraging **Gurobi's callback functionality**.  

### **Key Features**  

- **Modular and extensible design** for easy customization of the stochastic CFLP formulation based on different problem sizes and parameters.  
- **Comprehensive implementation** showcasing how to integrate Gurobi, formulate **advanced MIP models**, and apply **Benders decomposition** dynamically.  
- **Python-based optimization framework** suitable for researchers, practitioners, and students interested in **facility location, logistics, and large-scale optimization**.  

---

## **Stochastic CFLP Overview**  

The **Stochastic Capacitated Facility Location Problem (CFLP)** is a fundamental **facility location** problem where facilities must be opened, and customer demand must be allocated while considering **uncertainty in demand**. The goal is to **minimize total costs**, including:  
1. **Fixed costs** for opening facilities.  
2. **Variable transportation costs** for serving customers under different demand scenarios.  

### **Mathematical Formulation**  

#### **Sets and Parameters**  

- $I$: Set of customers.  
- $J$: Set of candidate facility locations.  
- $S$: Set of demand scenarios.  
- $fj $: Fixed cost of opening a facility at location $j \in J$.  
- $c_{ij}$: Transportation cost per unit from facility $j$ to customer $i$.  
- $d_{i,s}$: Demand of customer $i$ under scenario $s$.  
- $u_j$: Capacity of facility $j$.  

#### **Decision Variables**  

- $x_{ij,s}$: Amount of demand from customer $i$ served by facility $j$ in scenario $s$.  
- $y_j$: Binary variable indicating whether facility $j$ is open $1$ or closed $0$  

#### **Objective Function**  

The objective is to **minimize the total cost**, including **fixed facility costs** and **expected transportation costs**:  

```math
\text{minimize} \quad \sum_{j \in J} f_j y_j + \frac{1}{|S|} \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij,s}
```

#### **Constraints**  

- **Demand satisfaction:** Every customer's demand must be met.  
```math
\sum_{j \in J} x_{ij,s} \geq d_{i,s},\quad \forall i \in I, \forall s \in S
```

- **Capacity constraint:** Each facility cannot exceed its capacity if opened.  
```math
\sum_{i \in I} x_{ij,s} \leq u_j y_j, \quad \forall j \in J, \forall s \in S
```

- **Variable domains:**  
```math
x_{ij,s} \geq 0, \quad y_j \in \{0, 1\}
```

---

## **Benders Decomposition Approach**  

Benders decomposition efficiently handles large-scale **stochastic CFLPs** by **decomposing** them into smaller subproblems. The approach iterates between:  

1. **Master Problem** (Facility location decisions).  
2. **Subproblems** (Optimal demand allocation for given facility locations).  

The process continues **iteratively**, refining decisions until convergence.  

### **Master Problem**  

The **master problem** selects facilities to open and introduces an **auxiliary variable** $ \eta_s $ to estimate subproblem costs.  

```math
\begin{aligned}
    & \text{minimize} \quad && \sum_{j \in J} f_j y_j + \frac{1}{|S|} \eta_s \\
    & \text{subject to} && \sum_{j \in J} u_j y_j \geq \max_{s \in S} \sum_{i \in I} d_{i,s}, \\
    &&& \eta_s \geq 0, \quad \forall s \in S \\
    &&& y_j \in \{0, 1\}, \quad \forall j \in J.
\end{aligned}
```

This ensures enough capacity is available while keeping costs minimal.  

### **Subproblem**  

For a given facility selection $ \bar{y} $, the **subproblem** optimally assigns demand, minimizing transportation costs:  

```math
\begin{aligned}
    \psi(\bar{y}) ={} & \min\ && \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij,s}\\
    & \text{s.t.} && \sum_{j \in J} x_{ij,s} \geq d_{i,s}, \quad \forall i \in I \\
    &&& \sum_{i \in I} x_{ij,s} \leq u_j \bar{y}_j, \quad \forall j \in J \\
    &&& x_{ij,s} \geq 0.
\end{aligned}
```

If $ \psi_s^\ast(\bar{y}) $ exceeds \( \bar{\eta_s} \), an **optimality cut** is generated.  

### **Optimality Cut Generation**  

From the **dual of the subproblem**, the **optimality cut** is:  

```math
\eta_s \geq \sum_{i \in I} \mu^\ast_{i,s} d_{i,s} - \sum_{j \in J} \nu^\ast_{j,s} u_j y_j
```

These **cuts** are added iteratively, refining the master problem for faster convergence.  

---

## **Implementation Details**  

This project utilizes **Gurobi's callback mechanism** to dynamically add **Benders cuts** during the branch-and-bound process, significantly improving computational efficiency.  

### **Key Files**  

- **`data.py`**: Generates problem instances with customizable parameters.  
- **`main.py`**: Entry point for solving the CFLP using Benders decomposition.  
- **`master_problem.py`**: Defines the master MIP model using **Gurobi**.  
- **`callbacks.py`**: Implements **Benders decomposition** via a callback function.  
- **`subproblem.py`**: Solves the **LP subproblem** and retrieves dual values for cuts.  
- **`requirements.txt`**: Lists dependencies for easy installation.  

### **Gurobi Callback Usage**  

- Extracts **current master problem solution**.  
- Solves **subproblem** and retrieves **dual variables**.  
- **Generates and adds optimality cuts dynamically**.  

This **adaptive approach** speeds up convergence by **reducing the search space**.  

---

## **References**  

- **Wentges, P.** (1996). Accelerating Benders' decomposition for the capacitated facility location problem. *Mathematical Methods of Operations Research*, **44**, 267–290.  
  [DOI:10.1007/BF01194335](https://doi.org/10.1007/BF01194335)  
- [Benders Decomposition (Wikipedia)](https://en.wikipedia.org/wiki/Benders_decomposition)  
- [Gurobi Optimizer](https://www.gurobi.com/solutions/gurobi-optimizer/)  
- [GurobiPy Python Interface](https://pypi.org/project/gurobipy/)  

---

This **Python-based Benders decomposition framework** provides a **scalable and efficient solution** to the **Stochastic CFLP**, making it a valuable tool for research, logistics, and facility location problems. 🚀
