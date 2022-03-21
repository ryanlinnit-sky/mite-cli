import logging
import os
import pathlib
from shutil import rmtree

from git import Repo

logger = logging.getLogger(__name__)


def new_project(project_dir: str) -> None:
    if os.path.isdir(project_dir):
        logger.error("Directory already exists, please choose a new directory path")
        return

    project_name = pathlib.Path(project_dir).name

    Repo.clone_from("https://github.com/ryanlinnit-sky/mite-demo.git", project_dir)

    write_setup(os.path.join(project_dir, "setup.cfg"), project_name)

    rmtree(os.path.join(project_dir, ".git"))

    r = Repo.init(project_dir)
    r.index.add(["*", ".*"])
    r.index.commit("initial commit")


def write_setup(setup_cfg_filepath: str, project_name: str) -> None:
    with open(setup_cfg_filepath, "r") as fp:
        setup_cfg = fp.readlines()

    for index, line in enumerate(setup_cfg):
        if "mite-demo" in line:
            setup_cfg[index] = line.replace("mite-demo", project_name)

    with open(setup_cfg_filepath, "w") as fp:
        fp.writelines(setup_cfg)
