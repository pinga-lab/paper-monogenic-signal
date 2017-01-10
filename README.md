# paper-monogenic-signal

## About
Source code, data and manuscript for the article "The monogenic signal of potential-field data: A Python Implementation". Published in the GEOPHYSICS 
by [Marlon C. Hidalgo-Gato](http://lattes.cnpq.br/4057248251995225)
and [Valéria C. F. Barbosa](http://lattes.cnpq.br/0391036221142471)

This repository contains the manuscript, supplementary source code and data for a
paper about the open-source program *Monogenic*.

The *Monogenic* program is written in the Python 2.7/3.5 programming language.
**This program calculates the non-scale and the Poisson scale-space monogenic signal attributes based on the definitions introduced by [Hidalgo-Gato and Barbosa (2015)] (http://library.seg.org/doi/10.1190/geo2015-0025.1)**. 
In addition, we make available the Python script “synthetic.py” and the data “data.dat” to run our synthetic test example. 

You will find the source-code for *Monogenic* and the contents of this
repository at [software.seg.org](http://software.seg.org).
A "live" version of this repository is available at
[github.com/pinga-lab/paper-monogenic-signal](https://github.com/pinga-lab/paper-monogenic-signal).

## Abstract

We have presented the program *Monogenic*, a Python 2.7/3.5 package of two functions to calculate the non-scale and the Poisson scale-space monogenic signals of a 2D data. Both monogenic signal functions return the local amplitude, the local phase and the local orientation of a potential-field data or any kind of 2D array. Compared with the Poisson scale-space monogenic signal, the non-scale monogenic signal is easier to use because the former requires band-pass filtering the data whereas non-scale monogenic signal requires only the original data set. However, the Poisson scale-space monogenic signal yields a sharper image of boundaries of the geologic bodies than the non-scale monogenic signal. We demonstrated the use of the monogenic signal by applying it to a synthetic magnetic data. The Python script “synthetic.py” contains the algorithm to run our synthetic example. This example was run using specific Poisson scale-space parameters. However, the users can try different Poisson scale-space parameters for the same synthetic model. Finally, we stress that the application of the non-scale and the Poisson scale-space monogenic signals to enhance other geophysical data (e.g., seismic, GPR, gravity, multiple-component gravity gradiometry, magnetic gradient data) has no methodological obstacles.

## Cite us

The *Monogenic* program is a research software made by scientists. Your citations help us justify the effort that goes into developing open-source codes. 

If you use the *Monogenic* program in your research, please cite it in your publications as: 

    Hidalgo-Gato, M.C. and V. C. F. Barbosa (2017), The monogenic signal of potential-field data: A Python Implementation, Geophysics,  XX(X), XX–XX, DOI: XXXXXXXXXX.

Please,  also cite the main method [Hidalgo-Gato and Barbosa (2015)] (http://library.seg.org/doi/10.1190/geo2015-0025.1): 

     Hidalgo-Gato, M.C. and V. C. F. Barbosa (2015), Edge detection of potential-field sources using scale-space
        monogenic signal: Fundamental principles, Geophysics, 80(5), J27–J36, DOI: 10.1190/GEO2015-0025.1

## Content

**Phyton codes:**

- monogenic.py:
	General Python module containing the two functions to calculate the local
	amplitude, local phase and local orientation in the Poisson scale-space Monogenic
	Signal and the local amplitude, local phase and local orientation of the non-scale
	Monogenic Signal.

- synthetic.py:
	Python script to generate the published results. The script loads the total-field
	anomaly of a synthetic model from the file *data.dat* and calculates the local
	amplitude, local phase and local orientation of the non-scale and in the Poisson
	scale-space monogenic signals using the functions in *monogenic.py*

**Data files:**

- data.dat:
	Synthetic magnetic data generated using the Python packaged "Fatiando a Terra":
	http://fatiando.org/. This data is an example used in the current publication.


## Getting the files

To actually run the code, you will need to have the files on your machine. 
You can download the files "monogenic.py", "synthetic.py" and "data.dat" on your machine. 
Also, you can download a zip archive of this repository to get everything. 
Alternatively, you can download a zip archive of this repository at: [software.seg.org](http://software.seg.org).

## Installing the software

**Prerequisites:**

The Python program *Monogenic* v1.0 - "monogenic.py" requires the Python library "numpy" 
and the script "synthetic.py" requires the Python packages "numpy" and "matplotlib". 

The easiest way to get Python and all libraries installed is through the [Anaconda Python
distribution](http://continuum.io/downloads). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib

The program *Monogenic* and the script "synthetic.py" were tested on Windows and Linux
platforms using Python 2.7 and 3.5 as well.


## Running the files

Once Anaconda and the libraries are installed, download the files "monogenic.py",
"synthetic.py" and "data.dat" on your machine. Alternatively, you can download a zip archive of this
repository at: [software.seg.org](http://software.seg.org). Following, be sure that all files
are in the same directory. There are two easy ways to run the synthetic test: "synthetic.py"

1. Open the command prompt windows (terminal) and run the command:

	python synthetic.py

2. Open the Spyder program that comes with the Ananconda installation.  In the Spyder, open the example script "synthetic.py" and click in "play" inside the Spyder to execute it.

If everything runs ok, a set of figures shown in the publication will show up.

The  module "monogenic.py" can be imported to an interactive Python session or called from
an external Python module.  Their functionalities are documented using standard Python
docstrings.

The file "synthetic.py" is a Python-based command line script. By using this script, the
figures presented in the publication can be reproduced.

##License

All source code is made available under a BSD 3-clause license. You can freely use and modify the code, without warranty, so long as you provide attribution to the authors. See LICENSE.txt for the full license text.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE 
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
OF THE POSSIBILITY OF SUCH DAMAGE.


## Disclaimer

If you obtained this set of codes from the SEG (download from [software.seg.org](http://software.seg.org)) you must also agree to the following disclaimer: [software.seg.org](http://software.seg.org/disclaimer2.txt) 

