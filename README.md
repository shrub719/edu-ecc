# Edu-ECC

A simplified visual demonstration and implementation of elliptic curve cryptography. Part of my Independent Research Project.

> **Note:** this program is **NOT** cryptographically secure or fit for use in production. It is purely for educational purposes and does not guarantee strong elliptic curves or random number generation.


## Structure

This project is composed of two parts:
- [A program](#program-edu-ecc) written in Python used to implement and visually demonstrate elliptic curve cryptography
- [A paper](#paper) on ECC and the issues posed to cryptographic standards by technological advancement


## Program (Edu-ECC)

[Edu-ECC](src/main.py) is a Python program that implements elliptic curve arithmetic over finite fields from scratch, and uses this for several EC-based cryptography schemes.

### Usage
Clone this repo and run:
```
pip install -r requirements.txt
```  
> **Note:** dependencies are only required for graphing capabilities.

`main.py` contains several demo functions to show the capabilities of the libraries.

For information on using the libraries themselves, check the [documentation](docs/README.md).
<!-- TODO: make it into an actual pypi library? -->


## Paper

The paper accompanying this program [here](./utils/Elliptic curves in modern cryptography.pdf), is my own research and interpretation of the current state of modern cryptographic standards with regards to elliptic curve cryptography.  
It is written in LaTeX.

---

$$  y^2 = x^3 + 4x + 20  $$