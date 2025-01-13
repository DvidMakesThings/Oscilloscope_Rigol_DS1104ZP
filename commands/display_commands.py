"""Display commands for Rigol oscilloscope"""

class DisplayCommands:
    def __init__(self, device):
        self.device = device

    def clear(self):
        """Clear display"""
        self.device.send_command(':DISPlay:CLEar')

    def get_data(self):
        """Get display data"""
        return self.device.query(':DISPlay:DATA?')

    def set_type(self, type: str):
        """Set display type"""
        valid_types = ['VECTors', 'DOTS']
        if type.upper() not in valid_types:
            raise ValueError(f'Invalid type. Must be one of {valid_types}')
        self.device.send_command(f':DISPlay:TYPE {type}')

    def set_grading_time(self, time: str):
        """Set persistence time"""
        self.device.send_command(f':DISPlay:GRADing:TIME {time}')

    def set_waveform_brightness(self, brightness: int):
        """Set waveform brightness"""
        if not 0 <= brightness <= 100:
            raise ValueError('Brightness must be between 0 and 100')
        self.device.send_command(f':DISPlay:WBRightness {brightness}')

    def set_grid(self, grid: str):
        """Set grid type"""
        valid_grids = ['FULL', 'HALF', 'NONE']
        if grid.upper() not in valid_grids:
            raise ValueError(f'Invalid grid. Must be one of {valid_grids}')
        self.device.send_command(f':DISPlay:GRID {grid}')

    def set_grid_brightness(self, brightness: int):
        """Set grid brightness"""
        if not 0 <= brightness <= 100:
            raise ValueError('Brightness must be between 0 and 100')
        self.device.send_command(f':DISPlay:GBRightness {brightness}')