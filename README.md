# searchmarcrecord

searchmarcrecord is a Python3 program that searches a single MARC record via a given id (controlfield 001) in a given (binary) MARC records file and writes it into a single (binary) MARC file

## Requirements

* [argparse](https://docs.python.org/3/library/argparse.html#module-argparse)
* [pymarc](https://github.com/edsu/pymarc)

## Run

* clone this git repo or just download the [searchmarcrecord.py](searchmarcrecord/searchmarcrecord.py) file
* run ./searchmarcrecord.py
* for a hackish way to use searchmarcrecord system-wide, copy to /usr/local/bin

### Install system-wide via pip

* via pip:
    ```
    sudo -H pip3 install --upgrade [ABSOLUTE PATH TO YOUR LOCAL GIT REPOSITORY OF SEARCHMARCRECORD]
    ```
    (which provides you ```searchmarcrecord``` as a system-wide commandline command)

## Usage

    searchmarcrecord [-h] -id ID -input-file INPUT_FILE -output-file
                            OUTPUT_FILE

required arguments:

    -id ID                              the record id (default: None)
    -input-file INPUT_FILE              the input MARC file (with multiple records) (default: None)
    -output-file OUTPUT_FILE            the output MARC file (with one found record) (default: None)

optional arguments:

    -h, --help                          show this help message and exit
    -continue-search-after-first-hit    continues search after first hit, i.e., also determines whether multiple records for the given id occur in the input MARC records file (default: False)

### Usage example

    searchmarcrecord -id [MARC record ID (IN CONTROL FIELD 001)] -input-file [INPUT BINARY MARC RECORDS FILE] -output-file [OUTPUT BINARY MARC RECORD FILE (CONTAINING THE FOUND MARC RECORD)]
