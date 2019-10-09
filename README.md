# Satellite+
### Project Overview
Satellite+ aims to use satellite imagery in combination with other relevant features to predict wildfire risk. The imagery data is curated from the NASA Landsat 8 satellite, a low orbit satellite equipped with 11 different detectors, including red, green, blue, and near infrared sensors, allowing a composite true color image to be created. These images are publicly available on AWS, and are searchable and downloadable through the use of sat-stac and sat-util, two python geospatial libraries. The goal of the project is to develop a machine learning architecture which can utilize a Convolutional Neural Network on the image data, and combine this with the results of passing features such as temperature, cloud coverage, etc. to a neural network, in an attempt to improve predictive capabilities compared to only using a CNN.
### Downloading Image Data
The first step of the project is to create a train, test, and validation set. To do so, Landsat 8 data was downloaded from AWS using the sat-util python library.<br>
This step of the process was done in a Spyder notebook using Anaconda to manage packages.<br>
To reproduce an environment needed to run the code to download images, open Anaconda Prompt and use the following commands:<br>
`conda create -n sat+ python=3.7 anaconda`<br>
`conda activate sat+`<br>
`conda install -n sat+ -c conda-forge sat-stac`<br>
`conda install -n sat+ -c conda-forge satsearch`<br>
