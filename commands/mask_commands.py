"""Mask commands for Rigol oscilloscope"""

class MaskCommands:
    def __init__(self, device):
        self.device = device

    def set_enable(self, enabled: bool):
        """Enable/disable mask test"""
        self.device.send_command(f':MASK:ENABle {1 if enabled else 0}')

    def set_source(self, source: str):
        """Set mask source"""
        self.device.send_command(f':MASK:SOURce {source}')

    def set_operate(self, operate: str):
        """Set mask operation"""
        self.device.send_command(f':MASK:OPERate {operate}')

    def set_mdisplay(self, enabled: bool):
        """Set mask display"""
        self.device.send_command(f':MASK:MDISplay {1 if enabled else 0}')

    def set_soutput(self, enabled: bool):
        """Set mask stop on output"""
        self.device.send_command(f':MASK:SOOutput {1 if enabled else 0}')

    def set_output(self, output: str):
        """Set mask output"""
        self.device.send_command(f':MASK:OUTPut {output}')

    def set_x(self, value: float):
        """Set horizontal adjustment"""
        self.device.send_command(f':MASK:X {value}')

    def set_y(self, value: float):
        """Set vertical adjustment"""
        self.device.send_command(f':MASK:Y {value}')

    def create(self):
        """Create mask"""
        self.device.send_command(':MASK:CREate')

    def get_passed(self):
        """Get passed frames"""
        return int(self.device.query(':MASK:PASSed?'))

    def get_failed(self):
        """Get failed frames"""
        return int(self.device.query(':MASK:FAILed?'))

    def get_total(self):
        """Get total frames"""
        return int(self.device.query(':MASK:TOTal?'))

    def reset(self):
        """Reset statistics"""
        self.device.send_command(':MASK:RESet')