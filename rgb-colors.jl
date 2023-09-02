using Colors
println("Red: ")
r = parse(Int, readline())
println("Green: ")
g = parse(Int, readline())
println("Blue: ")
b = parse(Int, readline())
r /= 255
g /= 255
b /= 255
c = RGB(r, g, b)
print(Lab(c))
print(Luv(c))
print(XYZ(c))
print(xyY(c))
print(LCHab(c))
print(LCHuv(c))
print(DIN99(c))
print(DIN99d(c))
print(DIN99o(c))
print(LMS(c))
print(Gray(c))