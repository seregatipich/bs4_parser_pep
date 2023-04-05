[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Practicum.Yandex](https://img.shields.io/badge/-Practicum.Yandex-464646?style=flat&logo=Practicum.Yandex&logoColor=56C0C0&color=008080)](https://practicum.yandex.ru/)
# OrbitCounter
## Description
Parser of information about Python from **https://docs.python.org/3/** and **https://peps.python.org/**

## Installation

To run this script on your computer, follow these steps:

1. Clone the repository using the command
```
git clone git@github.com:seregatipich/bs4_parser_pep.git
``` 
2. Navigate to the application directory using the command
```
cd bs4_parser_pep
``` 
3. Create virtual environment
```
python -m venv venv
```
4. Activate virtual environment
```
source venv/Scripts/activate
```
or
```
source venv/bin/activate
```
5. Install the dependencies from requirements.txt
```
pip install -r requirements.txt
```

## Usage

1. change directory to src
```
cd src/
```
### run the file main.py by selecting the desired parser and the arguments (listed below)
```
python main.py [parser option] [arguments]
```
### built-in parsers
- whats-new   
A parser parsing whats-new in python.
```
python main.py whats-new [arguments]
```
- latest_versions
A parser that lists the versions of python and links to its documentation.
```
python main.py latest-versions [arguments]
```
- download   
A parser that downloads a zip archive with python documentation in pdf format.
```
python main.py download [arguments]
```
- pep
A parser listing the statuses of pep documents
and the number of documents in each status. 
```
python main.py pep [arguments]
```
### Arguments
It is possible to specify arguments to change the way the program works:   
-h, --help
General information about the commands.
```
python main.py -h
```
-c, --clear-cache
Clearing the cache before parsing.
```
python main.py [parser variant] -c
```
-o {pretty,file}, -output {pretty,file}   
More ways to output data   
pretty - prints the data on the command line in a table   
file - saves information in csv format in folder ./results/
```
python main.py [parser variant] -o file
```

## License

This project is licensed under the MIT License. You are free to use it in your projects.