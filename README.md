# The problem

To upgrade a 2.7 codebase to 3.5, you need to change any relative import statements written like this:

```py
# pack/a.py
import b
```

To this:

```py
# pack/a.py
from pack import b
```

However, this doesn't work when you have circular imports within the same package. Python 3.5 fixed this problem, but in 2.7
the above import will still fail.

```py
import b # works in 2.7, not in 3.5

from pack import b # works in 3.5, not in 2.7
```

To fix, use `importlib`:

```py
import importlib
b = importlib.import_module('.b', 'pack')
```
