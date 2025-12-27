import logging
from homework010 import log_event

def test_log_event_success(caplog):
    with caplog.at_level(logging.INFO):
        log_event('alice', 'success')

    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == 'INFO'
    assert 'alice' in record.message

def test_log_event_exception(caplog):
    with caplog.at_level(logging.WARNING):
        log_event('anna', 'expired')

    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == 'WARNING'
    assert 'expired' in record.message

def test_log_event_failed(caplog):
    with caplog.at_level(logging.ERROR):
        log_event('sasha', 'failed')

    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelname == 'ERROR'
    assert 'failed' in record.message

def test_log_event_unknown_status(caplog):
    with caplog.at_level(logging.ERROR):
        log_event('victory', 'unknown')

    assert caplog.records[0].levelname == 'ERROR'