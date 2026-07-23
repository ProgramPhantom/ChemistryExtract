#!/bin/bash

# Script to create the validation folder outline for a given corpus.
# Usage: ./create_validation_outline.sh /tests/corpus/<corpus_name>

if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_corpus>"
    echo "Example: $0 /tests/corpus/benchmark"
    exit 1
fi

RAW_PATH="$1"
# Strip trailing slash if present
RAW_PATH="${RAW_PATH%/}"

# Resolve corpus path (handle leading slash if path is relative to repo root)
CORPUS_PATH="$RAW_PATH"
if [ ! -d "$CORPUS_PATH" ] && [ -d "${RAW_PATH#/}" ]; then
    CORPUS_PATH="${RAW_PATH#/}"
fi

if [ ! -d "$CORPUS_PATH" ]; then
    echo "Error: Corpus directory '$RAW_PATH' does not exist."
    exit 1
fi

CORPUS_NAME=$(basename "$CORPUS_PATH")
VALIDATION_BASE_DIR="tests/validation/${CORPUS_NAME}"

echo "Creating validation outline for corpus '${CORPUS_NAME}' at '${VALIDATION_BASE_DIR}'..."

mkdir -p "$VALIDATION_BASE_DIR"

count=0
for item in "$CORPUS_PATH"/*; do
    [ -e "$item" ] || continue
    
    filename=$(basename "$item")
    
    # Skip hidden files and json cache files
    if [[ "$filename" == .* ]] || [[ "$filename" == *.json ]]; then
        continue
    fi
    
    # Strip extension (e.g. paper10.pdf -> paper10, paper10 -> paper10)
    paper_name="${filename%.*}"
    
    paper_val_dir="${VALIDATION_BASE_DIR}/${paper_name}"
    cat_dir="${paper_val_dir}/categorisation"
    sum_dir="${paper_val_dir}/summary"
    
    mkdir -p "$cat_dir"
    mkdir -p "$sum_dir"
    
    # Create template table1.json in categorisation if it doesn't exist
    if [ ! -f "${cat_dir}/table1.json" ]; then
        cat << 'EOF' > "${cat_dir}/table1.json"
{
  "contains_scientific_data": false,
  "contains_raw_diffusion_data": false,
  "contains_mark_houwink_parameters": false,
  "contains_flory_parameters": false,
  "contains_polymer_diffusion_coeff": false
}
EOF
    fi
    
    # Create template summary.json in summary if it doesn't exist
    if [ ! -f "${sum_dir}/summary.json" ]; then
        cat << 'EOF' > "${sum_dir}/summary.json"
{
  "title": "",
  "authors": [],
  "doi": ""
}
EOF
    fi
    
    count=$((count + 1))
    echo "  Created outline for: ${paper_name}"
done

echo "Done! Created validation outline for ${count} paper(s) in '${VALIDATION_BASE_DIR}'."
