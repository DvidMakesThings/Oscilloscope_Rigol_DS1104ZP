"""Function commands for Rigol oscilloscope"""

class FunctionCommands:
    def __init__(self, device):
        self.device = device

    def set_record_end(self, frame: int):
        """Set waveform record end frame"""
        self.device.send_command(f':FUNCtion:WRECord:FEND {frame}')

    def get_record_max(self):
        """Get maximum number of frames"""
        return int(self.device.query(':FUNCtion:WRECord:FMAX?'))

    def set_record_interval(self, interval: int):
        """Set waveform record interval"""
        self.device.send_command(f':FUNCtion:WRECord:FINTerval {interval}')

    def set_record_prompt(self, enabled: bool):
        """Enable/disable record prompt"""
        self.device.send_command(f':FUNCtion:WRECord:PROMpt {1 if enabled else 0}')

    def set_record_operate(self, operate: str):
        """Set record operation"""
        self.device.send_command(f':FUNCtion:WRECord:OPERate {operate}')

    def set_record_enable(self, enabled: bool):
        """Enable/disable waveform record"""
        self.device.send_command(f':FUNCtion:WRECord:ENABle {1 if enabled else 0}')

    def set_replay_start(self, frame: int):
        """Set replay start frame"""
        self.device.send_command(f':FUNCtion:WREPlay:FSTart {frame}')

    def set_replay_end(self, frame: int):
        """Set replay end frame"""
        self.device.send_command(f':FUNCtion:WREPlay:FEND {frame}')

    def get_replay_max(self):
        """Get maximum number of replay frames"""
        return int(self.device.query(':FUNCtion:WREPlay:FMAX?'))

    def set_replay_interval(self, interval: int):
        """Set replay interval"""
        self.device.send_command(f':FUNCtion:WREPlay:FINTerval {interval}')

    def set_replay_mode(self, mode: str):
        """Set replay mode"""
        self.device.send_command(f':FUNCtion:WREPlay:MODE {mode}')

    def set_replay_direction(self, direction: str):
        """Set replay direction"""
        self.device.send_command(f':FUNCtion:WREPlay:DIRection {direction}')

    def set_replay_operate(self, operate: str):
        """Set replay operation"""
        self.device.send_command(f':FUNCtion:WREPlay:OPERate {operate}')

    def get_replay_current(self):
        """Get current frame"""
        return int(self.device.query(':FUNCtion:WREPlay:FCURrent?'))