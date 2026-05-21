# Rcon-honeypot

Simple Python honeypot for logging fake Minecraft RCON login attempts.

## Features
- Logs incoming connections
- Captures password attempts
- Sends alerts to Discord webhook
- Saves passwords to a text file

## Install
```bash
pip install requests
```

## Usage
1. Add your Discord webhook:
```python
discord_webhook = "YOUR_WEBHOOK_URL"
```

2. Run the script:
```bash
python honeypot.py
```

## Output
Captured passwords are saved to:
```text
honeypot_passwords.txt
```
