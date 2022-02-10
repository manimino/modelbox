from multiprocessing import Process

import pytest
import time

from iris.main import run_api


@pytest.fixture
def server():
    proc = Process(target=run_api, args=(), daemon=True)
    proc.start()
    time.sleep(0.1)
    yield
    proc.kill()