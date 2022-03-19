#!/usr/bin/env python

"""mite-cli

Usage:
    mite-cli new <project_dir> [options]

Options:
    --log-level=LEVEL       Set logger level: DEBUG, INFO, WARNING, ERROR, CRITICAL [default: INFO]

"""  # noqa: E501

import logging

from docopt import docopt

logger = logging.getLogger(__name__)


def setup_logging(opts):
    logging.basicConfig(
        level=opts["--log-level"],
        format="[%(asctime)s] <%(levelname)s> [%(name)s] %(message)s",
        force=True,
    )


def main():
    opts = docopt(__doc__)
    setup_logging(opts)


if __name__ == "__main__":
    main()
