import cmath
x = 1 + 4j
r = 2
phi = 1.4
print(cmath.phase(x))
print(abs(x))

print(cmath.rect(r,phi))

# use isclose for euler eq

print(cmath.isclose(cmath.exp(cmath.pi*1j) + 1,0, abs_tol= 0.0001))

