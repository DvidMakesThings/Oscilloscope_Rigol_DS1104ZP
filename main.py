"""Main script for Rigol oscilloscope waveform acquisition and FFT analysis"""

import numpy as np
import matplotlib.pyplot as plt
from rigol_scope import RigolScope
import argparse

def acquire_and_plot_data(scope):
    """Acquire and plot waveform data"""
    # Configure waveform parameters
    scope.waveform.set_source('CHANnel1')  # Set channel 1 as source
    scope.waveform.set_mode('NORMal')      # Set normal mode
    scope.waveform.set_format('BYTE')      # Set byte format

    # Request waveform data
    raw_data = scope.query(':WAV:DATA?')

    # Process the data
    # Skip first 11 bytes (header) and last byte (terminator)
    # Header format: #9000012345 where 9 is the length of the number that follows (000012345)
    header_length = 11
    data = [int(byte) for byte in raw_data[header_length:-1].encode('latin-1')]
    wave = np.array(data)

    # Calculate FFT
    fft_size = 2048
    fft_spec = np.fft.fft(wave, fft_size)
    fft_rms = np.abs(fft_spec)
    fft_db = 20 * np.log10(fft_rms)

    # Plot results
    plt.figure(figsize=(12, 8))

    # Plot waveform
    plt.subplot(211)
    plt.plot(wave)
    plt.title('Waveform')
    plt.xlabel('Sample Points')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot FFT
    plt.subplot(212)
    plt.plot(fft_db[:fft_size//2])  # Plot only positive frequencies
    plt.title('FFT Spectrum')
    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Rigol Oscilloscope Data Acquisition')
    parser.add_argument('--connection', choices=['usb', 'lan'], default='usb',
                      help='Connection type (usb or lan)')
    parser.add_argument('--ip', default='192.168.1.100',
                      help='IP address for LAN connection')
    parser.add_argument('--port', type=int, default=5555,
                      help='Port number for LAN connection')
    parser.add_argument('--resource', 
                      default='USB0::0x1AB1::0x04CE::DS1ZA160801111::INSTR',
                      help='USB resource string')
    
    args = parser.parse_args()

    # Create oscilloscope instance
    scope = RigolScope()
    connected = False

    try:
        # Connect based on specified connection type
        if args.connection == 'usb':
            connected = scope.connect_usb(args.resource)
            if not connected:
                print("Failed to connect via USB")
                return
        else:  # LAN connection
            connected = scope.connect_lan(args.ip, args.port)
            if not connected:
                print(f"Failed to connect via LAN to {args.ip}:{args.port}")
                return

        print(f"Successfully connected via {args.connection.upper()}")
        
        # Get device identification
        idn = scope.ieee.get_identification()
        print(f"Device identification: {idn}")

        # Acquire and plot the data
        acquire_and_plot_data(scope)

    finally:
        if connected:
            scope.disconnect()
            print("Disconnected from oscilloscope")

if __name__ == '__main__':
    main()