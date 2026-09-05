#!/usr/bin/env python3
"""
OpenXR Cube Simulation (STEM Virtual Space)
Author: Asst. Prof. Dr. Chewa Thassana (chewa.t@rbru.ac.th)
Rambhai Barni Rajabhat University
"""

import sys
import time
import numpy as np

def init_openxr_session():
    print("[OpenXR STEM] Initializing OpenXR Instance...")
    print("[OpenXR STEM] Selected Runtime: Monado / Khronos OpenXR Standard")
    print("[OpenXR STEM] Requesting Extensions: XR_KHR_opengl_enable, XR_EXT_hand_tracking")
    time.sleep(0.1)
    print("[OpenXR STEM] Reference Space created: XR_REFERENCE_SPACE_TYPE_STAGE (Room-scale)")
    return True

def render_stem_cube(t):
    # คำนวณการหมุนของคิวบ์จำลองทางฟิสิกส์
    omega = 1.5  # rad/s
    angle = omega * t
    q_y = np.sin(angle / 2.0)
    q_w = np.cos(angle / 2.0)
    
    pos = np.array([0.0, 1.2 + 0.1 * np.sin(2.0 * t), -0.8], dtype=np.float32)
    return pos, (q_w, 0.0, q_y, 0.0)

def main():
    if not init_openxr_session():
        sys.exit(1)
        
    print("[OpenXR STEM] Entering 90 FPS Simulation Loop. Press Ctrl+C to stop.")
    start_time = time.time()
    frame_count = 0
    
    try:
        while frame_count < 180:  # ทดสอบรันตัวอย่าง 2 วินาที
            t = time.time() - start_time
            pos, quat = render_stem_cube(t)
            if frame_count % 30 == 0:
                print(f"Frame {frame_count:04d} | Pos: ({pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f}) | Quat(w,y): ({quat[0]:.3f}, {quat[2]:.3f})")
            frame_count += 1
            time.sleep(0.011)  # ~90 FPS
    except KeyboardInterrupt:
        pass
        
    print("[OpenXR STEM] Simulation ended cleanly.")

if __name__ == "__main__":
    main()
