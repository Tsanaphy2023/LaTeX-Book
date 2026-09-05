#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_book05.py - Generates 8 comprehensive laboratory chapters for Book 05: AR with AI Manual
Adhering strictly to RBRU Masterclass Layout Standards and academic formatting rules.
"""

import os

CHAPTERS_DIR = "05_ARwithAI_manual/chapters"
os.makedirs(CHAPTERS_DIR, exist_ok=True)

chapters_data = [
    {
        "filename": "lab01_webar_frameworks.tex",
        "number": 1,
        "title": "สถาปัตยกรรม WebAR และเครื่องมือพัฒนา",
        "subtitle": "การวางโครงสร้าง Three.js, A-Frame และ WebXR Device API บนเว็บเบราว์เซอร์",
        "objectives": [
            "เข้าใจสถาปัตยกรรมระบบความจริงเสริมบนเว็บ (Web-based Augmented Reality Architecture)",
            "สามารถติดตั้งและกำหนดค่า Three.js และ A-Frame เพื่อเรนเดอร์ฉาก 3 มิติ",
            "สามารถควบคุมวงรอบการเรนเดอร์กราฟิกให้มีอัตราการแสดงผลระดับ 60 เฟรมต่อวินาที"
        ],
        "tools": "เว็บเบราว์เซอร์สมัยใหม่ (Chrome/Edge), Visual Studio Code, Three.js r128, A-Frame v1.4.0",
        "theory": r"""เทคโนโลยีความจริงเสริมบนเว็บเบราว์เซอร์ (Web-based Augmented Reality หรือ WebAR) เป็นวิวัฒนาการสำคัญที่ช่วยให้ผู้ใช้งานสามารถเข้าถึงประสบการณ์เสมือนจริงได้ทันทีผ่านโปรแกรมเปิดเว็บโดยไม่ต้องดาวน์โหลดและติดตั้งแอปพลิเคชันที่มีขนาดใหญ่ สถาปัตยกรรมของ WebAR อาศัยการทำงานร่วมกันของมาตรฐานเปิดระดับสากล ได้แก่ WebGL สำหรับการประมวลผลกราฟิกฮาร์ดแวร์เร่งความเร็ว และ WebXR Device API ซึ่งทำหน้าที่ตรวจจับและเชื่อมต่อข้อมูลเชิงพื้นที่จากเซนเซอร์ของอุปกรณ์เข้ากับฉากทัศน์เสมือน

หัวใจหลักของกราฟิก 3 มิติบนเว็บคือเอนจิน Three.js ซึ่งทำหน้าที่เป็นตัวประสานงานระดับสูง (High-level Abstraction) ครอบ WebGL ช่วยลดความซับซ้อนในการเขียนภาษาเฉดเดอร์ (GLSL) โดยแบ่งโครงสร้างออกเป็น 3 ส่วนหลัก ได้แก่ ฉากทัศน์ (Scene) ทำหน้าที่เป็นพื้นที่รองรับวัตถุและโมเดล กล้องเสมือน (Camera) เช่น กล้องมุมมองแบบเพอร์สเปกทีฟ (Perspective Camera) ที่จำลองสายตาของมนุษย์ และตัวเรนเดอร์ (WebGLRenderer) ทำหน้าที่คำนวณและวาดภาพลงบนผืนผ้าใบแบบเฟรมต่อเฟรม ผ่านฟังก์ชัน \texttt{requestAnimationFrame()}""",
        "code_snippet": r"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>WebAR Lab 01 - Three.js Fundamentals</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body { margin: 0; overflow: hidden; background: #030712; }
        canvas { width: 100vw; height: 100vh; display: block; }
    </style>
</head>
<body>
    <div id="webgl-container"></div>
    <script>
        // 1. กำหนดตัวแปรหลักสำหรับฉากทัศน์ กล้อง และตัวเรนเดอร์
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        document.getElementById('webgl-container').appendChild(renderer.domElement);

        // 2. สร้างวัตถุเรขาคณิต 3 มิติแบบโฮโลกราฟิก
        const geometry = new THREE.BoxGeometry(1.2, 1.2, 1.2);
        const material = new THREE.MeshStandardMaterial({
            color: 0x06b6d4,
            wireframe: false,
            metalness: 0.8,
            roughness: 0.2
        });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // 3. กำหนดแหล่งกำเนิดแสงในฉาก
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        scene.add(ambientLight);
        const pointLight = new THREE.PointLight(0x38bdf8, 2, 50);
        pointLight.position.set(5, 5, 5);
        scene.add(pointLight);

        camera.position.z = 3.5;

        // 4. วงรอบการเรนเดอร์แบบ 60 FPS
        function animate() {
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.015;
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>""",
        "activity": "ให้นักศึกษาปรับแต่งขนาดรูปทรงเรขาคณิตให้เป็นทรงกลม (SphereGeometry) และเพิ่มแหล่งกำเนิดแสงสีส้มทอง (Amber Light) อีก 1 จุด พร้อมคำนวณอัตราการใช้หน่วยความจำและการตอบสนองต่อการปรับขนาดหน้าจอแบบ Responsive",
        "questions": [
            "สถาปัตยกรรมของ WebXR Device API แตกต่างจากการเรียกใช้ WebGL ดั้งเดิมอย่างไรในแง่ของการจัดการพิกัดเชิงพื้นที่",
            "เหตุใดการตั้งค่า `alpha: true` ใน WebGLRenderer จึงมีความจำเป็นอย่างยิ่งสำหรับการพัฒนาแอปพลิเคชันแบบความจริงเสริม",
            "จงอธิบายบทบาทของฟังก์ชัน requestAnimationFrame() ต่อการรักษาอัตราเฟรมเรตและการประหยัดพลังงานประมวลผล"
        ]
    },
    {
        "filename": "lab02_mediapipe_hands.tex",
        "number": 2,
        "title": "วิทัศน์คอมพิวเตอร์และการตรวจจับโครงร่างมือ",
        "subtitle": "การประมวลผลวิดีโอสตรีมสดและสกัดพิกัดมือ 21 จุดร่วมด้วย MediaPipe Hands",
        "objectives": [
            "เข้าใจทฤษฎีโครงข่ายประสาทเทียมตรวจจับจุดสำคัญของมือ (Hand Landmark Topology)",
            "สามารถเชื่อมต่อสตรีมวิดีโอสดจากเว็บแคมเข้าสู่ไปป์ไลน์ MediaPipe Hands",
            "สามารถสกัดและวาดจุดพิกัด 21 ตำแหน่งลงบนผืนผ้าใบแบบเรียลไทม์"
        ],
        "tools": r"เว็บแคมความละเอียด 720p ขึ้นไป, MediaPipe Hands API (@mediapipe/camera\_utils, @mediapipe/hands)",
        "theory": r"""เทคโนโลยีการตรวจจับโครงกระดูกมือ (Hand Pose Estimation) ของ MediaPipe อาศัยแบบจำลองการเรียนรู้เชิงลึกแบบสองขั้นตอน (Two-stage Deep Learning Pipeline) ได้แก่:
1. โมเดลตรวจจับฝ่ามือ (Palm Detector Model): ทำหน้าที่ค้นหาขอบเขตของฝ่ามือจากภาพวิดีโอทั้งภาพ (Bounding Box Detection) ซึ่งเป็นขั้นตอนที่ตรวจจับได้ง่ายเนื่องจากฝ่ามือมีลักษณะสัณฐานคงที่และบดบังตัวเองน้อยกว่านิ้วมือ
2. โมเดลจุดสังเกตสำคัญ (Hand Landmark Model): เมื่อทราบตำแหน่งฝ่ามือ โมเดลจะตัดภาพเฉพาะบริเวณมือมาประมวลผล เพื่อพยากรณ์พิกัด 3 มิติ $(x, y, z)$ ของจุดร่วมทั้ง 21 จุดสำคัญ (Landmarks) บนมืออย่างแม่นยำ

พิกัด $x$ และ $y$ จะถูกปรับให้เป็นสเกลมาตรฐานสัมพัทธ์ $[0.0, 1.0]$ ตามความกว้างและความสูงของภาพ ส่วนพิกัด $z$ แสดงความลึกสัมพัทธ์ (Relative Depth) โดยมีจุดอ้างอิงอยู่ที่ข้อมือ (Landmark 0: Wrist) ซึ่งจุดสำคัญเหล่านี้ถูกจัดกลุ่มเป็น 5 นิ้ว ได้แก่ นิ้วหัวแม่มือ (Landmarks 1-4), นิ้วชี้ (Landmarks 5-8), นิ้วกลาง (Landmarks 9-12), นิ้วนาง (Landmarks 13-16) และนิ้วก้อย (Landmarks 17-20)""",
        "code_snippet": r"""// กำหนดค่าและเริ่มต้นใช้งาน MediaPipe Hands
const videoElement = document.getElementById('webcam-video');
const canvasElement = document.getElementById('output-canvas');
const canvasCtx = canvasElement.getContext('2d');

const hands = new Hands({
    locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`
});

hands.setOptions({
    maxNumHands: 2,
    modelComplexity: 1,
    minDetectionConfidence: 0.7,
    minTrackingConfidence: 0.7
});

hands.onResults((results) => {
    canvasCtx.save();
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    canvasCtx.drawImage(results.image, 0, 0, canvasElement.width, canvasElement.height);

    if (results.multiHandLandmarks) {
        for (const landmarks of results.multiHandLandmarks) {
            // วาดเส้นเชื่อมต่อกระดูกและจุดพิกัด 21 ตำแหน่ง
            drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS, {color: '#06b6d4', lineWidth: 3});
            drawLandmarks(canvasCtx, landmarks, {color: '#f59e0b', lineWidth: 1, radius: 4});
            
            // สกัดพิกัดปลายนิ้วชี้ (Landmark 8) และนิ้วโป้ง (Landmark 4)
            const indexTip = landmarks[8];
            const thumbTip = landmarks[4];
            console.log(`Index: (${indexTip.x.toFixed(3)}, ${indexTip.y.toFixed(3)}, ${indexTip.z.toFixed(3)})`);
        }
    }
    canvasCtx.restore();
});

const camera = new Camera(videoElement, {
    onFrame: async () => { await hands.send({image: videoElement}); },
    width: 1280, height: 720
});
camera.start();""",
        "activity": "ให้นักศึกษาเขียนโปรแกรมเพิ่มเติมเพื่อจำแนกมือซ้ายและมือขวาจากข้อมูล `results.multiHandedness` และแสดงข้อความระบุชื่อมือพร้อมค่าความเชื่อมั่น (Confidence Score) บนผืนผ้าใบ",
        "questions": [
            "เหตุใดสถาปัตยกรรมของ MediaPipe จึงเลือกใช้การตรวจจับฝ่ามือก่อนการพยากรณ์จุดสำคัญ 21 จุดแทนการค้นหานิ้วมือโดยตรง",
            "พิกัดแกน $z$ ที่รายงานโดยโมเดลจุดสังเกตสำคัญของ MediaPipe มีความหมายทางกายภาพอย่างไรและอ้างอิงกับจุดใด",
            "หากสภาพแสงในห้องทดลองมีความสว่างน้อย จะส่งผลต่อค่า minDetectionConfidence และอัตราการกระตุกของเฟรมอย่างไร"
        ]
    },
    {
        "filename": "lab03_spatial_gestures.tex",
        "number": 3,
        "title": "การเขียนโปรแกรมตรวจจับพิกัดเชิงพื้นที่และท่าทางมือ",
        "subtitle": "การคำนวณระยะทางแบบยูคลิดเพื่อตรวจจับการจีบนิ้วและการกรองสัญญาณรบกวน",
        "objectives": [
            "เข้าใจการแปลงพิกัดภาพ 2 มิติสู่เวกเตอร์เชิงพื้นที่ 3 มิติ",
            "สามารถประยุกต์สมการระยะทางแบบยูคลิดเพื่อตรวจจับท่าทางจีบนิ้ว (Pinch Gesture)",
            "สามารถออกแบบตัวกรองแบบเอ็กซ์โพเนนเชียล (Exponential Moving Average) เพื่อลดการสั่นไหวของพิกัด"
        ],
        "tools": "MediaPipe Hands, โมดูลคณิตศาสตร์เวกเตอร์เชิงเส้น (Vector3)",
        "theory": r"""ในการสร้างระบบควบคุมไร้สัมผัส (Touchless Interaction) ท่าทางการจีบนิ้ว (Pinch Gesture) ระหว่างปลายนิ้วหัวแม่มือ (Landmark 4) และปลายนิ้วชี้ (Landmark 8) ถือเป็นท่าทางมาตรฐานเทียบเท่ากับการคลิกเมาส์ในระบบปฏิบัติการทั่วไป การตรวจจับท่าทางนี้ทำได้โดยการคำนวณระยะทางแบบยูคลิด 3 มิติ (3D Euclidean Distance) ระหว่างจุดทั้งสอง:
\begin{equation}
d_{\text{pinch}} = \sqrt{(x_8 - x_4)^2 + (y_8 - y_4)^2 + (z_8 - z_4)^2}
\end{equation}
เมื่อค่า $d_{\text{pinch}}$ มีค่าน้อยกว่าเกณฑ์ที่กำหนด (Threshold เช่น $d < 0.035$ ในระบบพิกัดสัมพัทธ์) ระบบจะส่งสัญญาณเหตุการณ์การคลิกหรือหยิบจับวัตถุ

อย่างไรก็ตาม พิกัดที่ได้จากระบบวิทัศน์คอมพิวเตอร์มักมีสัญญาณรบกวนความถี่สูง (High-frequency Jitter) ซึ่งเกิดจากความผันผวนของแสงและการประมวลผลระดับพิกเซล การแก้ปัญหานี้จำเป็นต้องใช้ตัวกรองปรับเรียบ (Smoothing Filter) เช่น Exponential Moving Average (EMA):
\begin{equation}
\mathbf{P}_{\text{filtered}}^{(t)} = \alpha \mathbf{P}_{\text{raw}}^{(t)} + (1 - \alpha) \mathbf{P}_{\text{filtered}}^{(t-1)}
\end{equation}
โดยที่ $\alpha \in (0, 1]$ คือค่าน้ำหนักปรับเรียบ (Smoothing Factor) หากกำหนด $\alpha$ ต่ำ สัญญาณจะนิ่งเรียบแต่มีความหน่วง (Latency) เพิ่มขึ้น""",
        "code_snippet": r"""// ฟังก์ชันคำนวณระยะทางแบบยูคลิด 3 มิติ
function calculateDistance(p1, p2) {
    const dx = p1.x - p2.x;
    const dy = p1.y - p2.y;
    const dz = p1.z - p2.z;
    return Math.sqrt(dx * dx + dy * dy + dz * dz);
}

// ตัวแปรเก็บพิกัดปรับเรียบก่อนหน้า
let smoothedIndex = { x: 0, y: 0, z: 0 };
const ALPHA = 0.35; // ค่าน้ำหนักตัวกรอง EMA
const PINCH_THRESHOLD = 0.035;

function processGestures(landmarks) {
    const thumbTip = landmarks[4];
    const indexTip = landmarks[8];

    // ปรับเรียบพิกัดนิ้วชี้ด้วยสมการ EMA
    smoothedIndex.x = ALPHA * indexTip.x + (1 - ALPHA) * smoothedIndex.x;
    smoothedIndex.y = ALPHA * indexTip.y + (1 - ALPHA) * smoothedIndex.y;
    smoothedIndex.z = ALPHA * indexTip.z + (1 - ALPHA) * smoothedIndex.z;

    const pinchDist = calculateDistance(thumbTip, indexTip);
    const isPinching = pinchDist < PINCH_THRESHOLD;

    return {
        cursor: smoothedIndex,
        isPinching: isPinching,
        distance: pinchDist
    };
}""",
        "activity": "ให้นักศึกษาพัฒนาท่าทางเพิ่มเติมอีก 2 ท่าทาง ได้แก่ ท่าทางกำมือ (Fist Detection) โดยตรวจสอบระยะห่างระหว่างปลายนิ้วทั้งสี่กับจุดกึ่งกลางฝ่ามือ และท่าทางกางมือ (Open Palm) เพื่อใช้เป็นคำสั่งรีเซ็ตระบบ",
        "questions": [
            "เหตุใดการตรวจจับท่าทางจีบนิ้วจึงต้องคำนึงถึงพิกัดแกน $z$ ร่วมด้วย แทนที่จะคำนวณเฉพาะระยะทางบนระนาบ $x-y$",
            "จงวิเคราะห์ข้อดีและข้อเสียของการตั้งค่าพารามิเตอร์ $\\alpha$ ในตัวกรอง EMA ที่มีค่าสูง ($0.8$) เทียบกับค่าต่ำ ($0.15$)",
            "หากระยะห่างระหว่างมือกับกล้องเปลี่ยนไป จะส่งผลกระทบต่อเกณฑ์การตัดสิน $d_{\\text{pinch}}$ หรือไม่ อย่างไร"
        ]
    },
    {
        "filename": "lab04_interactive_3d_raycasting.tex",
        "number": 4,
        "title": "การสร้างปฏิสัมพันธ์กับวัตถุ 3 มิติในพื้นที่เสมือน",
        "subtitle": "การประยุกต์ Raycasting เพื่อการตรวจจับการชน การยกย้าย และการหมุนโมเดล",
        "objectives": [
            "เข้าใจทฤษฎีการฉายรังสีตรวจจับการชน (Raycasting Collision Detection)",
            "สามารถแปลงพิกัด Normalized Device Coordinates (NDC) จากมือสู่ระนาบ 3 มิติ",
            "สามารถเขียนโปรแกรมจับ ยก ย้าย และปล่อยวัตถุในฉากเสมือนจริงได้อย่างราบรื่น"
        ],
        "tools": "Three.js Raycaster, เวกเตอร์พิกัดมือจากการทดลองที่ 3",
        "theory": r"""การสร้างปฏิสัมพันธ์ระหว่างผู้ใช้กับวัตถุในสภาพแวดล้อม 3 มิติโดยไม่มีอุปกรณ์สัมผัสกายภาพ อาศัยกระบวนการฉายรังสีเสมือน (Raycasting) ซึ่งเป็นการสร้างรังสีเรขาคณิต (Mathematical Ray) ที่มีจุดกำเนิด $\mathbf{O}$ และเวกเตอร์ทิศทาง $\mathbf{D}$:
\begin{equation}
\mathbf{R}(t) = \mathbf{O} + t\mathbf{D}, \quad t \ge 0
\end{equation}
ในระบบความจริงเสริม พิกัดจากกล้องเว็บแคมจะถูกแปลงเข้าสู่ระบบพิกัดอุปกรณ์มาตรฐาน (Normalized Device Coordinates: NDC) โดยมีขอบเขต $[-1.0, 1.0]$ ทั้งแกน $X$ และ $Y$:
\begin{equation}
x_{\text{ndc}} = 2 \cdot x_{\text{hand}} - 1, \quad y_{\text{ndc}} = -(2 \cdot y_{\text{hand}} - 1)
\end{equation}
เมื่อนำเวกเตอร์ $(x_{\text{ndc}}, y_{\text{ndc}})$ ส่งผ่านกล้องเสมือน (Camera Projection Matrix) ตัวเรนเดอร์จะยิงรังสีทะลุเข้าไปในฉากทัศน์ 3 มิติ และคำนวณจุดตัด (Intersection) กับรูปทรงเรขาคณิตของวัตถุ หากเกิดจุดตัดและผู้ใช้ทำท่าทางจีบนิ้ว (Pinch) วัตถุจะถูกผูกโยงพิกัดเข้ากับมือของผู้ใช้ ทำให้สามารถเคลื่อนย้ายวัตถุไปตามทิศทางการเคลื่อนไหวของมือได้อย่างสมจริง""",
        "code_snippet": r"""// การสร้าง Raycaster และแปลงพิกัดมือเป็น NDC
const raycaster = new THREE.Raycaster();
const mouseNDC = new THREE.Vector2();
let selectedObject = null;

function updateHandInteraction(cursor, isPinching) {
    // แปลงพิกัดมือ [0, 1] เป็นพิกัด NDC [-1, 1]
    mouseNDC.x = (cursor.x * 2) - 1;
    mouseNDC.y = -(cursor.y * 2) + 1;

    // ยิงรังสีจากตำแหน่งกล้องผ่านพิกัด NDC
    raycaster.setFromCamera(mouseNDC, camera);
    const intersects = raycaster.intersectObjects(scene.children);

    if (intersects.length > 0) {
        const hit = intersects[0].object;
        if (isPinching && !selectedObject) {
            selectedObject = hit;
            selectedObject.material.emissive.setHex(0x06b6d4); // เรืองแสงเมื่อถูกจับ
        }
    }

    // หากมีการจับวัตถุอยู่ ให้เคลื่อนย้ายวัตถุตามพิกัด 3D ของรังสี
    if (selectedObject) {
        if (isPinching) {
            const targetPos = raycaster.ray.at(3.0, new THREE.Vector3());
            selectedObject.position.copy(targetPos);
        } else {
            // ปล่อยวัตถุเมื่อเลิกจีบนิ้ว
            selectedObject.material.emissive.setHex(0x000000);
            selectedObject = null;
        }
    }
}""",
        "activity": "ให้นักศึกษาเพิ่มคุณสมบัติการหมุนวัตถุ (Rotation) ตามการเอียงของแนวระนาบฝ่ามือ โดยใช้เวกเตอร์ระหว่างจุด Landmark 0 (ข้อมือ) และ Landmark 9 (โคนนิ้วกลาง)",
        "questions": [
            "เพราะเหตุใดสูตรการแปลงพิกัด $y_{\\text{hand}}$ สู่ $y_{\\text{ndc}}$ จึงต้องติดเครื่องหมายลบด้านหน้า",
            "การคำนวณการชนด้วย Raycasting กับโมเดลที่มีโพลีกอนจำนวนมาก (High-poly models) ส่งผลต่อประสิทธิภาพอย่างไร และมีวิธีแก้ไขอย่างไร",
            "จงอธิบายหลักการของ Bounding Box (AABB) ในการเพิ่มความเร็วให้แก่อัลกอริทึมตรวจจับการชน"
        ]
    },
    {
        "filename": "lab05_browser_ml_teachable.tex",
        "number": 5,
        "title": "การประยุกต์โมเดล Machine Learning บนเบราว์เซอร์",
        "subtitle": "การผสานโมเดลจำแนกภาพ Teachable Machine และ TensorFlow.js สู่ฉากเสมือน",
        "objectives": [
            "เข้าใจกระบวนการฝึกโมเดลจำแนกภาพถ่ายด้วย Google Teachable Machine",
            "สามารถแปลงและโหลดโมเดล TensorFlow.js เข้าสู่หน่วยความจำเบราว์เซอร์",
            "สามารถเชื่อมโยงผลการพยากรณ์คลาส (Class Prediction) เข้ากับการเปลี่ยนสถานะของวัตถุเสมือน 3 มิติ"
        ],
        "tools": "Google Teachable Machine (Image Project), TensorFlow.js (@tensorflow/tfjs), ชุดภาพถ่ายตัวอย่าง",
        "theory": r"""การผสานปัญญาประดิษฐ์เข้ากับเทคโนโลยีเสมือนจริงบนเว็บเบราว์เซอร์ทำได้อย่างมีประสิทธิภาพสูงด้วย TensorFlow.js ซึ่งใช้ประโยชน์จาก WebGL หรือ WebGPU ในการคำนวณแบบขนานบนหน่วยประมวลผลกราฟิก (GPU) ของอุปกรณ์โดยตรง ทำให้ไม่ต้องพึ่งพาเซิร์ฟเวอร์ภายนอก (Zero Server Latency) และรักษาความเป็นส่วนตัวของข้อมูลผู้ใช้งาน

ในปฏิบัติการนี้ ผู้เรียนจะฝึกแบบจำลองโครงข่ายประสาทเทียมแบบคอนโวลูชัน (Convolutional Neural Network: CNN) ที่ผ่านการเรียนรู้ถ่ายโอน (Transfer Learning) จาก MobileNet ผ่านแพลตฟอร์ม Google Teachable Machine เพื่อจำแนกประเภทวัตถุทางวิทยาศาสตร์ เช่น ตัวอย่างแร่ธาตุ ตัวอย่างใบไม้ หรือการแสดงท่าทางพิเศษ ผลลัพธ์จากการพยากรณ์จะอยู่ในรูปของเวกเตอร์ความน่าจะเป็นแบบซอฟต์แมกซ์ (Softmax Probability Vector):
\begin{equation}
P(C_i \mid \mathbf{x}) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
\end{equation}
เมื่อคลาสใดมีค่าความน่าจะเป็นสูงสุดเกินเกณฑ์ความเชื่อมั่นที่กำหนด ระบบจะเรียกใช้ฟังก์ชันควบคุมโมเดล 3 มิติเพื่อแสดงข้อมูลสารสนเทศ แอนิเมชัน หรือป้ายกำกับโฮโลกราฟิกที่สอดคล้องกัน""",
        "code_snippet": r"""// การโหลดและรันโมเดล Teachable Machine บนเบราว์เซอร์
const MODEL_URL = './my_model/';
let model, maxPredictions;

async function initAIModel() {
    const modelURL = MODEL_URL + 'model.json';
    const metadataURL = MODEL_URL + 'metadata.json';

    // โหลดโมเดลผ่านไลบรารี tmImage
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();
    console.log(`โมเดลโหลดสำเร็จ: รองรับ ${maxPredictions} คลาส`);
}

async function predictFrame(videoElement) {
    const prediction = await model.predict(videoElement);
    
    for (let i = 0; i < maxPredictions; i++) {
        const className = prediction[i].className;
        const probability = prediction[i].probability.toFixed(2);
        
        // หากตรวจพบวัตถุเป้าหมายด้วยความแม่นยำมากกว่า 85%
        if (probability > 0.85) {
            triggerARResponse(className);
        }
    }
}

function triggerARResponse(detectedClass) {
    // ปรับเปลี่ยนสีและหมุนโมเดลตามคลาสที่ AI ตรวจพบ
    if (detectedClass === "Mineral_Quartz") {
        cube.material.color.setHex(0x38bdf8);
        cube.scale.set(1.5, 1.5, 1.5);
    } else if (detectedClass === "Mineral_Pyrite") {
        cube.material.color.setHex(0xf59e0b);
        cube.scale.set(1.0, 1.0, 1.0);
    }
}""",
        "activity": "ให้นักศึกษาฝึกสอนโมเดล Teachable Machine ด้วยภาพถ่ายการแสดงสัญลักษณ์มือ 3 แบบ (OK, Peace, Thumbs Up) และเขียนเงื่อนไขเพื่อเปลี่ยนรูปแบบแสงไฟและระบบเสียงสังเคราะห์ในฉาก WebAR ตามสัญลักษณ์ที่ตรวจจับได้",
        "questions": [
            "จงอธิบายข้อดีของการใช้ Transfer Learning บน MobileNet สำหรับการประมวลผลบนเบราว์เซอร์",
            "เหตุใดการรันโมเดล AI ผ่าน WebGL Shader จึงมีความเร็วสูงกว่าการคำนวณผ่าน JavaScript เอนจินแบบเดิม",
            "หากภาพวิดีโอมีพื้นหลังซับซ้อน จะส่งผลต่อค่าความน่าจะเป็นในสมการ Softmax อย่างไร และมีวิธีแก้ปัญหาในขั้นตอนการเตรียมข้อมูลอย่างไร"
        ]
    },
    {
        "filename": "lab06_ai_iot_integration.tex",
        "number": 6,
        "title": "การเชื่อมต่อระบบปัญญาประดิษฐ์และเซนเซอร์ IoT",
        "subtitle": "การรับส่งสตรีมข้อมูลเซนเซอร์ผ่าน WebSocket และเรนเดอร์แดชบอร์ด 3D Spatial Hologram",
        "objectives": [
            "เข้าใจการรับส่งข้อมูลเรียลไทม์ระหว่างอุปกรณ์ IoT และ WebAR ผ่านโปรโตคอล WebSocket / MQTT",
            "สามารถแปลงข้อมูลอนุกรมเวลา (Time-series Sensor Data) เป็นแผนภูมิ 3 มิติเชิงพื้นที่",
            "สามารถสร้างระบบดิจิทัลทวิน (Digital Twin) พื้นฐานที่ตอบสนองต่อสภาวะแวดล้อมจริง"
        ],
        "tools": "ไมโครคอนโทรลเลอร์ ESP32 พร้อมเซนเซอร์ DHT22/BME280 หรือจำลองผ่าน WebSocket Server",
        "theory": r"""การบูรณาการระบบกายภาพและระบบไซเบอร์เข้าด้วยกัน (Cyber-Physical Systems: CPS) เป็นหัวใจของเทคโนโลยีดิจิทัลทวิน (Digital Twin) ในการทดลองนี้ ข้อมูลกายภาพจากเซนเซอร์ IoT เช่น ค่าอุณหภูมิ ความชื้น และค่าฝุ่นละอองขนาดเล็ก จะถูกส่งเข้าสู่เว็บแอปพลิเคชันผ่านช่องทางสื่อสารสองทิศทางความเร็วสูง (WebSocket Protocol):
\begin{equation}
\text{Data Stream}: \{ t_k, T_k, H_k, \text{PM}_{2.5}^{(k)} \} \xrightarrow{\text{WebSocket}} \text{WebAR Scene}
\end{equation}
ในฝั่ง WebAR ข้อมูลที่ได้รับจะถูกนำไปอัปเดตสถานะของแบบจำลอง 3 มิติ เช่น การเปลี่ยนสีของการ์ดแสดงผลโฮโลกราฟิก การปรับเปลี่ยนความหนาแน่นของอนุภาคละอองลอย (Particle System) เพื่อจำลองมลพิษในอากาศตามค่าจริง และการส่งสัญญาณเตือนภัยด้วยแสงและเสียงเมื่อตรวจพบค่าที่ผิดปกติผ่านการวิเคราะห์ด้วยโมเดลการเรียนรู้ของเครื่อง""",
        "code_snippet": r"""// การเชื่อมต่อ WebSocket Client ใน WebAR
const socket = new WebSocket('ws://localhost:8080');

socket.onopen = () => {
    console.log('เชื่อมต่อเซิร์ฟเวอร์ IoT เรียบร้อย');
};

socket.onmessage = (event) => {
    const telemetry = JSON.parse(event.data);
    updateSpatialDashboard(telemetry);
};

function updateSpatialDashboard(data) {
    // ปรับเปลี่ยนค่าพารามิเตอร์ของวัตถุ 3 มิติตามข้อมูลเซนเซอร์
    const temp = data.temperature;
    const humidity = data.humidity;
    
    // ปรับสีวัตถุตามอุณหภูมิ: เย็น (สีฟ้า) -> ร้อน (สีแดง)
    const normalizedTemp = Math.min(Math.max((temp - 20) / 20, 0), 1);
    const targetColor = new THREE.Color().lerpColors(
        new THREE.Color(0x06b6d4), // ฟ้า
        new THREE.Color(0xef4444), // แดง
        normalizedTemp
    );
    cube.material.color = targetColor;
    
    // อัปเดตข้อความ 3D Spatial Canvas
    updateTextTexture(`Temp: ${temp} C | Humid: ${humidity}%`);
}""",
        "activity": "ให้นักศึกษาเขียนโค้ดเพิ่มระบบจำลองอนุภาคฝุ่นควัน (Smoke Particle System) ใน Three.js โดยให้ความเร็วในการลอยตัวและจำนวนอนุภาคแปรผันตามค่าตัวเลขมลพิษที่ได้รับจากเซนเซอร์",
        "questions": [
            "เปรียบเทียบข้อดีและข้อเสียของการใช้ WebSocket เทียบกับ HTTP REST Polling ในงานแสดงผลค่าเซนเซอร์เชิงพื้นที่",
            "แนวคิดของ ดิจิทัลทวิน (Digital Twin) แตกต่างจากการทำกราฟแสดงผลแดชบอร์ด 2 มิติทั่วไปอย่างไร",
            "หากการเชื่อมต่อเครือข่ายขาดหายไประหว่างการแสดงผล ควรมีกลยุทธ์การคืนสภาพ (Failover \\& State Reconnect) ใน WebAR อย่างไร"
        ]
    },
    {
        "filename": "lab07_stem_virtual_lab.tex",
        "number": 7,
        "title": "การพัฒนาห้องปฏิบัติการวิทยาศาสตร์เสมือนจริง",
        "subtitle": "การสร้างระบบจำลองฟิสิกส์เชิงโต้ตอบและการสังเคราะห์เสียงประกอบด้วย Web Audio API",
        "objectives": [
            "เข้าใจการผสานสมการอนุพันธ์ทางฟิสิกส์เข้าสู่วงรอบการเรนเดอร์กราฟิก 3 มิติ",
            "สามารถพัฒนาแบบจำลองการแกว่งของลูกตุ้มนาฬิกาแบบไม่เชิงเส้น (Non-linear Pendulum)",
            "สามารถสังเคราะห์เสียงตอบสนองแบบเรียลไทม์ด้วย Web Audio API โดยไม่ต้องโหลดไฟล์เสียงภายนอก"
        ],
        "tools": "Three.js, Web Audio API (AudioContext, OscillatorNode, GainNode)",
        "theory": r"""การสร้างห้องปฏิบัติการวิทยาศาสตร์เสมือนจริง (Virtual STEM Lab) ต้องการความสมจริงทั้งด้านทัศนศาสตร์ กลศาสตร์ และสวนศาสตร์ (Acoustics) ในแบบจำลองลูกตุ้มอย่างง่าย พิกัดเชิงมุม $\theta(t)$ ถูกควบคุมด้วยสมการเชิงอนุพันธ์อันดับสอง:
\begin{equation}
\frac{d^2\theta}{dt^2} + \frac{b}{m}\frac{d\theta}{dt} + \frac{g}{L}\sin\theta = 0
\end{equation}
โดยที่ $L$ คือความยาวเชือก, $g$ คือความเร่งโน้มถ่วง และ $b$ คือสัมประสิทธิ์ความเสียดทานของอากาศ การแก้สมการนี้ทำได้ในวงรอบการเรนเดอร์ด้วยระเบียบวิธีออยเลอร์-โครเมอร์ (Euler-Cromer Method)

ด้านเสียงตอบสนอง Web Audio API ช่วยสร้างเสียงสังเคราะห์ผ่านวงจรออสซิลเลเตอร์ดิจิทัล (OscillatorNode) โดยสามารถปรับเปลี่ยนความถี่ฮาร์มอนิก ($f$) และอัตราขยายสัญญาณ (Gain) ได้ทันทีตามพลังงานจลน์ของลูกตุ้ม ทำให้ผู้เรียนรับรู้ถึงการชนหรือการเคลื่อนที่ด้วยประสาทสัมผัสคู่ (Multimodal Sensory Feedback)""",
        "code_snippet": r"""// ระบบจำลองฟิสิกส์ลูกตุ้มและการสังเคราะห์เสียง
let theta = Math.PI / 4; // มุมเริ่มต้น 45 องศา
let omega = 0.0;         // ความเร็วเชิงมุม
const g = 9.81, L = 2.0, b = 0.05, dt = 0.016;

// เริ่มต้นระบบเสียง Web Audio API
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playSpatialSound(frequency, duration) {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(frequency, audioCtx.currentTime);
    
    gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
}

function updatePhysics() {
    // ระเบียบวิธี Euler-Cromer
    const alpha = -(g / L) * Math.sin(theta) - b * omega;
    omega += alpha * dt;
    theta += omega * dt;

    // อัปเดตตำแหน่งลูกตุ้มใน Three.js
    pendulumBob.position.x = L * Math.sin(theta);
    pendulumBob.position.y = -L * Math.cos(theta);

    // ส่งเสียงสังเคราะห์เมื่อลูกตุ้มแกว่งผ่านจุดต่ำสุด (ความเร็วสูงสุด)
    if (Math.abs(theta) < 0.02 && Math.abs(omega) > 0.5) {
        playSpatialSound(440 + Math.abs(omega) * 50, 0.15);
    }
}""",
        "activity": "ให้นักศึกษาเพิ่มปฏิสัมพันธ์ให้ผู้ใช้สามารถใช้ท่าทางนิ้วมือ (Pinch) จับลูกตุ้มแล้วลากไปวางที่มุมใดๆ เพื่อปล่อยให้แกว่งใหม่ พร้อมคำนวณและแสดงค่าพลังงานรวมของระบบ (ศักย์ + จลน์) แบบเรียลไทม์",
        "questions": [
            "เหตุใดระเบียบวิธี Euler-Cromer จึงมีความเสถียรด้านพลังงานสูงกว่าระเบียบวิธี Euler ดั้งเดิมในการจำลองการสั่นแบบฮาร์มอนิก",
            "การสังเคราะห์เสียงด้วย Web Audio API มีข้อได้เปรียบอย่างไรเมื่อเทียบกับการเล่นไฟล์เสียงแบบ MP3/WAV ในงานความจริงเสมือน",
            "จงอธิบายแนวทางการคำนวณเวกเตอร์ความเร่งหนีศูนย์กลางที่เกิดขึ้นกับมวลลูกตุ้ม"
        ]
    },
    {
        "filename": "lab08_mobile_xr_deployment.tex",
        "number": 8,
        "title": "การคอมไพล์และติดตั้งบนอุปกรณ์พกพาและแว่น XR",
        "subtitle": "การห่อหุ้มเว็บแอปพลิเคชันเป็น Android APK และการทดสอบประสิทธิภาพเชิงลึก",
        "objectives": [
            "เข้าใจสถาปัตยกรรมการแปลงเว็บแอปพลิเคชันไฮบริดสู่แอปเนทีฟด้วย Capacitor / Cordova",
            "สามารถกำหนดค่าสิทธิ์การเข้าถึงกล้องและเซนเซอร์ในไฟล์ AndroidManifest.xml",
            "สามารถคอมไพล์ สร้างไฟล์ APK และติดตั้งเพื่อทดสอบบนสมาร์ทโฟนหรือแว่นสวมศีรษะ XR"
        ],
        "tools": "Node.js, Capacitor CLI, Android Studio / Gradle Build Tools, อุปกรณ์ Android สำหรับทดสอบ",
        "theory": r"""แม้ว่า WebAR จะมีความยืดหยุ่นสูงในการเข้าถึงผ่านเบราว์เซอร์ แต่ในสถานการณ์ที่ต้องการประสิทธิภาพสูงสุด การเข้าถึงฮาร์ดแวร์โดยตรงโดยไม่มีแถบควบคุมของเบราว์เซอร์ (Fullscreen Immersive Experience) หรือการติดตั้งในโรงเรียนที่ไม่มีการเชื่อมต่ออินเทอร์เน็ต การห่อหุ้มเว็บแอปพลิเคชัน (Web Packaging) เข้าสู่รูปแบบแอปพลิเคชันเนทีฟ (Native APK) จึงเป็นแนวทางมาตรฐานที่นิยมใช้

สถาปัตยกรรมของ Capacitor หรือ Cordova ทำงานโดยการฝังส่วนประกอบ WebView ประสิทธิภาพสูงลงในแอปเนทีฟ และเปิดสะพานเชื่อมต่อคำสั่งจาวาสคริปต์ (JavaScript Bridge) ช่วยให้โค้ด WebGL และ MediaPipe เดิมสามารถเข้าถึงกล้องหลัง กล้องหน้า และเซนเซอร์วัดการหมุน (IMU) ของอุปกรณ์ได้อย่างรวดเร็ว

ขั้นตอนสำคัญประกอบด้วยการกำหนดค่าความปลอดภัยและการขอสิทธิ์การใช้งานกล้องในไฟล์ \texttt{AndroidManifest.xml} การปรับแต่งตัวแปรใน \texttt{capacitor.config.json} เพื่อเปิดใช้งานการเร่งความเร็วด้วยฮาร์ดแวร์ (Hardware Acceleration) และการคอมไพล์ด้วยคำสั่ง \texttt{gradlew assembleDebug} เพื่อให้ได้ไฟล์ติดตั้ง \texttt{.apk} ที่พร้อมใช้งาน""",
        "code_snippet": r"""<!-- การกำหนดสิทธิ์การใช้งานกล้องใน AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="th.ac.rbru.ar.aimotion">

    <!-- สิทธิ์การเข้าถึงกล้องและอินเทอร์เน็ต -->
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-feature android:name="android.hardware.camera" />
    <uses-feature android:name="android.hardware.camera.autofocus" />

    <application
        android:allowBackup="true"
        android:hardwareAccelerated="true"
        android:label="AR AI Lab RBRU"
        android:theme="@style/AppTheme.NoActionBar">
        
        <activity
            android:name=".MainActivity"
            android:configChanges="orientation|keyboardHidden|screenSize"
            android:screenOrientation="landscape"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>""",
        "activity": "ให้นักศึกษาทำตามขั้นตอนการ Build APK และติดตั้งลงบนสมาร์ทโฟนของตนเองผ่านสาย USB ด้วยคำสั่ง adb install พร้อมบันทึกภาพหน้าจอขณะทดสอบการตรวจจับมือและตรวจวัดอัตราการแสดงผล FPS จริงบนอุปกรณ์",
        "questions": [
            "จงอธิบายบทบาทของ Android WebView ในการประมวลผลโค้ด Three.js และ MediaPipe",
            "เหตุใดจึงต้องกำหนดคุณสมบัติ android:hardwareAccelerated=\"true\" ในการพัฒนาแอปพลิเคชันความจริงเสริม",
            "หากเปิดแอปพลิเคชันแล้วพบหน้าจอสีดำ ไม่ปรากฏภาพจากกล้อง ควรตรวจสอบจุดบกพร่องใดเป็นอันดับแรก"
        ]
    }
]

for ch in chapters_data:
    out_path = os.path.join(CHAPTERS_DIR, ch["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"% =========================================================================\n")
        f.write(f"% ปฏิบัติการที่ {ch['number']}: {ch['title']}\n")
        f.write(f"% =========================================================================\n\n")
        
        # Chapter header
        f.write(f"\\chapter{{{ch['title']}}}\n")
        f.write(f"\\label{{ch:lab{ch['number']:02d}}}\n\n")
        
        # Subtitle
        f.write(f"\\noindent{{\\large\\bfseries\\color{{cyberblue}} {ch['subtitle']}}}\n\n")
        f.write(f"\\vspace{{0.4cm}}\n\n")
        
        # Objectives box
        f.write(f"\\begin{{labobjectivebox}}{{{ch['title']}}}\n")
        f.write(f"\\textbf{{วัตถุประสงค์การเรียนรู้}}\n")
        f.write(f"\\begin{{enumerate}}[leftmargin=1.8cm, itemsep=2pt]\n")
        for obj in ch["objectives"]:
            f.write(f"    \\item {obj}\n")
        f.write(f"\\end{{enumerate}}\n\n")
        f.write(f"\\vspace{{4pt}}\n")
        f.write(f"\\textbf{{เครื่องมือและอุปกรณ์จำเป็น}} \\enspace {ch['tools']}\n")
        f.write(f"\\end{{labobjectivebox}}\n\n")
        
        # Section 1: Theory
        f.write(f"\\section{{หลักการและทฤษฎีพื้นฐาน}}\n\n")
        f.write(f"{ch['theory']}\n\n")
        
        # Concept box
        f.write(f"\\begin{{conceptbox}}{{สาระสำคัญของปฏิบัติการที่ {ch['number']}}}\n")
        f.write(f"การเข้าใจโครงสร้างทางคณิตศาสตร์และการประมวลผลเชิงพื้นที่ ช่วยให้นักศึกษาสามารถออกแบบระบบเสมือนจริงที่ตอบสนองต่อผู้ใช้งานได้อย่างเป็นธรรมชาติและแม่นยำสูง ทั้งยังสามารถต่อยอดสู่การพัฒนาแอปพลิเคชันทางวิทยาศาสตร์และอุตสาหกรรมได้อย่างมีประสิทธิภาพ\n")
        f.write(f"\\end{{conceptbox}}\n\n")
        
        # Section 2: Implementation & Source Code
        f.write(f"\\section{{ขั้นตอนการปฏิบัติการและการทดลอง}}\n\n")
        f.write(f"ให้นักศึกษาดำเนินการสร้างไฟล์โครงการและเขียนคำสั่งตามลำดับขั้นตอนต่อไปนี้ โดยตรวจสอบความถูกต้องของไลบรารีที่เรียกใช้งานและเส้นทางไฟล์\n\n")
        
        f.write(f"\\begin{{codebox}}{{โครงสร้างโค้ดหลักของปฏิบัติการที่ {ch['number']}}}\n")
        f.write(f"\\begin{{lstlisting}}[language=HTML]\n")
        f.write(f"{ch['code_snippet']}\n")
        f.write(f"\\end{{lstlisting}}\n")
        f.write(f"\\end{{codebox}}\n\n")
        
        # Section 3: Verification & Results
        f.write(f"\\section{{การทดสอบระบบและการบันทึกผล}}\n\n")
        f.write(f"เมื่อรันโปรแกรมบนเซิร์ฟเวอร์จำลอง (Local Development Server) ให้ทำการทดสอบการทำงานตามเกณฑ์ประเมินในตารางต่อไปนี้ พร้อมบันทึกผลการสังเกตการณ์ลงในรายงานผลการทดลอง\n\n")
        
        f.write(f"\\begin{{table}}[htbp]\n")
        f.write(f"\\centering\n")
        f.write(f"\\small\n")
        f.write(f"\\begin{{tabularx}}{{\\textwidth}}{{c X c Y}}\n")
        f.write(f"\\toprule\n")
        f.write(f"\\textbf{{ลำดับ}} & \\textbf{{รายการทดสอบและพฤติกรรมที่คาดหวัง}} & \\textbf{{เกณฑ์ผ่าน}} & \\textbf{{ผลการทดสอบ}} \\\\\n")
        f.write(f"\\midrule\n")
        f.write(f"1 & การเริ่มต้นระบบและการเข้าถึงสิทธิ์ฮาร์ดแวร์ & ภายใน 3 วินาที & ผ่าน / ไม่ผ่าน \\\\\n")
        f.write(f"2 & ความเสถียรของการตรวจจับและการคำนวณพิกัด & อัตราความแม่นยำ $> 90\\%$ & ผ่าน / ไม่ผ่าน \\\\\n")
        f.write(f"3 & อัตราการแสดงผลกราฟิกต่อเนื่อง (Framerate) & ไม่ต่ำกว่า 55 FPS & ผ่าน / ไม่ผ่าน \\\\\n")
        f.write(f"4 & การตอบสนองต่อปฏิสัมพันธ์เชิงพื้นที่ & ความหน่วง $< 40$ ms & ผ่าน / ไม่ผ่าน \\\\\n")
        f.write(f"\\bottomrule\n")
        f.write(f"\\end{{tabularx}}\n")
        f.write(f"\\caption{{ตารางประเมินผลการทำงานของระบบในปฏิบัติการที่ {ch['number']}}}\n")
        f.write(f"\\label{{tab:eval_lab{ch['number']:02d}}}\n")
        f.write(f"\\end{{table}}\n\n")
        
        # Section 4: Hands-on Activity Challenge
        f.write(f"\\section{{ภารกิจท้าทายและการต่อยอด}}\n\n")
        f.write(f"\\begin{{activitybox}}{{กิจกรรมส่งเสริมทักษะขั้นสูง}}\n")
        f.write(f"{ch['activity']}\n")
        f.write(f"\\end{{activitybox}}\n\n")
        
        # Section 5: Discussion & Review Questions
        f.write(f"\\section{{คำถามท้ายการทดลอง}}\n\n")
        f.write(f"ให้นักศึกษาตอบคำถามเชิงวิเคราะห์ต่อไปนี้ลงในสมุดบันทึกปฏิบัติการ\n\n")
        f.write(f"\\begin{{enumerate}}[leftmargin=1.8cm, itemsep=6pt]\n")
        for q in ch["questions"]:
            f.write(f"    \\item {q}\n")
        f.write(f"\\end{{enumerate}}\n\n")

print("Successfully generated all 8 lab chapters for Book 05.")
