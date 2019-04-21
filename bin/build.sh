echo "building report"
pandoc \
  -N \
  --from markdown+implicit_header_references \
  --variable secnumdepth=3 \
  --variable titlepage=true \
  --variable block-headings \
  --variable fontsize=12pt \
  --variable version=2.0 \
  --toc \
  --listings \
  -H ./bin/listings-setup.tex \
  --filter ./bin/filter.py \
  --filter pandoc-citeproc \
  --bibliography=references.bib \
  --template ./bin/template.tex \
  -o report.tex \
  `node bin/scripts/filelist.js`
  # test.md
  # --pdf-engine=xelatex \