# Sylo - Syllogism Solver

A command line tool which determines the validity of a given syllogism.

## Dependencies

* [Python 3](https://www.python.org/)
* [CLIPS](http://www.clipsrules.net/)
* [Inflect (python package)](https://pypi.org/project/inflect/)

## Usage

Sylo can be run either interactively or as a batch program.

To run in interactive mode run
```
sylo.py
```
and give the program the number of premises, then the premises one by one and lastly the conclusion.

To run it as a batch program use
```
sylo.py <path-to-file-containing-syllogism>
```
The file needs to be in the same format described previously with each input being on a separate line.

For examples look in the [exs](/exs) directory.
