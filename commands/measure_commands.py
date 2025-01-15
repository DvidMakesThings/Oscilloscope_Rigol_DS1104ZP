"""Measure commands for Rigol oscilloscope"""

class MeasureCommands:
    def __init__(self, device):
        self.device = device

    def set_adisplay(self, enabled: bool):
        """Set all measurement display"""
        self.device.send_command(f':MEASure:ADISplay {1 if enabled else 0}')

    def set_amsource(self, source: str):
        """Set all measurement source"""
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4', 'MATH']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':MEASure:AMSource {source}')

    def set_setup_max(self, value: float):
        """Set maximum measurement setup"""
        self.device.send_command(f':MEASure:SETup:MAX {value}')

    def set_setup_mid(self, value: float):
        """Set middle measurement setup"""
        self.device.send_command(f':MEASure:SETup:MID {value}')

    def set_setup_min(self, value: float):
        """Set minimum measurement setup"""
        self.device.send_command(f':MEASure:SETup:MIN {value}')

    def set_setup_psa(self, value: float):
        """Set phase setup A"""
        self.device.send_command(f':MEASure:SETup:PSA {value}')

    def set_setup_psb(self, value: float):
        """Set phase setup B"""
        self.device.send_command(f':MEASure:SETup:PSB {value}')

    def set_setup_dsa(self, value: float):
        """Set delay setup A"""
        self.device.send_command(f':MEASure:SETup:DSA {value}')

    def set_setup_dsb(self, value: float):
        """Set delay setup B"""
        self.device.send_command(f':MEASure:SETup:DSB {value}')

    def set_statistic_display(self, enabled: bool):
        """Set statistics display"""
        self.device.send_command(f':MEASure:STATistic:DISPlay {1 if enabled else 0}')

    def set_statistic_mode(self, mode: str):
        """Set statistics mode"""
        valid_modes = ['EXTREMUM', 'DIFFERENCE', 'NORMAL']
        if mode.upper() not in [m.upper() for m in valid_modes]:
            raise ValueError(f'Invalid mode. Must be one of {valid_modes}')
        self.device.send_command(f':MEASure:STATistic:MODE {mode}')

    def reset_statistics(self):
        """Reset statistics"""
        self.device.send_command(':MEASure:STATistic:RESet')

    def set_statistic_item(self, item: str, value: str):
        """Set statistics item"""
        valid_items = ['VMAX', 'VMIN', 'VPP', 'VTOP', 'VBASe', 'VAMP', 'VAVG', 'VRMS', 
                      'OVERshoot', 'PREShoot', 'MARea', 'MPARea', 'PERiod', 'FREQuency', 
                      'RTIMe', 'FTIMe', 'PWIDth', 'NWIDth', 'PDUTy', 'NDUTy', 'RDELay', 
                      'FDELay', 'RPHase', 'FPHase', 'TVMAX', 'TVMIN', 'PSLEWrate', 
                      'NSLEWrate', 'VUPper', 'VMID', 'VLOWer', 'VARIance', 'PVRMS', 
                      'PPULses', 'NPULses', 'PEDGes', 'NEDGes']
        if item.upper() not in [i.upper() for i in valid_items]:
            raise ValueError(f'Invalid item. Must be one of {valid_items}')
        self.device.send_command(f':MEASure:STATistic:ITEM {item},{value}')

    def set_item(self, item: str, source: str):
        """Set measurement item"""
        valid_items = ['VMAX', 'VMIN', 'VPP', 'VTOP', 'VBASe', 'VAMP', 'VAVG', 'VRMS', 
                      'OVERshoot', 'PREShoot', 'MARea', 'MPARea', 'PERiod', 'FREQuency', 
                      'RTIMe', 'FTIMe', 'PWIDth', 'NWIDth', 'PDUTy', 'NDUTy', 'RDELay', 
                      'FDELay', 'RPHase', 'FPHase', 'TVMAX', 'TVMIN', 'PSLEWrate', 
                      'NSLEWrate', 'VUPper', 'VMID', 'VLOWer', 'VARIance', 'PVRMS', 
                      'PPULses', 'NPULses', 'PEDGes', 'NEDGes']
        if item.upper() not in [i.upper() for i in valid_items]:
            raise ValueError(f'Invalid item. Must be one of {valid_items}')
        self.device.send_command(f':MEASure:ITEM {item},{source}')

    def get_counter_value(self):
        """Get counter value"""
        return float(self.device.query(':MEASure:COUNter:VALue?'))

    def set_counter_source(self, source: str):
        """Set counter source"""
        valid_sources = ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 
                        'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'CHANnel1', 'CHANnel2', 
                        'CHANnel3', 'CHANnel4', 'LA', 'EXT']
        if source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        self.device.send_command(f':MEASure:COUNter:SOURce {source}')

    def clear_measurements(self):
        """Clear all measurements"""
        self.device.send_command(':MEASure:CLEar')

    def get_measurement(self, item: str, source: str = None):
        """Get measurement value
        
        Args:
            item: Measurement item (e.g., VPP, VRMS, PERiod)
            source: Source channel (e.g., CHANnel1)
            
        Returns:
            float: Measured value
        """
        valid_items = ['VMAX', 'VMIN', 'VPP', 'VTOP', 'VBASe', 'VAMP', 'VAVG', 'VRMS', 
                      'OVERshoot', 'PREShoot', 'MARea', 'MPARea', 'PERiod', 'FREQuency', 
                      'RTIMe', 'FTIMe', 'PWIDth', 'NWIDth', 'PDUTy', 'NDUTy', 'RDELay', 
                      'FDELay', 'RPHase', 'FPHase', 'TVMAX', 'TVMIN', 'PSLEWrate', 
                      'NSLEWrate', 'VUPper', 'VMID', 'VLOWer', 'VARIance', 'PVRMS', 
                      'PPULses', 'NPULses', 'PEDGes', 'NEDGes']
        if item.upper() not in [i.upper() for i in valid_items]:
            raise ValueError(f'Invalid item. Must be one of {valid_items}')
        
        command = f':MEASure:ITEM? {item}'
        if source:
            command += f',{source}'
        return float(self.device.query(command))

    def get_all_measurements(self):
        """Get all measurement values
        
        Returns:
            str: Comma-separated list of all measurements
        """
        return self.device.query(':MEASure:ITEM:ALL?')

    def get_frequency(self, source: str = None):
        """Get frequency measurement
        
        Args:
            source: Source channel (e.g., CHANnel1)
            
        Returns:
            float: Measured frequency in Hz
        """
        valid_sources = ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4', 'MATH']
        if source and source.upper() not in [s.upper() for s in valid_sources]:
            raise ValueError(f'Invalid source. Must be one of {valid_sources}')
        
        command = ':MEASure:FREQuency?'
        if source:
            command += f' {source}'
        return float(self.device.query(command))