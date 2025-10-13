---
layout: default
title: "stoc 2020 workshop derandomizing space bounded computation"
---

---
url: "/stoc-2020-workshop-derandomizing-space-bounded-computation/"
title: "Avishay Tal - STOC 2020 Workshop: Derandomizing Space-Bounded Computation"
---

# **STOC 2020 Workshop: Derandomizing Space-Bounded Computation**

[**Videos from the workshop**](https://www.youtube.com/watch?v=NfzE-WfGgq8&list=PLn0nrSd4xjjbEL2VLMeMUjqBmoPUUa6EF&index=33#t=3m)

**Time and Date:** 10:00 PDT to 13:00 PDT, Friday, June 26, 2020.

**Organizers:**[Raghu Meka](https://www.google.com/url?q=https%3A%2F%2Fraghumeka.github.io&sa=D&sntz=1&usg=AOvVaw2pr78elJHdWi5ATHS2tjK4) (raghum@cs.ucla.edu),[Avishay Tal](https://www.google.com/url?q=https%3A%2F%2Fwww.avishaytal.org&sa=D&sntz=1&usg=AOvVaw17orPWK1D0rZg80HwLlrQZ) (atal@berkeley.edu), and[David Zuckerman](https://www.google.com/url?q=https%3A%2F%2Fwww.cs.utexas.edu%2F~diz%2F&sa=D&sntz=1&usg=AOvVaw1uZamyin9KP4c9DmFqzZEb) (diz@utexas.edu)

**Description:**A major question in computer science asks what is the power of randomness in computation? Does BPP=P? However, the BPP versus P problem entails proving strong lower bounds, so probably the most exciting prospect of a big unconditional derandomization result is that BPL=L. This would imply BPSPACE(S)=DSPACE(S) for any space-constructible S(n) >= log(n). Despite much effort, we still don’t know any better theorem than BPL in L3/2, proved by Saks and Zhou over 20 years ago. On the other hand, there has recently been some exciting progress in several related directions. That’s the focus of this workshop.

**Goals:**The goals of this workshop are to understand these new directions. They include new pseudorandom generators (PRGs) using pseudorandom restrictions, including PRGs for any-order read-once branching programs and product tests; constructions of hitting sets and newly defined “pseudorandom pseudo-distributions” that have optimal dependence on the error; and a new approach based on Laplacian solvers. The talks are aimed to be accessible to non-experts, and informative to experts.

**Schedule:**

10:00 - 10:40 (PDT) -[Avishay Tal](http://www.google.com/url?q=http%3A%2F%2Fwww.avishaytal.org&sa=D&sntz=1&usg=AOvVaw0J1guJkM-JGDJ1QzcD2Z7W) \-\- PRGs via Pseudorandom Restrictions

10:45 - 11:25 (PDT) -[Michael A. Forbes](http://www.google.com/url?q=http%3A%2F%2Fmiforbes.cs.illinois.edu&sa=D&sntz=1&usg=AOvVaw3KhSHR7t7CdX2YYoJlEIXh) \-\- PRGs for Read-Once Branching Programs, in any Order

11:25 - 11:35 (PDT) - Break

11:35 - 12:15 (PDT) - [Sumegha Garg](https://www.google.com/url?q=https%3A%2F%2Fwww.cs.princeton.edu%2F~sumeghag%2F&sa=D&sntz=1&usg=AOvVaw0ltvmCnmx9Tc_vsuQYdsuT) \-\- Pseudorandom Pseudo-Distributions with Near-Optimal Error for Read-Once Branching Programs

12:20 - 1:00 (PDT) - [Salil Vadhan](https://www.google.com/url?q=https%3A%2F%2Fsalil.seas.harvard.edu&sa=D&sntz=1&usg=AOvVaw1ZxHe41MO7m5SelRAkInNy) \-\- Derandomizing Space-Bounded Computation via Laplacian Solvers

**Abstracts:**

**Pseudorandom Generators via Pseudorandom Restrictions**

[Avishay Tal](http://www.google.com/url?q=http%3A%2F%2Fwww.avishaytal.org&sa=D&sntz=1&usg=AOvVaw0J1guJkM-JGDJ1QzcD2Z7W), University of California, Berkeley

Can we derandomize computation without increasing the memory footprint? This is essentially the RL vs. L question. A major approach towards this goal is to construct pseudorandom generators (PRGs) with O(log n) seed-length that fool log-space computation. Despite many efforts, this approach has been stuck at the O(log^2(n)) barrier for three decades now, since the seminal result of Nisan.

I will survey some recent work from the last decade that revived the restrictions-based PRG approach of Ajtai and Wigderson (which predates Nisan's PRG!). The idea is as follows. Numerous results in complexity theory show that certain classes of Boolean functions become simpler under random restrictions (most notably "Håstad's Switching Lemma" for AC0 circuits). Ajtai and Wigderson show that it suffices to fool the restricted (simpler) function to get a PRG for the original (more complicated) function. This is achieved via a recursive approach, where one partitions the bits pseudorandomly to buckets and then picks pseudorandomly values for each bucket. This approach was revived and strengthened in the beautiful work of Gopalan, Meka, Reingold, Trevisan, and Vadhan. GMRTV observed that it suffices to fool the average of the restricted functions, instead of fooling each one individually -- an easier task in many cases. GMRTV approach led to a nearly optimal PRG for read-once DNF/CNF formulae, combinatorial rectangles, and more. In the realm of small-space computation, this PRG almost matches the state-of-the-art PRGs by Nisan and INW (to be highlighted in Michael's talk), and in some special cases, even surpasses it. Understanding the full power and limitations of this PRG remains open.

[**Slides**](https://drive.google.com/open?id=1Dip-MN6yl5Jw32hxlkUC3yS3mBXnt6BT)

**Pseudorandom Generators for Read-Once Branching Programs, in any Order**

[Michael A. Forbes](http://www.google.com/url?q=http%3A%2F%2Fmiforbes.cs.illinois.edu&sa=D&sntz=1&usg=AOvVaw3KhSHR7t7CdX2YYoJlEIXh), University of Illinois at Urbana-Champaign

A central question in derandomization is whether randomized logspace (RL) equals deterministic logspace (L). To show that RL=L, it suffices to construct explicit pseudorandom generators (PRGs) that fool polynomial-size read-once (oblivious) branching programs (roBPs). Starting with the work of Nisan, pseudorandom generators with seed-length O(log^2 n) were constructed. Unfortunately, improving on this seed-length in general has proven challenging and seems to require new ideas.

A recent line of inquiry has suggested focusing on a particular limitation of the existing PRGs, which is that they only fool roBPs when the variables are read in a particular \*known\* order, such as x\_1<...<x\_n.

In comparison, existentially one can obtain logarithmic seed-length for fooling the set of polynomial-size roBPs that read the variables under any fixed \*unknown\* permutation x\_{pi(1)}<...<x\_{pi(n)}. While recent works have established novel PRGs in this setting for subclasses of roBPs, there were no known n^{o(1)} seed-length explicit PRGs for general polynomial-size roBPs in this setting.

In this work, we follow the "bounded independence plus noise" paradigm of Haramaty, Lee and Viola, and give an improved analysis in the general roBP unknown-order setting. With this analysis we obtain an explicit PRG with seed-length O(log^3 n) for polynomial-size roBPs reading their bits in an unknown order. Plugging in a recent Fourier tail bound of Chattopadhyay, Hatami, Reingold, and Tal, we can obtain a ~O(log^2 n) seed-length when the roBP is of constant width.

Joint work with Zander Kelley.

**Pseudorandom Pseudo-Distributions with Near-Optimal Error for Read-Once Branching Programs**

[Sumegha Garg](https://www.google.com/url?q=https%3A%2F%2Fwww.cs.princeton.edu%2F~sumeghag%2F&sa=D&sntz=1&usg=AOvVaw0ltvmCnmx9Tc_vsuQYdsuT), Princeton University

Nisan \[Nis92\] constructed a pseudorandom generator for length n, width w read-once branching programs (ROBPs) with error ε and seed length O(log^2 n + log n · log w + log n · log(1/ε)). Informally, a pseudorandom generator with seed length s specifies 2^s paths such that for any length n, width w ROBP, the probability of acceptance (over 2^n paths) can be approximated, upto error ε, by the fraction of these 2^s paths that are accepting. A major goal in complexity theory is to reduce the seed length, hopefully, to O(log nw/ε)), or to construct improved hitting sets, as these would yield stronger derandomization of BPL (randomized log-space computation with two-sided error) and RL (randomized log-space computation with one-sided error), respectively. In contrast to a successful line of work in restricted settings, for general unrestricted ROBPs (for n=w), no progress had been made since \[Nis92\].

A recent line of work \[BCG'18, HZ'18, CL'20\] made improvements for the general case by constructing hitting sets and pseudorandom pseudo-distributions with optimal dependence on ε (seed length ~O(log^2 n + log n · log w + log(1/ε))). The regime of parameters in which these constructions strictly improve upon prior works, namely, log(1/ε) ≫ log n, is also motivated by the work of Saks and Zhou \[SZ99\] who use pseudorandom generators with error ε, for length n, width w read-once branching programs, such that w, 1/ε = 2^(log^2 n) in their proof for BPL ⊆ L^3/2.

In this talk, we survey this line of work and focus on the starting work of \[BCG'18\]. In this work, we introduce and construct a new type of primitive called pseudorandom pseudo-distributions. Informally, this is a generalization of pseudorandom generators in which one may assign negative and unbounded weights to paths as opposed to working with probability distributions. We show that such a primitive yields hitting sets and, for derandomization purposes, can be used to derandomize two-sided error algorithms.

Joint work with Mark Braverman and Gil Cohen (STOC'18).

[**Slides**](https://drive.google.com/open?id=1FDJ2D6K0je6ayZ07kg7hI3wjF0PoMyTN)

**Derandomizing Space-Bounded Computation via Laplacian Solvers**

[Salil Vadhan](https://www.google.com/url?q=https%3A%2F%2Fsalil.seas.harvard.edu&sa=D&sntz=1&usg=AOvVaw1ZxHe41MO7m5SelRAkInNy), Harvard University

I will describe a series of works that attacks the derandomization of space-bounded computation (e.g. seeking to prove BPL=L) using a combination of ideas from the literature on time-efficient Laplacian solvers (Spielman and Teng, STOC \`04; Peng and Spielman, STOC \`14; Cheng et al. \`15; Cohen et al. FOCS \`16, STOC \`17, FOCS \`18) with ones used to show that Undirected S-T Connectivity is in deterministic logspace (Reingold, STOC \`05 and JACM \`08; Rozenman and Vadhan, RANDOM \`05).

In particular, for Eulerian directed graphs and hence also undirected graphs, we obtain deterministic, nearly logarithmic-space algorithms for (a) estimating random walk probabilities to within polynomially small error and (b) approximately solving linear systems given by graph Laplacians. Previously both of these problems were known to be solvable for general directed graphs by randomized algorithms in logarithmic space (Aleliunas et al. FOCS \`79; Doron, Le Gall, and Ta-Shma RANDOM \`17), and hence by deterministic algorithms using space O(log^{3/2} N) (Saks and Zhou, FOCS \`95 and JCSS \`99). Extending these results to general directed graphs (as was done in the time-bounded case) would suffice to derandomize all of BPL.

Joint works with Murtagh, Reingold, and Sidford (FOCS \`17 and RANDOM \`19) and Ahmadinejad, Kelner, Murtagh, Peebles, and Sidford (arXiv \`19).

[**Slides**](https://drive.google.com/open?id=1oNy929eBOHby0yIHEQ5U5obK7220y6Lq)

Another excellent resource is this[two](https://www.youtube.com/watch?v=Wjo7o8aOiQ4&list=PLKVCRT3MRed4SGJseuvBIUSm85PPBYEap&index=4&t=0s)-[part](https://www.youtube.com/watch?v=fl3_4TczN4w&list=PLKVCRT3MRed4SGJseuvBIUSm85PPBYEap&index=4) tutorial lectures by[Omer Reingold](https://www.google.com/url?q=https%3A%2F%2Fomereingold.wordpress.com&sa=D&sntz=1&usg=AOvVaw2POtfAcZPUATVc0SV_ZAKs) about the same topic from CCC 2019.
