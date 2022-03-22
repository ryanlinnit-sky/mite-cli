import logging
import os
import subprocess
import venv

logger = logging.getLogger(__name__)


class EnvBuilderWithReqs(venv.EnvBuilder):
    def __init__(self, *args, **kwargs):
        self.project_dir = kwargs["project_dir"]
        del kwargs["project_dir"]

        super().__init__(*args, **kwargs)

    def post_setup(self, context):
        pip_install_requirements = [
            context.env_exe,
            "-m",
            "pip",
            "install",
            "-r",
            os.path.join(self.project_dir, "requirements.txt"),
        ]
        pip_install_proc = subprocess.run(pip_install_requirements, capture_output=True)
        logger.debug(pip_install_proc.stdout.decode("utf-8"))
