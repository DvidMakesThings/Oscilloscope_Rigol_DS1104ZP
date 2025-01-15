"""Trigger commands for Rigol oscilloscope"""

class TriggerCommands:
    def __init__(self, device):
        self.device = device

    def set_mode(self, mode: str):
        """Set trigger mode"""
        valid_modes = ['EDGE', 'PULSe', 'RUNT', 'WINDow', 'NEDGE', 'SLOPe', 'VIDeo', 
                      'PATTern', 'DELay', 'TIMeout', 'DURation', 'SHOLd', 'RS232', 'IIC', 'SPI']
        if mode.upper() not in valid_modes:
            raise ValueError(f'Invalid mode. Must be one of {valid_modes}')
        self.device.send_command(f':TRIGger:MODE {mode}')

    def set_coupling(self, coupling: str):
        """Set trigger coupling"""
        valid_couplings = ['DC', 'AC', 'LFReject', 'HFReject']
        if coupling.upper() not in valid_couplings:
            raise ValueError(f'Invalid coupling. Must be one of {valid_couplings}')
        self.device.send_command(f':TRIGger:COUPling {coupling}')

    def get_status(self):
        """Get trigger status"""
        return self.device.query(':TRIGger:STATus?')

    def set_sweep(self, sweep: str):
        """Set trigger sweep mode"""
        valid_sweeps = ['AUTO', 'NORMal', 'SINGle']
        if sweep.upper() not in valid_sweeps:
            raise ValueError(f'Invalid sweep. Must be one of {valid_sweeps}')
        self.device.send_command(f':TRIGger:SWEep {sweep}')

    def set_holdoff(self, time: float):
        """Set trigger holdoff time"""
        self.device.send_command(f':TRIGger:HOLDoff {time}')

    def set_noise_reject(self, enabled: bool):
        """Enable/disable noise reject"""
        self.device.send_command(f':TRIGger:NREJect {1 if enabled else 0}')

    def get_position(self):
        """Get trigger position"""
        return float(self.device.query(':TRIGger:POSition?'))

    # Edge trigger commands
    def set_edge_source(self, source: str):
        """Set edge trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4', 'AC', 'EXT']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:EDGe:SOURce {source}')

    def set_edge_slope(self, slope: str):
        """Set edge trigger slope"""
        valid_slopes = ['POSitive', 'NEGative', 'RFALl']
        if slope.upper() not in [s.upper() for s in valid_slopes]:
            raise ValueError(f'Invalid slope. Must be one of {valid_slopes}')
        self.device.send_command(f':TRIGger:EDGe:SLOPe {slope}')

    def set_edge_level(self, level: float):
        """Set edge trigger level"""
        self.device.send_command(f':TRIGger:EDGe:LEVel {level}')

    # Pulse trigger commands
    def set_pulse_source(self, source: str):
        """Set pulse trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4', 'EXT']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:PULSe:SOURce {source}')

    def set_pulse_when(self, when: str):
        """Set pulse trigger condition"""
        valid_conditions = ['PGReater', 'PLESs', 'NGReater', 'NLESs', 'PGLess', 'NGLess']
        if when.upper() not in valid_conditions:
            raise ValueError(f'Invalid condition. Must be one of {valid_conditions}')
        self.device.send_command(f':TRIGger:PULSe:WHEN {when}')

    def set_pulse_width(self, width: float):
        """Set pulse trigger width"""
        self.device.send_command(f':TRIGger:PULSe:WIDTh {width}')

    # Slope trigger commands
    def set_slope_source(self, source: str):
        """Set slope trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:SLOPe:SOURce {source}')

    def set_slope_when(self, when: str):
        """Set slope trigger condition"""
        valid_conditions = ['PGReater', 'PLESs', 'NGReater', 'NLESs']
        if when.upper() not in valid_conditions:
            raise ValueError(f'Invalid condition. Must be one of {valid_conditions}')
        self.device.send_command(f':TRIGger:SLOPe:WHEN {when}')

    def set_slope_time(self, time: float):
        """Set slope trigger time"""
        self.device.send_command(f':TRIGger:SLOPe:TIME {time}')

    # Video trigger commands
    def set_video_source(self, source: str):
        """Set video trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:VIDeo:SOURce {source}')

    def set_video_mode(self, mode: str):
        """Set video trigger mode"""
        valid_modes = ['ODDField', 'EVENfield', 'LINE', 'ALINes']
        if mode.upper() not in valid_modes:
            raise ValueError(f'Invalid mode. Must be one of {valid_modes}')
        self.device.send_command(f':TRIGger:VIDeo:MODE {mode}')

    def set_video_standard(self, standard: str):
        """Set video standard"""
        valid_standards = ['PAL', 'NTSC']
        if standard.upper() not in valid_standards:
            raise ValueError(f'Invalid standard. Must be one of {valid_standards}')
        self.device.send_command(f':TRIGger:VIDeo:STANdard {standard}')

    # Pattern trigger commands
    def set_pattern_pattern(self, pattern: str):
        """Set pattern trigger pattern"""
        self.device.send_command(f':TRIGger:PATTern:PATTern {pattern}')

    def set_pattern_source(self, source: str, level: float):
        """Set pattern trigger source level"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:PATTern:LEVel {source},{level}')

    # Duration trigger commands
    def set_duration_source(self, source: str):
        """Set duration trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:DURATion:SOURce {source}')

    def set_duration_type(self, type: str):
        """Set duration trigger type"""
        valid_types = ['GREater', 'LESS', 'GLESs']
        if type.upper() not in valid_types:
            raise ValueError(f'Invalid type. Must be one of {valid_types}')
        self.device.send_command(f':TRIGger:DURATion:TYPE {type}')

    # Optional trigger types
    def set_timeout_source(self, source: str):
        """Set timeout trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:TIMeout:SOURce {source}')

    def set_runt_source(self, source: str):
        """Set runt trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:RUNT:SOURce {source}')

    def set_windows_source(self, source: str):
        """Set windows trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:WINDows:SOURce {source}')

    def set_delay_source1(self, source: str):
        """Set delay trigger source 1"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:DELay:SA {source}')

    def set_shold_source1(self, source: str):
        """Set setup/hold trigger source 1"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:SHOLd:DSrc {source}')

    def set_nedge_source(self, source: str):
        """Set nth edge trigger source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':TRIGger:NEDGe:SOURce {source}')

    def set_rs232_source(self, source: str):
        """Set RS232 trigger source"""