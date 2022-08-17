# stop-thread
[![pytest](https://github.com/ffreemt/stop-thread/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/stop-thread/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/stop_thread.svg)](https://badge.fury.io/py/stop_thread)

Stop a thread in a nasty way

## Install it

```shell
pip install stop-thread
# pip install git+https://github.com/ffreemt/stop-thread
# poetry add git+https://github.com/ffreemt/stop-thread
# git clone https://github.com/ffreemt/stop-thread && cd stop-thread
```

## Use it
```python
import threading
from stop_thread import stop_thread

ident = threading.current_thread().ident
stop_thread(ident)
# possibly follow up with some clean-up to properly terminate the thread
# e.g. thread.quit(); thread.wait()
```
