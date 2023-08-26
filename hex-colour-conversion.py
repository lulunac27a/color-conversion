#!/usr/bin/env python
# coding: utf-8

# In[38]:


import colour
import numpy as np
hex = input('hex: ')
rgb = colour.notation.HEX_to_RGB(hex)
xYWhite = colour.xy_to_XYZ(colour.CCS_ILLUMINANTS["CIE 1931 2 Degree Standard Observer"]["D65"]) * 100
L_A = 64 / np.pi * 0.2
Y_b = 20
surround = colour.VIEWING_CONDITIONS_CIECAM02["Average"]
print("R", rgb[0] * 255, "G", rgb[1] * 255, "B", rgb[2] * 255)
xyz = colour.sRGB_to_XYZ(rgb)
print("XYZ:", "X", xyz[0] * 100, "Y", xyz[1] * 100, "Z", xyz[2] * 100)
ciecam02 = colour.XYZ_to_CIECAM02(xyz * 100, xYWhite, L_A, Y_b, surround)
print("CIECAM02:", "J", ciecam02.J, "C", ciecam02.C, "h", ciecam02.h)
ciecam16 = colour.XYZ_to_CIECAM16(xyz * 100, xYWhite, L_A, Y_b, surround)
print("CIECAM16:", "J", ciecam16.J, "C", ciecam16.C, "h", ciecam16.h)
oklab = colour.XYZ_to_Oklab(xyz)
print("Oklab:", "L", oklab[0], "a", oklab[1], "b", oklab[2])
prolab = colour.XYZ_to_ProLab(xyz)
print("ProLab:", "L", prolab[0], "a", prolab[1], "b", prolab[2])
osa_ucs = colour.XYZ_to_OSA_UCS(xyz * 100)
print("OSA-UCS:", "L", osa_ucs[0], "j", osa_ucs[1], "g", osa_ucs[2])
lab = colour.XYZ_to_Lab(xyz)
print("Lab:", "L", lab[0], "j", lab[1], "g", lab[2])
luv = colour.XYZ_to_Luv(xyz)
print("Luv:", "L", luv[0], "j", luv[1], "g", luv[2])


# In[ ]:




