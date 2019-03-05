# PyQuad
![First Project](https://img.shields.io/badge/First-Project-brightgreen.svg) ![MIT License](https://badges.frapsoft.com/os/mit/mit.png?v=103)  
A cli that gives you all the information on a quadratic equation given in standard form.  
This includes:
- Coefficients.
- Factored and vertex form of given formula.
- X or Y intercepts.
- Y value for a given X.
- Graph
## Getting Started
To run it as a stand-alone program, simply clone or download it and run `python PyQuad.py`.  
Alternatively, `Quad.py` can be imported for use in other code.
### Prerequisites
Modules used in this version are:
- Numpy 1.14.2
- Matplotlib 2.2.2  
  
The latest version of these modules should work just fine.
You can install them by running `pip install numpy` and `pip install matplotlib`
## Usage Examples
When instantiating the class, the 3 coefficients of the formula are passed as arguments
```
>>> import Quad
>>> q = Quad.Quadratic(5, 25, 30)
>>> print(q)
f(x) = 5x^2 + 25x + 30
>>> q.vertex()
(-2.5, -1.25)
>>> q.factored_form()
f(x) = 5(x+2)(x+3)
```
Each coefficient can be accessed by calling it's respective conventional variable name (a, b, c).
```
>>> q.a
5.0
>>> q.c
30.0
```
### Methods of the class are:
- has_x_intercept(): Checks if the graph of the formula has 1 or more x-intercepts and returns a boolean.
- x_intercepts(): Returns the x-intercept(s) of the graph or `None` if there aren't any.
- is_factorable(): Checks if the formula is factorable and returns a boolean.
- factored_form(): Returns the formula in factored form or `None` if not factorable.
- vertex(): Returns the x and y coordinates of the graph as a tuple.
- vertex_form(): Returns the formula in vertex form.
- evaluate(x): Returns the y value for any given x.
- graph(xrange, vector): Graphs the formula within the given xrange (default is 5 units on each side of the vertex point) as a png image or a pdf if the vector argument is `True`. The graph is saved in the same directory as Quad.py.
## Author
[Khachig Ainteblian](https://github.com/Khachig) - Sole author
## License
MIT License. *Copyright (C) 2018 Khachig Ainteblian.*

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

## Note
This is my first project so any contribution or advice beyond code is appreciated.  
For example, advice on the repository itself and how to follow github conventions is welcome.
