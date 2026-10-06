Drop your organisation's root CA certificate(s) here as `*.crt` (PEM) if your
network inspects HTTPS traffic. They're added to the image's trust store at build
time and used by pip and requests. Don't commit them: `*.crt` is git-ignored.
