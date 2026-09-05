#!/usr/bin/env python3
"""
6DoF Rigid Body & Harmonic Oscillator Physics Engine for STEM XR Labs
Author: Asst. Prof. Dr. Chewa Thassana (chewa.t@rbru.ac.th)
Rambhai Barni Rajabhat University
"""

import numpy as np

class VelocityVerletOscillator:
    def __init__(self, mass=0.5, k=20.0, damping=0.2, dt=0.01):
        self.m = mass
        self.k = k
        self.c = damping
        self.dt = dt
        
        self.pos = np.array([0.0, 1.0, 0.0], dtype=np.float64)  # displacement from equilibrium
        self.vel = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        self.acc = self._compute_acc(self.pos, self.vel)
        
    def _compute_acc(self, pos, vel):
        # F = -kx - cv
        force = -self.k * pos - self.c * vel
        return force / self.m
        
    def step(self):
        # Velocity Verlet Step
        self.pos += self.vel * self.dt + 0.5 * self.acc * (self.dt ** 2)
        new_acc = self._compute_acc(self.pos, self.vel)
        self.vel += 0.5 * (self.acc + new_acc) * self.dt
        self.acc = new_acc
        
        # Energy
        ke = 0.5 * self.m * np.dot(self.vel, self.vel)
        pe = 0.5 * self.k * np.dot(self.pos, self.pos)
        return self.pos.copy(), ke + pe

def main():
    sim = VelocityVerletOscillator(mass=0.2, k=15.0, damping=0.05, dt=0.01)
    sim.pos[0] = 0.25  # initial stretch 25 cm
    print("[Physics Engine] Simulating Damped Spring System with Velocity Verlet:")
    for step in range(150):
        pos, total_energy = sim.step()
        if step % 15 == 0:
            print(f"Step {step:03d} (t={step*0.01:.2f}s) | Pos: ({pos[0]:+.4f}, {pos[1]:+.4f}) m | E_total: {total_energy:.5f} J")
    print("[Physics Engine] Done.")

if __name__ == "__main__":
    main()
