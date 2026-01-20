import unittest.mock as mock
from main import main

@mock.patch('main.main')
def test_main(mock_cli_main):
    # This test is a bit redundant now but let's just check it doesn't crash 
    # and calls the underlying cli main if we were to test the execution.
    # Actually, the 'from main import main' already imported it.
    pass

@mock.patch('snoring.cli.asyncio.run')
def test_main_execution(mock_run):
    main()
    mock_run.assert_called_once()