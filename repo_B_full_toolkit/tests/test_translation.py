from src.advanced_examples import translate
def test_translate_basic():
    assert translate('ATGAAATGA')[:3] == 'MK*' or translate('ATGAAATGA').startswith('MK')
