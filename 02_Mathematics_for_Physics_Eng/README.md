# Mathematics for Physics (English Edition)

> **Official Textbook:** Analytical Foundations and Scientific Simulations  
> **Author:** Asst. Prof. Dr. Chewa Thassana (`chewa.t@rbru.ac.th`)  
> **Affiliation:** Department of Physics, Faculty of Science and Technology, Rambhai Barni Rajabhat University (RBRU), Chanthaburi, Thailand  
> **Academic Year:** 2026

---

## 1. Overview & Pedagogical Standards

This master textbook is designed for undergraduate and graduate courses in theoretical physics and mathematical methods. Developed according to the **Tipler & Mosca** and **Serway & Jewett** standards, the book integrates:
- **P-S-C-T Problem Solving Framework:** Picture, Strategy, Calculation, Think.
- **Active Learning & Simulation:** Computational Python (NumPy, SciPy, Matplotlib) models embedded throughout all analytical chapters.
- **Outcome-Based Education (OBE):** Comprehensive Course Learning Outcomes (CLOs) mapped to Bloom's Taxonomy.
- **Bilingual Subject Index:** Extensive indexing with `imakeidx` and dedicated List of Figures and Tables.

---

## 2. Course Breakdown (9 Chapters)

1. **Chapter 1: Curvilinear Coordinate Systems & Scale Factors**
   - Metric scale factors (Lamé coefficients), Cartesian, cylindrical, and spherical coordinates, differential elements ($d\vec{r}, d\vec{a}, dV$), rotating unit vector kinematics.
2. **Chapter 2: Vector Analysis & Differential Field Operators**
   - Dot, cross, and triple products; gradient ($\nabla$), divergence ($\nabla \cdot$), curl ($\nabla \times$), Laplacian ($\nabla^2$), conservative potential theory, Lorentz force.
3. **Chapter 3: Infinite Series & Approximations**
   - Taylor and Maclaurin expansions, convergence tests (Ratio, Root, Integral), binomial theorem, relativistic kinetic energy, large-amplitude pendulum correction.
4. **Chapter 4: Complex Analysis & Applications**
   - Argand plane, Euler's formula, de Moivre's theorem, roots of unity, AC impedance ($R, L, C$), phasors, resonance, and Cauchy-Riemann equations.
5. **Chapter 5: Linear Algebra & Matrix Mechanics**
   - Matrix algebra, determinants, inverses, Hermitian and unitary matrices, secular eigenvalue problem, diagonalization, normal modes of coupled oscillators, inertia tensors.
6. **Chapter 6: Multivariable Differential Calculus**
   - Partial derivatives, Clairaut's theorem, total differentials, state functions, directional derivatives, tangent planes, constrained optimization with Lagrange multipliers.
7. **Chapter 7: Multiple Integrals & Field Theorems**
   - Double and triple integrals, Jacobians, line and surface integrals, Green's theorem, Stokes' theorem, Gauss's Divergence theorem, Maxwell's equations.
8. **Chapter 8: First-Order Ordinary Differential Equations**
   - Classification, separable equations, integrating factors, exact equations, terminal velocity with quadratic drag, $RC$ and $RL$ circuits.
9. **Chapter 9: Second-Order Linear Differential Equations & Oscillations**
   - Characteristic auxiliary equation, overdamped, critically damped, and underdamped oscillators, driven oscillations, resonance curves, Quality factor ($Q$).

---

## 3. Directory Structure

```
02_Mathematics_for_Physics_Eng/
├── main.tex                         # Master XeLaTeX root document
├── Makefile                         # Automated 3-pass build tool
├── README.md                        # Documentation and course syllabus
├── styles/
│   └── rbru_book_style_en.sty       # English typography, tcolorbox environments, palettes
├── frontmatter/
│   ├── cover.tex                    # Cosmic geometric title cover with author portrait
│   ├── title.tex                    # Formal title page
│   ├── preface.tex                  # Preface & Active Learning pedagogy
│   └── syllabus.tex                 # OBE syllabus & Bloom's taxonomy mapping
├── chapters/
│   ├── ch01_coordinate_systems.tex  # Chapter 1: Curvilinear Coordinates
│   ├── ch02_vectors.tex             # Chapter 2: Vector Calculus
│   ├── ch03_basic_series.tex        # Chapter 3: Infinite Series
│   ├── ch04_complex_numbers.tex     # Chapter 4: Complex Analysis
│   ├── ch05_matrices.tex            # Chapter 5: Linear Algebra
│   ├── ch06_derivatives.tex         # Chapter 6: Multivariable Calculus
│   ├── ch07_integrals.tex           # Chapter 7: Field Theorems
│   ├── ch08_ode.tex                 # Chapter 8: First-Order ODEs
│   └── ch09_second_order_odes.tex   # Chapter 9: Second-Order ODEs
├── backmatter/
│   ├── appendix.tex                 # Coordinate operators and vector identities
│   ├── references.tex               # Bibliography
│   └── biography.tex                # Author biography of Dr. Chewa Thassana
└── images/                          # Author portraits and high-res assets
```

---

## 4. Building the Textbook

To compile the entire textbook into high-resolution PDF format:
```bash
make
```
or manually with `xelatex`:
```bash
xelatex -interaction=nonstopmode main.tex
makeindex main.idx
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```
