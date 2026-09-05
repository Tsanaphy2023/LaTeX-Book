#!/usr/bin/env python3
"""
Zero-GC 21-Joint Skeletal Hand Tracking Streamer for STEM Apparatus
Author: Asst. Prof. Dr. Chewa Thassana (chewa.t@rbru.ac.th)
Rambhai Barni Rajabhat University
"""

import numpy as np
import time

class ZeroGCHandTracker:
    def __init__(self, enter_th=0.025, exit_th=0.035):
        self.enter_th = enter_th
        self.exit_th = exit_th
        self.is_pinching = False
        
        # จองบัฟเฟอร์คงที่ 21 จุดข้อต่อ (x, y, z)
        self.joints_3d = np.zeros((21, 3), dtype=np.float32)
        self._diff = np.zeros(3, dtype=np.float32)
        
    def update_mock_joints(self, t):
        # นิ้วหัวแม่มือ (Joint 4)
        self.joints_3d[4] = np.array([0.05 + 0.01*np.sin(t*3), 1.0, -0.4], dtype=np.float32)
        # ปลายนิ้วชี้ (Joint 8)
        self.joints_3d[8] = np.array([0.06 - 0.01*np.sin(t*3), 1.01, -0.4], dtype=np.float32)
        
        # คำนวณระยะห่างระหว่างปลายนิ้วชี้และนิ้วหัวแม่มือแบบ Zero-GC
        np.subtract(self.joints_3d[4], self.joints_3d[8], out=self._diff)
        dist = np.linalg.norm(self._diff)
        
        # ฟังก์ชันฮิสเทอรีซิส
        if not self.is_pinching and dist <= self.enter_th:
            self.is_pinching = True
        elif self.is_pinching and dist >= self.exit_th:
            self.is_pinching = False
            
        return self.is_pinching, dist

def main():
    tracker = ZeroGCHandTracker()
    print("[Hand Tracker] Started 21-Joint Skeletal Streamer. Zero-GC active.")
    for i in range(100):
        t = i * 0.02
        pinching, dist = tracker.update_mock_joints(t)
        if i % 10 == 0:
            status = "GRAB / PINCH ACTIVE" if pinching else "RELEASED"
            print(f"Frame {i:03d} | Pinch Distance: {dist*100:.2f} cm | Status: {status}")
        time.sleep(0.01)
    print("[Hand Tracker] Stream finished.")

if __name__ == "__main__":
    main()
