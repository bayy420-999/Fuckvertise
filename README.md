# Fuckvertise
Fuck that annoying shortlink! Powered by `bypass.vip`

Supported links:
[Check their website](https://bypass.vip/)

## Installation 

- Download and go to project folder
```
$ git clone https://github.com/bayy420-999/Fuckvertise.git
$ cd Fuckvertise
```

- Install program
```
$ pip install .
```

## How to use

- Command Line Interface

Usage: 

```
usage: Fuckvertise [-h] [-b BATCH] [-o OUTPUT_FILE] [-v]
                   [urls ...]

Fuckvertise CLI program

positional arguments:
  urls                  List of url

options:
  -h, --help            show this help message and exit
  -b BATCH, --batch BATCH
                        Provide `.txt` file that contains
                        list of url
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Provide output file
  -v, --verbose         For verbosity reason
```

Example:
```
$ Fuckvertise https://linkvertise.com/258316/your-of-folder-here-yzs4s/1 -v
$ Fuckvertise -b batch.txt -o result1.txt -v
```

- As API
```
Class:
`Fuckvertise`     -> Argument: `verbose` (optional)
                  -> Use     : `bypass.vip` wrapper API

Method:
`load_from_txt`   -> Argument: `filename` (required)
                  -> Use     : load shortlink from txt file

`get_direct_link` -> Argument: `datas` (can be optional if you load shortlink from txt file)
                  -> Use     : get direct link

`save_results`    -> Argument: `filename` (required)
                  -> Use     : save result from `get_direct_link`
```

Example:
```
from Fuckvertise import Fuckvertise

urls = ['https://linkvertise.com/258316/your-of-folder-here-yzs4s/1']

fv = Fuckvertise(verbose = True)
fv.get_direct_link(urls)
fv.save_results('result.txt')
```
