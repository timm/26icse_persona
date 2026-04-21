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

MAIN   ?= paper.tex
BUILD  ?= $(HOME)/tmp/$(notdir $(I))
PDF    := $(BUILD)/$(MAIN:.tex=.pdf)

pdf: ## build paper/$(MAIN) with tectonic; outputs to ~/tmp/<repo>/
	@mkdir -p $(BUILD)
	@tectonic --keep-logs --keep-intermediates --outdir $(BUILD) paper/$(MAIN)
	@echo "→ $(PDF)"
	@open $(PDF) 2>/dev/null || true

clean: ## remove build directory
	@rm -rf $(BUILD)
	@echo "cleaned $(BUILD)"
