import interop as interop
import argparse as argparse


def connect_to_client(givenURL, givenUser, givenPass):
    client = interop.Client(url=givenURL,
                          username=givenUser,
                          password=givenPass)

    if (client):
        print("Successful Connection to client")
    else:
        print("Connection to client failed")


def main():

    parser = argparse.ArgumentParser(description="Interop Server Command Line Interface")

    parser.add_argument("--url", required=True,
                        help="URL for Server")
    parser.add_argument("--username", required=True,
                        help="Username for Account")
    parser.add_argument("--password", required=True,
                        help="Password for Account")

    args = parser.parse_args()

    connect_to_client(args.url, args.username, args.password)


if __name__ == "__main__":
    main()
