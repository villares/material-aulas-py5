### how to set up this repo

Context: This is an attempt at making a jupyter{book} version of my `material-aulas` teaching repository

Goal: Make class materials that can profit from Thebe/MyBinder.org execution.

#### Recording steps taken so far (work in progress)

2021-09-18 First attempt, lots of help fro @hx2A, first jupyter book working page!
2021-09-19 Cleaning up the steps needed (removed some wrong turns taken)

- Cloned requirements and settings froms https://py5.ixora.io Jupyter Book docs
   - This repo is kind of a hollowed out clone of the `py5` docs
- Reading https://jupyterbook.org/start/overview.html
   - Installed `jupyter-book` in my `pycoding` conda env that I also use to run `py5`
   - Installed `ghp-import`
   - Created a `gh-pages` branch in this repo
   - Do not change the `_config.yml` to point to the gh-pages branch, keep it looking for `main` (where the binder folder is)
   - For GitHub token authentication, now using [GitHub CLI auth login](https://cli.github.com/manual/gh_auth_login), to install follow https://github.com/cli/cli#installation
   - Used `jupyter-book build /`
      - TOC still confusing, trying `jupyter-book toc from-project /` (should learn how to pipe this to the propper file!)
   - Use `ghp-import -n -p -f _build/html` command to rebuild the publishing `gh-pages` branch, needs `push` afterwards I think.
   - Might need to install additional `py5bot` kernel to use "static mode" examples. [Instructions here](https://py5.ixora.io/content/install.html#jupyter-notebook-kernels).
   
