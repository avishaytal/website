---
layout: default
title: "cs 278 complexity theory"
---

---
title: "Avishay Tal - CS 278 Computational Complexity Theory"
---

# **CS 278 Computational Complexity Theory**

**Course Description:**

Computational Complexity studies the power and limitations of efficient computation. What can be computed with bounded resources such as time, memory, randomness, communication, and parallel cores? In this course, we will explore these beautiful questions. While most of them are widely open (e.g., Is verifying easier than proving? Is parallelism always helpful? Does randomness help in computation?), we will see many surprising connections between them. The course will be based on selected chapters from the book “[**Computational Complexity**](http://www.google.com/url?q=http%3A%2F%2Ftheory.cs.princeton.edu%2Fcomplexity%2F&sa=D&sntz=1&usg=AOvVaw1GaQAp5jJ9EQDHhz9-vovr)” by **Sanjeev Arora** and **Boaz Barak**.

Among the highlights, we will discuss Randomized Algorithms, Bounded-Space Algorithms, Savitch's Theorem, Immerman-Szelepcsényi's Theorem, the PCP Theorem and its connections to Hardness of Approximation, Interactive Proofs and IP = PSPACE, Hardness vs. Randomness, Pseudorandomness and Derandomization, Hardness Amplification, Introduction to Communication Complexity, Karchmer-Wigderson games, Circuit Complexity, Hardness within P.

**General Information:**

**Time and Place:**Tuesday, Thursday 2:00-3:30 PM (via Zoom)

**Instructor:**[Avishay Tal](http://www.google.com/url?q=http%3A%2F%2Fwww.avishaytal.org%2F&sa=D&sntz=1&usg=AOvVaw1_ca4aFO3SN8SmWhTCFqSc), atal "at" berkeley.edu

**Office Hours:**Monday 4:00-5:00 PM

**TA:**[Nagaganesh Jaladanki](https://www.google.com/url?q=https%3A%2F%2Fnagaganesh.com&sa=D&sntz=1&usg=AOvVaw2ILpckbk4XWJfh9JMk9RGM), nagaganesh "at" berkeley.edu

**Grading:**Homework assignments - 50% (5 assignments), scribe - mandatory + replaces the lowest-grade hw assignment, Final Project & Presentation - 50%. Participation in class - extra credit.

**Prereqs:** CS170 or equivalent is required. CS172 or equivalent is recommended.

**Pre-Reading:**

For those of you that want a refresher on the general setting, or those that haven't took 172, please see Chapter 3 in Sipser's book ("**Introduction to the Theory Of Computation**" by **Michael Sipser**) or chapters 1 & 2[**Arora-Barak.**](http://www.google.com/url?q=http%3A%2F%2Ftheory.cs.princeton.edu%2Fcomplexity%2F&sa=D&sntz=1&usg=AOvVaw1GaQAp5jJ9EQDHhz9-vovr)

**Textbooks & Lecture Notes:**

- Sanjeev Arora, Boaz Barak -[Computational Complexity, A Modern Approach](http://www.google.com/url?q=http%3A%2F%2Ftheory.cs.princeton.edu%2Fcomplexity%2F&sa=D&sntz=1&usg=AOvVaw1GaQAp5jJ9EQDHhz9-vovr) \+ [Web Addendum](https://www.google.com/url?q=https%3A%2F%2Fwww.cs.utexas.edu%2F~danama%2Fcourses%2Fadv-comp20%2Faccnexp.pdf&sa=D&sntz=1&usg=AOvVaw1xAhmPfR9mzKo4ZXHouWuQ)

- Oded Goldreich - [Computational Complexity, A Conceptual Perspective](http://www.google.com/url?q=http%3A%2F%2Fwww.wisdom.weizmann.ac.il%2F~oded%2Fcc-book.html&sa=D&sntz=1&usg=AOvVaw0cceU_q18Lhfqoq5epE0bz)

- Avi Wigderson -[Mathematics and Computation](https://www.google.com/url?q=https%3A%2F%2Fwww.math.ias.edu%2Favi%2Fbook&sa=D&sntz=1&usg=AOvVaw1R3HNh-y2TegJ9_vM0TeMt)

- Gil Cohen - [A Taste of Circuit Complexity Pivoted at NEXP not in ACC (and more)](http://www.google.com/url?q=http%3A%2F%2Feccc.hpi-web.de%2Fresources%2Fpdf%2Fcohen.pdf&sa=D&sntz=1&usg=AOvVaw3LzZMku3lkaxB7pHb0BwAK)
[Piazza](http://www.google.com/url?q=http%3A%2F%2Fpiazza.com%2Fberkeley%2Fspring2021%2Fcs278%2Fhome&sa=D&sntz=1&usg=AOvVaw2sxbfa5Nv7tAdn8P48wGg7)

[Gradescope](https://www.google.com/url?q=https%3A%2F%2Fwww.gradescope.com%2Fcourses%2F242906&sa=D&sntz=1&usg=AOvVaw18OauiCpkMxY7XfZ0Bgd4M)

**Problem Sets:**

- [Homework 1](https://drive.google.com/open?id=1KO3nmX0AmXOEiW8XMXxZ5UCgcUyhQ4TP) \- Due Thursday, Feb 11.

- [Homework 2](https://drive.google.com/open?id=1Qn-hueIXHg5UHe6w2OZYpqJsq8Z9269z)\- Due Monday, Mar 1.

- [Homework 3](https://drive.google.com/open?id=1NQYTyLTnpZub9w2EpW47cbG81y5bRMoi) \- Due Thursday, Mar 18.

- [Homework 4](https://drive.google.com/open?id=1naoQEjgq9-Fg53vYO-S0u6O_oQmu_XKO) \- Due Friday, Apr 16.
**Topics:**

**Time-Complexity (Chapter 3 AB)**

Hierarchy Theorems

Barriers to diagonalization

**Space-Complexity (Chapter 4 AB)**

PSPACE, LogSPACE

st-conn is NL complete

Savitch’s Theorem (NSPACE\[s\] in DSPACE\[s^2\])

Immerman-Szelepcsényi's Theorem (NSPACE is closed to complement)

**Randomness in Computation (Chapters 5,7 AB)**

Relation to the Polynomial Hierarchy

Relation to Circuits

Derandomization

**Circuit Complexity (Chapters 6, 14, 23 AB)**

The circuit complexity approach to P!=NP

The Karp-Lipton Theorem

Uncoditional lower bounds for restrictive circuit classes like bounded-depth circuits

KW-Games

NEXP not in ACC^0

Barriers: Natural Proofs.

**Hardness vs Randomness (Chapters 19, 20 AB)**

Pseudorandom Generators from Hard functions

Derandomization implies Circuit Lower Bounds

Hardness Amplification

**Interactive Proofs (Chapter 8 AB)**

Arthur-Merlin Protocols

IP = PSPACE

**The PCP theorem and its connections to Hardness of Approximation (Chapter 11 AB)**

**Communication Complexity -**KW Games, Lower Bounds on Randomized Communication Complexity

**Hardness within P**

[**Scribe Notes**](https://drive.google.com/open?id=1Yy1tb_Dj4g63LtnzK38pT0XYJiI-Vtxw)

[**172 Review Session**](https://drive.google.com/open?id=1j5G0lvvc8R7Kc7MXahNSUrrFh1UN92nc)
