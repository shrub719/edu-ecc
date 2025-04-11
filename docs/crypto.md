# Crypto
```py
import crypto
```
Crypto extends classes in EC to implement several cryptography schemes, such as ECDH and hybrid assymetric key encryption.

> **Note:** this module is **NOT** cryptographically secure or fit for use in production. It is purely for educational purposes and does not guarantee strong elliptic curves or random number generation.


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
The client's private key is generated with `random.randint` and as such is not cryptographically secure.   
A client's key pair can be accessed by `DHClient.public` and `DHClient._private`. 

### Key derivation

To generate a shared key between two clients without transferring private keys, call `DHClient.generate_shared_key(other)` on both clients.  
However, Crypto has several functions that simplify connections/key exchange:

- To connect two clients, use `dh_connect(client1, client2)`.
- To connect a list of clients in a mesh, use `dh_mesh_connect(*clients)`.

### Show clients

Crypto provides several ways of displaying clients:

- `print(client)`
- To show multiple clients, use `show_clients(*clients)`.
- To draw a graph of a connected mesh, use `dh_mesh_nx_graph(graph, *clients)`.  
Pass in a `networkx` `Graph` object, then `nx.draw()` and `plt.show()` the graph.
