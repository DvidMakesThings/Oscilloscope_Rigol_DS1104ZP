"""Calibrate commands for Rigol oscilloscope"""

class CalibrateCommands:
    def __init__(self, device):
        self.device = device

    def quit(self):
        """Quit calibration"""
        self.device.send_command(':CALibrate:QUIT')

    def start(self):
        """Start calibration"""
        self.device.send_command(':CALibrate:STARt')