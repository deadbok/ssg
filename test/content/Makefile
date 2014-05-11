rwildcard=$(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2) $(filter $(subst *,%,$2),$d))

HTMLS=$(call rwildcard,.,*.rst)
TXTDIR=.
#HTMLS=$(wildcard *.rst)
MDS=$(patsubst %.rst,$(TXTDIR)/%.md, $(HTMLS))

.PHONY : all

all : $(MDS)

$(TXTDIR):
	mkdir $(TXTDIR)

$(TXTDIR)/%.md : %.rst $(TXTDIR)
	pandoc -r rst -w markdown -s $< -o $@
