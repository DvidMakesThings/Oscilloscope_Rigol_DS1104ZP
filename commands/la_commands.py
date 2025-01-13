"""Logic Analyzer commands for Rigol oscilloscope"""

class LACommands:
    def __init__(self, device):
        self.device = device

    def set_active(self, channel: str):
        """Set active channel"""
        self.device.send_command(f':LA:ACTive {channel}')

    def set_autosort(self, enabled: bool):
        """Enable/disable auto sort"""
        self.device.send_command(f':LA:AUTosort {1 if enabled else 0}')

    def set_digital_display(self, channel: int, enabled: bool):
        """Set digital channel display"""
        self.device.send_command(f':LA:DIGital{channel}:DISPlay {1 if enabled else 0}')

    def set_digital_position(self, channel: int, position: int):
        """Set digital channel position"""
        self.device.send_command(f':LA:DIGital{channel}:POSition {position}')

    def set_digital_label(self, channel: int, label: str):
        """Set digital channel label"""
        self.device.send_command(f':LA:DIGital{channel}:LABel {label}')

    def set_display(self, enabled: bool):
        """Set LA display"""
        self.device.send_command(f':LA:DISPlay {1 if enabled else 0}')

    def set_pod_display(self, pod: int, enabled: bool):
        """Set pod display"""
        self.device.send_command(f':LA:POD{pod}:DISPlay {1 if enabled else 0}')

    def set_pod_threshold(self, pod: int, threshold: float):
        """Set pod threshold"""
        self.device.send_command(f':LA:POD{pod}:THReshold {threshold}')

    def set_size(self, size: str):
        """Set LA size"""
        self.device.send_command(f':LA:SIZE {size}')

    def set_state(self, enabled: bool):
        """Set LA state"""
        self.device.send_command(f':LA:STATe {1 if enabled else 0}')

    def set_tcalibrate(self, time: float):
        """Set time calibration"""
        self.device.send_command(f':LA:TCALibrate {time}')