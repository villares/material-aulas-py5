# A brief overview of py5 modes

The **py5** library, for creative coding in Python using the Processing graphics infrastructure, at this time can be used in 4 ways, coding styles or contexts, we call "modes". More details can be found at [py5coding.org - The Four py5 Modes](http://py5coding.org/content/py5_modes.html)

> ⚠️ **If on a Mac:**<br>
> You should read [Special Notes for OSX Users](http://py5coding.org/content/osx_users.html).

### Module mode

This might look familiar to some Python programmers. You import the library at the top, and define some special functions that py5 will call for you, like, `setup()` (runs once when the sketch starts), `draw()` (repeats continously, used for interaction and animations) and maybe some other [event functions](http://py5coding.org/reference/sketch.html). In the end you call `py5.run_sketch()`.

The following example will create a small Sketch that draws rectangles at the current mouse position:

```python
import py5

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
```
![image](https://user-images.githubusercontent.com/3694604/201694987-f78a4856-1329-4693-a312-4ab3402fe689.png)

> ⚠️ **Caution:**<br>
> Do not use `from py5 import *`, it will break many things! If you'd like to avoid the `py5.`prefixes, consider using the *imported mode*.

> ℹ️ **Note:**<br>
> If you have not defined `settings()` (optional in this mode), the `setup()` function will be split into `setup()` and `settings()` for you under the hood, according to some special rules, like `size()` needing to be in `settings()`, a Processing requirement.

### Imported mode

Originally designed to be used by beginner programmers, *imported mode* is analogous to the way code is written by users in the Processing IDE. You don't need to type `py5.` everywhere.

To use this mode you'll need a *py5 Jupyter Notebook Kernel* ([install instructions here](http://py5coding.org/content/install.html)) or, if using other code editors, you'll need to execute your code from the `run_sketch` command line tool (`$ run_sketch your_sketch.py`).

Another option is to have *Thonny IDE* with the [thonny-py5mode](https://github.com/tabreturn/thonny-py5mode/) plug-in installed, a *py5* menu will appear with an option called *Imported mode for py5*, when it is checked, Thonny will call the `run_sketch` tool for you.

This is the previous example written for *imported mode*:

```python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    rect(mouse_x, mouse_y, 10, 10)

# If you are using a Jupyter Notebook, add this:
run_sketch()
```

When using the `run_sketch` tool or the *thonny-py5mode* plug-in, you don't need `run_sketch()` at the end of your *imported mode* code.

### Static mode

*Static mode* lets you create static images using functionless code. It is designed for beginner programmers who are making their first steps into Python programming.

The code bellow, written for *static mode*, will create a 300 by 200 pixel image with a gray background and 20 randomly positioned squares:

```python
size(300, 200)
rect_mode(CENTER)
for _ in range(20):
    rect(random_int(width), random_int(height), 10, 10)
```

![image](https://user-images.githubusercontent.com/3694604/201693378-ccce119a-29ca-4569-bebc-1a3ec2f4c4da.png)

To use static mode in Jupyter Lab install the *py5bot Kernel* as described on the [Install py5 page](http://py5coding.org/content/install.html), then start Jupyter Lab using `$ jupyter lab`. You will see *py5bot* presented as an option in the Launcher. Click on it and put the code in a notebook cell.

You can also use the `run_sketch` tool or the Thonny IDE plug-in as described for *imported mode*.

### Class mode

For more advanced users who may want to run multiple sketches at the same time, *class mode* invites you to create a class with a `settings` method, now required, `setup`,`draw` and other desired methods. 

The first *module mode* example coded for *class mode* would be like this:

```python
from py5 import Sketch


class TestSketch(Sketch):

    def settings(self):
        self.size(300, 200)

    def setup(self):
        self.rect_mode(self.CENTER)

    def draw(self):
        self.rect(self.mouse_x, self.mouse_y, 10, 10)


test = TestSketch()
test.run_sketch()
```

## Further reading

For more details please visit the full **py5 documentation** at [py5coding.org](https://py5coding.org)
