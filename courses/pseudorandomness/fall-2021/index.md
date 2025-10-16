# **CS 294-202 Pseudorandomness (Fall 2021)**

## Course Description:

Randomized algorithms give a broad and rich algorithmic toolkit (e.g., sampling, Monte Carlo methods). Randomness is an essential resource in distributed computing, cryptography, and interactive proofs. In this course, we would explore the role of randomness in computation: Can we derandomize algorithms without changing their time or space complexity? Can we "purify" randomness from a weak source of randomness?

Pseudo-randomness is the property of "appearing random" while having little or no randomness. Pseudo-randomness plays a significant role in error-correcting codes, expander graphs, randomness extractors, and pseudo-random generators. In this course, we will see all these beautiful applications. In the second part of the course, we would focus on the question of derandomization of small-space computation, also known as the "**RL** versus **L**" question. It asks whether all problems that can be decided in randomized logarithmic space (RL) can also be decided in deterministic logarithmic space (L). We would cover recent approaches towards showing that RL = L.

Undergraduate students who wish to take this class should fill out the following [Google Form](https://docs.google.com/forms/d/1O-O7mAX8B86BW3_BntKQSofifxKp1zN1K8sP2CyIbmo/edit).

## General Information:

**Time and Place:** Tuesday, Thursday 3:30-5:00 PM, Soda 405

**Office Hours:** Monday 3:00-4:00 PM (via Zoom).

**Instructor:** [Avishay Tal](http://www.avishaytal.org/), atal "at" berkeley.edu

**TA:** [Kewen Wu](https://shlw.github.io), shlw\_kevin \[at\] hotmail \[dot\] com

**Grading:** Homeworks - 40% (4 assignments), Final Project & Presentation - 50%, Scribes - 10%.

**Prereqs:** CS170 or equivalent is required.

[**Gradescope**](https://www.gradescope.com/courses/310808)

[**Piazza**](http://piazza.com/berkeley/fall2021/cs294202)

**Textbook:** - Salil Vadhan - [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/)

## Problem Sets:

- [Homework 1](https://drive.google.com/open?id=1hWKWDmRkJJia3IJtIk6KL7TtoxcKmIsk) \- Due Monday, Sep 20.

- [Homework 2](https://drive.google.com/open?id=1a5sh-HBUEWbI6oYCibVLmszw70akgI9k) \- Due Wednesday, Oct 6.

- [Homework 3](https://drive.google.com/open?id=1fEZuPwn8l5YjafzLJ5_m9FlYhcAsJrUw) \- Due Thursday, Oct 21.

- [Homework 4](https://drive.google.com/open?id=1dg-36TBTuEr4NSfberBIsKZL44GF-yq6) \- Due Thursday, Nov 18.

## Topics:

- k-wise Independence

- ε-Biased Distributions

- Error Correcting Codes

- Expander Graphs - Cheeger's Inequality, Zig-Zag Product, SL=L

- Pseudorandom Generators - NW Construction

- Randomness Extractors

- Connections between all the above

- Derandomization of Small-Space Computation

## Lectures:

01. Introduction + derandomizing an approximation algorithm Max-Cut [Lecture note](https://drive.google.com/file/d/1AylPHRG8TgqdpkJz_WMSEEyLG0YMu9KW/view?usp=sharing)

02. k-wise independence [Lecture note](https://drive.google.com/file/d/1SpP7xnUiQDhBTVa3ZRQnFhd3HrUejgt_/view?usp=sharing)

03. Error reduction + Intro to PRGs [Lecture note](https://drive.google.com/file/d/1pc0-e1HMoyNriLldOl6woZcJ-wtcWMJl/view?usp=sharing)

04. Construction of small biased distributions \[AGHP\] + Brief introduction to discrete Fourier analysis [Lecture note](https://drive.google.com/file/d/1S_AvJTF7X_XcfgdguQ7Zb1oyridoL03R/view?usp=sharing)

05. Error correcting codes, Code concatenation, Connections between small biased distributions and error correcting codes [Lecture note](https://drive.google.com/file/d/1TS8SQTH2IVrGJI-CeLi4Na0pj4_Yj0g_/view?usp=sharing)

06. Expander Graphs - Combinatorial Definition, Existence using the Probabilistic Method [Lecture note](https://drive.google.com/file/d/1NJjWe9j8aaMEg2nBXjDMAbe-jYTuqCFD/view?usp=sharing)

07. Spectral Expansion [Lecture note](https://drive.google.com/file/d/1x9xsz1ernnL0hfdCdDjTFwZINuOGNbPe/view?usp=sharing)

08. Expander Mixing Lemma [Lecture note](https://drive.google.com/file/d/1HbDcD9_ETZ1oA-gfp-WHgAPxBSGeYnts/view?usp=sharing)

09. Random Walks on Expanders [Lecture note](https://drive.google.com/file/d/1At8nZc41fnw47YKjtIVDBn-sGlg2m_27/view?usp=sharing)

10. Zig-Zag Product [Lecture note](https://drive.google.com/file/d/1MJ5RuhabE6nod8li_E1YUQCawfEoPUwW/view?usp=sharing)

11. SL=L [Lecture note](https://drive.google.com/file/d/1pESAOH0UOV49Uv1DrSEsKkv5hB0G7fJy/view?usp=sharing)

12. Randomness Extractors: Definition, Existence of Seeded-Extractors, Leftover Hash Lemma [Lecture note](https://drive.google.com/file/d/1OE04MdyJduQgPjW7eNrTgTpyJO4Ead2u/view?usp=sharing)

13. Seeded-Extractors: Graph Theoretic View, Samplers [Lecture note](https://drive.google.com/file/d/1uU8uy90v7K7fmf4ydbZNiQLoCssXpQTt/view?usp=sharing)

14. Pseudorandom Generators: Next-Bit Unpredictability [Lecture note](https://drive.google.com/file/d/1McBjUTYeD1iP5GkM6y9fxDCu9oONhfaq/view?usp=sharing)

15. Pseudorandom Generators: the Nisan-Wigderson Construction [Lecture note](https://drive.google.com/file/d/1HLUmaRtOhpbI7G3wuJtfVdwIQsulhVql/view?usp=sharing)

16. Trevisan's Extractor [Lecture note](https://drive.google.com/file/d/1b1jJCCeTNTx0rATUAjD35T6i5uI-8kXi/view?usp=sharing)

17. Two-Source Extractor [Lecture note](https://drive.google.com/file/d/1MxNthKi-Hi9p0OWoxBZUg4uqkT4-RAY3/view?usp=sharing)

**Derandomizing Small-Space Computation:**

18. Nisan's PRG [Lecture note](https://drive.google.com/file/d/1DXdmCAf6rqARVFwFx4h6kpI1Mk2a4iJN/view?usp=sharing)

19. Nisan-Zuckerman's PRG [Lecture note](https://drive.google.com/file/d/1-49OGVmQaUa9rXz7Yc61GsIUx0VKcySo/view?usp=sharing)

20. Saks-Zhou: BPL in L^{3/2} [Lecture note](https://drive.google.com/file/d/1hsojoXRGau1yLjLvebyoEBL0prYyzvts/view?usp=sharing)

21. Ajtai-Wigderson Framework: Random-Restriction Based PRGs [Lecture note](https://drive.google.com/file/d/1RY-ovManA-VC00muFuKAlxQwDYHyPjpO/view?usp=sharing)

22. Forbes-Kelley: Fooling Read-Once Branching Programs in any Order [Lecture note](https://drive.google.com/file/d/1YQui9DaAg4rzuivsYHrCtn384RfG67Rm/view?usp=sharing)

23. Cheng-Hoza: Hitting Sets Give Two-Sided Derandomization of Small Space [Lecture note](https://drive.google.com/file/d/13KFoyY6D57SkDWlo0GHgWe14kkL06Z5i/view?usp=sharing)

24. Fractional PRGs and Polarizing Random Walks [Lecture note](https://drive.google.com/file/d/11GODwOXkJeT03DYV6UNja4E0Cdoyufxh/view?usp=sharing)

## Student Final Projects:

- [Survey of Interlacing Families for Bipartite Ramanujan Graphs](https://drive.google.com/file/d/1C9nJtrFQsuKts0K4aE9I2HdF8k1AcG8a/view?usp=sharing) by Aaron (Louie) Putterman and Saachi Mutreja

- [Pseudorandom Walks: 2006 and Now](https://drive.google.com/file/d/16HQlaXgO6o2WG4JoHIpERCHrv50AxzxM/view?usp=sharing) by Nathaniel Young and Vint Lee

- [Fractional Pseudorandom Generators from Any Fourier Level](https://drive.google.com/file/d/1vOEODRNPFEDXLqcaHpY2stLvWzR-3sMY/view?usp=sharing) by Ishaq Aden-Ali and Nathan Ju

- [Fooling Polytopes](https://drive.google.com/file/d/1VJquW2hM6HuwFoJKNlM9OPuS-2DwqUzq/view?usp=sharing) by Isaac Merritt, Justin Yokota, and Yuwen Zhang

- [Constructions of near-Ramanujan Graphs](https://drive.google.com/file/d/1wD80rcQ37S9kpm4lMKRdtBngacbufnmr/view?usp=sharing) by Andrew Lin and Ansh Nagda

- [PRGs for Polynomial Threshold Functions](https://drive.google.com/file/d/15i9m35oQt9HDd7FJCOPycK4Lw_6AkkNc/view?usp=sharing) by Thiago Bergamaschi and Yinuo Zhang

- [Expander Random Walks: A Fourier-Analytic Approach](https://drive.google.com/file/d/19xBoe5tmOexr0NlDSbI9x4y_WdT_Kyhu/view?usp=sharing) by Devon Ding and Xin Lyu

- [PRGs for Monotone Read-Once Branching Programs](https://drive.google.com/file/d/1MPlKxIKHh9UctYbaUXqJ_f1aDiF5Nig1/view?usp=sharing) by Zoë Bell and Malvika Raj

- [Computational Extractors & Applications](https://drive.google.com/file/d/1cpdNbCdVuqExw4WFV-hxF6FAQcY8AMum/view?usp=sharing) by Jialin Li and Dhanya Jayagopal

## Additional Reading:

- [Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf) by [Ryan O'Donnell](https://www.cs.cmu.edu/~odonnell/).

- [Simple Construction of Almost k-wise Independent Random Variables](https://www.wisdom.weizmann.ac.il/~oded/p_aghp.html) by Alon, Goldreich, Håstad, Peralta

- [Expander Graphs and Their Applications](https://www.cs.huji.ac.il/~nati/PAPERS/expander_survey.pdf) by Hoory, Linial, Wigderson
