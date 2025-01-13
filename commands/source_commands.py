"""Source commands for Rigol oscilloscope"""

class SourceCommands:
    def __init__(self, device):
        self.device = device

    def set_output(self, source: int, enabled: bool):
        """Enable/disable source output"""
        self.device.send_command(f':SOURce{source}:OUTPut {1 if enabled else 0}')

    def set_impedance(self, source: int, impedance: str):
        """Set output impedance"""
        valid_impedances = ['OMEG', 'FIFTy']
        if impedance.upper() not in valid_impedances:
            raise ValueError(f'Invalid impedance. Must be one of {valid_impedances}')
        self.device.send_command(f':SOURce{source}:OUTPut:IMPedance {impedance}')

    def set_frequency(self, source: int, frequency: float):
        """Set output frequency"""
        self.device.send_command(f':SOURce{source}:FREQuency {frequency}')

    def set_function(self, source: int, function: str):
        """Set output function"""
        valid_functions = ['SINusoid', 'SQUare', 'RAMP', 'PULSe', 'NOISe', 'DC', 'USER']
        if function.upper() not in valid_functions:
            raise ValueError(f'Invalid function. Must be one of {valid_functions}')
        self.device.send_command(f':SOURce{source}:FUNCtion {function}')

    def set_voltage(self, source: int, voltage: float):
        """Set output voltage"""
        self.device.send_command(f':SOURce{source}:VOLTage {voltage}')

    def set_voltage_offset(self, source: int, offset: float):
        """Set voltage offset"""
        self.device.send_command(f':SOURce{source}:VOLTage:OFFSet {offset}')