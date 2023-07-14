pip install poetry
poetry config virtualenvs.in-project true
poetry install --no-root
poetry run pre-commit install
sudo apt update
sudo apt install -y screen
echo $'set completion-ignore-case on\nset show-all-if-ambiguous off\nTAB: menu-complete' > ~/.inputrc
cat .devcontainer/aliases >> ~/.bashrc
