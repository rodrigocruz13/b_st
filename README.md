![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)
# BS - Estimator

:rocket: Star us on GitHub  *it helps*! :rocket:

![BS - Estimator](https://i.imgur.com/uHg2Aww.png)


**BS - Estimator** is a simple tool to quote the cost of U units according to the data set by the users for 4 ranges of data
* R0: 5 ≥ u > 50
* R1: 50 ≥ u > 500
* R2: 500 ≥ u > 5000
* R3: 5000 ≥ u ≥ 50000

For each range it will create a linear equation that will simulate the behaviour of the cost function c(u) and that will allow to estimate the desired value.

![BS - Estimator](https://i.imgur.com/twoaDxB.jpg)


## Installation
If you want to install ** Estimator**, the source [files are here]([https://github.com/rodrigocruz13/b_st] (https://github.com/rodrigocruz13/b_st)). You can download them, compile then and install it with no further permission.

* Download or copy this repository
* Under a Pyhton 3.7 enviroment run the command ./main.py
* It will start the application 


## Usage

- `In the local folder run the main file for starting: ./main.py`
- `Once you are asked type any valid ID and hit enter`
- `Type the number of units you want to quote`
- `The results then are displayed`
- `If you want to quit type Q or q`

### Example Usage
```
- $           In the prompt type: ./main.py and hit enter`
```


### Screenshots

![1](https://i.imgur.com/1zP7S3j.jpg)
![2](https://i.imgur.com/tJvPFi3.jpg)
![3](https://i.imgur.com/KTCYWfP.jpg)
![4](https://i.imgur.com/7M4Lp15.jpg)
![5](https://i.imgur.com/B18mbuI.jpg)
![6](https://i.imgur.com/hexWwXY.jpg)



### Current features
* Load the out.txt file
* Calculates the slope (m) and y intersection (b) for each user and range 
* Generates a quote of U units for user ID
* Shows 15 cheapests cuotation for that number of units u. 


## Files

This is the list of the files required to compile and create the shell.

| # | Type | File   | Description |
| -- |------  |  -----------  | ----------- |
|1|Doc| README.md |Readme file|
|2|Doc| out.txt |Txt file with the original information|
|3|Doc| Estimate.xlsx |Excel file with quotes for windows enviroments|
|4|py file|main.py|Main file. Generates the loop for reading & showing info|
|5|py file|calculate.py|It constains all the methods and functions|


## Compiling process
No need to compile

## License

This program is licensed under the terms of the GPL Open Source license and is available for free.
This document is only for usage of Bunny Studios(1.0)


## Links & Tech
Operating systems (OS)
* [Linux](https://www.linux.org)
* [Ubuntu 14.04](http://releases.ubuntu.com/14.04/)
* [Python](https://www.python.org/)


Editors
* [vi basic commands](https://www.ccsf.edu/Pub/Fac/vi.html)
* [vi unix editor](https://sourceforge.net/projects/ex-vi/)
* [Emacs](https://www.gnu.org/software/emacs/)

School
* [Holberton School Bogotá](https://www.holbertonschool.com/co)

## About


- A Full Stack Engineer is an engineer who is able to understand and work on any level of a software
application: starting from the hardware, system and network, to the security and scalability. Our students
will be familiar with software architecture, data modeling, coding, testing, shipping, user experience,
design, project management, marketing,  While one cant be an expert in all of the layers, students
will have the foundation required to be able to navigate any of those.
It also means that our students will be able to interact with low and high level technologies: for code,
it will mean from assembly to the latest programming framework. For system infrastructure, it will mean
creating your infrastructure from scratch, to using a ready-to-go Cloud solution.

Kris Bredemeier - Holberton School (SF)


## Authors

 Photo  | Name | Email |
 -----  | ---- | ----- |
![Rodrigo](https://i.imgur.com/C2LoErX.jpg)| Rodrigo Cruz | rodrigocruzayala@gmail.com


 Github | linkedin |
 ---- | -----  |
 https://github.com/rodrigocruz13 | https://www.linkedin.com/in/rodrigo-cruz-devops/

Yep ... just me 


#
> SPECIAL THANKS
> To all our peers, mentors, and staff from Holberton School in San Francisco, New Heaven and Bogota.
>Every day is a journey for new discoveries, a route that you walk alone but do not feel that way, because
without your time, help and dedication to try to explain those issues that we do not understand, none of
this would have been possible.

![logo](https://i.imgur.com/9ONYhd0.png)
