import pexpect


def execute_commands_with_sudo(commands, password):
    results = []
    for command in commands:
        try:
            full_command = f"sudo {command}"

            child = pexpect.spawn(full_command)
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


def main(if_stopped_redis_now=False):
    commands = [
        "systemctl stop redis",
        "service redis stop",
        "docker-compose down",
    ]
    password = "12345678"
    if not if_stopped_redis_now:
        commands = [commands[2]]
    results = execute_commands_with_sudo(commands, password)

    for result in results:
        print(f"COMMAND:\n {result['command']}")
        print(f"OUTPUT:\n {result['output']}")
        print(f"RETURN CODE:\n {result['return_code']}")
        print("=" * 100)


if __name__ == "__main__":
    if_stopped_redis_now = False
    main(if_stopped_redis_now)
