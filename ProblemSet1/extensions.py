'''
Problem Set 1
Program: File Extensions
Alexis Varas Ortiz
'''

def main():
    #Asks for input from user. Removed whitespace. Converts string to lowercase
    file_name = input("File name: ").strip().lower()
    #Splits the string into a list when a '.' is found
    ext = file_name.split(".") #

    #Calls function. Pases the value of the last index of the list into the argument
    media(ext[-1])

def media(e):
    #Compares extension to determine the media type for the file
    match e:
        case "gif":
            print("image/" + e)
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/" + e)
        case "pdf":
            print("application/" + e)
        case "zip":
            print("application/" + e)
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


main()
