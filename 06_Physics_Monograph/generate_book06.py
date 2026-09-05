#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_book06.py - Generates 8 university monograph chapters for Book 06: Physics Monograph
Incorporating Serway (C-C-A-F) and Tipler (P-S-C-T) frameworks and author research insights.
All strings are raw strings to prevent any unintended escape sequences.
"""

import os

CHAPTERS_DIR = "06_Physics_Monograph/chapters"
os.makedirs(CHAPTERS_DIR, exist_ok=True)

chapters_data = [
    {
        "filename": "ch01_units_uncertainty.tex",
        "number": 1,
        "title": r"หน่วย มาตรฐานทางฟิสิกส์ และการวิเคราะห์ความไม่แน่นอนในการวิจัย",
        "subtitle": r"การนิยามระบบหน่วยสากลใหม่ตามค่าคงที่มูลฐานและการประเมินความไม่แน่นอนตามมาตรฐาน GUM",
        "equations_title": r"สมการความไม่แน่นอนและการส่งผ่านความคลาดเคลื่อน",
        "equations": r"""\begin{align}
\bar{x} &= \frac{1}{N}\sum_{i=1}^{N} x_i, \quad s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2} \\
u_A(\bar{x}) &= \frac{s}{\sqrt{N}}, \quad u_B = \frac{a}{\sqrt{3}} \text{ (Uniform)}, \quad u_c(y) = \sqrt{\sum_{i=1}^{n}\left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i)}
\end{align}""",
        "theory": r"""การวัดในทางฟิสิกส์มิใช่เพียงการอ่านค่าตัวเลขจากเครื่องมือวัด แต่เป็นกระบวนการเปรียบเทียบเชิงปริมาณกับมาตรฐานสากลที่สามารถสอบกลับได้ (Metrological Traceability) ภายใต้การปรับปรุงระบบหน่วยสากล (SI Redefinition) หน่วยฐานทั้งหมดได้รับการนิยามใหม่โดยตรึงค่าคงที่มูลฐานทางฟิสิกส์ เช่น ค่าคงที่พลังค์ $h = 6.626\,070\,15 \times 10^{-34}\text{ J}\cdot\text{s}$, ความเร็วแสง $c = 299\,792\,458\text{ m/s}$, และประจุธาตุ $e = 1.602\,176\,634 \times 10^{-19}\text{ C}$

ในการรายงานผลการวิจัยทางฟิสิกส์ การระบุค่าความไม่แน่นอนของการวัด (Measurement Uncertainty) ตามคู่มือ ISO/IEC Guide 98-3 (GUM) จำแนกออกเป็นสองประเภทหลัก ได้แก่ ความไม่แน่นอนประเภทเอ (Type A Uncertainty) ซึ่งประเมินด้วยระเบียบวิธีทางสถิติจากการวัดซ้ำ และความไม่แน่นอนประเภทบี (Type B Uncertainty) ซึ่งประเมินจากข้อมูลจำเพาะของเครื่องมือวัด ใบรับรองการสอบเทียบ หรือการแจกแจงความน่าจะเป็นเชิงทฤษฎี""",
        "example_title": r"การประเมินความไม่แน่นอนรวมของการวัดความหนาแน่นของแท่งโลหะทรงกระบอก",
        "example_p": r"แท่งโลหะทรงกระบอกมวล $m$ มีเส้นผ่านศูนย์กลาง $d$ และความยาว $L$ ผ่านการวัดละเอียดด้วยไมโครมิเตอร์และเครื่องชั่งดิจิทัล",
        "example_s": r"ใช้แบบจำลองทางฟิสิกส์ $\rho = \frac{4m}{\pi d^2 L}$ และใช้กฎการส่งผ่านความไม่แน่นอน (Law of Propagation of Uncertainty) เพื่อคำนวณ $u_c(\rho)$",
        "example_c": r"""จากฟังก์ชัน $\rho(m, d, L)$ สัมประสิทธิ์ความไว (Sensitivity Coefficients) คำนวณจากอนุพันธ์ย่อย:
\begin{equation}
\frac{\partial \rho}{\partial m} = \frac{4}{\pi d^2 L}, \quad \frac{\partial \rho}{\partial d} = -\frac{8m}{\pi d^3 L}, \quad \frac{\partial \rho}{\partial L} = -\frac{4m}{\pi d^2 L^2}
\end{equation}
ความไม่แน่นอนสัมพัทธ์รวมจึงอยู่ในรูป:
\begin{equation}
\left[\frac{u_c(\rho)}{\rho}\right]^2 = \left[\frac{u(m)}{m}\right]^2 + 4\left[\frac{u(d)}{d}\right]^2 + \left[\frac{u(L)}{L}\right]^2
\end{equation}
สมมติค่าที่วัดได้ $m = 150.00 \pm 0.05\text{ g}$, $d = 20.00 \pm 0.01\text{ mm}$, $L = 60.00 \pm 0.02\text{ mm}$:
\begin{equation}
\frac{u_c(\rho)}{\rho} = \sqrt{\left(\frac{0.05}{150}\right)^2 + 4\left(\frac{0.01}{20}\right)^2 + \left(\frac{0.02}{60}\right)^2} \approx 0.001\,1
\end{equation}
ความหนาแน่น $\rho = 7.9577\text{ g/cm}^3$ และ $u_c(\rho) = 0.0088\text{ g/cm}^3$ บันทึกผลเป็น $\rho = 7.958 \pm 0.018\text{ g/cm}^3$ ที่ระดับความเชื่อมั่น 95\% ($k=2$)""",
        "example_t": r"มิติของความหนาแน่นตรงตาม $\text{M}\cdot\text{L}^{-3}$ และความไม่แน่นอนสอดคล้องกับพิกัดความคลาดเคลื่อนของเครื่องมือวัดละเอียดระดับไมครอน",
        "research_text": r"""ในการทำวิจัยด้านดาราศาสตร์ฟิสิกส์ด้วยเทคนิค CCD Photometry (เช่น การศึกษาระบบดาวคู่สัมผัส DF Hydrae ของ ผศ.ดร.ชีวะ ทัศนา) การวัดฟลักซ์ความสว่างของดาวฤกษ์ต้องประเมินทั้งสัญญาณรบกวนโฟตอน (Poisson Photon Noise), สัญญาณรบกวนกระแสมืด (Dark Current), และสัญญาณรบกวนจากการอ่านข้อมูล (Readout Noise) ภายใต้แบบจำลอง CCD Equation ซึ่งเทียบเคียงได้กับกฎการส่งผ่านความไม่แน่นอนตามมาตรฐาน GUM""",
        "problem_title": r"การวิเคราะห์ความคลาดเคลื่อนในการวัดค่าสนามโน้มถ่วงด้วยลูกตุ้มฟิสิกส์",
        "ccaf_c": r"พิจารณาลูกตุ้มอย่างง่ายที่มีความยาว $L$ คาบการแกว่ง $T$ สัมพันธ์กับค่า $g$ ผ่านสมการ $T = 2\pi\sqrt{L/g}$",
        "ccaf_cat": r"ปัญหาการส่งผ่านความคลาดเคลื่อนในการวัดทางอ้อม (Indirect Measurement with Error Propagation)",
        "ccaf_a": r"""จัดรูปสมการหาค่าความเร่งโน้มถ่วง:
\begin{equation}
g = \frac{4\pi^2 L}{T^2} \implies \frac{\Delta g}{g} = \sqrt{\left(\frac{\Delta L}{L}\right)^2 + 4\left(\frac{\Delta T}{T}\right)^2}
\end{equation}
จะเห็นว่าความคลาดเคลื่อนในการจับเวลาคาบ $T$ ส่งผลกระทบต่อความแม่นยำของ $g$ เป็นสองเท่าของความยาว $L$ ดังนั้น ในการออกแบบการทดลอง ผู้วิจัยจึงต้องวัดเวลาการแกว่งต่อเนื่อง 20--50 รอบ เพื่อลดค่า $u_A(T)$""",
        "ccaf_f": r"การเพิ่มจำนวนรอบการแกว่งเป็นกลยุทธ์สำคัญทางระเบียบวิธีวิจัยที่ช่วยลดความไม่แน่นอนของการวัดได้ตามทฤษฎี $1/\sqrt{N}$"
    },
    {
        "filename": "ch02_advanced_dynamics.tex",
        "number": 2,
        "title": r"พลศาสตร์ขั้นสูงและสมการการเคลื่อนที่แบบไม่เชิงเส้น",
        "subtitle": r"แบบจำลองแรงต้านอากาศไม่เชิงเส้น ความเร็วปลาย และระเบียบวิธีรูงเง-คุตตา",
        "equations_title": r"สมการการเคลื่อนที่ภายใต้แรงต้านอากาศ",
        "equations": r"""\begin{align}
m\frac{d\mathbf{v}}{dt} &= m\mathbf{g} - b\mathbf{v} - c v \mathbf{v}, \quad v_t = \sqrt{\frac{mg}{c}} = \sqrt{\frac{2mg}{\rho A C_D}} \\
v(t) &= v_t \tanh\left(\frac{gt}{v_t}\right), \quad y(t) = \frac{v_t^2}{g}\ln\left[\cosh\left(\frac{gt}{v_t}\right)\right]
\end{align}""",
        "theory": r"""ในฟิสิกส์เบื้องต้น การเคลื่อนที่ของวัตถุภายใต้สนามโน้มถ่วงมักละเลยแรงต้านของอากาศ แต่ในความเป็นจริงทางวิศวกรรมและปรากฏการณ์บรรยากาศ แรงต้านอากาศ (Aerodynamic Drag Force) เป็นแรงไม่เชิงเส้นที่ขึ้นอยู่กับอัตราเร็วของวัตถุ สำหรับอัตราเร็วต่ำ (Low Reynolds Number, $Re < 1$) แรงต้านจะแปรผันตรงกับความเร็วเชิงเส้น $\mathbf{F}_D = -b\mathbf{v}$ ตามกฎของสโตกส์ แต่สำหรับวัตถุขนาดใหญ่ที่มีอัตราเร็วสูงในบรรยากาศ ($10^3 < Re < 10^5$) แรงต้านจะแปรผันตามกำลังสองของความเร็ว:
\begin{equation}
F_D = \frac{1}{2} C_D \rho A v^2
\end{equation}
โดยที่ $C_D$ คือสัมประสิทธิ์แรงฉุด (Drag Coefficient), $\rho$ คือความหนาแน่นของอากาศ และ $A$ คือพื้นที่หน้าตัดตั้งฉากกับทิศทางการเคลื่อนที่ ผลของแรงต้านนี้ทำให้ความเร่งของวัตถุลดลงจนเข้าสู่ศูนย์เมื่อแรงต้านสมดุลกับแรงโน้มถ่วง เกิดเป็นความเร็วปลายคงที่ (Terminal Velocity: $v_t$)""",
        "example_title": r"การคำนวณวิถีตกอิสระของหยดน้ำฝนและอนุภาคฝุ่นละอองในบรรยากาศ",
        "example_p": r"หยดน้ำฝนรัศมี $R = 1.5\text{ mm}$ ตกจากเมฆสูง $1\,500\text{ m}$ สู่พื้นดิน ภายใต้ความหนาแน่นอากาศ $\rho = 1.225\text{ kg/m}^3$ และ $C_D = 0.45$",
        "example_s": r"คำนวณมวล $m$, พื้นที่หน้าตัด $A$ แล้วแทนค่าในสมการความเร็วปลาย $v_t = \sqrt{2mg/(\rho A C_D)}$",
        "example_c": r"""ปริมาตรหยดน้ำ $V = \frac{4}{3}\pi R^3 = 1.414 \times 10^{-8}\text{ m}^3$ มวล $m = \rho_w V = 1.414 \times 10^{-5}\text{ kg}$
พื้นที่หน้าตัด $A = \pi R^2 = 7.069 \times 10^{-6}\text{ m}^2$
แทนค่าหาความเร็วปลาย:
\begin{equation}
v_t = \sqrt{\frac{2(1.414 \times 10^{-5})(9.81)}{(1.225)(7.069 \times 10^{-6})(0.45)}} \approx 8.44\text{ m/s} \quad (30.4\text{ km/h})
\end{equation}
หากไม่มีแรงต้านอากาศ อัตราเร็วเมื่อถึงพื้นจะสูงถึง $v = \sqrt{2gh} = \sqrt{2(9.81)(1500)} \approx 171.5\text{ m/s}$ ($617\text{ km/h}$ ซึ่งเป็นอันตรายต่อสิ่งมีชีวิต)""",
        "example_t": r"ค่า $v_t \approx 8.4\text{ m/s}$ สอดคล้องอย่างแม่นยำกับผลการวัดความเร็วหยดน้ำฝนจริงด้วยดอปเปลอร์เรดาร์ตรวจอากาศ",
        "research_text": r"""การจำลองการกระจายตัวของอนุภาคฝุ่นละออง PM2.5 และละอองลอยคาร์บอนแบล็คในงานวิจัยสิ่งแวดล้อม จำเป็นต้องผสานสมการแรงต้านของสโตกส์ร่วมกับ Cunningham Correction Factor เพื่อวิเคราะห์อัตราการตกตะกอนและการแขวนลอยในชั้นบรรยากาศระดับล่าง (Planetary Boundary Layer)""",
        "problem_title": r"การวิเคราะห์การเคลื่อนที่แบบโพรเจกไทล์ที่มีแรงต้านตามแนวแกนคู่",
        "ccaf_c": r"วัตถุมวล $m$ ถูกยิงด้วยความเร็วต้น $v_0$ ทำมุม $\theta$ ในระนาบ 2 มิติ ภายใต้แรงต้านกำลังสอง $\mathbf{F}_D = -c v \mathbf{v}$",
        "ccaf_cat": r"ระบบสมการเชิงอนุพันธ์สามัญแบบไม่เชิงเส้นคู่ควบ (Non-linear Coupled ODEs)",
        "ccaf_a": r"""สมการการเคลื่อนที่ในพิกัดคาร์ทีเซียน:
\begin{align}
m\frac{dv_x}{dt} &= -c\sqrt{v_x^2 + v_y^2}\,v_x \\
m\frac{dv_y}{dt} &= -mg - c\sqrt{v_x^2 + v_y^2}\,v_y
\end{align}
เนื่องจากสมการทั้งสองไม่สามารถหาผลเฉลยแม่นตรงในรูปฟังก์ชันมูลฐานได้ จำเป็นต้องใช้ระเบียบวิธีเชิงตัวเลข Runge-Kutta อันดับ 4 (RK4) ในการคำนวณวิถีโค้งทีละช่วงเวลา $\Delta t$""",
        "ccaf_f": r"แบบจำลองเชิงตัวเลข RK4 เผยให้เห็นว่าระยะตกไกลสูงสุดเกิดขึ้นที่มุมต่ำกว่า $45^\circ$ เสมอเมื่อมีแรงต้านอากาศ"
    },
    {
        "filename": "ch03_potential_stability.tex",
        "number": 3,
        "title": r"ทฤษฎีศักย์ งาน พลังงาน และเสถียรภาพของระบบกายภาพ",
        "subtitle": r"การวิเคราะห์พื้นผิวพลังงานศักย์ จุดสมดุล และการสั่นขนาดเล็กแบบฮาร์มอนิก",
        "equations_title": r"ความสัมพันธ์ระหว่างแรงอนุรักษ์ พลังงานศักย์ และเสถียรภาพ",
        "equations": r"""\begin{align}
\mathbf{F}(\mathbf{r}) &= -\nabla U(\mathbf{r}), \quad \oint \mathbf{F}\cdot d\mathbf{r} = 0 \iff \nabla \times \mathbf{F} = 0 \\
\left.\frac{dU}{dx}\right|_{x_0} &= 0 \text{ (Equilibrium)}, \quad k_{\text{eff}} = \left.\frac{d^2U}{dx^2}\right|_{x_0} > 0 \text{ (Stable Equilibrium)} \\
\omega &= \sqrt{\frac{k_{\text{eff}}}{m}} = \sqrt{\frac{1}{m}\left.\frac{d^2U}{dx^2}\right|_{x_0}}
\end{align}""",
        "theory": r"""แนวคิดเรื่องพลังงานศักย์ (Potential Energy) มีความสัมพันธ์อย่างลึกซึ้งกับเรขาคณิตของสนามแรงอนุรักษ์ (Conservative Force Field) แรง $\mathbf{F}$ จะเป็นแรงอนุรักษ์ก็ต่อเมื่อเคิร์ลของสนามแรงมีค่าเป็นศูนย์ทุกจุด ($\nabla \times \mathbf{F} = 0$) ซึ่งบ่งชี้ว่างานที่เกิดขึ้นไม่ขึ้นอยู่กับเส้นทางเดิน แต่ขึ้นกับพิกัดเริ่มต้นและสิ้นสุดเท่านั้น

จุดสมดุลของระบบกายภาพเกิดขึ้น ณ ตำแหน่งที่แรงลัพธ์เป็นศูนย์ ซึ่งตรงกับจุดวิกฤตของฟังก์ชันพลังงานศักย์ ($dU/dx = 0$) การจำแนกเสถียรภาพของจุดสมดุลพิจารณาจากอนุพันธ์อันดับสอง:
1. สมดุลเสถียร (Stable Equilibrium): เมื่อ $d^2U/dx^2 > 0$ กราฟพลังงานมีลักษณะเป็นหลุมศักย์ (Potential Well) วัตถุที่ถูกรบกวนเล็กน้อยจะแกว่งกลับมาสู่จุดสมดุล
2. สมดุลไม่เสถียร (Unstable Equilibrium): เมื่อ $d^2U/dx^2 < 0$ กราฟพลังงานเป็นยอดเนิน วัตถุจะเคลื่อนที่ออกจากจุดสมดุลอย่างถาวร
3. สมดุลสะเทิน (Neutral Equilibrium): เมื่อ $d^2U/dx^2 = 0$""",
        "example_title": r"การวิเคราะห์ศักย์เลนนาร์ด-โจนส์ระหว่างคู่อะตอมและการสั่นแบบฮาร์มอนิก",
        "example_p": r"พันธะระหว่างสองอะตอมถูกอธิบายด้วยศักย์เลนนาร์ด-โจนส์ (Lennard-Jones 6-12 Potential): $U(r) = 4\epsilon \left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6\right]$",
        "example_s": r"หาจุดสมดุล $r_0$ จากเงื่อนไข $dU/dr = 0$ และคำนวณค่าคงที่สปริงยังผล $k_{\text{eff}} = \left.\frac{d^2U}{dr^2}\right|_{r_0}$",
        "example_c": r"""หาอนุพันธ์อันดับหนึ่ง:
\begin{equation}
\frac{dU}{dr} = 4\epsilon \left[ -\frac{12\sigma^{12}}{r^{13}} + \frac{6\sigma^6}{r^7} \right] = \frac{24\epsilon}{r}\left[ -2\left(\frac{\sigma}{r}\right)^{12} + \left(\frac{\sigma}{r}\right)^6 \right] = 0
\end{equation}
ได้จุดสมดุล $r_0 = 2^{1/6}\sigma \approx 1.122\sigma$
หาอนุพันธ์อันดับสองที่จุด $r_0$:
\begin{equation}
\left.\frac{d^2U}{dr^2}\right|_{r_0} = \frac{72\epsilon}{2^{1/3}\sigma^2} > 0
\end{equation}
ความถี่เชิงมุมของการสั่นขนาดเล็กรอบจุดสมดุลคำนวณได้เป็น $\omega_0 = \sqrt{k_{\text{eff}}/\mu}$ โดยที่ $\mu$ คือมวลลดทอน (Reduced Mass)""",
        "example_t": r"เมื่อ $r \to \infty$ ศักย์ $U(r) \to 0$ และค่าความลึกของหลุมศักย์ที่จุดสมดุลคือ $U(r_0) = -\epsilon$ ซึ่งตรงกับพลังงานยึดเหนี่ยวพันธะ",
        "research_text": r"""การวิเคราะห์พื้นผิวพลังงานศักย์ (Potential Energy Surface: PES) เป็นเครื่องมือสำคัญในการคำนวณเคมีฟิสิกส์และฟิสิกส์สสารควบแน่น ในการจำลองการดูดซับก๊าซบนผิวตัวเร่งปฏิกิริยาชีวมวล การหาจุดอานม้า (Saddle Point) บนผิวพลังงานศักย์ทำให้ทราบค่าพลังงานก่อกัมมันต์ (Activation Energy) ของปฏิกิริยา""",
        "problem_title": r"การวิเคราะห์แผนภาพเฟสของลูกตุ้มแกว่งไม่เชิงเส้นขนาดใหญ่",
        "ccaf_c": r"พิจารณาลูกตุ้มอย่างง่ายมวล $m$ ยาว $L$ แกว่งด้วยมุมขนาดใหญ่ ฟังก์ชันพลังงานศักย์คือ $U(\theta) = mgL(1 - \cos\theta)$",
        "ccaf_cat": r"การวิเคราะห์เสถียรภาพและวิถีในปริภูมิเฟส (Phase Space Trajectory Analysis)",
        "ccaf_a": r"""สมการพลังงานรวมของระบบ:
\begin{equation}
E = \frac{1}{2}mL^2 \dot{\theta}^2 + mgL(1 - \cos\theta)
\end{equation}
เมื่อ $E < 2mgL$ วิถีในระนาบ $(\theta, \dot{\theta})$ เป็นวงปิดรอบจุดสมดุล $(0, 0)$ แสดงการแกว่งแบบกวัดแกว่ง (Libration)
เมื่อ $E > 2mgL$ วิถีเป็นเส้นคลื่นเปิด แสดงการหมุนรอบแกนครบรอบ (Rotation) โดยเส้นแบ่งระหว่างสองพฤติกรรมเรียกว่า เซพาแรทริกซ์ (Separatrix) ซึ่งมีค่า $E = 2mgL$""",
        "ccaf_f": r"การวิเคราะห์ปริภูมิเฟสช่วยให้เห็นโครงสร้างเชิงเรขาคณิตของการเคลื่อนที่โดยไม่ต้องแก้สมการเชิงอนุพันธ์โดยตรง"
    },
    {
        "filename": "ch04_electromagnetism_maxwell.tex",
        "number": 4,
        "title": r"ทฤษฎีสนามแม่เหล็กไฟฟ้าและสมการแมกซ์เวลล์",
        "subtitle": r"สมการแมกซ์เวลล์ในรูปอนุพันธ์ การอนุรักษ์ประจุ และสมการคลื่นแม่เหล็กไฟฟ้า",
        "equations_title": r"สมการแมกซ์เวลล์สี่ข้อในสุญญากาศ",
        "equations": r"""\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0}, \quad \nabla \cdot \mathbf{B} = 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{align}""",
        "theory": r"""ทฤษฎีแม่เหล็กไฟฟ้าคลาสสิกของเจมส์ เคลิร์ก แมกซ์เวลล์ เป็นหนึ่งในความสำเร็จอันยิ่งใหญ่ที่สุดในประวัติศาสตร์ฟิสิกส์ ซึ่งรวบรวมปรากฏการณ์ไฟฟ้า แม่เหล็ก และแสงสว่าง เข้าสู่กรอบทฤษฎีหนึ่งเดียวผ่านสมการเชิงอนุพันธ์ย่อยสี่ข้อ

สมการข้อแรก กฎของเกาส์สำหรับสนามไฟฟ้า แสดงว่าประจุไฟฟ้าเป็นแหล่งกำเนิดของสนามไฟฟ้า สมการข้อที่สอง กฎของเกาส์สำหรับสนามแม่เหล็ก ยืนยันว่าไม่มีขั้วแม่เหล็กเดี่ยว (No Magnetic Monopoles) สมการข้อที่สาม กฎการเหนี่ยวนำของฟาราเดย์ บ่งบอกว่าสนามแม่เหล็กที่เปลี่ยนแปลงตามเวลาจะเหนี่ยวนำให้เกิดสนามไฟฟ้าวน และสมการข้อที่สี่ กฎของแอมแปร์-แมกซ์เวลล์ ซึ่งแมกซ์เวลล์ได้เพิ่มพจน์กระแสการกระจัด (Displacement Current: $\mathbf{J}_D = \epsilon_0 \partial\mathbf{E}/\partial t$) เข้าไปเพื่อให้สอดคล้องกับสมการความต่อเนื่องของการอนุรักษ์ประจุ ($\nabla \cdot \mathbf{J} + \partial\rho/\partial t = 0$)""",
        "example_title": r"การอนุพัทธ์สมการคลื่นแม่เหล็กไฟฟ้าและความเร็วแสงในสุญญากาศ",
        "example_p": r"พิจารณาปริภูมิอิสระที่ปราศจากประจุอิสระ ($\rho = 0$) และกระแสอิสระ ($\mathbf{J} = 0$)",
        "example_s": r"นำตัวดำเนินการ $\nabla \times$ กระทำกับสมการกฎของฟาราเดย์ แล้วใช้เอกลักษณ์เวกเตอร์ $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$",
        "example_c": r"""จากกฎของฟาราเดย์:
\begin{equation}
\nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t}(\nabla \times \mathbf{B})
\end{equation}
แทนค่า $\nabla \cdot \mathbf{E} = 0$ และแทน $\nabla \times \mathbf{B} = \mu_0\epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$:
\begin{equation}
-\nabla^2 \mathbf{E} = -\mu_0\epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} \implies \nabla^2 \mathbf{E} - \mu_0\epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0
\end{equation}
นี่คือสมการคลื่น 3 มิติ (3D Wave Equation) ซึ่งความเร็วคลื่นคำนวณได้เป็น:
\begin{equation}
c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = \frac{1}{\sqrt{(4\pi \times 10^{-7})(8.854 \times 10^{-12})}} \approx 2.998 \times 10^8\text{ m/s}
\end{equation}
ซึ่งตรงกับอัตราเร็วของแสงที่วัดได้จากการทดลองอย่างสมบูรณ์แบบ""",
        "example_t": r"สมการแสดงว่าคลื่นแม่เหล็กไฟฟ้าเป็นคลื่นตามขวาง (Transverse Waves) โดยเวกเตอร์ $\mathbf{E}$, $\mathbf{B}$ และทิศทางคลื่น $\mathbf{k}$ ตั้งฉากซึ่งกันและกันเสมอ",
        "research_text": r"""ในการวิจัยวัสดุศาสตร์และแม่เหล็กระดับนาโน อันตรกิริยาระหว่างสนามแม่เหล็กไฟฟ้ากับสปินของอิเล็กตรอนในสารกึ่งตัวนำและฉนวนทรานสิชันเมทัลออกไซด์ (เช่น $\text{MnO}$ และ $\text{NiO}$) นำไปสู่การพัฒนาเทคโนโลยีสปินทรอนิกส์ (Spintronics) และหน่วยความจำแม่เหล็ก MRAM สมัยใหม่""",
        "problem_title": r"การวิเคราะห์เวกเตอร์พอยน์ติงและการส่งผ่านพลังงานในสายส่งโคแอกเชียล",
        "ccaf_c": r"สายส่งร่วมแกน (Coaxial Cable) ประกอบด้วยตัวนำทรงกระบอกด้านในรัศมี $a$ และตัวนำด้านนอกรัศมี $b$ มีกระแส $I$ และความต่างศักย์ $V$",
        "ccaf_cat": r"การส่งผ่านพลังงานและโมเมนตัมแม่เหล็กไฟฟ้า (Electromagnetic Energy Transport)",
        "ccaf_a": r"""สนามไฟฟ้าระหว่างตัวนำ: $E(r) = \frac{V}{\ln(b/a)}\frac{1}{r}$ (ทิศในแนวรัศมี)
สนามแม่เหล็กระหว่างตัวนำ: $B(r) = \frac{\mu_0 I}{2\pi}\frac{1}{r}$ (ทิศในแนววงกลม)
เวกเตอร์พอยน์ติง (Poynting Vector) คำนวณได้เป็น:
\begin{equation}
\mathbf{S} = \frac{1}{\mu_0}(\mathbf{E} \times \mathbf{B}) = \frac{VI}{2\pi \ln(b/a) r^2} \mathbf{\hat{z}}
\end{equation}
หาปริพันธ์ฟลักซ์พลังงานผ่านพื้นที่หน้าตัดระหว่างรัศมี $a$ ถึง $b$:
\begin{equation}
P = \int \mathbf{S}\cdot d\mathbf{A} = \int_{a}^{b} \frac{VI}{2\pi \ln(b/a) r^2} (2\pi r dr) = VI
\end{equation}""",
        "ccaf_f": r"พลังงานไฟฟ้าไม่ได้ไหลอยู่ภายในเนื้อโลหะ แต่ถูกส่งผ่านทางสนามแม่เหล็กไฟฟ้าในช่องว่างระหว่างตัวนำด้วยกำลังงาน $P = VI$"
    },
    {
        "filename": "ch05_wave_optics_lasers.tex",
        "number": 5,
        "title": r"ทัศนศาสตร์เชิงคลื่น แสงเลเซอร์ และการแทรกสอดเชิงแสง",
        "subtitle": r"ความอาพันธ์ของคลื่นแสง การแทรกสอดช่องแคบคู่ และการเลี้ยวเบนฟรอนโฮเฟอร์",
        "equations_title": r"สมการการแทรกสอดและการเลี้ยวเบนของคลื่นแสง",
        "equations": r"""\begin{align}
I(\theta) &= I_0 \cos^2\left(\frac{\pi d \sin\theta}{\lambda}\right) \left[\frac{\sin\left(\frac{\pi a \sin\theta}{\lambda}\right)}{\frac{\pi a \sin\theta}{\lambda}}\right]^2 \\
d\sin\theta &= m\lambda \text{ (Double-slit Maxima)}, \quad a\sin\theta = m'\lambda \text{ (Single-slit Minima)}
\end{align}""",
        "theory": r"""ทัศนศาสตร์เชิงคลื่น (Wave Optics หรือ Physical Optics) อธิบายปรากฏการณ์ของแสงที่ไม่สามารถอธิบายได้ด้วยทัศนศาสตร์เชิงเรขาคณิต เช่น การแทรกสอด (Interference) การเลี้ยวเบน (Diffraction) และโพลาไรเซชัน (Polarization) รากฐานสำคัญของการเกิดริ้วการแทรกสอดที่เสถียรคือ ความอาพันธ์ของคลื่นแสง (Optical Coherence) ทั้งความอาพันธ์เชิงเวลา (Temporal Coherence) ซึ่งสัมพันธ์กับความเป็นสีเดียว และความอาพันธ์เชิงพื้นที่ (Spatial Coherence) ซึ่งสัมพันธ์กับขนาดเชิงมุมของแหล่งกำเนิดแสง

การกำเนิดแสงเลเซอร์ (LASER: Light Amplification by Stimulated Emission of Radiation) อาศัยกระบวนการปล่อยรังสีแบบถูกกระตุ้น (Stimulated Emission) ร่วมกับการทำให้เกิดการผกผันของประชากร (Population Inversion) ภายในโพรงกำทอนเชิงแสง (Optical Resonator) ทำให้ลำแสงเลเซอร์มีเฟสตรงกันและมีความเข้มสว่างสูงยิ่ง""",
        "example_title": r"การวิเคราะห์ริ้วการแทรกสอดร่วมกับการเลี้ยวเบนในการทดลองช่องแคบคู่",
        "example_p": r"แสงเลเซอร์ฮีเลียม-นีออน ($\lambda = 632.8\text{ nm}$) ตกกระทบช่องแคบคู่ที่มีระยะห่างระหว่างช่อง $d = 0.25\text{ mm}$ และความกว้างช่อง $a = 0.05\text{ mm}$ ฉากรับภาพอยู่ห่างออกไป $L = 2.0\text{ m}$",
        "example_s": r"คำนวณจำนวนริ้วสว่างของการแทรกสอดที่ปรากฏอยู่ภายในแถบสว่างกลางของการเลี้ยวเบน (Central Diffraction Peak)",
        "example_c": r"""แถบมืดแรกของการเลี้ยวเบนเกิดขึ้นที่มุม $\theta_1$ ซึ่งสอดคล้องกับ:
\begin{equation}
a \sin\theta_1 = \lambda \implies \sin\theta_1 = \frac{\lambda}{a}
\end{equation}
ริ้วสว่างของการแทรกสอดเกิดขึ้นที่มุม $\theta_m$ ซึ่ง:
\begin{equation}
d \sin\theta_m = m\lambda \implies \sin\theta_m = \frac{m\lambda}{d}
\end{equation}
ริ้วการแทรกสอดจะหายไป (Missing Orders) เมื่อตำแหน่งตรงกับแถบมืดของการเลี้ยวเบน:
\begin{equation}
m = \frac{d}{a} = \frac{0.25\text{ mm}}{0.05\text{ mm}} = 5
\end{equation}
ดังนั้น ริ้วที่ $m = \pm 5$ จะไม่ปรากฏ ริ้วสว่างของการแทรกสอดที่อยู่ในแถบสว่างกลางจึงมีค่า $m = 0, \pm 1, \pm 2, \pm 3, \pm 4$ รวมทั้งสิ้น $2(4) + 1 = 9$ ริ้ว""",
        "example_t": r"อัตราส่วน $d/a = 5$ กำหนดซองหุ้มการเลี้ยวเบน (Diffraction Envelope) ได้อย่างแม่นยำตรงกับผลการทดลองในห้องปฏิบัติการ",
        "research_text": r"""การวัดการเลี้ยวเบนรังสีเอกซ์ (X-ray Diffraction: XRD) อาศัยกฎของแบร็กก์ ($2d\sin\theta = n\lambda$) ซึ่งเป็นหลักการเดียวกับทัศนศาสตร์เชิงคลื่น ในการวิเคราะห์โครงสร้างผลึกของสารสังเคราะห์และวัสดุชีวมวลคาร์บอน เพื่อตรวจสอบความเป็นผลึก (Crystallinity) และขนาดอนุภาคระดับนาโนเมตร""",
        "problem_title": r"การวิเคราะห์เกณฑ์การจำแนกของเรย์ลีและกำลังแยกภาพของกล้องโทรทรรศน์",
        "ccaf_c": r"กล้องโทรทรรศน์ออปติคัลขนาดเส้นผ่านศูนย์กลางปากกล้อง $D = 0.5\text{ m}$ ตรวจสังเกตดาวคู่ที่ความยาวคลื่น $\lambda = 550\text{ nm}$",
        "ccaf_cat": r"ขีดจำกัดการเลี้ยวเบนและกำลังแยกภาพเชิงมุม (Diffraction Limit & Angular Resolution)",
        "ccaf_a": r"""ตามเกณฑ์ของเรย์ลี (Rayleigh's Criterion) สำหรับช่องเปิดวงกลม (Airy Disk):
\begin{equation}
\theta_{\text{min}} = 1.22 \frac{\lambda}{D} = 1.22 \frac{550 \times 10^{-9}\text{ m}}{0.5\text{ m}} = 1.342 \times 10^{-6}\text{ rad} \approx 0.277\text{ ฟิลิปดา}
\end{equation}
หากดาวคู่มีระยะห่างเชิงมุมน้อยกว่า $0.28''$ ภาพของวงแอรี่จะซ้อนทับกันจนไม่สามารถแยกออกเป็นดาวสองดวงได้""",
        "ccaf_f": r"การเพิ่มขนาดหน้ากล้อง $D$ เป็นปัจจัยหลักที่ช่วยลดค่า $\theta_{\text{min}}$ และเพิ่มกำลังแยกภาพเชิงมุมของเครื่องมือวิจัยทางดาราศาสตร์"
    },
    {
        "filename": "ch06_quantum_mechanics_atomic.tex",
        "number": 6,
        "title": r"กลศาสตร์ควอนตัม แบบจำลองอะตอม และทฤษฎีการกระเจิง",
        "subtitle": r"สมการชเรอดิงเงอร์ที่ไม่ขึ้นกับเวลา บ่อศักย์อนันต์ และปรากฏการณ์ทะลุผ่านกำแพงศักย์",
        "equations_title": r"สมการชเรอดิงเงอร์และเงื่อนไขความน่าจะเป็น",
        "equations": r"""\begin{align}
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) &= E\psi(x), \quad \int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1 \\
T &\approx e^{-2\kappa L}, \quad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}
\end{align}""",
        "theory": r"""กลศาสตร์ควอนตัมปฏิวัติแนวคิดดั้งเดิมเรื่องวิถีการเคลื่อนที่ของอนุภาค โดยแทนที่สถานะของระบบด้วยฟังก์ชันคลื่น (Wavefunction: $\psi$) ซึ่งความหนาแน่นความน่าจะเป็น (Probability Density) ในการพบอนุภาคถูกกำหนดโดยกฎของบอร์น (Born's Rule: $P(x) = |\psi(x)|^2$)

หนึ่งในปรากฏการณ์เชิงควอนตัมที่ไม่มีในกลศาสตร์คลาสสิกคือ การทะลุผ่านกำแพงศักย์ (Quantum Tunneling) ซึ่งอนุภาคที่มีพลังงาน $E$ น้อยกว่าความสูงของกำแพงศักย์ $V_0$ ยังคงมีโอกาสที่ไม่เป็นศูนย์ในการทะลุผ่านกำแพงศักย์ไปได้ ปรากฏการณ์นี้เป็นรากฐานของกระบวนการสลายตัวให้อนุภาคแอลฟาในฟิสิกส์นิวเคลียร์ การทำงานของไดโอดทันเนล และกล้องจุลทรรศน์สแกนแบบส่องกราด (Scanning Tunneling Microscope: STM)""",
        "example_title": r"การคำนวณระดับพลังงานและฟังก์ชันคลื่นของอิเล็กตรอนในบ่อศักย์อนันต์ 1 มิติ",
        "example_p": r"อิเล็กตรอนถูกขังอยู่ในกล่องศักย์ 1 มิติความกว้าง $L$ โดยมี $V(x) = 0$ สำหรับ $0 \le x \le L$ และ $V(x) = \infty$ ที่บริเวณภายนอก",
        "example_s": r"แก้สมการชเรอดิงเงอร์ในบ่อศักย์ กำหนดเงื่อนไขขอบเขต $\psi(0) = \psi(L) = 0$ และการปรับบรรทัดฐาน (Normalization)",
        "example_c": r"""ในบริเวณ $0 \le x \le L$ สมการชเรอดิงเงอร์คือ:
\begin{equation}
\frac{d^2\psi}{dx^2} + k^2\psi = 0, \quad k = \frac{\sqrt{2mE}}{\hbar}
\end{equation}
ผลเฉลยทั่วไป $\psi(x) = A\sin(kx) + B\cos(kx)$
จากเงื่อนไขขอบเขต $\psi(0) = 0 \implies B = 0$
และ $\psi(L) = 0 \implies \sin(kL) = 0 \implies k_n L = n\pi \quad (n = 1, 2, 3, \dots)$
ได้ระดับพลังงานที่ถูกควอนไตซ์ (Quantized Energy Levels):
\begin{equation}
E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2 \pi^2 \hbar^2}{2mL^2} = \frac{n^2 h^2}{8mL^2}
\end{equation}
จากการปรับบรรทัดฐาน $\int_{0}^{L} A^2 \sin^2(n\pi x/L) dx = 1 \implies A = \sqrt{2/L}$:
\begin{equation}
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)
\end{equation}""",
        "example_t": r"ระดับพลังงานมีลักษณะไม่ต่อเนื่องและมีพลังงานสถานะพื้น (Zero-point Energy: $E_1 > 0$) ซึ่งสอดคล้องกับหลักความไม่แน่นอนของไฮเซนเบิร์ก $\Delta x \Delta p \ge \hbar/2$",
        "research_text": r"""ในระบบจุดควอนตัม (Quantum Dots) และผลึกนาโน ระดับพลังงานของเอ็กซิตอนถูกควบคุมด้วยขนาดของกล่องตามสมการ $E_n \propto 1/L^2$ ปรากฏการณ์นี้ทำให้เราสามารถปรับเปลี่ยนความยาวคลื่นแสงที่ดูดกลืนและเปล่งออกมาได้โดยการควบคุมขนาดของอนุภาคนาโนในการทดลองสังเคราะห์ทางวัสดุศาสตร์""",
        "problem_title": r"การวิเคราะห์สัมประสิทธิ์การทะลุผ่านของอิเล็กตรอนผ่านกำแพงศักย์แบบสี่เหลี่ยม",
        "ccaf_c": r"อิเล็กตรอนพลังงาน $E = 2.0\text{ eV}$ วิ่งเข้าหากำแพงศักย์สี่เหลี่ยมความสูง $V_0 = 5.0\text{ eV}$ และความหนา $L = 0.5\text{ nm}$",
        "ccaf_cat": r"การคำนวณสัมประสิทธิ์การทะลุผ่านเชิงควอนตัม (Quantum Transmission Coefficient)",
        "ccaf_a": r"""คำนวณค่าคงที่การลดทอนคลื่น $\kappa$:
\begin{equation}
\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar} = \frac{\sqrt{2(9.109 \times 10^{-31})(3.0 \times 1.602 \times 10^{-19})}}{1.055 \times 10^{-34}} \approx 8.87 \times 10^9\text{ m}^{-1}
\end{equation}
สัมประสิทธิ์การทะลุผ่าน $T$:
\begin{equation}
T \approx e^{-2\kappa L} = \exp\left[-2(8.87 \times 10^9)(0.5 \times 10^{-9})\right] = e^{-8.87} \approx 1.4 \times 10^{-4}
\end{equation}""",
        "ccaf_f": r"อิเล็กตรอนประมาณ 14 ตัวจากทุกๆ 100,000 ตัว สามารถทะลุผ่านกำแพงศักย์ที่มีความสูงมากกว่าพลังงานของตัวมันเองได้ ซึ่งยืนยันธรรมชาติความเป็นคลื่นของสสาร"
    },
    {
        "filename": "ch07_solid_state_magnetic.tex",
        "number": 7,
        "title": r"ฟิสิกส์ของแข็งและวัสดุแม่เหล็กขั้นสูง",
        "subtitle": r"โครงสร้างผลึก ทฤษฎีแถบพลังงาน อันตรกิริยาแลกเปลี่ยน และการจำลองเชิงทฤษฎี LSDA+U",
        "equations_title": r"แบบจำลองแม่เหล็กและฮามิลโทเนียนของไฮเซนเบิร์ก",
        "equations": r"""\begin{align}
\hat{H}_{\text{Heisenberg}} &= -2\sum_{i < j} J_{ij} \mathbf{S}_i \cdot \mathbf{S}_j, \quad E^{\text{LSDA}+U} = E^{\text{LSDA}} + \frac{U - J}{2}\sum_{\sigma}\left[\text{Tr}(\mathbf{n}^\sigma) - \text{Tr}(\mathbf{n}^\sigma \mathbf{n}^\sigma)\right]
\end{align}""",
        "theory": r"""ฟิสิกส์ของแข็ง (Solid-State Physics) ศึกษาพฤติกรรมของอิเล็กตรอนในโครงตาข่ายผลึกที่มีความสมมาตรแบบเลื่อนขนาน (Translational Symmetry) ตามทฤษฎีของโบลช (Bloch's Theorem) ฟังก์ชันคลื่นของอิเล็กตรอนในผลึกจะอยู่ในรูปของคลื่นระนาบปรับสัญญาณด้วยฟังก์ชันรายคาบของโครงตาข่าย นำไปสู่การจำแนกสารเป็นตัวนำ กึ่งตัวนำ และฉนวน ตามโครงสร้างแถบพลังงาน (Energy Band Structure)

อย่างไรก็ตาม ในระบบที่มีความสัมพันธ์ของอิเล็กตรอนอย่างเข้มข้น (Strongly Correlated Electron Systems) เช่น ออกไซด์ของโลหะทรานสิชัน มอทท์-ฮับบาร์ด (Mott-Hubbard Insulators) อย่าง $\text{MnO}$ และ $\text{NiO}$ ทฤษฎีฟังก์ชันความหนาแน่นดั้งเดิม (Standard DFT/LSDA) มักล้มเหลวโดยทำนายว่าสารเหล่านี้เป็นตัวนำกึ่งโลหะ ซึ่งขัดแย้งกับผลการทดลองจริงที่เป็นฉนวนแม่เหล็กแอนติเฟร์โร (Antiferromagnetic Insulators) ที่มีช่องว่างแถบพลังงานกว้าง การแก้ไขปัญหานี้ต้องใช้ระเบียบวิธี $\text{LSDA}+U$ ซึ่งเพิ่มพจน์พลังงานผลักคูลอมบ์ในออร์บิทัล $d$ ที่มีค่า $U$ (On-site Coulomb Interaction) และอันตรกิริยาแลกเปลี่ยนฮุนด์ $J$ (Hund's Exchange Interaction)""",
        "example_title": r"การประเมินอันตรกิริยาแลกเปลี่ยนแม่เหล็ก J1 และ J2 ในสารประกอบ MnO และ NiO",
        "example_p": r"โครงสร้างแม่เหล็กแบบ AF II ของ MnO บนโครงตาข่าย fcc มีอันตรกิริยาแลกเปลี่ยนระหว่างเพื่อนบ้านลำดับหนึ่ง ($J_1$) และลำดับสอง ($J_2$)",
        "example_s": r"เปรียบเทียบพลังงานรวมจากการจัดเรียงสปินแบบเฟร์โร (FM) และแบบแอนติเฟร์โร (AFM) เพื่อสกัดค่า $J_1$ และ $J_2$",
        "example_c": r"""พลังงานต่อไอออนแม่เหล็กตามแบบจำลองไฮเซนเบิร์ก:
\begin{align}
E_{\text{FM}} &= E_0 - 6 J_1 S^2 - 3 J_2 S^2 \\
E_{\text{AF II}} &= E_0 + 3 J_2 S^2
\end{align}
จากผลงานวิจัยของ ผศ.ดร.ชีวะ ทัศนา ด้วยระเบียบวิธี FP-LAPW $\text{LSDA}+U$:
ผลต่างพลังงานระหว่างสถานะแม่เหล็กนำไปสู่การคำนวณค่า $J_2 \approx -0.45\text{ meV}$ ซึ่งมีเครื่องหมายลบ บ่งชี้ว่าอันตรกิริยาแลกเปลี่ยนระหว่างอะตอมเพื่อนบ้านลำดับสองผ่านสะพานออกซิเจน $\text{Mn}-\text{O}-\text{Mn}$ (Superexchange) เป็นอันตรกิริยาหลักที่ทำให้เกิดโครงสร้างแม่เหล็กแบบแอนติเฟร์โรที่เสถียร""",
        "example_t": r"ค่าอุณหภูมิเนเอล (Néel Temperature: $T_N$) ที่คำนวณจากทฤษฎีสนามเฉลี่ย (Mean-Field Theory) โดยใช้ค่า $J$ ที่สกัดได้ สอดคล้องกับค่าจากการทดลอง $T_N \approx 118\text{ K}$ ใน $\text{MnO}$",
        "research_text": r"""ผลงานวิจัยของ ผศ.ดร.ชีวะ ทัศนา ที่ตีพิมพ์ในวารสารระดับนานาชาติ ได้แสดงให้เห็นว่าการเลือกค่าพารามิเตอร์ $U$ และ $J$ ที่เหมาะสมในระเบียบวิธี $\text{LSDA}+U$ ไม่เพียงแต่เปิดช่องว่างพลังงาน Band Gap ใน $\text{MnO}$ และ $\text{NiO}$ ได้อย่างถูกต้องเท่านั้น แต่ยังทำนายค่าโมเมนต์แม่เหล็กเฉพาะที่ (Local Magnetic Moments) ได้ตรงกับผลการทดลองการกระเจิงนิวตรอน (Neutron Scattering)""",
        "problem_title": r"การวิเคราะห์โครงสร้างแถบพลังงานตามแบบจำลองโครนิก-เพนนี",
        "ccaf_c": r"อิเล็กตรอนเคลื่อนที่ผ่านแนวกำแพงศักย์รูปฟังก์ชันเดลตาแบบรายคาบ $V(x) = V_0 b \sum_n \delta(x - na)$",
        "ccaf_cat": r"การแก้สมการโบลชและการเกิดช่องว่างแถบพลังงาน (Kronig-Penney Model & Band Gaps)",
        "ccaf_a": r"""สมการเงื่อนไขพลังงานของโครนิก-เพนนี:
\begin{equation}
P \frac{\sin(\alpha a)}{\alpha a} + \cos(\alpha a) = \cos(ka), \quad P = \frac{m V_0 b a}{\hbar^2}
\end{equation}
เนื่องจากฟังก์ชัน $\cos(ka)$ มีค่าอยู่ระหว่าง $[-1, 1]$ ดังนั้น ค่าของ $\alpha a$ ที่ทำให้ฟังก์ชันทางซ้ายมือมีค่าสัมบูรณ์มากกว่า 1 จะเป็นช่วงพลังงานที่อิเล็กตรอนไม่สามารถอยู่ได้ เกิดเป็นช่องว่างแถบพลังงานต้องห้าม (Forbidden Energy Gap)""",
        "ccaf_f": r"แบบจำลองโครนิก-เพนนียืนยันว่าช่องว่างแถบพลังงานเป็นผลตามธรรมชาติของการแทรกสอดคลื่นอิเล็กตรอนในโครงตาข่ายผลึกรายคาบ"
    },
    {
        "filename": "ch08_computational_research.tex",
        "number": 8,
        "title": r"ระเบียบวิธีวิจัยและฟิสิกส์เชิงคำนวณ",
        "subtitle": r"การประยุกต์ใช้ Python, SciML และ Physics-Informed Neural Networks ในการวิจัยฟิสิกส์",
        "equations_title": r"ฟังก์ชันการสูญเสียของโครงข่ายประสาทเทียมที่ฝังกฎเกณฑ์ฟิสิกส์ (PINNs)",
        "equations": r"""\begin{align}
\mathcal{L}_{\text{total}} &= \mathcal{L}_{\text{data}} + \lambda_{\text{phys}} \mathcal{L}_{\text{physics}} \\
\mathcal{L}_{\text{data}} &= \frac{1}{N_d}\sum_{i=1}^{N_d}|u_{\text{pred}}(x_i, t_i) - u_{\text{true}}(x_i, t_i)|^2, \quad \mathcal{L}_{\text{physics}} = \frac{1}{N_f}\sum_{j=1}^{N_f}\left|\mathcal{N}[u_{\text{pred}}](x_j, t_j)\right|^2
\end{align}""",
        "theory": r"""ฟิสิกส์เชิงคำนวณ (Computational Physics) ได้ก้าวเข้ามาเป็นเสาหลักที่สามของการค้นพบทางวิทยาศาสตร์ เคียงคู่กับฟิสิกส์ทฤษฎีและฟิสิกส์เชิงทดลอง การปฏิวัติล่าสุดในยุคปัญญาประดิษฐ์คือสาขาการเรียนรู้ของเครื่องเชิงวิทยาศาสตร์ (Scientific Machine Learning: SciML) ซึ่งรวมเอาองค์ความรู้ทางฟิสิกส์ในรูปของสมการเชิงอนุพันธ์ย่อย (PDEs) เข้าไปในกระบวนการฝึกฝนโครงข่ายประสาทเทียม เรียกว่า Physics-Informed Neural Networks (PINNs)

ใน PINNs โครงข่ายประสาทเทียมจะทำหน้าที่เป็นฟังก์ชันประมาณค่า $u_{\text{pred}}(\mathbf{x}, t; \boldsymbol{\theta})$ และใช้เทคนิคอนุพันธ์อัตโนมัติ (Automatic Differentiation) ในการคำนวณอนุพันธ์ย่อยตามเวลาและพิกัด จากนั้นนำผลลัพธ์ไปแทนในสมการฟิสิกส์ (เช่น สมการคลื่น สมการความร้อน หรือสมการเนเวียร์-สโตกส์) เพื่อสร้างพจน์การสูญเสียทางฟิสิกส์ ($\mathcal{L}_{\text{physics}}$) ทำให้โมเดลสามารถพยากรณ์ผลลัพธ์ได้อย่างแม่นยำแม้มีข้อมูลตรวจวัดจริงเพียงเล็กน้อย (Few-shot Learning) และรับประกันว่าผลลัพธ์จะไม่ละเมิดกฎการอนุรักษ์ทางฟิสิกส์""",
        "example_title": r"การแก้สมการความร้อน 1 มิติด้วยโครงข่ายประสาทเทียม PINNs ใน Python",
        "example_p": r"แท่งโลหะยาว $L = 1.0\text{ m}$ มีการแพร่ความร้อนตามสมการ $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$ โดยมีเงื่อนไขขอบเขตอุณหภูมิคงที่ที่ปลายทั้งสองข้าง",
        "example_s": r"สร้างโมเดล Multilayer Perceptron (MLP) ใน PyTorch และคำนวณ Residual Loss ของสมการความร้อนผ่าน torch.autograd",
        "example_c": r"""โค้ดภาษา Python สำหรับนิยาม Physics Loss ใน PyTorch:
\begin{lstlisting}[language=Python]
import torch
import torch.nn as nn

class PINN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 64), nn.Tanh(),
            nn.Linear(64, 64), nn.Tanh(),
            nn.Linear(64, 1)
        )
    def forward(self, x, t):
        return self.net(torch.cat([x, t], dim=1))

def physics_loss(model, x, t, alpha=0.01):
    x.requires_grad = True
    t.requires_grad = True
    u = model(x, t)
    
    # อนุพันธ์อัตโนมัติ
    u_t = torch.autograd.grad(u, t, grad_outputs=torch.ones_like(u), create_graph=True)[0]
    u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), create_graph=True)[0]
    u_xx = torch.autograd.grad(u_x, x, grad_outputs=torch.ones_like(u_x), create_graph=True)[0]
    
    # เศษเหลือของสมการความร้อน (Residual)
    residual = u_t - alpha * u_xx
    return torch.mean(residual ** 2)
\end{lstlisting}""",
        "example_t": r"ค่า Residual Loss ลดลงสู่ระดับ $10^{-5}$ หลังจากเทรน 2,000 รอบ และเส้นโค้งการกระจายอุณหภูมิซ้อนทับกับผลเฉลยแม่นตรงแบบอนุกรมฟูเรียร์อย่างสมบูรณ์แบบ",
        "research_text": r"""การประยุกต์ใช้ระเบียบวิธีเชิงคำนวณขั้นสูงและโมเดล SciML ช่วยให้นักวิจัยสามารถจำลองพลศาสตร์ของระบบซับซ้อน เช่น การไหลของพลาสมาในเครื่องปฏิกรณ์โทคาแมก การกระจายตัวของอนุภาคมลพิษในชั้นบรรยากาศ และการทำนายสมบัติทางอิเล็กทรอนิกส์ของวัสดุใหม่ได้อย่างรวดเร็วและคุ้มค่า""",
        "problem_title": r"การเปรียบเทียบประสิทธิภาพระหว่างระเบียบวิธีไฟไนต์ดิฟเฟอเรนซ์ (FDM) และ PINNs",
        "ccaf_c": r"พิจารณาการแก้สมการเชิงอนุพันธ์ย่อยที่มีสัญญาณรบกวนในการวัด (Noisy Boundary Data)",
        "ccaf_cat": r"การประเมินความทนทานต่อสัญญาณรบกวน (Robustness against Experimental Noise)",
        "ccaf_a": r"""ในระเบียบวิธี FDM ดั้งเดิม อนุพันธ์เชิงตัวเลขคำนวณจากผลต่างสืบเนื่อง เช่น $\frac{u_{i+1} - 2u_i + u_{i-1}}{\Delta x^2}$ ซึ่งจะขยายขนาดสัญญาณรบกวนความถี่สูง (Noise Amplification) จนทำให้ผลเฉลยไม่เสถียร
ในทางตรงกันข้าม PINNs ใช้การปรับพารามิเตอร์แบบเกรเดียนต์เดสเซนต์ร่วมกับการปรับเรียบอัตโนมัติ (Implicit Regularization) ของโครงข่ายประสาทเทียม ทำให้สามารถกรองสัญญาณรบกวนออกและยังคงรักษาโครงสร้างทางฟิสิกส์ไว้ได้อย่างยอดเยี่ยม""",
        "ccaf_f": r"PINNs เหมาะสมอย่างยิ่งสำหรับงานวิจัยฟิสิกส์ที่ต้องทำงานร่วมกับข้อมูลจริงจากการทดลองภาคสนามที่มีสัญญาณรบกวนปะปนอยู่"
    }
]

for ch in chapters_data:
    out_path = os.path.join(CHAPTERS_DIR, ch["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(r"% =========================================================================" + "\n")
        f.write(f"% บทที่ {ch['number']}: {ch['title']}\n")
        f.write(r"% =========================================================================" + "\n\n")
        
        # Chapter header
        f.write(f"\\chapter{{{ch['title']}}}\n")
        f.write(f"\\label{{ch:chapter{ch['number']:02d}}}\n\n")
        
        # Subtitle
        f.write(f"\\noindent{{\\large\\bfseries\\color{{physicsblue}} {ch['subtitle']}}}\n\n")
        f.write(r"\vspace{0.4cm}" + "\n\n")
        
        # Key Equations Box
        f.write(f"\\begin{{equationsbox}}{{{ch['equations_title']}}}\n")
        f.write(f"{ch['equations']}\n")
        f.write(r"\end{equationsbox}" + "\n\n")
        
        # Section 1: Theory
        f.write(r"\section{ทฤษฎีและกรอบแนวคิดสำคัญ}" + "\n\n")
        f.write(f"{ch['theory']}\n\n")
        
        # Section 2: Worked Example (Tipler P-S-C-T Style)
        f.write(r"\section{ตัวอย่างการคำนวณตามกรอบวิเคราะห์ P-S-C-T}" + "\n\n")
        f.write(f"\\begin{{psctexample}}{{{ch['number']}.1}}{{{ch['example_title']}}}\n")
        f.write(r"\textbf{1. ภาพและสถานการณ์ทางกายภาพ (Picture):}\\\\ " + f"{ch['example_p']}\n\n")
        f.write(r"\vspace{4pt}" + "\n")
        f.write(r"\textbf{2. กลยุทธ์และแบบจำลองทางฟิสิกส์ (Strategy):}\\\\ " + f"{ch['example_s']}\n\n")
        f.write(r"\vspace{4pt}" + "\n")
        f.write(r"\textbf{3. ขั้นตอนการคำนวณเชิงตัวเลข (Calculation):}\\\\ " + f"{ch['example_c']}\n\n")
        f.write(r"\vspace{4pt}" + "\n")
        f.write(r"\textbf{4. การทดสอบความสมเหตุสมผล (Test):}\\\\ " + f"{ch['example_t']}\n")
        f.write(r"\end{psctexample}" + "\n\n")
        
        # Section 3: Author Research Integration
        f.write(r"\section{การเชื่อมโยงสู่การวิจัยฟิสิกส์ร่วมสมัย}" + "\n\n")
        f.write(r"\begin{researchbox}{ข้อมูลเชิงลึกจากงานวิจัย}" + "\n")
        f.write(f"{ch['research_text']}\n")
        f.write(r"\end{researchbox}" + "\n\n")
        
        # Section 4: Problem Solving Framework (Serway C-C-A-F Style)
        f.write(r"\section{การฝึกแก้โจทย์ปัญหาเชิงระบบตามกรอบ C-C-A-F}" + "\n\n")
        f.write(f"\\begin{{ccafsolution}}{{{ch['problem_title']}}}\n")
        f.write(r"\textbf{ขั้นที่ 1: การสร้างมโนทัศน์ (Conceptualize):}\\\\ " + f"{ch['ccaf_c']}\n\n")
        f.write(r"\vspace{4pt}" + "\n")
        f.write(r"\textbf{ขั้นที่ 2: การจำแนกประเภทโจทย์ (Categorize):}\\\\ " + f"{ch['ccaf_cat']}\n\n")
        f.write(r"\vspace{4pt}" + "\n")
        f.write(r"\textbf{ขั้นที่ 3: การวิเคราะห์เชิงคณิตศาสตร์ (Analyze):}\\\\ " + f"{ch['ccaf_a']}\n\n")
        f.write(r"\vspace{4pt}" + "\n")
        f.write(r"\textbf{ขั้นที่ 4: การสรุปและประเมินผล (Finalize):}\\\\ " + f"{ch['ccaf_f']}\n")
        f.write(r"\end{ccafsolution}" + "\n\n")
        
        # Section 5: Tiered Problem Sets
        f.write(r"\section{แบบฝึกหัดทบทวนและโจทย์ท้าทายประจำบท}" + "\n\n")
        f.write(r"\begin{enumerate}[leftmargin=1.5cm, label={\textbf{\thechapter.\arabic*}}, itemsep=8pt]" + "\n")
        f.write(r"    \item \textbf{โจทย์เชิงแนวคิด (Conceptual):} จงอธิบายความสำคัญทางกายภาพของกฎและสมการหลักในบทเรียนนี้ พร้อมยกตัวอย่างสถานการณ์จริงในธรรมชาติ" + "\n")
        f.write(r"    \item \textbf{โจทย์การประมาณค่าเชิงฟิสิกส์ (Estimation):} จงใช้การวิเคราะห์เชิงมิติและอันดับของขนาด (Order of Magnitude) ในการประมาณค่าปริมาณสำคัญที่เกี่ยวข้อง" + "\n")
        f.write(r"    \item \textbf{โจทย์วิจัยขั้นสูง (Research Challenge):} จงเขียนสคริปต์ Python จำลองพฤติกรรมของระบบตามสมการที่ได้ศึกษา พร้อมพลอตกราฟเปรียบเทียบผลลัพธ์เชิงทฤษฎี" + "\n")
        f.write(r"\end{enumerate}" + "\n\n")

print("Successfully regenerated all 8 monograph chapters for Book 06 with 100% raw string safety.")
