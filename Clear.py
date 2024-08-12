import logging

import pexpect

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def execute_commands_with_sudo(commands, password):
    results = []
    for command in commands:
        try:
            # Определяем, нужно ли использовать sudo
            if not command.startswith("python") and not command.startswith("python3") and not command.startswith(
                    "docker"):
                full_command = f"sudo {command}"
            else:
                full_command = command

            child = pexpect.spawn(full_command)

            # Если команда использует sudo, ожидаем ввода пароля
            if full_command.startswith("sudo"):
                child.expect("password")
                child.sendline(password)

            child.expect(pexpect.EOF)
            output = child.before.decode('utf-8')
            return_code = child.exitstatus

            results.append({
                "command": full_command,
                "output": output,
                "return_code": return_code
            })
        except pexpect.exceptions.ExceptionPexpect as e:
            logging.error(f"Не удалось выполнить команду '{full_command}': {e}")
            results.append({
                "command": full_command,
                "output": "",
                "error": str(e),
                "return_code": -1
            })
    return results


def main():
    commands = [
        "systemctl stop rabbitmq-server",
        "service rabbitmq-server stop",
        "docker-compose -f docker/rabbitmq/docker-compose.yml down",
        "python3 Free_ports.py 15672 6379",
    ]
    password = "12345678"  # Убедись, что пароль безопасен
    results = execute_commands_with_sudo(commands, password)

    for result in results:
        print(f"КОМАНДА:\n {result['command']}")
        print(f"РЕЗУЛЬТАТ:\n {result['output']}")
        print(f"КОД ВОЗВРАТА:\n {result['return_code']}")
        if 'error' in result:
            print(f"ОШИБКА:\n {result['error']}")
        print("=" * 44)


if __name__ == "__main__":
    main()
