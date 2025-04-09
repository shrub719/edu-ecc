# EC
```py
import ec
```
EC contains classes related to elliptic curves over finite fields.


## Creating a curve

EC really only contains one class you'll need to worry about: `Curve`.  

`Curve` represents an elliptic curve over a finite prime field in supersingular Weierstrauss form, <!-- FIX: is this right? --> i.e. in the form $y^2 = x^3 + ax + b \pmod p$.

When initialising a `Curve` pass in $a$, $b$ and $p$. For example,
```py
curve = Curve(4, 20, 29)
```
creates the curve $y^2 = x^3 + 4x + 20 \pmod{29}$.


## Creating a point

EC `Point`s need to be created from a `Curve` which they lie on.

To do this, **don't** call the `Point()` constructor. Rather, use the `Curve.point(x, y)` method.  
This returns a `Point` object:
```py
a = curve.point(5, 22)
```

> **Note:** the **point at infinity** `(None, None)` is valid for every curve.


## Elliptic curve arithmetic

Two points on the same curve can be added together using the `+` operator, following the rules of elliptic curve point addition:
```py
a = curve.point(5, 22)
b = curve.point(10, 4)
c = a + b
```

A point can be doubled using the `+` or `*` operator:
```py
a = curve.point(5, 22)
b = a * 2
b = a + a
```

A point can also be multiplied by a scalar with the double-and-add method using the `*` operator:
```py
a = curve.point(5, 22)
b = a * 12
b = 12 * a
```
