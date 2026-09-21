# ============================================================
# 15. REAL-WORLD EXAMPLE - TEMPERATURE DIFFERENCE
# ============================================================
#
# Expected temperature:
#
#     30°C
#
# Actual temperatures:
#
#     28, 32, 25, 35
#
# We want to know how FAR each temperature is from 30.
#
# Formula:
#
#     difference = abs(actual - expected)
# ============================================================
import numpy as np

actual = np.array([28, 32, 25, 35])

result = np.abs(actual - 30)
print(result)