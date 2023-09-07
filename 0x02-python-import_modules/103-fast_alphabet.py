#!/usr/bin/python3

print(chr(65) if (lambda f, x: f(f, x))(lambda self, n: chr(n) + self(self, n + 1) if n < 91 else '', 65) else '')
