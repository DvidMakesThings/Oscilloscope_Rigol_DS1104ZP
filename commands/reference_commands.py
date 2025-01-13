"""Reference commands for Rigol oscilloscope"""

class ReferenceCommands:
    def __init__(self, device):
        self.device = device

    def set_display(self, enabled: bool):
        """Set reference display"""
        self.device.send_command(f':REFerence:DISPlay {1 if enabled else 0}')

    def set_channel_enable(self, channel: int, enabled: bool):
        """Enable/disable reference channel"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:ENABle {1 if enabled else 0}')

    def set_source(self, channel: int, source: str):
        """Set reference source"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:SOURce {source}')

    def set_vertical_scale(self, channel: int, scale: float):
        """Set reference vertical scale"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:VSCale {scale}')

    def set_vertical_offset(self, channel: int, offset: float):
        """Set reference vertical offset"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:VOFFset {offset}')

    def reset(self, channel: int):
        """Reset reference settings"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:RESet')

    def set_current(self, channel: int):
        """Set current reference channel"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:CURRent')

    def save(self, channel: int):
        """Save reference waveform"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:SAVe')

    def set_color(self, channel: int, color: str):
        """Set reference color"""
        self._validate_channel(channel)
        self.device.send_command(f':REFerence{channel}:COLor {color}')

    def _validate_channel(self, channel: int):
        """Validate reference channel number"""
        if not 1 <= channel <= 10:
            raise ValueError('Channel must be between 1 and 10')