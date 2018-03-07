import interop as interop


def connect_to_client(givenUser, givenPass):
    client = interop.Client(url='http://127.0.0.1:8000',
                          username=givenUser,
                          password=givenPass)

    if (client):
        print("Successful Connection to client")
    else:
        print("Connection to client failed")


def main():
    connect_to_client("testuser", "testpass")


if __name__ == "__main__":
    main()
