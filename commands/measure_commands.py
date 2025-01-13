"""Measure commands for Rigol oscilloscope"""

class MeasureCommands:
    def __init__(self, device):
        self.device = device

    # ... existing methods ...

    def set_adisplay(self, enabled: bool):
        """Set all measurement display"""
        self.device.send_command(f':MEASure:ADISplay {1 if enabled else 0}')

    def set_amsource(self, source: str):
        """Set all measurement source"""
        self.device.send_command(f':MEASure:AMSource {source}')

    def set_setup_max(self, value: float):
        """Set maximum measurement setup"""
        self.device.send_command(f':MEASure:SETup:MAX {value}')

    def set_setup_mid(self, value: float):
        """Set middle measurement setup"""
        self.device.send_command(f':MEASure:SETup:MID {value}')

    def set_setup_min(self, value: float):
        """Set minimum measurement setup"""
        self.device.send_command(f':MEASure:SETup:MIN {value}')

    def set_setup_psa(self, value: float):
        """Set phase setup A"""
        self.device.send_command(f':MEASure:SETup:PSA {value}')

    def set_setup_psb(self, value: float):
        """Set phase setup B"""
        self.device.send_command(f':MEASure:SETup:PSB {value}')

    def set_setup_dsa(self, value: float):
        """Set delay setup A"""
        self.device.send_command(f':MEASure:SETup:DSA {value}')

    def set_setup_dsb(self, value: float):
        """Set delay setup B"""
        self.device.send_command(f':MEASure:SETup:DSB {value}')

    def set_statistic_display(self, enabled: bool):
        """Set statistics display"""
        self.device.send_command(f':MEASure:STATistic:DISPlay {1 if enabled else 0}')

    def set_statistic_mode(self, mode: str):
        """Set statistics mode"""
        self.device.send_command(f':MEASure:STATistic:MODE {mode}')

    def reset_statistics(self):
        """Reset statistics"""
        self.device.send_command(':MEASure:STATistic:RESet')

    def set_statistic_item(self, item: str, value: str):
        """Set statistics item"""
        self.device.send_command(f':MEASure:STATistic:ITEM {item},{value}')

    def set_item(self, item: str, source: str):
        """Set measurement item"""
        self.device.send_command(f':MEASure:ITEM {item},{source}')