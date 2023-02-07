# PasteBin.com Command Line Interface
---
A python command line interface for pastebin.com

## Installation
First make sure you have python installed on your system.

Then install the required packages
```
pip install requests
```

Then get your api key from [here](https://pastebin.com/doc_api#1)
That's it!

## Help message
```
usage: pastein.py [-h] [-k API_KEY] [-f FILE] [-c PASTE] [--version]

Pastebin.com Command Line Interface 

options:
 -h, --help show this help message and exit
 -k API_KEY, --api-key API_KEY 
                       your api key from http://pastebin.com/doc_api#1
 -f FILE, --file FILE the file that you want to paste 
 -c PASTE, --get PASTE reads the paste from paste code.
 --version shows the version number
```
## Examples
To paste a code:


```
python3 pastein.py -k <<whatever your api key is>> -f test.txt
```


To get a code:


```
python3 pastein.py -c bVygpfYz
````


## Notes
+ Dirty and quick project
+ But still usable
