import os
import transaction

CODESPACE_NAME = os.environ.get("CODESPACE_NAME", None)
if CODESPACE_NAME:
    DOMAIN = os.environ["GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN"]
    hostname = f"{CODESPACE_NAME}-8080.{DOMAIN}"
    app.virtual_hosting.set_map(f"localhost:8080/VirtualHostBase/https/{hostname}:443/VirtualHostRoot")
    transaction.commit()
