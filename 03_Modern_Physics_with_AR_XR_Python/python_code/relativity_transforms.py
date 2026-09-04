"""
Relativity Transforms & Lorentz Factor Simulation
Author: Dr. Chewa Thassana (chewa.t@rbru.ac.th)
Department of Physics, Rambhai Barni Rajabhat University (RBRU)
"""

import math

C = 299792458.0  # Speed of light in m/s

def lorentz_factor(velocity):
    """
    Calculate Lorentz factor (gamma)
    gamma = 1 / sqrt(1 - (v/c)^2)
    """
    beta = velocity / C
    if abs(beta) >= 1.0:
        raise ValueError("Velocity must be strictly less than the speed of light c.")
    return 1.0 / math.sqrt(1.0 - beta**2)

def time_dilation(proper_time, velocity):
    """
    Calculate dilated time: t = gamma * t_0
    """
    return lorentz_factor(velocity) * proper_time

def length_contraction(proper_length, velocity):
    """
    Calculate contracted length: L = L_0 / gamma
    """
    return proper_length / lorentz_factor(velocity)

if __name__ == "__main__":
    print("=== Special Relativity Computational Engine ===")
    speeds_fraction = [0.1, 0.5, 0.8, 0.9, 0.99, 0.999]
    print(f"{'v/c':<10} | {'Lorentz Factor (gamma)':<25} | {'Length (100m rod)':<20} | {'Dilated Time (1s)':<20}")
    print("-" * 80)
    for frac in speeds_fraction:
        v = frac * C
        gamma = lorentz_factor(v)
        L = length_contraction(100.0, v)
        t = time_dilation(1.0, v)
        print(f"{frac:<10.3f} | {gamma:<25.4f} | {L:<20.4f} | {t:<20.4f}")
