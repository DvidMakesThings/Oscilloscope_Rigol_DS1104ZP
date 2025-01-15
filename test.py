import socket

# Oscilloscope details
HOST = '192.168.0.5'  # Oscilloscope IP
PORT = 5555  # Default port for SCPI over LAN

def send_scpi_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall((command + '\n').encode('utf-8'))
        response = s.recv(1024).decode('utf-8').strip()
        return response

if __name__ == "__main__":
    print("Requesting ID...")
    idn = send_scpi_command("*IDN?")
    print(f"Oscilloscope ID: {idn}")
