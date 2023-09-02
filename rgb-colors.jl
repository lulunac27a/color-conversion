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
println(Lab(c))
println(Luv(c))
println(XYZ(c))
println(xyY(c))
println(LCHab(c))
println(LCHuv(c))
println(DIN99(c))
println(DIN99d(c))
println(DIN99o(c))
println(LMS(c))
println(Gray(c))
