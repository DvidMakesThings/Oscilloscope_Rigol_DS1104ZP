"""IEEE488.2 Common Commands for Rigol oscilloscope"""

class IEEECommands:
    def __init__(self, device):
        self.device = device

    def clear_status(self):
        """Clear status registers"""
        self.device.send_command('*CLS')

    def set_event_enable(self, value: int):
        """Set standard event enable register"""
        self.device.send_command(f'*ESE {value}')

    def get_event_status(self):
        """Get standard event status register"""
        return int(self.device.query('*ESR?'))

    def get_identification(self):
        """Get device identification"""
        try:
            return self.device.query('*IDN?')
        except Exception as e:
            print(f"Failed to get identification: {str(e)}")
            return ""

    def operation_complete(self):
        """Set operation complete flag"""
        self.device.send_command('*OPC')

    def reset(self):
        """Reset device to default state"""
        self.device.send_command('*RST')

    def set_service_enable(self, value: int):
        """Set service request enable register"""
        self.device.send_command(f'*SRE {value}')

    def get_status_byte(self):
        """Get status byte register"""
        return int(self.device.query('*STB?'))

    def self_test(self):
        """Perform self-test"""
        return int(self.device.query('*TST?'))

    def wait(self):
        """Wait for pending operations"""
        self.device.send_command('*WAI')