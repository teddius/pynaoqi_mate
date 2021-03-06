#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alautonomousmovesproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALAutonomousMoves(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALAutonomousMoves")

    def getBackgroundStrategy(self):
        """Gets the background strategy.

        :returns str: The autonomous background posture strategy. ("none" or "backToNeutral")
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.getBackgroundStrategy()

    def getExpressiveListeningEnabled(self):
        """If expressive listening is enabled.

        :returns bool: The boolean value: true means it is enabled, false means it is disabled.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.getExpressiveListeningEnabled()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.ping()

    def setBackgroundStrategy(self, strategy):
        """The background strategy.

        :param str strategy: The autonomous background posture strategy. ("none" or "backToNeutral")
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.setBackgroundStrategy(strategy)

    def setExpressiveListeningEnabled(self, enable):
        """Enable or disable expressive listening.

        :param bool enable: The boolean value: true to enable, false to disable.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.setExpressiveListeningEnabled(enable)

    def startSmallDisplacements(self):
        """DEPRECATED since 2.0: do ALBasicAwareness.setTrackingMode("MoveContextually") instead.Start small base moves.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.startSmallDisplacements()

    def stopSmallDisplacements(self):
        """DEPRECATED since 2.0: do ALBasicAwareness.setTrackingMode instead.Stop small base moves.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.stopSmallDisplacements()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAutonomousMoves")
        return self.proxy.version()
