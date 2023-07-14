# CQ4DS 

## Starting with Github Codespaces

- Go to [https://github.com/codespaces](https://github.com/codespaces)
- New codespace
- Select the repository (This will fill all the other fields)
- Create codespace
- Wait 2-3 minutes

## Startup todo list:

Select local the virtual environment:
- Select a python file
- Bottom left next to `Python` click `3.10.6 64-bit` (You can only see this if you select a .py file!!!)
- Select `('.venv': poetry)`
- If not shown enter: `/workspaces/class-test/.venv/bin`
- Refresh browser window to make `black` work

Enable shortcuts:
- Run in the terminal: `source aliases`
Enables (See `aliases` file for more):
- `gs`: git status
- `gb`: git branch
- `venv`: activates virtual environment
- `deac`: deactivates virtual environment

Start jupyter server:
- New terminal: `+` next to `bash` top right on the terminal window
- Run in the terminal: `screen -S jupyter`
- Run `source aliases`
- Run `venv`
- Run in the terminal: `jupyter notebook`
- Copy token (long hash after `token=`) you will need this to login to the notebook server
- Switch to "PORTS"
- Make port visibility "Public"
- Hover over the address under "Local Address" and click the globe icon, that will open the notebook server
- Enter the token if requested
- Switch back to "TERMINAL"
- Shut down the terminal (trashcan on the right), notebook server remain running in the background

Getting back the jupyter terminal:
- Start new terminal:
- Run: `screen -x jupyter`

## Basic git

Create a new branch:
- `git checkout -b <new branch name>`
Add file:
- `git add <filename>`
Commit changes:
- `git commit -m '<commit message>'`
Push (send to Github):
- `git push`
- First time it will reply with another command like:
- `git push --set-upstream origin <new branch name>`
- Copy-paste and run that instead
Create PR, approve it, squash-merge it, then return:
- `git checkout main` or `git checkout master`
- `git pull`

## Setting secret environment variables

These should absolutely _not_ be in the repository, instead:
- Go to `https://github.com/settings/codespaces`
- At `Codespaces secrets` click `New secret`
- Add name and value
- Select relevant repository
- Reload codespace (VSCode will also prompt you)

## Starting with poetry manually

This is already done in the repo, repeated here for reference:
- `pip install poetry`
- `poetry config virtualenvs.in-project true`
- `poetry init -n`
- `poetry env use python3.10`
- `poetry add black`
- `poetry install --no-root`
- `source .venv/bin/activate`
- Activate the environment in VSCode (like at startup)

Set up `black`:
Add this to `pyproject.toml` at the end:
```
[tool.black]
skip-string-normalization = true
line-length = 120
```

## New repository on Github

- Name: kebab case
- Select private
- Select add readme
- Select `python` for `.gitignore`
- Create repository
- Clone repository

Add repository to existing directory
- Name: kebab case
- Select private
- Don't add anything
- Create repository
- Follow the instructions on the next page

## Install pre-commit hooks

This is already done in the repo, repeated here for reference:
- `pip install pre-commit`
- `pre-commit install`
- Create `.pre-commit-config.yaml`
- Add relevant hooks, see current file for examples
- Regularly check for new versions
    - Go to hook repository
    - Dropdown at the "main" or "master" branch
    - Switch to tags
    - Update the `rev` field in the `YAML` file with the newest tag

Check link for details [https://pre-commit.com/](https://pre-commit.com/)
Check link for more hooks [https://pre-commit.com/hooks.html](https://pre-commit.com/hooks.html)

When you commit new files and everything is "Passed" or "Skipped" the commit is successful.
Otherwise "Failed" and a message for the reason, ruff will try and fix it if the `--fix` option is enabled. (It is for this repository.) Fix the remaining errors manually and commit again. The

## Live Share

- Click on the Arrow-Above-A-Sphere icon on the middle right
- Click "Share
- Click "Make Public"
- Share the link (it is already copied)
- On Live Share menu at the top click the person's name you want to follow (you will see the screen moving when they move theirs)
- Stop "Live Share": Hover over "SESSION DETAILS"
- Click the Stop Sign

## Misc

See memory and CPU usage:
- `htop`
