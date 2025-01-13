# Rigol DS1104ZP Oscilloscope Automation Script

This project provides a script to help automate measurements with the Rigol DS1104Z Plus Oscilloscope. It includes functionalities for waveform acquisition and FFT analysis.

## Features

- Connect to the Rigol DS1104Z Plus Oscilloscope via USB or LAN.
- Acquire waveform data from the oscilloscope.
- Perform FFT analysis on the acquired waveform data.
- Plot the waveform and FFT spectrum using Matplotlib.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- PyVISA

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DvidMakesThings/Oscilloscope_Rigol_DS1104ZP.git
    cd Oscilloscope_Rigol_DS1104ZP
    ```

2. Install the required Python packages:
    ```sh
    pip install numpy matplotlib pyvisa
    ```

## Usage

1. Connect the Rigol DS1104Z Plus Oscilloscope to your computer via USB or LAN.

2. Run the script with the appropriate connection type and parameters:
    ```sh
    python main.py --connection usb --resource 'USB0::0x1AB1::0x04CE::DS1ZA160801111::INSTR'
    ```
    or
    ```sh
    python main.py --connection lan --ip 192.168.1.100 --port 5555
    ```

## Command Line Arguments

- `--connection`: Connection type (`usb` or `lan`). Default is `usb`.
- `--ip`: IP address for LAN connection. Default is `192.168.1.100`.
- `--port`: Port number for LAN connection. Default is `5555`.
- `--resource`: USB resource string. Default is `USB0::0x1AB1::0x04CE::DS1ZA160801111::INSTR`.

## Example

To connect via USB and acquire waveform data:
```sh
python main.py --connection usb --resource 'USB0::0x1AB1::0x04CE::DS1ZA160801111::INSTR'
```

To connect via LAN and acquire waveform data:
```sh
python main.py --connection lan --ip 192.168.1.100 --port 5555
```

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

## Contact

For any questions or feedback, please contact:
- Email: [s.dvid@hotmail.com](mailto:s.dvid@hotmail.com)
- GitHub: [DvidMakesThings](https://github.com/DvidMakesThings)