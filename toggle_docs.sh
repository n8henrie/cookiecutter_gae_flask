#!/bin/bash -e
# toggle_docs.sh
# Uses pandoc to change all .md to .rst and vice-versa in a given directory tree.
# I don't really care for .rst, but PyPI needs it. 

if [ "$(find . -iname "*.md")" ] && [ "$(find . -iname "*.rst")" ]; then
  echo "Both .md and .rst filetypes exist, please make it so only one of two is there."
elif [ ! "$(find . -iname "*.md")" ] && [ ! "$(find . -iname "*.rst")" ]; then
  echo "Neither .md or .rst filetypes exist, you should have one or the other."
else

  # Do the converstion
  if [ "$(find . -iname "*.md")" ]; then
    for f in $(find . -iname "*.md"); do pandoc --from=markdown --to=rst "$f" > "${f%md}rst"; rm "$f"; done
  elif [ "$(find . -iname "*.rst")" ]; then
    for f in $(find . -iname "*.rst"); do pandoc --from=rst --to=markdown "$f" > "${f%rst}md"; rm "$f"; done
  fi

fi

