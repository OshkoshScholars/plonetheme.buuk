# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.buuk.testing import PLONETHEME_BUUK_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.buuk is properly installed."""

    layer = PLONETHEME_BUUK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.buuk is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('plonetheme.buuk'))

    def test_browserlayer(self):
        """Test that IPlonethemeBuukLayer is registered."""
        from plonetheme.buuk.interfaces import IPlonethemeBuukLayer
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeBuukLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_BUUK_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.buuk'])

    def test_product_uninstalled(self):
        """Test if plonetheme.buuk is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('plonetheme.buuk'))
