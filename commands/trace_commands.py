"""Trace commands for Rigol oscilloscope"""

class TraceCommands:
    def __init__(self, device):
        self.device = device

    def set_data(self, trace: int, data: str):
        """Set trace data"""
        self.device.send_command(f':TRACe{trace}:DATA {data}')

    def set_data_dac16(self, trace: int, data: str):
        """Set trace DAC16 data"""
        self.device.send_command(f':TRACe{trace}:DATA:DAC16 {data}')

    def set_data_dac(self, trace: int, data: str):
        """Set trace DAC data"""
        self.device.send_command(f':TRACe{trace}:DATA:DAC {data}')

    def set_points(self, trace: int, points: int):
        """Set number of points"""
        self.device.send_command(f':TRACe{trace}:DATA:POINts {points}')

    def set_points_interpolate(self, trace: int, enabled: bool):
        """Enable/disable points interpolation"""
        self.device.send_command(f':TRACe{trace}:DATA:POINts:INTerpolate {1 if enabled else 0}')

    def get_data_load(self, trace: int):
        """Get trace data load"""
        return self.device.query(f':TRACe{trace}:DATA:LOAD?')

    def set_data_value(self, trace: int, volatile: bool, points: int, data: str):
        """Set trace data value"""
        self.device.send_command(f':TRACe{trace}:DATA:VALue {1 if volatile else 0},{points},{data}')