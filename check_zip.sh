#! /bin/bash
for f in *.zip
do
  zip --test $f 1>/dev/null && echo $f ': OK'
  if (($? > 0)); then
    # use double quote for $f to function
    printf '%s \n' "$f : bad file" >&2
  fi
done
