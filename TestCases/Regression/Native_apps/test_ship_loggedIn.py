import pytest
import Utilities.CustomLogger as cl
import logging
import softest
import Static.Constants as const
import time
import allure
from Utilities.PageBase import PageBase

log = cl.customLogger(logging.INFO)

val = ''


@pytest.mark.usefixtures('login')
@pytest.mark.usefixtures('create_resource')
class TestShipLoggedInNative(softest.TestCase):
    '''
    Test Class for Ship Loggedin Page
    '''
