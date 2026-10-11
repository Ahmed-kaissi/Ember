from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser


ROOT = Path(__file__).resolve().parent
PORTS = range(8765, 8786)


def create_server(root=ROOT, ports=PORTS):
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    for port in ports:
        try:
            return ThreadingHTTPServer(("127.0.0.1", port), handler), port
        except OSError:
            continue
    raise OSError("No free local port is available between 8765 and 8785.")


def main():
    if not (ROOT / "ember-ai.html").is_file():
        print("Ember could not find ember-ai.html beside this launcher.")
        print("Re-extract the complete ember-ai-package.zip and keep its files together.")
        return 1

    try:
        server, port = create_server()
    except OSError as error:
        print(f"Could not start Ember's local server: {error}")
        return 1

    version = (ROOT / "ember-ai.html").stat().st_mtime_ns
    url = f"http://127.0.0.1:{port}/ember-ai.html?v={version}"
    print(f"Ember is running at {url}")
    print("Keep this window open while you use Ember. Press Ctrl+C to stop.")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
