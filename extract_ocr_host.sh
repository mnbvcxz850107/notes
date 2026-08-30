#!/bin/bash
pdfs=(
    "BM110|/Users/furyan/.gemini/antigravity/brain/85a37da7-0822-435b-8c94-865ea85951d9/.user_uploaded/media_1788116041796.pdf"
    "BM111|/Users/furyan/.gemini/antigravity/brain/85a37da7-0822-435b-8c94-865ea85951d9/.user_uploaded/media_1788116044808.pdf"
    "BM112|/Users/furyan/.gemini/antigravity/brain/85a37da7-0822-435b-8c94-865ea85951d9/.user_uploaded/media_1788116174745.pdf"
    "BM113|/Users/furyan/.gemini/antigravity/brain/85a37da7-0822-435b-8c94-865ea85951d9/.user_uploaded/media_1788116174544.pdf"
)

mkdir -p /Users/furyan/.gemini/antigravity/scratch/notes/ocr_data
mkdir -p /Users/furyan/.gemini/antigravity/scratch/notes/img_tmp

for item in "${pdfs[@]}"; do
    name="${item%%|*}"
    path="${item##*|}"
    txt="/Users/furyan/.gemini/antigravity/scratch/notes/ocr_data/${name}.txt"
    
    if [ ! -f "$txt" ]; then
        echo "Processing $name..."
        rm -rf /Users/furyan/.gemini/antigravity/scratch/notes/img_tmp/*
        pdftoppm -r 150 -f 1 -l 80 -png "$path" /Users/furyan/.gemini/antigravity/scratch/notes/img_tmp/p
        
        for img in /Users/furyan/.gemini/antigravity/scratch/notes/img_tmp/*.png; do
            echo "--- PAGE $img ---" >> "$txt"
            tesseract "$img" stdout -l chi_tra+eng 2>/dev/null >> "$txt"
        done
        echo "Saved $txt"
    fi
done
echo "All done!"
