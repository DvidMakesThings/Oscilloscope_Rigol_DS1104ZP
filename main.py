"""Main script for measuring 1kHz 3.3Vpp signal on Rigol oscilloscope"""

from rigol_scope import RigolScope
import time

def main():
    # Create oscilloscope instance and connect via LAN
    scope = RigolScope()
    
    try:
        # Connect using default LAN settings (192.168.0.5:5555)
        if not scope.connect_lan():
            print("Failed to connect to oscilloscope")
            return

        print("Connected to oscilloscope")
        
        # Get device identification
        idn = scope.ieee.get_identification()
        print(f"Device identification: {idn}")

        # Wait for connection to stabilize
        time.sleep(2)  # Increased wait time

        # Basic channel setup
        scope.channel.set_display(1, True)
        scope.channel.set_coupling(1, "DC")
        scope.channel.set_scale(1, 2)
        
        # Basic timebase setup
        scope.timebase.set_main_scale(0.0002)
        
        # Basic trigger setup
        scope.trigger.set_mode("EDGE")
        scope.trigger.set_edge_source("CHANnel1")
        scope.trigger.set_edge_slope("POSitive")
        scope.trigger.set_sweep("AUTO")
        scope.trigger.set_edge_level(1.0)

        # Wait for signal to stabilize
        time.sleep(2)

        # Measure frequency
        freq = scope.measure.get_frequency("CHANnel1")
        print(f"Frequency: {freq:.2f} Hz")

        # Measure Vpp
        vpp = scope.measure.get_measurement("VPP", "CHANnel1")
        print(f"Vpp: {vpp:.3f} V")

        # Additional measurements
        vrms = scope.measure.get_measurement("VRMS", "CHANnel1")
        period = scope.measure.get_measurement("PERiod", "CHANnel1")
        print(f"Vrms: {vrms:.3f} V")
        print(f"Period: {period*1000:.3f} ms")


        # Enable autoscale
        scope.system.set_autoscale(1)

        # Wait for measurements to stabilize
        time.sleep(1)

        # Additional measurements
        vpp = scope.measure.get_measurement("VPP", "CHANnel1")
        print(f"Vpp: {vpp:.3f} V")
        vrms = scope.measure.get_measurement("VRMS", "CHANnel1")
        period = scope.measure.get_measurement("PERiod", "CHANnel1")
        print(f"Vrms: {vrms:.3f} V")
        print(f"Period: {period*1000:.3f} ms")


    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if scope.connected:
            scope.disconnect()
            print("Disconnected from oscilloscope")

if __name__ == '__main__':
    main()