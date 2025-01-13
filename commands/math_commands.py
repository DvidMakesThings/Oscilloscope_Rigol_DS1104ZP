"""Math commands for Rigol oscilloscope"""

class MathCommands:
    def __init__(self, device):
        self.device = device

    def set_display(self, enabled: bool):
        """Enable/disable math display"""
        self.device.send_command(f':MATH:DISPlay {1 if enabled else 0}')

    def set_operator(self, operator: str):
        """Set math operator"""
        valid_operators = ['ADD', 'SUBTract', 'MULTiply', 'DIVision', 'AND', 'OR', 'XOR', 'NOT',
                         'FFT', 'INTG', 'DIFF', 'SQRT', 'LOG', 'LN', 'EXP', 'ABS']
        if operator.upper() not in valid_operators:
            raise ValueError(f'Invalid operator. Must be one of {valid_operators}')
        self.device.send_command(f':MATH:OPERator {operator}')

    def set_source1(self, source: str):
        """Set first source"""
        self.device.send_command(f':MATH:SOURce1 {source}')

    def set_source2(self, source: str):
        """Set second source"""
        self.device.send_command(f':MATH:SOURce2 {source}')

    def set_scale(self, scale: float):
        """Set vertical scale"""
        self.device.send_command(f':MATH:SCALe {scale}')

    def set_offset(self, offset: float):
        """Set vertical offset"""
        self.device.send_command(f':MATH:OFFSet {offset}')

    def set_invert(self, enabled: bool):
        """Enable/disable invert"""
        self.device.send_command(f':MATH:INVert {1 if enabled else 0}')

    def reset(self):
        """Reset math settings"""
        self.device.send_command(':MATH:RESet')

    def set_fft_source(self, source: str):
        """Set FFT source"""
        self.device.send_command(f':MATH:FFT:SOURce {source}')

    def set_fft_window(self, window: str):
        """Set FFT window"""
        valid_windows = ['RECTangle', 'HANNing', 'HAMMing', 'BLACkman', 'FLATtop']
        if window.upper() not in valid_windows:
            raise ValueError(f'Invalid window. Must be one of {valid_windows}')
        self.device.send_command(f':MATH:FFT:WINDow {window}')

    def set_fft_split(self, enabled: bool):
        """Set FFT split display"""
        self.device.send_command(f':MATH:FFT:SPLit {1 if enabled else 0}')

    def set_fft_unit(self, unit: str):
        """Set FFT unit"""
        self.device.send_command(f':MATH:FFT:UNIT {unit}')

    def set_fft_hscale(self, scale: float):
        """Set FFT horizontal scale"""
        self.device.send_command(f':MATH:FFT:HSCale {scale}')

    def set_fft_hcenter(self, center: float):
        """Set FFT center frequency"""
        self.device.send_command(f':MATH:FFT:HCENter {center}')

    def set_fft_mode(self, mode: str):
        """Set FFT mode"""
        self.device.send_command(f':MATH:FFT:MODE {mode}')

    def set_filter_type(self, type: str):
        """Set filter type"""
        self.device.send_command(f':MATH:FILTer:TYPE {type}')

    def set_filter_w1(self, freq: float):
        """Set filter frequency 1"""
        self.device.send_command(f':MATH:FILTer:W1 {freq}')

    def set_filter_w2(self, freq: float):
        """Set filter frequency 2"""
        self.device.send_command(f':MATH:FILTer:W2 {freq}')

    def set_option_start(self, start: float):
        """Set operation start"""
        self.device.send_command(f':MATH:OPTion:STARt {start}')

    def set_option_end(self, end: float):
        """Set operation end"""
        self.device.send_command(f':MATH:OPTion:END {end}')

    def set_option_invert(self, enabled: bool):
        """Set operation invert"""
        self.device.send_command(f':MATH:OPTion:INVert {1 if enabled else 0}')

    def set_option_sensitivity(self, sens: float):
        """Set operation sensitivity"""
        self.device.send_command(f':MATH:OPTion:SENSitivity {sens}')

    def set_option_distance(self, dist: float):
        """Set operation distance"""
        self.device.send_command(f':MATH:OPTion:DIStance {dist}')

    def set_option_ascale(self, enabled: bool):
        """Set auto scale"""
        self.device.send_command(f':MATH:OPTion:ASCale {1 if enabled else 0}')

    def set_option_threshold1(self, threshold: float):
        """Set threshold 1"""
        self.device.send_command(f':MATH:OPTion:THReshold1 {threshold}')

    def set_option_threshold2(self, threshold: float):
        """Set threshold 2"""
        self.device.send_command(f':MATH:OPTion:THReshold2 {threshold}')

    def set_option_fx_source1(self, source: str):
        """Set FX source 1"""
        self.device.send_command(f':MATH:OPTion:FX:SOURce1 {source}')

    def set_option_fx_source2(self, source: str):
        """Set FX source 2"""
        self.device.send_command(f':MATH:OPTion:FX:SOURce2 {source}')

    def set_option_fx_operator(self, operator: str):
        """Set FX operator"""
        self.device.send_command(f':MATH:OPTion:FX:OPERator {operator}')