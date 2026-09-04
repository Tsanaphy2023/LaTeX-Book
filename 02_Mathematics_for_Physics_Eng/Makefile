# Makefile for Mathematics for Physics (English Edition)
# Asst. Prof. Dr. Chewa Thassana

MAIN = main
COMPILER = xelatex -interaction=nonstopmode
INDEXER = makeindex

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(COMPILER) $(MAIN).tex
	$(INDEXER) $(MAIN).idx
	$(COMPILER) $(MAIN).tex
	$(COMPILER) $(MAIN).tex

clean:
	rm -f *.aux *.log *.toc *.out *.idx *.ind *.ilg *.lof *.lot *.listing *.synctex.gz
