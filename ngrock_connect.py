from pyngrok import ngrok

# Open a SSH tunnel
# <NgrokTunnel: "tcp://0.tcp.ngrok.io:12345" -> "localhost:22">
ssh_tunnel = ngrok.connect("8443")
print(ssh_tunnel.public_url)
input()