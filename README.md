## Material for Python lesson

This is material for the Python lesson at the 2016-06-29-leeds
SWC workshop. 

In order to get these files run the following in a shell (pressing return
after each line):

    cd
    cd Desktop
    git clone https://github.com/andreww/2017-01-04-python1.git
    cd 2017-01-04-python1

Then start up a jupyter notebook:

    jupyter notebook

You should see a web browser start up with a notebook window.


### If people have python 2 installed

If you already have anaconda and python 2.7 installed you can add python3
as a new environment with the command 
`conda create -n python3 python=3.5 anaconda`. This installs python 3.5 
alongside whatever you already have installed.

In order to switch from python 2.7 to python 3.5 you can then run 
`source activate python3`. Anything installed after this point is part of 
the "python3" environment. 

To drop out of this environemnt and return to your default setup run source deactive. The current environment is local to the particular shell and the command under Windows drops source.
