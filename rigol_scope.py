# Main Rigol oscilloscope interface

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
    DEFAULT_USB_RESOURCE = 'ASRL/dev/ttyUSB0::INSTR'
    DEFAULT_IP = '192.168.0.5'  # Default IP for LAN connection
    DEFAULT_PORT = 5555  # Default port for LAN connection (set to match VISA resource)
    VISA_RESOURCE = 'TCPIP0::192.168.0.5::INSTR'  # Correct VISA resource for the scope

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

    def connect_usb(self, resource_name: str = None):
        """Connect to oscilloscope via USB/serial"""
        try:
            self.visa_rm = visa.ResourceManager('@py')
            resource = resource_name or self.DEFAULT_USB_RESOURCE
            self.device = self.visa_rm.open_resource(resource)
            self.device.timeout = 5000  # Increase timeout to 5 seconds
            self.connection_type = 'USB'
            self.connected = True
            return True
        except Exception as e:
            print(f"Failed to connect via USB: {str(e)}")
            return False

    def connect_lan(self, ip_address: str = None, port: int = None):
        """Connect to oscilloscope via LAN"""
        ip_address = ip_address or self.DEFAULT_IP
        port = port or self.DEFAULT_PORT
        try:
            self.visa_rm = visa.ResourceManager('@py')
            self.device = self.visa_rm.open_resource(self.VISA_RESOURCE)
            self.device.timeout = 5000  # Set timeout for LAN communication
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
            elif self.connection_type == 'LAN' and self.device:
                self.device.close()
                self.visa_rm.close()
            
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
            if self.connection_type in ['USB', 'LAN']:
                self.device.write(command)
            return True
        except Exception as e:
            print(f"Failed to send command: {str(e)}")
            return False

    def query(self, command: str) -> str:
        """Query oscilloscope and return response"""
        if not self.connected:
            raise ConnectionError("Not connected to oscilloscope")
        
        try:
            if self.connection_type in ['USB', 'LAN']:
                return self.device.query(command).strip()
        except Exception as e:
            print(f"Failed to query: {str(e)}")
            return ""

    def get_sources(self):
        """Get available sources for waveform"""
        return ['CHANnel1', 'CHANnel2', 'CHANnel3', 'CHANnel4', 'MATH', 'FFT', 'LA']
