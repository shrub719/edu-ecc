# Edu-ECC [WIP]

A simplified visual demonstration of several mathematical concepts in cryptography. Currently a work in progress. Part of my Independent Research Project.

> **Note:** this program is **NOT** cryptographically secure or fit for use in production. It is purely for educational purposes and does not guarantee strong elliptic curves or random number generation.


## Structure

This project is composed of two parts:
- [A program](#program-edu-ecc) written in Python used to implement and visually demonstrate elliptic curve cryptography
- [A paper](#paper) on ECC and the issues posed to cryptographic standards by technological advancement


## Program (Edu-ECC)

[Edu-ECC](src/main.py) is a Python program that implements elliptic curve arithmetic over finite fields from scratch, and uses this for several EC-based cryptography schemes.

### Goals
The program should (in order of priority):
- ~~Draw elliptic curves and/or their discrete finite field representations using matplotlib~~
- Animate point scalar multiplication using tangents
- ~~Implement EC calculation and arithmetic operations (i.e. stop using `tinyec`)~~
- ~~Implement ECDH-based secret key derivation~~
- **Implement EC hybrid assymetric key encryption** 
- Allow for the tweaking of curve parameters to demonstrate the importance of choosing cryptographically secure curves **[?]**

### Usage
Clone this repo and run:
```
pip install -r requirements.txt
```  

`main.py` contains several demo functions to show the capabilities of the libraries.

For information on using the libraries themselves, check the [documentation](docs/README.md).
<!-- TODO: make it into an actual pypi library? -->


## Essay

The essay accompanying this program [here](./utils/paper.md), is my own research and interpretation of the current state of modern cryptographic standards including elliptic curve and lattice-based cryptography.  
It is written in MarkDown with TeX support (using [VS Code's KaTeX plugin](https://github.com/microsoft/vscode-markdown-it-katex)). <!-- REMEMBER to export to PDF or something w pandoc -->

### Goals
The paper should cover (in chronological <!-- chronological?? --> order):
- ECC
    - What they are and useful/special properties
    - Finite fields, restrictions to prime finite fields
    - Binary fields **[?]**
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

$$  y^2 = x^3 + 4x + 20  $$