#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Setup EventManager
#
from CvPythonExtensions import *
import CvUtil
# import BugUtil

# Updater Mod
import CvScreensInterface
import CvModUpdaterScreen
# Updater Mod END


gc = CyGlobalContext()
localText = CyTranslator()

iPlayerOptionCheck = 0  # Triggers for == 1, decrements for >= 0

def check_show_ressources():
    iPlayer = gc.getGame().getActivePlayer()
    if (iPlayer != -1
        and gc.getPlayer(iPlayer).isOption(
            PlayerOptionTypes.PLAYEROPTION_MODDER_1)
       ):
        CvUtil.pyPrint('toggle resource symbols on')
        bResourceOn = ControlTypes.CONTROL_RESOURCE_ALL + 1001
        CyGame().doControlWithoutWidget(bResourceOn)  # Ctrl+r


def integrate(eventManager, _EVENT_FUNCTION_MAP):

    # Updater Mod
    # Note: In difference to the normal EventManager handlers, a second arg,
    # eventType, is added.
    # def _onWindowActivation(self, argsList):
    def _onWindowActivation(self, eventType, argsList):
        'Called when the game window activates or deactivates'
        bActive = argsList[0]

        if not hasattr(CvScreensInterface, "showModUpdaterScreen"):
            CvModUpdaterScreen.integrate()

        # Show ModUpdater screen after Window switch
        if (bActive and
            -1 == CyGame().getActivePlayer() and not CyGame().isPitbossHost()):
            CvScreensInterface.showModUpdaterScreen()

    # this does not work:
    # eventManager.addEventHandler('windowActivation', _onWindowActivation)
    # this works:
    _EVENT_FUNCTION_MAP["windowActivation"] = _onWindowActivation
    # Updater Mod END


    def _onLoadGame(argsList):
        global iPlayerOptionCheck
        # Attention, for iPlayerOptionCheck = 1 you will check aggainst
        # the option values stored in the save file, but not the current one!
        iPlayerOptionCheck = 8   # 1 = 1/4 sec

    def _onGameUpdate(argsList):
        global iPlayerOptionCheck
        if iPlayerOptionCheck > 0:
            iPlayerOptionCheck -= 1
            if iPlayerOptionCheck == 0:
                check_show_ressources()

    eventManager.addEventHandler('OnLoad', _onLoadGame)
    eventManager.addEventHandler('gameUpdate', _onGameUpdate)
