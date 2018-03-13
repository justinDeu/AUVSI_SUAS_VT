import interop as interop
import argparse as argparse


# Attempts to connect to the given interop client with the 
# Credentials provided
def connect_to_client(givenURL, givenUser, givenPass):
    client = interop.Client(url=givenURL,
                          username=givenUser,
                          password=givenPass)

    if (client):
        print("Successful Connection to client")
    else:
        print("Connection to client failed")

    return client

# Downloads the available missions from the interop client passed in
# and stores them in a local text file names 'missions.txt'
# TODO test file and add date before each file addition
def download_missions(client):

    file = open("missions.txt", "a")
    missions = client.get_missions()

    for mission in missions:
        file.write(mission)
        file.write()

    for line in file:
        print(line)
        print()

    file.close()


# The main method of the file that is ran when the file is opened directly
# This establishes the parser and analyzes the necessary arguements
def main():

    parser = argparse.ArgumentParser(description="Interop Server Command Line Interface")

    parser.add_argument("--url", required=True,
                        help="URL for Server")
    parser.add_argument("--username", required=True,
                        help="Username for Account")
    parser.add_argument("--password", required=True,
                        help="Password for Account")
    parser.add_argument("-missions",
            help="Downloads the missions available to a text file")

    args = parser.parse_args()

    client = connect_to_client(args.url, args.username, args.password)

    download_missions(client)


if __name__ == "__main__":
    main()
