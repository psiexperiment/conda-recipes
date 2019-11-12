You need a build environment:

	conda create -n build conda-build constructor anaconda-client

Packages in the environment:

- conda-build: builds conda packages
- constructor: creates installers
- anaconda-client: automatically uploads to your conda channel

First, build your PyPI distribution:

	cd <source_dir>
	python setup.py sdist bdist_wheel
	twinde upload dist/*

Now, build your conda package:

	cd <recipe_dir>
	conda-build <package_name>

[General instructions](https://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-packages/) on building conda packages.
