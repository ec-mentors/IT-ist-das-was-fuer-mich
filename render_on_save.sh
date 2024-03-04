#!/bin/bash
# render.sh starts from scratch, so no incremental builds and therefore slow
find . -type f -name "*.md" | entr bash render.sh
