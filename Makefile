# vim: ts=2 sw=2 sts=2 et  :
I := $(shell git rev-parse --show-toplevel)

help: ## show help.
	@gawk  '\
		BEGIN {FS = ":.*?##"; \
           printf "\nUsage:\n  make \033[36m<target>\033[0m\n\ntargets:\n"} \
         /^[~a-z0-9A-Z_%\.\/-]+:.*?##/ { \
           printf("  \033[36m%-15s\033[0m %s\n", $$1, $$2) | "sort " } \
		'$(MAKEFILE_LIST)

push: ## commit and push with prompted message
	@read -p "Reason? " msg; git commit -am "$$msg"; git push; git status

TEX := $(wildcard paper/*.tex)
MAIN ?= paper/paper.tex

pdf: ## build the paper PDF with latexmk (expects paper/paper.tex)
	@cd paper && latexmk -pdf -interaction=nonstopmode $(notdir $(MAIN))

clean: ## remove LaTeX build artifacts
	@cd paper && latexmk -C 2>/dev/null || true
