README for

SEG GEO-2016-XXXX, "The monogenic signal of potential-field data: A Python Implementation"

by Marlon C. Hidalgo-Gato (Observatório Nacional) & Valéria C. F. Barbosa (Observatório
Nacional) (2016)

This repository contains the manuscript and a collection of Python codes, synthetic data 
example and data file for a paper about the open-source software package Monogenic.The 
example data reproduces the results and figures shown in the SEG publication.The Monogenic
software is written in Python 2.7 and 3.5 programming language. To run the program,the 
numpy library is required. In addition, the matplotlib is required to run the script 
synthetic.py.

1 - Abstract
2 - Content
3 - Prerequisites
4 - Running the files
5 - License
6 - Disclaimer

================================================================================


1 - Abstract
----------------------
We present the codes to calculate the local amplitude, the local phase and the local
orientation of the non-scale and the Poisson scale-space monogenic signals of a potential-
field data in version 1.0 of the open-source program Monogenic. The monogenic vector of a
generic function is calculated in the wavenumber domain and then transformed back into the
space domain to find the monogenic signal attributes. We compare the use of the non-scale
monogenic signal with the Poisson scale-space monogenic signal in magnetic data. This
comparison shows that the latter can produce better result as an edge detection filter.
The implementation of the monogenic signal here presented can be used to enhance other
geophysical data such as seismic, GPR, gravity, multiple-component gravity gradiometry,
magnetic gradient data.


2 - Content
----------------------

Python codes

- monogenic.py
	General Python module containing the two functions to calculate the local
	amplitude, local phase and local orientation in the Poisson scale-space Monogenic
	Signal and the local amplitude, local phase and local orientation of the non-scale
	Monogenic Signal.

- synthetic.py
	Python script to generate the published results. The script loads the total-field
	anomaly of a synthetic model from the file "data.dat" and calculates the local
	amplitude, local phase and local orientation of the non-scale and in the Poisson
	scale-space monogenic signals using the functions in "monogenic.py"

Data files:

- data.dat
	Synthetic magnetic data generated using the Python packaged "Fatiando a Terra":
	http://fatiando.org/. This data is an example used in the current publication.


3 - Prerequisites
----------------------
The Python program Monogenic v1.0 - "monogenic.py" requires the Python library "numpy" 
and the script "synthetic.py" requires the Python packages "numpy" and "matplotlib". 
The easier way to get Python and all libraries installed is through the Anaconda Python 
distribution (http://continuum.io/downloads). After installed Anaconda, install the libraries 
by running the following command in your terminal:

	conda install numpy matplotlib

The program Monogenic and the script "synthetic.py" were tested on Windows and Linux
platforms using Python 2.7 and 3.5 as well.


4 - Running the files
----------------------
After Anaconda and the libraries are installed, download the files "monogenic.py",
"synthetic.py" and "data.dat" on your machine. You can download a zip archive of this
repository at: software.seg.org(http://software.seg.org). Following, be sure that all files
are in the same directory. There are two easy ways to run the synthetic test "synthetic.py"

1. Open the command prompt windows (terminal) and run the command:

	python synthetic.py

2. Open the Spyder program that comes with the Ananconda installation.  In the Spyder, open
the example script "synthetic.py" and click in "play" inside the Spyder to execute it.

If everything runs ok, a set of figures shown in the publication will show up.

The  module "monogenic.py" can be imported to an interactive Python session or called from
an external Python module.  Their functionalities are documented using standard Python
docstrings.

The file "synthetic.py" is a Python-based command line script. By using this script, the
figures presented in the publication can be reproduced.


5 - License
----------------------
The following legal note is restricted solely to the content of the named files. It cannot
overrule licenses from the Python standard distribution modules, which are imported and
used therein.

The "monogenic.py" and "synthetic.py" files are distributed under the following license
agreement:

Copyright (c) 2016, Marlon C. Hidalgo-Gato (Observatório Nacional) & Valéria C. F. Barbosa
(Observatório Nacional)

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used
to endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE 
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
OF THE POSSIBILITY OF SUCH DAMAGE.


6 - Disclaimer
----------------------
If you obtained this set of codes from the SEG (download from software.seg.org or
otherwise), you must also agree to the following disclaimer:

http://software.seg.org/disclaimer2.txt
