#!/usr/bin/env python

import os
import re

import httpx


def get_package_latest_version(package_name: str) -> str:
    """Get the latest stable version of a PyPI package."""
    response = httpx.get(f"https://pypi.org/pypi/{package_name}/json")
    latest_version: str = response.json()["info"]["version"]
    return latest_version


# --- Update pre-commit config ---#
with open(".pre-commit-config.yaml") as file:
    text = file.read()

for match in re.findall(r"[\w-]+==[\d\w.]+", text):
    package_name, current_version = match.split("==")
    latest_version = get_package_latest_version(package_name)
    text = re.sub(
        f"{package_name}=={current_version}", f"{package_name}=={latest_version}", text
    )

with open(".pre-commit-config.yaml", "w") as file:
    file.write(text)


# --- Update poetry dependencies ---#
os.system("poetry update")
os.system("poetry show -lo")
