jb build .
git add -A
git commit -m 'saving modifications `date --rfc-3339=seconds`'
git push
ghp-import -n -p -f _build/html
git checkout gh-pages
git add -A
git commit -m 'saving modifications `date --rfc-3339=seconds`'
git push
git checkout main
