import subprocess
import os


if "{{cookiecutter.__tooling_commitmsg_linter[cookiecutter.commitmsg_linter]}}" != "gitlint":
    if os.path.exists(".gitlint"):
        os.remove(".gitlint")


if "generate-changelog" not in {{cookiecutter.__tooling_packages[cookiecutter.tooling_environment]}}:
    if os.path.exists(".changelog-config.yaml"):
        os.remove(".changelog-config.yaml")

if "commitizen" not in {{cookiecutter.__tooling_packages[cookiecutter.tooling_environment]}}:
    if os.path.exists("changelog_commitizen-template.md.j2"):
        os.remove("changelog_commitizen-template.md.j2")


try:
    subprocess.call(['git', 'init', '--initial-branch', 'main'])
    subprocess.call(['git', 'commit', '--allow-empty', '-m', 'Root commit'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.project_repo }}'])
    subprocess.call(['git', 'add', '*'])
    if {{cookiecutter.initial_commit}}:
        subprocess.call(['git', 'commit', '-m', 'Initial commit from Cookiecutter template'])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print("Make sure to manually set up a git repository which is necessary for `hatch-vcs`")
