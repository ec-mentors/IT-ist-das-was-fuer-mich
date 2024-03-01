#!/bin/bash
# Run this to render both website and slides and check links
# Create slides
echo "Building slides"
make --makefile=SlidesMakefile all

# Re-create website
echo "Building website"
./render.sh

# Running linkcheck
echo "Linkcheck"
sphinx-build -b linkcheck -q -w linkcheck.txt source/ public/

echo "Done \o/"
