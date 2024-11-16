import requests
import base64


def fetch_pr_files(repo_url, pr_number, github_token=None):
    """Fetches the files changed in a pull request."""
    owner, repo = repo_url.split("/")[-2:]
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {"Authorization": f"token {github_token}"} if github_token else {}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def fetch_file_content(repo_url, file_path, github_token=None):
    """Fetches the raw content of a file from the repository."""
    owner, repo = repo_url.split("/")[-2:]
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization": f"token {github_token}"} if github_token else {}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()
    return base64.b64decode(content["content"]).decode()



