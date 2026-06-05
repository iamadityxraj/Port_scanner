import socket

print("=" * 50)
print("PYTHON PORT SCANNER")
print("=" * 50)

target = input("Enter Target IP or Website: ")

for port in range(1, 101):

    scanner = socket.socket()

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    scanner.close()