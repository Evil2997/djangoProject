import argparse
import logging

import psutil

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def find_and_kill_ports(ports):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port in ports:
            try:
                proc = psutil.Process(conn.pid)
                logging.info(
                    f"Процесс {proc.name()} (PID: {proc.pid}) использует порт {conn.laddr.port}. Завершаем процесс.")
                proc.terminate()
                proc.wait(timeout=3)  # Ждём до 3 секунд
                if proc.is_running():
                    logging.warning(
                        f"Процесс {proc.name()} (PID: {proc.pid}) не завершился. Принудительно завершаем процесс.")
                    proc.kill()
                    proc.wait()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                logging.warning(f"Не удалось завершить процесс, использующий порт {conn.laddr.port}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Завершить процессы, использующие указанные порты.")
    parser.add_argument('ports', metavar='P', type=int, nargs='+', help="Список портов, которые необходимо освободить.")
    args = parser.parse_args()

    if not args.ports:
        parser.error("Порты не указаны. Пожалуйста, укажите хотя бы один порт для освобождения.")

    find_and_kill_ports(args.ports)


if __name__ == "__main__":
    main()
