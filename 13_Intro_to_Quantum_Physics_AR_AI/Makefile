# Makefile for Quantum Physics with AR/XR & AI Deep Learning Textbook
TARGET = main
XETEX = xelatex -shell-escape -interaction=nonstopmode
MAKEINDEX = makeindex

all: $(TARGET).pdf

$(TARGET).pdf: $(TARGET).tex
	$(XETEX) $(TARGET).tex
	$(MAKEINDEX) $(TARGET).idx
	$(XETEX) $(TARGET).tex
	$(XETEX) $(TARGET).tex

clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.idx *.ilg *.ind *.listing
	find chapters -name "*.aux" -delete
	find frontmatter -name "*.aux" -delete
	find backmatter -name "*.aux" -delete

distclean: clean
	rm -f $(TARGET).pdf
