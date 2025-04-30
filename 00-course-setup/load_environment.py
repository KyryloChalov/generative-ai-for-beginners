from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the GITHUB_TOKEN variable
# github_token = os.getenv("GITHUB_TOKEN")

# Print the environment variables
print("Environment Variables:")
print("GITHUB_TOKEN:    ", os.getenv("GITHUB_TOKEN"))
print("GITHUB_REPO:     ", os.getenv("GITHUB_REPO"))
print("GITHUB_USERNAME: ", os.getenv("GITHUB_USERNAME"))
print("GITHUB_EMAIL:    ", os.getenv("GITHUB_EMAIL"))
print("GITHUB_BRANCH:   ", os.getenv("GITHUB_BRANCH"))
print("GITHUB_REPO_NAME:", os.getenv("GITHUB_REPO_NAME"))
print("GITHUB_REPO_URL: ", os.getenv("GITHUB_REPO_URL"))
print("GITHUB_REPO_PATH:", os.getenv("GITHUB_REPO_PATH"))
print("OPENAI_API_KEY:  ", os.getenv("OPENAI_API_KEY"))
print("MY_SECRET_WORLD:  ", os.getenv("MY_SECRET_WORLD"))


import requests

# Ваш персональний токен
token = os.getenv("GITHUB_TOKEN")
# token = "YOUR_PERSONAL_ACCESS_TOKEN"

# Запит до GitHub API
headers = {"Authorization": f"token {token}"}
response = requests.get("https://api.github.com/user/emails", headers=headers)


# Виведення результату
if response.status_code == 200:
    emails = response.json()
    for email in emails:
        print(f"Email: {email['email']}, Primary: {email['primary']}")
else:
    print(f"Error: {response.status_code}, {response.text}")


# import os
import subprocess

def get_git_info():
    try:
        # Отримати шлях до репозиторію
        repo_path = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()

        # Отримати назву репозиторію
        repo_name = os.path.basename(repo_path)

        # Отримати URL репозиторію
        repo_url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"], text=True
        ).strip()

        return {
            "GITHUB_REPO_NAME": repo_name,
            "GITHUB_REPO_URL": repo_url,
            "GITHUB_REPO_PATH": repo_path,
        }
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

# Виклик функції
git_info = get_git_info()
if git_info:
    print("GITHUB_REPO_NAME:", git_info["GITHUB_REPO_NAME"])
    print("GITHUB_REPO_URL:", git_info["GITHUB_REPO_URL"])
    print("GITHUB_REPO_PATH:", git_info["GITHUB_REPO_PATH"])
