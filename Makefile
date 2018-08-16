compile:
	hugo

serve:
	hugo serve

clean:
	cd cv && $(RM) fredrik-savje-cv.*

cv: static/fredrik-savje-cv.pdf

static/fredrik-savje-cv.pdf: cv/fredrik-savje-cv.tex
	cd cv && pdflatex fredrik-savje-cv.tex && pdflatex fredrik-savje-cv.tex
	mv -f cv/fredrik-savje-cv.pdf static/fredrik-savje-cv.pdf

cv/fredrik-savje-cv.tex: cv/cv_template.tex cv/gen_cv.py data/cv.json
	cd cv && python2 gen_cv.py
