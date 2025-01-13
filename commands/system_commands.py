"""System commands for Rigol oscilloscope"""

class SystemCommands:
    def __init__(self, device):
        self.device = device

    def set_autoscale(self, enabled: bool):
        """Enable/disable autoscale"""
        self.device.send_command(f':SYSTem:AUToscale {1 if enabled else 0}')

    def set_beeper(self, enabled: bool):
        """Enable/disable beeper"""
        self.device.send_command(f':SYSTem:BEEPer {1 if enabled else 0}')

    def get_error(self):
        """Get next error from error queue"""
        return self.device.query(':SYSTem:ERRor[:NEXT]?')

    def get_gam(self):
        """Get grid amplitude measurement"""
        return self.device.query(':SYSTem:GAM?')

    def set_language(self, language: str):
        """Set system language"""
        self.device.send_command(f':SYSTem:LANGuage {language}')

    def set_locked(self, enabled: bool):
        """Lock/unlock front panel"""
        self.device.send_command(f':SYSTem:LOCKed {1 if enabled else 0}')

    def set_power_on(self, config: str):
        """Set power-on configuration"""
        valid_configs = ['LAST', 'DEFault']
        if config.upper() not in valid_configs:
            raise ValueError(f'Invalid config. Must be one of {valid_configs}')
        self.device.send_command(f':SYSTem:PON {config}')

    def install_option(self, license: str):
        """Install option"""
        self.device.send_command(f':SYSTem:OPTion:INSTall {license}')

    def uninstall_option(self):
        """Uninstall option"""
        self.device.send_command(':SYSTem:OPTion:UNINSTall')

    def get_ram(self):
        """Get RAM usage"""
        return self.device.query(':SYSTem:RAM?')

    def set_setup(self, setup: str):
        """Set system setup"""
        self.device.send_command(f':SYSTem:SETup {setup}')