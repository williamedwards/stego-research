Steganography Research Code
Created by William Edwards

Dependencies: Python 2, numpy, scipy, pywt

Installation:
Ensure all dependcies are installed. On a Debian/Ubuntu based linux system this can be done by running the following command as root:

apt-get install python python-numpy python-scipy python-pwyt

Create a subdirectory to contain the python code and clone this repository to that location.  Then, in the parent directory create images/li_photograph.  Download the following archive:
http://www.stat.psu.edu/~jiali/li_photograph.tar
Then extract it to the li_photograph directory.

Running:
To generate all data for the final phase of experimentation. Execute the command
python finalstats.py

A data directory will be created in the parent directory and all results will be written there. This will take some time to complete.
