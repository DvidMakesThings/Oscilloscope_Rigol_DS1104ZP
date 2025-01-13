"""Decoder commands for Rigol oscilloscope"""

class DecoderCommands:
    def __init__(self, device):
        self.device = device

    def set_mode(self, decoder: int, mode: str):
        """Set decoder mode"""
        valid_modes = ['PARallel', 'RS232', 'IIC', 'SPI']
        if mode.upper() not in valid_modes:
            raise ValueError(f'Invalid mode. Must be one of {valid_modes}')
        self.device.send_command(f':DECoder{decoder}:MODE {mode}')

    def set_display(self, decoder: int, enabled: bool):
        """Set decoder display"""
        self.device.send_command(f':DECoder{decoder}:DISPlay {1 if enabled else 0}')

    def set_format(self, decoder: int, format: str):
        """Set decoder format"""
        valid_formats = ['HEX', 'ASCii', 'DEC', 'BIN']
        if format.upper() not in valid_formats:
            raise ValueError(f'Invalid format. Must be one of {valid_formats}')
        self.device.send_command(f':DECoder{decoder}:FORMat {format}')

    def set_position(self, decoder: int, position: int):
        """Set decoder position"""
        self.device.send_command(f':DECoder{decoder}:POSition {position}')

    def set_threshold(self, decoder: int, channel: int, threshold: float):
        """Set decoder threshold"""
        self.device.send_command(f':DECoder{decoder}:THREshold:CHANnel{channel} {threshold}')

    def set_config_label(self, decoder: int, label: str):
        """Set decoder label"""
        self.device.send_command(f':DECoder{decoder}:CONFig:LABel {label}')

    def set_config_line(self, decoder: int, line: str):
        """Set decoder line"""
        self.device.send_command(f':DECoder{decoder}:CONFig:LINE {line}')

    def set_config_format(self, decoder: int, format: str):
        """Set decoder config format"""
        self.device.send_command(f':DECoder{decoder}:CONFig:FORMat {format}')

    def set_config_endian(self, decoder: int, endian: str):
        """Set decoder endian"""
        valid_endians = ['LSB', 'MSB']
        if endian.upper() not in valid_endians:
            raise ValueError(f'Invalid endian. Must be one of {valid_endians}')
        self.device.send_command(f':DECoder{decoder}:CONFig:ENDian {endian}')

    def set_config_width(self, decoder: int, width: int):
        """Set decoder width"""
        self.device.send_command(f':DECoder{decoder}:CONFig:WIDth {width}')

    def get_config_srate(self, decoder: int):
        """Get decoder sample rate"""
        return float(self.device.query(f':DECoder{decoder}:CONFig:SRATe?'))

    def uart_set_tx_source(self, decoder: int, source: str):
        """Set UART TX source"""
        self.device.send_command(f':DECoder{decoder}:UART:TX {source}')

    def iic_set_sda(self, decoder: int, source: str):
        """Set IIC SDA source"""
        self.device.send_command(f':DECoder{decoder}:IIC:SDA {source}')

    def spi_set_mode(self, decoder: int, mode: str):
        """Set SPI mode"""
        self.device.send_command(f':DECoder{decoder}:SPI:MODE {mode}')

    def parallel_set_clock(self, decoder: int, source: str):
        """Set parallel clock source"""
        self.device.send_command(f':DECoder{decoder}:PARallel:CLK {source}')