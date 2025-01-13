"""Cursor commands for Rigol oscilloscope"""

class CursorCommands:
    def __init__(self, device):
        self.device = device

    def set_mode(self, mode: str):
        """Set cursor mode"""
        valid_modes = ['OFF', 'MANual', 'TRACk', 'AUTO', 'XY']
        if mode.upper() not in valid_modes:
            raise ValueError(f'Invalid mode. Must be one of {valid_modes}')
        self.device.send_command(f':CURSor:MODE {mode}')

    def set_manual_type(self, type: str):
        """Set manual cursor type"""
        valid_types = ['TIME', 'VOLTage']
        if type.upper() not in valid_types:
            raise ValueError(f'Invalid type. Must be one of {valid_types}')
        self.device.send_command(f':CURSor:MANual:TYPE {type}')

    def set_manual_source(self, source: str):
        """Set manual cursor source"""
        self.device.send_command(f':CURSor:MANual:SOURce {source}')

    def set_manual_time_unit(self, unit: str):
        """Set manual cursor time unit"""
        valid_units = ['S', 'HZ', 'DEGRee', 'PERCent']
        if unit.upper() not in valid_units:
            raise ValueError(f'Invalid unit. Must be one of {valid_units}')
        self.device.send_command(f':CURSor:MANual:TUNit {unit}')

    def set_manual_value(self, cursor: str, value: float):
        """Set manual cursor value"""
        if cursor.upper() not in ['AX', 'BX', 'AY', 'BY']:
            raise ValueError('Cursor must be AX, BX, AY, or BY')
        self.device.send_command(f':CURSor:MANual:{cursor} {value}')