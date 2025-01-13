"""Event Table commands for Rigol oscilloscope"""

class ETableCommands:
    def __init__(self, device):
        self.device = device

    def set_display(self, table: int, enabled: bool):
        """Set event table display"""
        self.device.send_command(f':ETABle{table}:DISP {1 if enabled else 0}')

    def set_format(self, table: int, format: str):
        """Set event table format"""
        self.device.send_command(f':ETABle{table}:FORMat {format}')

    def set_view(self, table: int, view: str):
        """Set event table view"""
        self.device.send_command(f':ETABle{table}:VIEW {view}')

    def set_column(self, table: int, column: str):
        """Set event table column"""
        self.device.send_command(f':ETABle{table}:COLumn {column}')

    def set_row(self, table: int, row: str):
        """Set event table row"""
        self.device.send_command(f':ETABle{table}:ROW {row}')

    def set_sort(self, table: int, sort: str):
        """Set event table sort"""
        self.device.send_command(f':ETABle{table}:SORT {sort}')

    def get_data(self, table: int):
        """Get event table data"""
        return self.device.query(f':ETABle{table}:DATA?')