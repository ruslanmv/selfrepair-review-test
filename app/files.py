from pathlib import Path

UPLOADS = Path("/srv/uploads")


def read_upload(name: str) -> bytes:
    return (UPLOADS / name).read_bytes()


def save_upload(name: str, data: bytes) -> None:
    path = UPLOADS / name
    f = open(path, "wb")
    f.write(data)
