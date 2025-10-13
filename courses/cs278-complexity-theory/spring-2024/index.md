# CS 278 Computational Complexity Theory (Spring 2024)

Course Description

Computational Complexity studies the power and limitations of efficient computation. What can be computed with bounded resources such as time, memory, randomness, communication, and parallel cores? In this course, we will explore these beautiful questions. While most of them are widely open (e.g., Is verifying easier than proving? Is parallelism always helpful? Does randomness help in computation?), we will see many surprising connections between them. The course will be based on selected chapters from the book “ [Computational Complexity](http://theory.cs.princeton.edu/complexity/)” by Sanjeev Arora and Boaz Barak.

Among the highlights, we will discuss Randomized Algorithms, Bounded-Space Algorithms, Savitch's Theorem, Immerman-Szelepcsényi's Theorem, the PCP Theorem and its connections to Hardness of Approximation, Interactive Proofs and IP = PSPACE, Hardness vs. Randomness, Pseudorandomness and Derandomization, Hardness Amplification, Introduction to Communication Complexity, Karchmer-Wigderson games, Circuit Complexity, Hardness within P.

General Information

Time and Place: Tuesday, Thursday 2:00 - 3:30 PM, Soda 405.

Instructor: [Avishay Tal](http://www.avishaytal.org/), email: atal "at" berkeley.edu, Office Hours: Thursday 3:30-4:30 PM.

TA: Hongxun Wu, email: wuhx"at" berkeley.edu, Office Hours: Thursday 9:00 - 10:00 AM at Soda 326.

Grading: Homework assignments - 50% (5 assignments), scribe - mandatory + replaces the lowest-grade hw assignment, Final Project & Presentation - 50%.

Prerequisite: CS170 or equivalent is required. CS172 or equivalent is recommended.

Pre-Reading: For those of you who want a refresher on the general setting, or those who haven't taken 172, please see Chapter 3 in Sipser's book ("Introduction to the Theory Of Computation" by Michael Sipser) or Chapters 1 & 2 [Arora-Barak.](http://theory.cs.princeton.edu/complexity/)

Textbooks & Lecture Notes:

- Sanjeev Arora, Boaz Barak - [Computational Complexity, A Modern Approach](http://theory.cs.princeton.edu/complexity/) + [Web Addendum](https://www.cs.utexas.edu/~danama/courses/adv-comp20/accnexp.pdf)

- Oded Goldreich -  [Computational Complexity, A Conceptual Perspective](http://www.wisdom.weizmann.ac.il/~oded/cc-book.html)

- Avi Wigderson - [Mathematics and Computation](https://www.math.ias.edu/avi/book)

- Gil Cohen - [A Taste of Circuit Complexity Pivoted at NEXP not in ACC (and more)](http://eccc.hpi-web.de/resources/pdf/cohen.pdf)

[Problem Sets](https://drive.google.com/drive/folders/1ip5SBq7pqWIdOWK3o3QzPDG7Ryz9v4p9?usp=sharing)

- [HW1](https://drive.google.com/file/d/1yNeSPiWIEuEtMyXHHHvMAx1ABNj9tH7L/view?usp=sharing) \-\- Due Feb 12

- [HW2](https://drive.google.com/file/d/1IAGFlgqni6e-R6QYS2Ip8OFz6MPzbcBk/view?usp=share_link) \-\- Due Mar 4

- [HW3](https://drive.google.com/file/d/1lxOIXJAUsIDCRWpqBwwaZbMEueKQINVM/view?usp=share_link) \-\- Due Mar 22

- [HW4](https://drive.google.com/file/d/12mM8QpJmL8Or6HlSRBlS9ZWlUH50kIxf/view?usp=share_link) \-\- Due Apr 19

[Lecture Notes](https://drive.google.com/drive/folders/1ip5SBq7pqWIdOWK3o3QzPDG7Ryz9v4p9?usp=share_link)

Topics

- Time-Complexity (Chapter 3 AB)

  - Hierarchy Theorems

  - Barriers to diagonalization
- Space-Complexity (Chapter 4 AB)

  - PSPACE, L (log-SPACE)

  - st-conn is NL complete

  - Savitch’s Theorem (NSPACE\[s\] in DSPACE\[s^2\])

  - Immerman-Szelepcsényi's Theorem (NSPACE is closed under complement)
- Randomness in Computation (Chapters 5,7 AB)

  - Relation to the Polynomial Hierarchy

  - Relation to Circuits

  - Derandomization
- Circuit Complexity (Chapters 6, 14, 23 AB)

  - The circuit complexity approach to P!=NP

  - The Karp-Lipton Theorem

  - Unconditional lower bounds for restrictive circuit classes like bounded-depth circuits

  - KW-Games

  - NEXP not in ACC^0

  - Barriers: Natural Proofs
- Hardness vs Randomness (Chapters 19, 20 AB)

  - Pseudorandom Generators from Hard functions

  - Derandomization implies Circuit Lower Bounds

  - Hardness Amplification
- Interactive Proofs (Chapter 8 AB)

  - Arthur-Merlin Protocols

  - IP = PSPACE
- The PCP theorem and its connections to Hardness of Approximation (Chapter 11 AB)

- Communication Complexity -

  - Karchmer-Wigderson Games (the connection between communication complexity and circuit complexity)

  - Lower Bounds on Randomized Communication Complexity

  - Lifting Theorems
- Hardness within P
