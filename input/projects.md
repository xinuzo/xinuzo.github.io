---
title: Projects
description: University and research projects by Rendi Adinata.
---

A selection of projects from my university coursework and research programs.

---

## {{ hl("forest-sequence", "Polymath Jr — Forest Sequence Log-Concavity") }}

As part of the [Polymath Jr](https://geometrynyc.wixsite.com/polymathreu) summer research
program, I worked with **Team Forest Axplorer** on the following question:

> **Is the vertex-set-indexed forest sequence log-concave?**

Given a graph $G$ on $n$ vertices, the _forest sequence_ $\{f_k(G)\}$ counts the number
of forests on exactly $k$ vertices of $G$. Log-concavity of such sequences is a natural
question in algebraic combinatorics, motivated by connections to matroid theory and
Lorentzian polynomials.

Our team used the [PatternBoost / Axplorer](https://axiommath.ai/) framework — an
AI-guided search pipeline that combines transformer models with local search — to
systematically hunt for counterexamples. We successfully found graphs whose forest
sequences **fail to be log-concave**, disproving the conjecture.

**Tools & Methods:**
- PatternBoost algorithm (transformer + greedy local search)
- Python, PyTorch, NumPy, NetworkX
- Combinatorial optimization on bipartite graphs

[GitHub](https://github.com/xinuzo)

---

## {{ hl("turing-machine", "Turing Machine — Repeated String Detector") }}

A project from my **Algorithm Design** course at ITB. The goal was to design and
hand-write Turing machine code that detects whether an input string consists of a
repeated pattern — i.e., whether the string can be written as $w^k$ for some
substring $w$ and integer $k \geq 2$.

Writing a Turing machine by hand to solve this problem was an exercise in patience
and precision. Every state transition had to be meticulously planned, and debugging
meant tracing tape movements step by step. It was extremely challenging, but deeply
rewarding as an exercise in understanding the foundations of computation.

**What I learned:**
- Low-level state-machine design and tape manipulation
- The gap between "theoretically computable" and "practically implementable"
- Deep appreciation for the abstractions modern programming languages provide

[GitHub](https://github.com/xinuzo/Turing_Machine_Repeated_String)
