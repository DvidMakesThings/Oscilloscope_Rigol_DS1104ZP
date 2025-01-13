"""Storage commands for Rigol oscilloscope"""

class StorageCommands:
    def __init__(self, device):
        self.device = device

    def set_image_type(self, type: str):
        """Set image type"""
        valid_types = ['PNG', 'BMP', 'TIFF']
        if type.upper() not in valid_types:
            raise ValueError(f'Invalid type. Must be one of {valid_types}')
        self.device.send_command(f':STORage:IMAGe:TYPE {type}')

    def set_image_invert(self, enabled: bool):
        """Set image invert"""
        self.device.send_command(f':STORage:IMAGe:INVERT {1 if enabled else 0}')

    def set_image_color(self, color: str):
        """Set image color"""
        valid_colors = ['COLor', 'GRAYscale']
        if color.upper() not in valid_colors:
            raise ValueError(f'Invalid color. Must be one of {valid_colors}')
        self.device.send_command(f':STORage:IMAGe:COLor {color}')