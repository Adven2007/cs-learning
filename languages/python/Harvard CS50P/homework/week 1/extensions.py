name = input("File name: ").strip().lower()
dot = name.rfind(".")
if (dot == -1):
    print("application/octet-stream")
else:
    suffix = name[dot:]
    match suffix:
        case ".gif" | ".jpeg" | ".png":
            print("image/" + name[(dot + 1):])
        case ".jpg":
            print("image/jpeg")
        case ".pdf" | ".zip":
            print("application/" + name[(dot + 1):])
        case ".txt":
            print("text/plain")
        case _:
            print("application/octet-stream")