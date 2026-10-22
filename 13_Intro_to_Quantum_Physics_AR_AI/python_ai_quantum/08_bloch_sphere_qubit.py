"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 8: การแปลงสถานะคิวบิตและวิวัฒน์บนทรงกลมบล็อค (Bloch Sphere)
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
สถานะคิวบิตบริสุทธิ์ทั่วไปเขียนในรูปมุมโพลาร์ theta และมุมแอซิมัท phi บนทรงกลมบล็อค:
    |psi> = cos(theta/2) |0> + e^{i * phi} sin(theta/2) |1>
พิกัดคาร์ทีเซียนบนทรงกลมบล็อค:
    x = sin(theta) * cos(phi) = <psi| sigma_x |psi>
    y = sin(theta) * sin(phi) = <psi| sigma_y |psi>
    z = cos(theta)            = <psi| sigma_z |psi>
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

def qubit_to_bloch(theta, phi):
    """แปลงมุม (theta, phi) เป็นพิกัด 3 มิติ (x, y, z) บนทรงกลมบล็อค"""
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z

def run_bloch_sphere_demo():
    print("=== การแสดงผลเวกเตอร์สถานะคิวบิตบนทรงกลมบล็อค ===")
    
    # ตัวอย่างสถานะมาตรฐาน
    states = {
        r'$|0\rangle$': (0.0, 0.0),
        r'$|1\rangle$': (np.pi, 0.0),
        r'$|+\rangle$': (np.pi / 2.0, 0.0),
        r'$|-\rangle$': (np.pi / 2.0, np.pi),
        r'$|+i\rangle$': (np.pi / 2.0, np.pi / 2.0),
        r'$|-i\rangle$': (np.pi / 2.0, 3 * np.pi / 2.0),
        r'$|\psi\rangle$ (Example)': (np.pi / 3.0, np.pi / 4.0)
    }
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # วาดโครงทรงกลม (Wireframe Sphere)
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(xs, ys, zs, color="cyan", alpha=0.15, linewidth=0.5)
    
    # วาดแกน X, Y, Z
    ax.quiver(0, 0, 0, 1.3, 0, 0, color='gray', arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 1.3, 0, color='gray', arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 0, 1.3, color='gray', arrow_length_ratio=0.08)
    ax.text(1.4, 0, 0, 'X', fontsize=11, fontweight='bold')
    ax.text(0, 1.4, 0, 'Y', fontsize=11, fontweight='bold')
    ax.text(0, 0, 1.4, r'Z ($|0\rangle$)', fontsize=11, fontweight='bold')
    ax.text(0, 0, -1.4, r'($|1\rangle$)', fontsize=11, fontweight='bold')
    
    # พล็อตเวกเตอร์สถานะ
    colors = ['navy', 'darkred', 'green', 'purple', 'orange', 'brown', 'red']
    for (name, (th, ph)), c in zip(states.items(), colors):
        x, y, z = qubit_to_bloch(th, ph)
        print(f"สถานะ {name:20s}: (theta = {th:5.2f}, phi = {ph:5.2f}) -> (x={x:5.2f}, y={y:5.2f}, z={z:5.2f})")
        ax.quiver(0, 0, 0, x, y, z, color=c, arrow_length_ratio=0.1, lw=2)
        ax.scatter([x], [y], [z], color=c, s=40)
        ax.text(x * 1.15, y * 1.15, z * 1.15, name, fontsize=10, color=c)
        
    ax.set_title("Bloch Sphere Representation of Single Qubit States", fontsize=13)
    ax.set_box_aspect([1, 1, 1])
    plt.tight_layout()
    plt.savefig('bloch_sphere_states.png', dpi=200)
    print(" บันทึกภาพผลการจำลองที่ 'bloch_sphere_states.png' สำเร็จ")

if __name__ == '__main__':
    run_bloch_sphere_demo()
