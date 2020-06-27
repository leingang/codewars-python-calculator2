# codewars-python-calculator2

Repository for the Codewars
“[Calculator](https://www.codewars.com/kata/5235c913397cbf2508000048/train/python)"
python kata

Adapted from [my prior
solution](https://github.com/leingang/codewars-python-calculator) to [another
kata](https://www.codewars.com/kata/52a78825cdfc2cfc87000005).  That one only
used integers.

## Developing

Use a python 3.6 virtual environment  I use the same one for all codewars katas:

    virtualenv-3.6 ~/.local/share/virtualenvs/codewars
    . ~/.local/share/virtualenvs/codewars/bin/activate

Then:

    python -m pip install -r requirements.txt

So far this only installs one python package: the Codewars test suite.

## Testing

Work in a module called `solution.py`.  Put the sample tests in `tests.py`.

The module `utils.py` provides a logging object whch is useful for debugging
and introspection.

## Submitting

Strip out the logging lines:

    sed -e '/logger/d' -e '/logging/d' solution.py | pbcopy

Then paste into the Codewars edit window.


