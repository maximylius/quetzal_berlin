# quetzal Berlin
This open source project is a macroscopic passenger transport model for the region of Germany. It supports research aimed at designing an integrated, renewable energy system with mobility behaviour insights.

It uses the quetzal transport modelling framework: https://github.com/systragroup/quetzal

The method is oriented towards classical four-step transport modelling. Focus lies on mode choice by using a purpose-segmented logit model.

This project was developed for the course Operations Research - Modeling Sustainable Mobility (OR-MSM) at TU Berlin.

## Structure

The directory structure is straight-forward:
> quetzal_berlin/</br>
> -- input/</br>
> -- --  transport_stats/</br>
> -- --  ungenutzt/</br>
> -- --  validation/</br>
> -- --  zone_stats/</br>
> -- --  zones/</br> 
> -- literatur/</br>
> -- model/</br>
> -- -- network/</br> 
> -- -- zones/</br> 
> -- notebooks/</br>
> -- outputs/</br>
> -- --  plots/</br> 

While input and output data as well as (temporary) model files are stored in seperate folders, Jupyter Notebooks contain all data management and modelling. Briefly, they are structured as follows (`X` as wildcard):
*  00_environment_test
*  00_launcher.ipynb
*  01_zone_creation.ipynb
*  02_OSM_POIs.ipynb
*  03_network_creation.ipynb
*  04_05_OD-LoS-stack_Four-Steps.ipynb

## Installation

1. Create a virtual environment for quetzal models: Clone the quetzal package into a local folder and create a virtual environment as described here *[1]*: https://github.com/systragroup/quetzal
2. Activate your quetzal environment, if not done yet
3. Clone this repository into a local folder: In your terminal, navigate to the position where you want to store the code. Type `git clone <this repo's URL>`. Navigate into the folder `quetzal_berlin`.
4. Download static input files from Zenodo *[2]* into a folder named `input_static/` within the `quetzal_germany` repository (see Structure): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5659679.svg)](https://doi.org/10.5281/zenodo.5659679)
5. Open the local project in Jupyter Notebook (in your terminal type `jupyter notebook`) and start running the notebooks

You can test your virtual environment by running the `00_environment_test` notebook.

*[1]*: If you face problems importing geopandas, consider uninstalling package `rtree` and reinstalling a version up to 0.9.3 (`conda install -c conda-forge rtree=0.9.3`) or uninstalling the whole environment and reinstalling it with the requirements file posted in this [issue](https://github.com/systragroup/quetzal/issues/45). If you have problems with `numba` or others, consider fetching an earlier, more stable, version of `quetzal` with this commit: `git checkout 1126c05c8366e871893b85a55bd57d9d20e7d1d0`
*[2]*: If you wonder why these files are not hosted in this very repository: Large input data files require different handling and some of them also require a license different to this repo's licensing.
