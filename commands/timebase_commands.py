"""Timebase commands for Rigol oscilloscope"""

class TimebaseCommands:
    def __init__(self, device):
        self.device = device

    def set_delay_enable(self, enabled: bool):
        """Enable/disable delayed sweep"""
        self.device.send_command(f':TIMebase:DELay:ENABle {1 if enabled else 0}')

    def set_delay_offset(self, offset: float):
        """Set delayed sweep offset"""
        self.device.send_command(f':TIMebase:DELay:OFFSet {offset}')

    def set_delay_scale(self, scale: float):
        """Set delayed sweep scale"""
        self.device.send_command(f':TIMebase:DELay:SCALe {scale}')

    def set_main_offset(self, offset: float):
        """Set main timebase offset"""
        self.device.send_command(f':TIMebase:OFFSet {offset}')

    def set_main_scale(self, scale: float):
        """Set main timebase scale"""
        self.device.send_command(f':TIMebase:SCALe {scale}')

    def set_mode(self, mode: str):
        """Set timebase mode"""
        valid_modes = ['MAIN', 'XY', 'ROLL']
        if mode.upper() not in valid_modes:
            raise ValueError(f'Invalid mode. Must be one of {valid_modes}')
        self.device.send_command(f':TIMebase:MODE {mode}')