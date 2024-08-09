import psutil
import argparse

def find_and_kill_ports(ports):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port in ports:
            try:
                proc = psutil.Process(conn.pid)
                print(f"Process {proc.name()} (PID: {proc.pid}) is using port {conn.laddr.port}. Terminating process.")
                proc.terminate()
                proc.wait()  # Ждём завершения процесса
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

def main():
    parser = argparse.ArgumentParser(description="Kill processes using specified ports.")
    parser.add_argument('ports', metavar='P', type=int, nargs='+', help="List of ports to be freed.")
    args = parser.parse_args()

    find_and_kill_ports(args.ports)

if __name__ == "__main__":
    main()
