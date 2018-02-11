# P3D3

## Purpose

The purpose of this Python package is to provide easy & extensive access to the D3 library from within a Python 3 Jupyter notebook.

It enables to code a generic D3 visualization in a separate .js file and load it from Python with a Pandas dataframe sent as input.

The package is on purpose very lightweight, to enable easy forking & publishing from/to bl.ocks.org, or any other kind of standalone deployment.

## Installation

`pip install p3d3`

or download repository from Github and `python setup.py install`

## Usage

Run:
```python
import p3d3
p3d3.init()
```

to download & initialize the d3 and Vega engines. Then you can use the functions `p3d3.p3d3()` and `p3d3.vegalite()`

Examples on how to use P3D3 are available in the `examples/` folder.

## Contribution

This package is in its early stages. You are very welcome to report issues & propose pull requests to improve it.
