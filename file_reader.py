try: 
    fname = input("Enter file name: ")
    fh = open(fname)
    
    file_contents = fh.read()
    formatted_contents = file_contents.upper().rstrip()
    print(formatted_contents)
    fh.close()
except FileNotFoundError:
    print(f"File '(fname)' not found.")
except Exception as e:
    print (f"An error occurred: {e}")