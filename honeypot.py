import socket
import struct
import requests

discord_webhook = ""

def send_to_discord(content):
    data = {"content": content}
    try:
        requests.post(discord_webhook, json=data)
    except Exception as e:
        print(f"Failed to send to Discord: {e}")

def start_honeypot(port=25575):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(100)
    print(f"[*] Fake RCON honeypot listening on port {port}")
    send_to_discord(f"[*] Fake RCON honeypot started on port {port}")
    while True:
        client, addr = server.accept()
        print(f"[+] Connection from {addr[0]}:{addr[1]}")
        send_to_discord(f"[+] Connection from {addr[0]}:{addr[1]}")
        data = client.recv(1024)
        if len(data) > 12:
            pkt_type = struct.unpack("<i", data[8:12])[0]
            if pkt_type == 3:
                body = data[12:].split(b'\x00')[0]
                password = body.decode('utf-8', errors='ignore')
                print(f"[!] PASSWORD ATTEMPT: {password}")
                send_to_discord(f"[!] PASSWORD ATTEMPT FROM {addr[0]}:{addr[1]} : {password}")
                with open("honeypot_passwords.txt", "a") as f:
                    f.write(f"{addr[0]}:{password}\n")
        client.close()

start_honeypot()