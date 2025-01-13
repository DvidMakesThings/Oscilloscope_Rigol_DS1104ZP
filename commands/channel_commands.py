"""Channel commands for Rigol oscilloscope"""

class ChannelCommands:
    def __init__(self, device):
        self.device = device

    def set_bandwidth_limit(self, channel: int, enabled: bool):
        """Set bandwidth limit for specified channel"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:BWLimit {1 if enabled else 0}')

    def set_coupling(self, channel: int, coupling: str):
        """Set coupling for specified channel"""
        self._validate_channel(channel)
        valid_couplings = ['AC', 'DC', 'GND']
        if coupling.upper() not in valid_couplings:
            raise ValueError(f'Invalid coupling. Must be one of {valid_couplings}')
        self.device.send_command(f':CHANnel{channel}:COUPling {coupling}')

    def set_display(self, channel: int, enabled: bool):
        """Set display state for specified channel"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:DISPlay {1 if enabled else 0}')

    def set_invert(self, channel: int, enabled: bool):
        """Set invert state for specified channel"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:INVert {1 if enabled else 0}')

    def set_offset(self, channel: int, offset: float):
        """Set offset for specified channel"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:OFFSet {offset}')

    def set_range(self, channel: int, range_value: float):
        """Set range for specified channel"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:RANGe {range_value}')

    def set_tcal(self, channel: int, time: float):
        """Set time calibration"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:TCAL {time}')

    def set_scale(self, channel: int, scale: float):
        """Set vertical scale"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:SCALe {scale}')

    def set_probe(self, channel: int, ratio: float):
        """Set probe ratio for specified channel"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:PROBe {ratio}')

    def set_units(self, channel: int, units: str):
        """Set units for specified channel"""
        self._validate_channel(channel)
        valid_units = ['VOLTage', 'AMPere', 'WATTs', 'UNKNown']
        if units.upper() not in valid_units:
            raise ValueError(f'Invalid units. Must be one of {valid_units}')
        self.device.send_command(f':CHANnel{channel}:UNITs {units}')

    def set_vernier(self, channel: int, enabled: bool):
        """Set vernier state for specified channel"""
        self._validate_channel(channel)
        self.device.send_command(f':CHANnel{channel}:VERNier {1 if enabled else 0}')

    def _validate_channel(self, channel: int):
        """Validate channel number"""
        if not 1 <= channel <= 4:
            raise ValueError('Channel must be between 1 and 4')