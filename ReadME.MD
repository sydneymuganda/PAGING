<figure>
    <img src="logo.jpg"
         width="800" height="300">
</figure>

# MGNSYD001~Sydney Muganda  CSC3002F OS1 ASSIGNMENT


![badge](https://img.shields.io/badge/license-Apache-blue.svg)
![badge](https://img.shields.io/badge/LinkedIn-IN%20-blue)

<!-- TABLE OF CONTENTS -->

## Table of Contents
* [About The Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project
a python program that implements the FIFO , LRU and OPTIMAL page replacement algorithms


<!-- GETTING STARTED -->
## Built With
python

<!-- GETTING STARTED -->
## Getting Started
1. download the zip file and save contents onto pc
2. you must open terminal
3. cd into directory where python script is saved on your pc
4. type python paging.py [number of frames] /n 
5. after type in the size of the page reference string you desire to be randomly generated

To get a local copy up and running follow these simple steps.

<!-- Prerequisites -->
used the [textbook](https://os.ecci.ucr.ac.cr/slides/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf)  plus  [this website to validate algorithms](https://solver.assistedcoding.eu/page_replacement)

### Installation

1. Clone the repo on github
   shh to nightmare
   git clone repo

   or just download zip file
   



<!-- USAGE EXAMPLES -->
### Usage
contains functions used to calculate the page faults for each  the page replacement algorithms.
-Therefore we first type in terminal :
    **python paging.py [number of frames]**  
- then input a size of desired page reference string
- then the output will be:
    **FIFO x faults**
    **LRU y faults** 
    **OPTIMAL z faults** 
- followed by output of generated string

### **To test individual functions**==
```python
import paging

#returns FIFO 5 page faults.
print('FIFO', paging.FIFO(8, [3, 3, 4, 6, 8, 4, 4, 0]), 'page faults.')
#returns LRU 5 page faults.
print('LRU', paging.LRU(4, [3, 3, 4, 6, 8, 4, 4, 0]), 'page faults.')
#returns OPT 5 page faults.
print('OPT', paging.OPT(4, [3, 3, 4, 6, 8, 4, 4, 0]), 'page faults.')
```

### **To test overall code on terminal**

```console
PS C:\Users\sydne\Desktop\csc3002f\OS1> python paging.py 4 
enter size of reference string:
8

FIFO 5 page faults.
LRU 5 page faults.
OPT 5 page faults.

The page reference string generated:
[3, 3, 4, 6, 8, 4, 4, 0]
```
<!-- ROAD MAP -->



<!-- CONTACT -->
## Contact

Feel free to reach out to me with questions comments, or concerns at one of the ways below.

Git Hub: [sydneymuganda](https://github.com/sydneymuganda)

Email: mgnsyd001@myuct.ac.za

LinkedIn Link: [sydney muganda](https://www.linkedin.com/in/sydney-muganda-91b2171aa/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BVo5VRHMRTCOmcGdoSwagWQ%3D%3D)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
just me MGNSYD001