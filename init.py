#! /usr/bin/env python3
import os
import shutil
import sys

import requests
from dotenv import load_dotenv


def create_directory_for_day(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def download_input(day: str):
    url = f"https://adventofcode.com/2021/day/{day}/input"
    response = requests.get(
        url, headers={"Cookie": f"session={os.environ['COOKIE_SESSION']}"}
    )
    with open(f"day{day}/input.txt", "w") as file:
        file.write(response.text)


def copy_template(directory: str):
    if not os.path.exists(f"{directory}/main.py"):
        shutil.copyfile("main.py.template", f"{directory}/main.py")


def main(day: str):
    directory = f"day{day}"
    create_directory_for_day(directory)
    download_input(day)
    copy_template(directory)


if __name__ == "__main__":
    load_dotenv()
    args = sys.argv
    main(args[1])
