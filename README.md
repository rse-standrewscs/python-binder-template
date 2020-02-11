[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/rse-standrewscs/python-binder-template/master)
[![Azure Notebooks](https://notebooks.azure.com/launch.png)](https://notebooks.azure.com/alex-konovalov/libraries/python-binder-template)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3662238.svg)](https://doi.org/10.5281/zenodo.3662238)

# python-binder-template

Template for publishing reproducible experiments in Python Jupyter notebooks runnable on Binder and Azure Notebooks

1. Create a new repository for your project, navigate to the directory 
with a clone of your repository, and start to add new content to your
repository, copying it from the template and modifying as appropriate.

Alternatively, you can first import this template into your GitHub account 
using GitHub importer as explained at
<https://help.github.com/en/github/importing-your-projects-to-github/importing-a-repository-with-github-importer>)
and then start to modify it as appropriate.

In addition to working with a local clone of your repository, you can
also use GitHub web interface.

2. You may follow the structure of this template:

- `data` directory for data files

- `code` directory for code

- `notebooks` directory for Jupyter notebooks

- `README.md` file for a brief description of your project, documented
dependencies, installation and usage instructions, etc.

- `LICENSE` file with copyright information and license details

- `requirements.txt` with specified dependencies of your project

- `postBuild` with additional steps needed after installation

3. Update URL for the Binder badge in the README file above. 
After you commit and push these changes, go to GitHub and click on the
Binder badge. A message `Loading repository: ...` will be displayed, followed 
by a non-interactive preview. Please be patient, since it may take a while, 
depending on the current load on Binder. You can click on "Show" to monitor 
the progress of the build in the build logs. When the server will be ready, 
you will see the main Jupyter screen with a file browser. Navigate to the
`notebooks` directory and open a Jupyter notebook (or create a new one).

In the Jupyter notebook you can now combine code, input and output, and a text
narrative to demonstrate your code and explain how it works. Please note 
that the notebook on Binder will not be preserved after the window will be 
closed, but you are able to download it via "File" -> "Download as" -> 
"Notebook (.ipynb) and then put it under version control, commit and push 
to GitHub, to make it available when you will launch the project on Binder
next time. Alternatively, you can install Python and Jupyter on your
computer and work with Jupyter notebooks locally.

For further information about Jupyter, see
https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/index.html.

4. When your project is ready for the release, make it citable by archiving it
(with assigning a DOI) on the data archiving tool Zenodo (https://zenodo.org/), 
following instructions at https://guides.github.com/activities/citable-code/.
