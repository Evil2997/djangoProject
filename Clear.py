import pexpect


def execute_commands_with_sudo(commands, password):
    results = []
    for command in commands:
        try:
            if command.startswith("python") or command.startswith("python3"):
                full_command = command
            else:
                full_command = f"sudo {command}"

            child = pexpect.spawn(full_command)

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
        "python3 Free_ports.py 15672 6379 15673 5672",
    ]
    password = "12345678"
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
