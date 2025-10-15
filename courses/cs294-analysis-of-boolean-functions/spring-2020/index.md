# **CS 294-92: Analysis of Boolean Functions (Spring 2020)**

Boolean functions are central objects of study in theoretical computer science and combinatorics. Analysis of Boolean functions, and in particular Fourier analysis, has been a successful tool in the areas of circuit lower bounds, hardness of approximation, social choice, threshold phenomena, pseudo-randomness, property testing, learning theory, cryptography, quantum computing, query complexity, and others.

These applications are derived by understanding fundamental beautiful concepts in the study of Boolean functions, such as influence, noise-sensitivity, approximation by polynomials, hyper-contractivity, and the invariance-principle (connecting the discrete Boolean domain with the continuous Gaussian domain).

We will study these foundational concepts of Boolean function as well as their applications to diverse areas in TCS and combinatorics.

**Textbook:**

The course will be mainly based on the wonderful [book](http://analysisofbooleanfunctions.net) by Ryan O'Donnell. The book is available for **free download** via this [link](http://get.analysisofbooleanfunctions.net), or available for purchase on Amazon.

In addition, we will highlight some recent exciting results that are not covered in the book.

## General Information:

**Semester:** Spring 2020

**Time and Place:** Tuesday, Thursday 5:00-6:30 PM -- 310 Soda Hall

**Instructor:** [Avishay Tal](http://www.avishaytal.org), Soda 635, atal "at" berkeley.edu

**Office Hours:** Monday 1:30-3:30 PM

**TA:** [Orr Paradise](http://people.eecs.berkeley.edu/~orrp/), Soda 626, orrp "at" eecs.berkeley.edu

**Office Hours:** Wednesday 2:30-3:30 PM (or fix an appointment by email). Please send questions/topics in advance.

**Grading:** Homeworks - 40% (4 assignments), Participation in class - 10%, Final Project & Presentation - 50%. Scribe - an exempt from one problem set and 10%.

## Problem Sets:

- [Homework 1](https://drive.google.com/open?id=1bb_sOPWWwCsDsT9pmGBlji5hDFZ_QB2q) \- Due Monday, Feb 10.

- [Homework 2](https://drive.google.com/open?id=1RPgTEehW_EZtlmZrjjwqX0b7fae3AUlS) \- Due Friday, Feb 28.

- [Homework 3](https://drive.google.com/open?id=1ur1V858TdKhk-ytZe2wS1E85U3Xyn9Fu) \- Due Tuesday, Mar 31.

- [Homework 4](https://drive.google.com/open?id=1L2huhm3Yp1HX8VwY_HI9YzRakRkI1gEd) \- Due Tuesday, May 5.
Discussions:[Piazza](https://piazza.com/class/k5swc8w6mn82f)

HW submissions: [Gradescope](https://www.gradescope.com/courses/85615)

## Topics (not necessarily in that order):

**Property Testing:**

\- Linearity Testing \[Blum-Luby-Rubinfeld\]

**Influence and Hypercontractivity:**

\- Arrow's Theorem (Kalai's Proof)

\- Bonami-Beckner Theorem

\- The Influence of Variables on Boolean Functions \[Kahn-Kalai-Linial\]

\- Friedgut's Junta Theorem

**Learning Theory:**

\- The Goldreich-Levin Algorithm (stemming from cryptography)

\- Learning Shallow Circuits \[Linial-Mansour-Nisan\]

\- Learning DNFs and Mansour's conjecture

\- Learning Juntas \[Mossel-O'Donnell-Servedio\]

**Circuit Complexity:**

**\-**Random Restrictions

\- Parity not in AC0: the Switching Lemma \[Håstad\]

\- Shrinkage of De Morgan Formulae \[Håstad\]

**Pseudo-randomness:**

\- Small-biased distributions \[Naor-Naor\]

\- Pseudo-randomness for low-degree functions \[Bogdanov-Viola, Lovett, Viola\].

\- Pseudo-randomness based on random restrictions \[Ajtai-Wigderson, Gopalan-Meka-Reingold-Trevisan-Vadhan, Steinke-Reingold-Vadhan\]

\- Fractional pseudo-random generators and polarizing random walks \[Chattopadhyay-Hatami-Hosseini-Lovett\]

**Hardness-of-Approximation:**

\- The unique-games conjecture and its implications.

**The Invariance Principle:**

\- Central limit theorems \[Berry–Esseen\]

\- "Majority is Stablest" \[Mossel-O'Donnell-Oleszkiewicz\]

**Query Complexity:**

\- The decision tree model, and its randomized, quantum, and non-deterministic analogs

\- The sensitivity theorem \[Huang\]

\- The polynomial method for quantum lower bounds \[Beals-Buhrman-Cleve-Mosca-de Wolf\]

## Lectures:

For each lecture - see the relevant chapters in O'Donnell's book + additional resources + lecture notes.

01. Jan 21 - The Fourier expansion, orthogonality of characters - Chapters 1.1-1.4

02. Jan 23 - BLR linearity testing - Chapters 1.5-1.6

03. Jan 28 - Social Choice, Influences, Effects, Derivatives - Chapters 2.1, 2.2 - [Lecture notes](https://drive.google.com/open?id=1sDIJQXYLIEXDcokZZg08p_LQTgDZbe_0)

04. Jan 30 - Influences, Effects, Isoperimetric Inequalities - Chapters 2.2, 2.3 - [Lecture notes](https://drive.google.com/open?id=1sDIJQXYLIEXDcokZZg08p_LQTgDZbe_0)

05. Feb 4 - Noise Stability, Arrow's Theorem - Chapters 2.4, 2.5 - [Lecture notes](https://drive.google.com/open?id=1sDIJQXYLIEXDcokZZg08p_LQTgDZbe_0)

06. Feb 6 - Spectral Concentration and Low-Degree Learning - Chapters 3.1-3.4 - [Lecture notes](https://drive.google.com/open?id=1QQpQJs48KNAoMn1dUwkYXkmyXyrAhe9Y) (Scribe: Alex Yu)

07. Feb 11 - Goldreich-Levin Algorithm - Chapter 3.5 - [Lecture notes](https://drive.google.com/open?id=1QQpQJs48KNAoMn1dUwkYXkmyXyrAhe9Y) (Scribe: Alex Yu)

08. Feb 13 - Learning Juntas -[\[Mossel-O'Donnell-Servedio'04\]](https://www.cs.cmu.edu/~odonnell/papers/juntas.pdf), [\[Valiant'12\]](https://dl.acm.org/doi/10.1145/2728167)

09. Feb 18 - DNFs, Random Restrictions - Chapters 3.3, 4.1, 4.3 - [Lecture notes](https://drive.google.com/open?id=1A9iMriSV7MuygygI2mVANHQSdICDsTHB) (Scribe: Nagaganesh Jaladanki)

10. Feb 20 - Fourier Concentration of DNFs - Chapter 4.4 - [Lecture notes](https://drive.google.com/open?id=1Mr5K6d8rEx_cU2ebUVhR83Vtoeq6mhXs) (Scribe: Antares Chen)

11. Feb 25 - Proof of the Switching Lemma - [Thapen's Notes](http://users.math.cas.cz/~thapen/switching.pdf) \- [Lecture notes](https://drive.google.com/open?id=1FFzH9xKVWgqFboSZf5w0zGpeLgtUcdkE) (Scribe: YiNuo Zhang)

12. Feb 27 - AC0 Circuits + Intro to Pseudorandomness - Chapter 4.5 + Chapters 6.1 - [Lecture notes](https://drive.google.com/open?id=1OO2g-rvl76pbn7cpvh5MqhL10Ld7MZkj) (Scribe: James Bartusek)

13. Mar 3 - Pseudorandomness - small-biased distributions - Chapters 6.3 + 6.4 - [Lecture notes](https://drive.google.com/open?id=1TqyMovXmfoiUGJhJk-eUpEDUlFLEn2R7) (Scribe: Luis Barroso-Luque)

14. Mar 5 - Pseudorandomness - fooling low-degree polynomials, Fractional PRGs - Chapter 6.5 +[CHHL'18](http://www.theoryofcomputing.org/articles/v015a010/) \- [Lecture notes](https://drive.google.com/open?id=15ztdLtxEyAhZ5TGyAA1eEwfqqpby3VZB) (Scribe: Yunchao Liu)

15. Mar 10 - LTFs and Central Limit Theorems - Chapters 5.1, 5.2 - [Lecture notes](https://drive.google.com/open?id=13fzu4zcqkaPHAHsii37XE7W3r1nfRojW) (Scribe: Wen Zhang)

16. Mar 12 - Noise Stability of the Majority Function and LTFs - Chapters 5.2, 5.5 - [Lecture notes](https://drive.google.com/open?id=1s6YXyy9-LvFtK17sIflijvazjNlfl463) (Scribe: Yimeng Wang)

17. Mar 17 - Hypercontractivity - Bonami's Lemma - Chapter 9 - [Lecture notes](https://drive.google.com/open?id=1GSCvLv_S7hLjeY48hYcNPi9JuTQgG22M) (Scribe: Emily Hsiao)

18. Mar 19 - Hypercontractivity - KKL Thm, Friedgut's Junta Lemma - Chapter 9- [Lecture notes](https://drive.google.com/open?id=1Pu_S_LLuF1_MiQBFUVYO8LvfBQ9jVrNw) (Scribe: David Mao)

19. Mar 31 - Dictator Testing & PCPPs - Chapter 7 - [Lecture notes](https://drive.google.com/open?id=1IQ-Xc3p4sWVwy4QBqSb7EL9MgH-yjLde) (Scribe: Wilson Wu)

20. Apr 2 - Hardness of Approximation from UGC - Chapter 7 - [Lecture notes](https://drive.google.com/open?id=1Iyxj__TOLW21pVilas0IpoeCt34J_nAQ) (Scribe: Jeff Xu)

21. Apr 7 - The Invariance Principle - Chapter 11

22. Apr 9 - Majority is Stablest & Hardness of Max-CUT - Chapter 11 - [Lecture notes](https://drive.google.com/open?id=1vtvQK8Zby3Kz894ghvsCSh6l-PIvOPKA) (Scribe: Michael Whitmeyer)

23. Apr 14 - Query Complexity -[\[Buhrman, de Wolf'00\]](http://www.cs.columbia.edu/~rocco/Teaching/S12/Readings/BdW.pdf) \- [Lecture notes](https://drive.google.com/open?id=161uQiNKIetJeAtqMZ_3uifw3BTy30htg) (Scribe: Vishnu Iyer)

24. Apr 16 - The Sensitivity Theorem - [\[Huang'19\]](http://www.mathcs.emory.edu/~hhuan30/papers/sensitivity_1.pdf) \- [Lecture notes](https://drive.google.com/open?id=1a4BiOj2NJnjUDT8a6WUbNa88W-danNe8) (Scribe: Jonathan Shafer)

25. Apr 21 - Presentations # 1

26. Apr 23 - Presentations # 2

27. Apr 28 - Presentations # 3

28. Apr 30 - Presentations # 4
Additional note: [FKN's Proof](https://drive.google.com/open?id=1gqqHv6iTVNYuvWA_9fr43796gjejN8Ul) (a new version).

## Resources and Other Courses:

Videos about Fourier concentration and random restriction based PRGs:

[PRGs for Small Space via Fourier Analysis](https://simons.berkeley.edu/talks/thomas-steinke-2017-03-09)

[Pseudorandom Generators from Polarizing Random Walks](https://simons.berkeley.edu/talks/tbd-10)

[Better Pseudorandom Generators from Milder Pseudorandom Restrictions](https://www.youtube.com/watch?v=IRnMcc8l7u4)

[Fourier tails for Boolean functions and their applications](https://www.youtube.com/watch?v=FmisseepEys)

[Li-Yang Tan - Stanford](http://theory.stanford.edu/~liyang/teaching/aobf-18.html) (2018)

[Shachar Lovett - UCSD](http://cseweb.ucsd.edu/~slovett/teaching/WI17-CSE291/) (2017)

[Yuval Filmus - Technion](https://filmus.net.technion.ac.il/analysis-of-boolean-functions/) (2015)

[Hamad Hatami - McGill](https://www.cs.mcgill.ca/~hatami/comp760-2014) (2014)

[Oded Regev - NYU](https://cims.nyu.edu/~regev/teaching/analysis_fall_2012/) (2012)

[Ryan O'Donnell - CMU](http://www.cs.cmu.edu/~odonnell/aobf12/)(2012)

[Guy Kindler - Weizmann](https://www.cse.huji.ac.il/~gkindler/weizmann-course/) (2008)

[Ryan O'Donnell - CMU](http://www.cs.cmu.edu/~odonnell/boolean-analysis/) (2007)

[Irit Dinur and Ehud Friedgut - HUJI](https://www.cse.huji.ac.il/~analyt/) (2005)

[Ryan O'Donnell - AOBF - Mini-Course](http://www.cs.cmu.edu/~odonnell/papers/barbados-aobf-lecture-notes.pdf) (2012) Scribe Notes by Li-Yang Tan

[Open Problems by Ryan O'Donnell](https://arxiv.org/abs/1204.6447) (2012)

[Open Problems - Simons Institute program on Real Analysis in Computer Science](https://simons.berkeley.edu/sites/default/files/openprobsmerged.pdf) (2014)

[Theory of Computing - Special Issue on Analysis of Boolean Functions](http://theoryofcomputing.org/articles/v009a016/)

**Videos from**[**Real Analysis in Computer Science**](https://simons.berkeley.edu/programs/realanalysis2013)**\`Boot Camp' at the Simons Institute (2013):**

[Inapproximability of Constraint Satisfaction Problems](https://simons.berkeley.edu/talks/inapproximability-of-constraint-satisfaction-problems) \- Johan Håstad - 5 talks

[Analytic Methods for Supervised Learning​](https://simons.berkeley.edu/talks/analytic-methods-supervised-learning) \- Adam Klivans - 4 talks

[Introduction to Analysis on the Discrete Cube](https://simons.berkeley.edu/talks/introduction-analysis-discrete-cube) \- Krzysztof Oleszkiewicz - 4 talks
