#### set up install for this repo

Context: This is an attempt at making a jupyter{book} version of my `material-aulas` teaching repository

Goal: Make class materials that can profit from Thebe/MyBinder.org execution.

Recording steps taken so far (unfinished, I might take a wrong turn):

- Cloned requitements and settings froms py5.ixora.io Jupyter Book docs
   - this repo is kind of a hollowed out clone of the `py5` docs
- Reading https://jupyterbook.org/start/overview.html
   - installed `jupyter-book` in my `pycoding` conda env that I also use to run `py5`
- Reading https://jupyterbook.org/start/publish.html
   - installed `ghp-import`
   - created a `gh-pages` branch in this repo
   - tried the `ghp-import -n -p -f _build/html` and **FAILED, because I can no longer auth gh with passwoed**
   - **Reading all over again about GitHub token authentication and some sort of GitHub CLI thing that has "web login"**
      - Maybe [creating-a-personal-access-token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) **Couldn't find out how to use the token after creating it :(**
      - Maybe https://cli.github.com/manual/gh_auth_login that needs https://github.com/cli/cli#installation
