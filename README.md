# Multi-period tutorial
A warm welcome! This is a tutorial for using the new multi-period (investment) modelling functionality from oemof.solph `v0.5.1` (upcoming).

## Installation
### Clone the repository
To get started, first of all clone the repository.

Navigate to your folder of choice (use command `cd` to change between directories) and then execute

`git clone https://github.com/jokochems/multiperiod_tutorial.git`

Now you have all the required files on your local machine.

### Install dependencies
To get started, you first need to have the required (python) dependencies. To do so, you can either use the
`environment.yml` file, in case you are using conda, mamba or another package manager, or directly install from `requirements.txt` file.

**Using conda or a similar package manager (recommended)**
To create an environment using conda, mamba, etc., navigate to the location where you have cloned the content and then execute:

`conda env create -f environment.yml`

This will collect all the dependencies from the YAML file and install them to a new environment called `multi_period_oemof`.
If you don't have python 3.9 at hand, change the python version in the `environment.yml` file.

To activate this environment, execute:

`conda activate multi_period_oemof`

**Using pip**
To simply install with pip, execute

`pip install requirements.txt`

In both cases, now you should have all the required dependencies.

**Installing a solver**:
Make sure you have a solver installed that is compatible with oemof.solph resp. pyomo! Please refer to the [oemof.solph README](https://github.com/oemof/oemof-solph#installing-a-solver) on this.
You can test your installation by running `oemof_installation_test` on a console which should inform you that at least one solver is working with oemof.solph.

## Usage
Basically, all you need is within one ipython jupyter notebook.
To get started, after activating your environment type

`jupyter lab`

which will open jupyterlab in the browser that is configured to do so. Now you can browse on the left hand side and open the file

[`multi_period_tutorial.ipynb`](https://github.com/jokochems/multiperiod_tutorial/blob/main/multi_period_tutorial.ipynb)

from the top level of the repository.

Feel free to use any IDE (e.g. VSCode, PyCharm professional) instead that offers ipynb support.

You are all set. Let's go! :-)

## Troubleshooting
In case, anything does not work out, please let me know. We'll probably have some time in the tutorial to address issues.

In case you get stuck, there is always the option to just listen and follow along on your computer by looking at a version of the jupyter notebook where I included all the cell outputs.

You can find this version here:

[`multi_period_tutorial-all-outputs.ipynb`](https://github.com/jokochems/multiperiod_tutorial/blob/main/multi_period_tutorial-all-outputs.ipynb)
