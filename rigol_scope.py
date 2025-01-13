"""Main Rigol oscilloscope interface"""

import socket
import pyvisa as visa
from commands.acquire_commands import AcquireCommands
from commands.calibrate_commands import CalibrateCommands
from commands.channel_commands import ChannelCommands
from commands.cursor_commands import CursorCommands
from commands.decoder_commands import DecoderCommands
from commands.display_commands import DisplayCommands
from commands.etable_commands import ETableCommands
from commands.function_commands import FunctionCommands
from commands.ieee_commands import IEEECommands
from commands.la_commands import LACommands
from commands.mask_commands import MaskCommands
from commands.math_commands import MathCommands
from commands.measure_commands import MeasureCommands
from commands.reference_commands import ReferenceCommands
from commands.source_commands import SourceCommands
from commands.storage_commands import StorageCommands
from commands.system_commands import SystemCommands
from commands.timebase_commands import TimebaseCommands
from commands.trace_commands import TraceCommands
from commands.trigger_commands import TriggerCommands
from commands.waveform_commands import WaveformCommands

class RigolScope:
    def __init__(self):
        self.visa_rm = None
        self.device = None
        self.socket = None
        self.connected = False
        self.connection_type = None

        # Initialize all command groups
        self.acquire = AcquireCommands(self)
        self.calibrate = CalibrateCommands(self)
        self.channel = ChannelCommands(self)
        self.cursor = CursorCommands(self)
        self.decoder = DecoderCommands(self)
        self.display = DisplayCommands(self)
        self.etable = ETableCommands(self)
        self.function = FunctionCommands(self)
        self.ieee = IEEECommands(self)
        self.la = LACommands(self)
        self.mask = MaskCommands(self)
        self.math = MathCommands(self)
        self.measure = MeasureCommands(self)
        self.reference = ReferenceCommands(self)
        self.source = SourceCommands(self)
        self.storage = StorageCommands(self)
        self.system = SystemCommands(self)
        self.timebase = TimebaseCommands(self)
        self.trace = TraceCommands(self)
        self.trigger = TriggerCommands(self)
        self.waveform = WaveformCommands(self)

    def connect_usb(self, resource_name: str):
        """Connect to oscilloscope via USB"""
        try:
            self.visa_rm = visa.ResourceManager()
            self.device = self.visa_rm.open_resource(resource_name)
            self.connection_type = 'USB'
            self.connected = True
            return True
        except Exception as e:
            print(f"Failed to connect via USB: {str(e)}")
            return False

    def connect_lan(self, ip_address: str, port: int = 5555):
        """Connect to oscilloscope via LAN"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((ip_address, port))
            self.connection_type = 'LAN'
            self.connected = True
            return True
        except Exception as e:
            print(f"Failed to connect via LAN: {str(e)}")
            return False

    def disconnect(self):
        """Disconnect from oscilloscope"""
        try:
            if self.connection_type == 'USB' and self.device:
                self.device.close()
                self.visa_rm.close()
            elif self.connection_type == 'LAN' and self.socket:
                self.socket.close()
            
            self.device = None
            self.visa_rm = None
            self.socket = None
            self.connected = False
            self.connection_type = None
            return True
        except Exception as e:
            print(f"Failed to disconnect: {str(e)}")
            return False

    def send_command(self, command: str):
        """Send command to oscilloscope"""
        if not self.connected:
            raise ConnectionError("Not connected to oscilloscope")
        
        try:
            if self.connection_type == 'USB':
                self.device.write(command)
            elif self.connection_type == 'LAN':
                self.socket.send(f"{command}\n".encode())
            return True
        except Exception as e:
            print(f"Failed to send command: {str(e)}")
            return False

    def query(self, command: str) -> str:
        """Query oscilloscope and return response"""
        if not self.connected:
            raise ConnectionError("Not connected to oscilloscope")
        
        try:
            if self.connection_type == 'USB':
                return self.device.query(command).strip()
            elif self.connection_type == 'LAN':
                self.socket.send(f"{command}\n".encode())
                return self.socket.recv(4096).decode().strip()
        except Exception as e:
            print(f"Failed to query: {str(e)}")
            return ""