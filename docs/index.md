---
title: Getting Started
---

## Install

```bash
# via pip
pip install xbool

# via poetry
poetry add xbool
```

## Introduction

General purpose bool/boolean utilities, extracting bools from strings.

## bool_value function

Converts any object to a bool.

Special-cases strings, which bool is returned is based on string contents.

```python
from xbool import bool_value

# Convert string to bool
assert bool_value('true') is True
assert bool_value('false') is False
```

Generally, if the value passed in is one of these, it's considered `True`:

- For Strings (after stripping any leading/training white-space):
    - "t"
    - "True"
    - "T"
    - "1"
    - "true"
    - "on"
- For `bool`:
    - We simply return whatever the passed-in bool is.
- Other Types Of Objects:
    - If object is True-like (where object's `__bool__()` value is True).


Otherwise, a `False` will be returned (ie: if string contains 'false', we return False).

If any `ValueError` is raised while trying to get bool-value from any object,
will return `False`.

### Examples

```python
from xbool import bool_value

# Convert string to bool
assert bool_value('true') is True
assert bool_value('false') is False

assert bool_value('y') is True
assert bool_value('n') is False

assert bool_value('on') is True
assert bool_value('off') is False

assert bool_value('t') is True
assert bool_value('f') is False

assert bool_value('yes') is True
assert bool_value('no') is False

assert bool_value('1') is True
assert bool_value('0') is False

# Any other string is generally considered False:
assert bool_value("some-other-string") is False

# Convert bools to bools:
assert bool_value(True) is True
assert bool_value(False) is False

# Generally, for non-strings, True-like objects return True:
some_object = object()
assert bool_value(some_object) is True

# And False-like objects return False:
assert bool_value(None) is False
```


## bool_env

Looks up environmental variable with passed in name.

Runs the env-var value though `bool_value` for you and returns the result.

Useful to easily get a bool-value from an environmental variable.

```python
from xbool import bool_env
import os

os.environ['SOME_ENV_VAR'] = "False"
assert bool_env('SOME_ENV_VAR') is False


os.environ['SOME_OTHER_ENV_VAR'] = "True"
assert bool_env('SOME_OTHER_ENV_VAR') is True
```
