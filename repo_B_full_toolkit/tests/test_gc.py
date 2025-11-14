import pytest
from src.advanced_examples import gc_content
def test_gc_empty():
    assert gc_content('') == 0.0
def test_gc_known():
    assert gc_content('GGCC') == 100.0
    assert gc_content('ATAT') == 0.0
