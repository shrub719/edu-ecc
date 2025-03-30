# Edu-ECC [WIP]

A simplified visual demonstration of several mathematical concepts in cryptography. Currently a work in progress. Part of my Independent Research Project. <!-- 1x -->


## Structure

This project is composed of two parts:
- [A program](#program-edu-ecc) written in Python used to visually demonstrate several mathematical concepts in cryptography. <!-- 2x -->
- [An essay/paper](#paper) <!-- FIX: essay or paper? --> on elliptic curve cryptography and the issues posed to cryptographic standards by technological advancement.


## Program (Edu-ECC)

[Edu-ECC](src/main.py) is a Python script meant to visually demonstrate some of the key trapdoor functions used in modern cryptography and their origins. <!-- 3x... -->
<!-- TODO: DRY -->

### Goals
The program should (in order of priority within categories):
- Demonstrate ECC
    - Draw elliptic curves and/or their discrete finite field representations using matplotlib
    - Animate point scalar multiplication using tangents
    - Animate the restriction of ECCs to a finite prime field
    - Implement EC calculation and arithmetic operations (i.e. stop using `tinyec`)
    - Implement ECDH-based secret key derivation
    - Allow for the tweaking of curve parameters to demonstrate the importance of choosing cryptographically secure curves
- Demonstrate lattice-based cryptography methods

### Usage
TODO <!-- instructions -->


## Paper

The paper accompanying this program, [Paper Name :)](./utils/paperName.md), is my own research and interpretation of the current state of modern cryptographic standards including elliptic curve and lattice-based cryptography.  
It is written in MarkDown with TeX support (using [VS Code's KaTeX plugin](https://github.com/microsoft/vscode-markdown-it-katex)). <!-- REMEMBER to export to PDF or something w pandoc -->

### Goals
The paper should cover (in chronological <!-- chronological?? --> order):
- ECC
    - What they are and useful/special properties
    - Finite fields, restrictions to prime finite fields
    - Binary fields??
    - Operations within the field of points (addition, scalar multiplication, point at infinity)
    - ECC-based key derivation
- Lattice-based cryptography
    - SVP
    - LWE
    - Variants such as MLWE and RLWE
    - NIST PQC competition
- Future-proofing standards
    - QRNG for key generation
    - Shor's algorithm
    - Feasibilty of large-scale quantum computers, error correction

---

$$  y^2 = x^3 + 7  $$