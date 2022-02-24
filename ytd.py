#/usr/bin/env python

#importing functions
import ytd_functions as ytdf
from datetime import datetime
import time as t

#main thread
def main():

    #main menu
    while True:
        
        ytdf.header(ytdf.standard_header, True)
        print("(1) - Download Youtube video/audio")
        print("(2) - Cut Video")
        print("(3) - Download and cut video")
        user_option = input("Option: ")

        match user_option:
            case "1":

                while True:
                    
                    ytdf.header(ytdf.standard_header, True)
                    ytdf.header("> Download Youtube Video")
                
                    url = input("- Video URL: ")
                    file_name = input(" - File output name: ")

                    if url == "" or file_name == "":
                        print("- Provide the info required!") ; input()
                    else:
                        print("- Success! Video downloaded!") if ytdf.download_video(url,file_name) else print("- Error! Video not downloaded!")
                        input()
                        break

            case "2":

                ytdf.header(ytdf.standard_header, True)
                ytdf.header("> Cut video")
                print("Option 2 logic here...") ; input()

            case "3":

                while True:

                    ytdf.header(ytdf.standard_header, True)
                    ytdf.header("> Download and Cut Youtube video")
                    
                    url = input("- Video URL: ")
                    file_name = input("- File output name: ")
                    start = input("- Start point: ")
                    end = input("- End point: ")

                    if ytdf.check_timestamps(start, end) and ytdf.check_url(url):
                        ytdf.download_and_cut_video(url, file_name, start, end)
                    break
        
            case("q"):
                print("Exiting now...")
                t.sleep(1)

            case _: 
                print("Insert a valid option...") ; t.sleep(1)

        if user_option.lower() == "q":
            break

if __name__ == "__main__":
   main()
