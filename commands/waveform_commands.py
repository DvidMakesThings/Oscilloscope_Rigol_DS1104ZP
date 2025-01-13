"""Waveform commands for Rigol oscilloscope"""

class WaveformCommands:
    def __init__(self, device):
        self.device = device

    def set_source(self, source: str):
        """Set waveform source (CHANnel1|CHANnel2|CHANnel3|CHANnel4|MATH|FFT|LA)"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4', 'MATH', 'FFT', 'LA']
        if source.upper() not in valid_sources:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':WAVeform:SOURce {source}')

    def set_mode(self, mode: str):
        """Set waveform mode (NORMal|MAXimum|RAW)"""
        valid_modes = ['NORMal', 'MAXimum', 'RAW']
        if mode.upper() not in valid_modes:
            raise ValueError(f'Invalid mode. Must be one of {valid_modes}')
        self.device.send_command(f':WAVeform:MODE {mode}')

    def set_format(self, format: str):
        """Set waveform format (WORD|BYTE|ASCii)"""
        valid_formats = ['WORD', 'BYTE', 'ASCii']
        if format.upper() not in valid_formats:
            raise ValueError(f'Invalid format. Must be one of {valid_formats}')
        self.device.send_command(f':WAVeform:FORMat {format}')

    def get_data(self):
        """Get waveform data"""
        return self.device.query(':WAVeform:DATA?')

    def get_x_increment(self):
        """Get X increment between data points"""
        return float(self.device.query(':WAVeform:XINCrement?'))

    def get_x_origin(self):
        """Get X origin time"""
        return float(self.device.query(':WAVeform:XORigin?'))

    def get_x_reference(self):
        """Get X reference time"""
        return float(self.device.query(':WAVeform:XREFerence?'))

    def get_y_increment(self):
        """Get Y increment between data points"""
        return float(self.device.query(':WAVeform:YINCrement?'))

    def get_y_origin(self):
        """Get Y origin voltage"""
        return float(self.device.query(':WAVeform:YORigin?'))

    def get_y_reference(self):
        """Get Y reference voltage"""
        return float(self.device.query(':WAVeform:YREFerence?'))

    def set_start(self, start: int):
        """Set start point of waveform data reading"""
        self.device.send_command(f':WAVeform:STARt {start}')

    def set_stop(self, stop: int):
        """Set stop point of waveform data reading"""
        self.device.send_command(f':WAVeform:STOP {stop}')

    def get_preamble(self):
        """Get waveform preamble information"""
        return self.device.query(':WAVeform:PREamble?')