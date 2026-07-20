from collections import defaultdict
import json
import os
from pathlib import Path
import subprocess
from typing import Dict
from dockerfile_parse import DockerfileParser


def main():
    registry = {
        "images": [],
        "packageIndex": defaultdict(dict),
    }

    for folder_name in os.listdir("."):
        folder_path = os.path.join(".", folder_name)
        dockerfile_path = Path(os.path.join(folder_path, "Dockerfile"))

        if os.path.isdir(folder_path) and os.path.exists(dockerfile_path):
            image_data = parse_image(dockerfile_path)
            registry["images"].append(image_data)

            for name, version in image_data.get("packages", {}).items():
                registry["packageIndex"][name][image_data["tag"]] = version

    with open("registry.json", "w") as f:
        json.dump(registry, f, indent=2)


def parse_image(path: Path) -> Dict:
    folder = path.parent
    tag = f"sciwin/{folder.name}"

    print(f"Building {tag}...")

    subprocess.run(
        [
            "docker",
            "build",
            "-t",
            tag,
            str(folder),
        ],
        check=True,
    )

    with open(path, "r") as f:
        content = f.read()

    dfp = DockerfileParser()
    dfp.content = content

    lang = dfp.labels.get("net.fairagro.sciwin.lang")
    langVersion = dfp.labels.get("net.fairagro.sciwin.version")

    if lang == "r":
        packages = get_r_deps(tag)
    elif lang == "python":
        packages = get_python_deps(tag)
    else:
        return {"tag": tag}

    packages = {pkg["name"]: pkg["version"] for pkg in packages}
    metadata = inspect_image(tag)

    return {
        "tag": tag,
        "lang": lang,
        "version": langVersion,
        **metadata,
        "packages": packages,
    }


def get_r_deps(tag: str):
    cmd = [
        "docker",
        "run",
        "--rm",
        tag,
        "Rscript",
        "-e",
        """
        ip <- installed.packages()[, c("Package", "Version")]
        cat(jsonlite::toJSON(
            data.frame(
                name = ip[, "Package"],
                version = ip[, "Version"]
            ),
            dataframe = "rows",
            auto_unbox = TRUE
        ))
        """,
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )

    return json.loads(result.stdout)


def get_python_deps(tag: str):
    cmd = ["docker", "run", "--rm", tag, "python", "-m", "pip", "list", "--format=json"]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )

    return json.loads(result.stdout)


def inspect_image(tag: str) -> dict:
    result = subprocess.run(
        ["docker", "image", "inspect", tag],
        capture_output=True,
        text=True,
        check=True,
    )

    image = json.loads(result.stdout)[0]

    return {
        "digest": image["Id"],
        "size": image["Size"],
        "created": image["Created"],
        "architecture": image["Architecture"],
        "os": image["Os"],
    }


if __name__ == "__main__":
    main()
