---
title: "Forest Sequence Log-Concavity"
description: "Research project investigating whether vertex-set-indexed forest sequences are log-concave."
---

## {{ hl("forest-sequence", "Polymath Jr — Forest Sequence Log-Concavity") }}

As part of the [Polymath Jr](https://geometrynyc.wixsite.com/polymathreu) summer research
program, I worked with **Team Forest** on the following question:

> **Is the vertex-set-indexed forest sequence log-concave?**

Given a graph $G$ on $n$ vertices, the _forest sequence_ $\{f_k(G)\}$ counts the number
of forests on exactly $k$ vertices of $G$. Log-concavity of such sequences is a natural
question in algebraic combinatorics, motivated by connections to matroid theory and
Lorentzian polynomials.

Our team used the [PatternBoost / Axplorer](https://axiommath.ai/) framework which is an
AI-guided search pipeline that combines transformer models with local search to
greedily search for counterexamples. We successfully found graphs whose forest
sequences **fail to be log-concave**, disproving the conjecture.

**Tools & Methods:**
- PatternBoost algorithm (transformer + greedy local search)
- Python, NumPy


Check out our [repo](https://github.com/agastya-arora/TeamForestAxplorer) and our [report](/static/docs/forest.pdf)
