# Makefile for Modern Physics with AR/XR Simulations and Python Computing
# Author: Asst. Prof. Dr. Chewa Thassana

MAIN = main
ENGINE = xelatex -interaction=nonstopmode
MAKEINDEX = makeindex

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex styles/modern_physics_style.sty
	$(ENGINE) $(MAIN).tex
	$(MAKEINDEX) $(MAIN).idx
	$(ENGINE) $(MAIN).tex
	$(ENGINE) $(MAIN).tex

clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.idx *.ind *.ilg *.fls *.fdb_latexmk
	rm -f frontmatter/*.aux chapters/*.aux backmatter/*.aux

.PHONY: all clean
