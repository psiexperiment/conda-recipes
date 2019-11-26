# Overview

The process of creating an installer consists of three steps. The first two tend to be platform-agnostic unless you have code that needs to be compiled (e.g., Cython code): 

1. Build the source distribution and wheel that will be uploaded to PyPI
2. Build the conda package
3. Create the installer

The Python script, `packages/build.py`, facilitates the first two steps. The Python script, `installers/build.py` facilitates the last step.

# Packaging manually

First, make sure your package works. This is important if you've been running in developer mode:

	conda create -n <test_env_name> python=<python version>
	cd <source_dir>
	python setup.py install
	<commands to make sure it works>

Now, remove the env:

	conda remove -n <test_env_name> --all

You need a build environment:

	conda create -n build conda-build constructor anaconda-client

Packages in the environment:

- conda-build: builds conda packages
- constructor: creates installers
- anaconda-client: automatically uploads to your conda channel

First, build your PyPI distribution:

	cd <source_dir>
	python setup.py sdist bdist_wheel
	twine upload dist/*

At this point, it may be worthwhile to verify that installing from pip works by creating another test environment. Once you're satisfied everything works, build your conda package:

	cd <recipe_dir>
	conda-build <package_name>

Now, cleanup if desired:

	conda-build purge

# Installers

## Windows

You need a build environment:

	conda create -n build constructor

# Useful links

* [General instructions](https://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-packages/) on building conda packages.
* [Wiki for menuinst](https://github.com/ContinuumIO/menuinst/wiki).
