# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.buuk


class PlonethemeBuukLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plonetheme.buuk)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.buuk:default')


PLONETHEME_BUUK_FIXTURE = PlonethemeBuukLayer()


PLONETHEME_BUUK_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_BUUK_FIXTURE,),
    name='PlonethemeBuukLayer:IntegrationTesting'
)


PLONETHEME_BUUK_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_BUUK_FIXTURE,),
    name='PlonethemeBuukLayer:FunctionalTesting'
)


PLONETHEME_BUUK_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_BUUK_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeBuukLayer:AcceptanceTesting'
)
