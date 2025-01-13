"""Acquire commands for Rigol oscilloscope"""

class AcquireCommands:
    def __init__(self, device):
        self.device = device

    def set_averages(self, count: int):
        """Set number of averages"""
        if not 2 <= count <= 1024:
            raise ValueError('Count must be between 2 and 1024')
        self.device.send_command(f':ACQuire:AVERages {count}')

    def set_memory_depth(self, depth: str):
        """Set memory depth"""
        valid_depths = ['AUTO', '12K', '120K', '1200K', '12M', '24M', '6K', '60K', '600K', '6M']
        if str(depth).upper() not in valid_depths:
            raise ValueError(f'Invalid depth. Must be one of {valid_depths}')
        self.device.send_command(f':ACQuire:MDEPth {depth}')

    def set_type(self, type: str):
        """Set acquisition type"""
        valid_types = ['NORMal', 'AVERages', 'PEAK', 'HRESolution']
        if type.upper() not in valid_types:
            raise ValueError(f'Invalid type. Must be one of {valid_types}')
        self.device.send_command(f':ACQuire:TYPE {type}')

    def get_sample_rate(self):
        """Get current sample rate"""
        return float(self.device.query(':ACQuire:SRATe?'))