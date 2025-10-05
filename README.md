# MonteCarlo Request Generation For YH Samples

This repository has three scripts that are all written for creating requests for YH Samples:

    1. ```Checker```: This code is used for finding out what all combinations of YH samples are missing. 
        - First download the list of datasets from Data Aggregation System: https://cmsweb.cern.ch/das/
        - Copy the list of existing datasets in a txt file. Then run the checker.py code with the list as input.
        - This will print out all the missing combinations of MX-MY
    
    2.  ```generator_from_list.py```: This code will create a csv file containing the names of the dataset, path of pythia fragment, number of events requested, gridpacks, etc.
        - This code takes a list of missing combinations and searches recursively in a directory containing all the gridpacks. 

    3. ```generator_from_arrays.py```: This code will create a csv file containing the names of the dataset, path of pythia fragmen,t number of events requested, gridpacks,      etc.   
        - This code takes arrays of missing combinations and searches recursively in a directory containing all the gridpacks. 
