# Crypto
```
import crypto
```
Crypto extends classes in EC to implement several cryptography schemes, such as ECDH and hybrid assymetric key encryption.


## Curve extensions

The `CryptoCurve` class is a `Curve` that also contains information on a common generator and subgroup that two clients use in a cryptographic protocol.  
The generator is a coordinate tuple of a point on the curve. The order of the subgroup is the number of distinct points that can be created by cyclic addition of the generator point:
```py
crypto_curve = CryptoCurve(4, 20, 29, (5, 22), 37)
```
creates a `CryptoCurve` $y^2 = x^3 + 4x + 20 \pmod{29}$ with generator $(5, 22)$ and order $37$.

Crypto adds a `Curve.to_crypto_curve()` method that turns a `Curve` into a `CryptoCurve`. To use it, pass in a valid generator coordinate tuple and the order of the subgroup created by the generator:
```py
curve = Curve(4, 20, 29)
crypto_curve = curve.to_crypto_curve((5, 22), 37)
```
creates a `CryptoCurve` $y^2 = x^3 + 4x + 20 \pmod{29}$ with generator $(5, 22)$ and order $37$.


## Elliptic Curve Diffie-Hellman (ECDH)

Crypto implements a `DHClient` class that represents a device with a public-private key pair. To initialise a `DHClient`, pass in a `CryptoCurve` and a name:
```py
alice = DHClient(crypto_curve, "Alice")
```