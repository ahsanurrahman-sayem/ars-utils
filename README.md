[![Build & Release Python Package](https://github.com/ahsanurrahman-sayem/ars-utils/actions/workflows/build-and-release.yml/badge.svg?branch=main)](https://github.com/ahsanurrahman-sayem/ars-utils/actions/workflows/build-and-release.yml)

## ars
- ars is a Python package contains various modules I made to use in future and make my works more moduler.

### Installation

```bash
python3 -m pip install https://github.com/ahsanurrahman-sayem/ars-utils/releases/download/latest/ars-1.2.2-py3-none-any.whl
```

## Usage - utils Module

```python
import ars
from ars import utils

# -- List available modules inside the package --
# -- Run same function to list available functions inside the moduels --

for i in dir(ars):
    print(i)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

[MIT](https://choosealicense.com/licenses/mit/)
