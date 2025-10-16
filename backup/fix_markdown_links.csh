#!/bin/csh

# Fix markdown links using sed (two separate passes)
# Only updates files if changes are detected
# Usage: ./fix_markdown_links.csh <file1.md> [file2.md ...]

if ($#argv == 0) then
    echo "Error: Please provide at least one filename"
    echo "Usage: $0 <file1.md> [file2.md ...]"
    echo "   or: $0 *.md"
    exit 1
endif

foreach file ($argv)
    if (! -f "$file") then
        echo "Warning: '$file' not found, skipping..."
        continue
    endif
    
    echo "Processing: $file"
    
    # Create new file with both fixes applied
    # Fix 1: Add space before [...](url) when preceded by alphanumeric character (but not escaped brackets or quotes)
    sed -E 's/([[:alnum:]])\[([^]]+)\]\(([^)]+)\)/\1 [\2](\3)/g' "$file" > "${file}.tmp1"
    
    # Fix 2: Add space after [text](url) when followed by alphanumeric character, but not when followed by punctuation, ), or quotes
    sed -E 's/\]\(([^)]+)\)([[:alnum:]])/](\1) \2/g' "${file}.tmp1" > "${file}.new"
    
    # Show which lines changed with colors
    echo "  Lines changed:"
    which colordiff >& /dev/null
    if ($status == 0) then
        colordiff -u "$file" "${file}.new" | grep '^[+-]' | head -20
    else
        diff --color=always -u "$file" "${file}.new" | grep '^[+-]' | head -20
    endif
    
    # Clean up intermediate temp file
    rm "${file}.tmp1"
    
    # Check if new file is different from original
    if (`diff -q "$file" "${file}.new" > /dev/null; echo $status` == 0) then
        echo "  No changes needed"
        rm "${file}.new"
    else
        echo "  Changes detected - created: ${file}.fixed"
        mv "${file}.new" "${file}.fixed"
    endif
end

echo "Done!"
