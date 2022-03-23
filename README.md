# Mite CLI

A command line tool to create a new [mite](https://github.com/sky-uk/mite/) project. 

## Installation

```bash
pip install mite-cli
```

## Usage

```
Usage:
    mite-cli new <project_dir> [options]

Options:
    --log-level=LEVEL       Set logger level: DEBUG, INFO, WARNING, ERROR, CRITICAL [default: INFO]
    -e --createvenv         Create a python virtual environment
```

### Create new mite project

```bash
mite-cli new my_project_dir
```

Create a new project and a virtual environment setup

```bash
mite-cli new my_project_dir -e
```

You can activate your new virtual environment with `source ~/.virtualenvs/my_project_dir/bin/activate`
This gives you access to the mockserver, mite, etc.

To run your first journey, open a terminal, activate your virtual environment and run `mockserver`.
Open a second terminal, activate your virtual environment and run the following command:

```bash
mite journey test application.journeys:get_url1_journey --config application.config:config
```

or a scenario

```bash
mite scenario test application.scenarios:quick_scenario --config application.config:config
```

When you check your `mockserver` output, you can see the endpoints getting hit multiple times.
