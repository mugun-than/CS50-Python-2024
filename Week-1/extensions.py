def main():
    filename = input("File name: ")
    if '.' in filename:
        document, extension = filename.lower().strip().rsplit(sep = '.', maxsplit = 1)
        match extension:
            case "gif" | "jpeg" | "png":
                print(f"image/{extension}")
            case "jpg":
                print("image/jpeg")
            case "pdf" | "zip":
                print(f"application/{extension}")
            case "txt":
                print("text/plain")
            case _:
                print("application/octet-stream")
    else:
        print("application/octet-stream")


main()
