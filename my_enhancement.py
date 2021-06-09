import os
import shutil
import sys
import cv2


# enhancement 1
def get_file_and_destination():
    input_file = input("What is the file name?")
    mp4_converter = ".mp4"
    input_file = input_file + mp4_converter

    destination_file = input("Where you want to save it to?")
    return input_file, destination_file


# enhancement 2
def get_user_input():
    user_preference = input("Enter your frame preference in total: ")
    if not user_preference.isnumeric():
        print("Please enter an integer!")
        new_value = get_user_input()
        user_preference = new_value
    return user_preference


class FrameCapture:
    """
        Class definition to capture frames
    """

    # changed the parameters in order for user to give his own directory name
    def __init__(self, file_path, directory):
        """
            initializing directory where the captured frames will be stored.
            Also truncating the directory where captured frames are stored, if exists.
        """
        self.directory = directory
        self.file_path = file_path
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_frames(self):
        '''
            This method captures the frames from the video file provided.
            This program makes use of openCV library
        '''
        cv2_object = cv2.VideoCapture(self.file_path)

        frame_number = 0
        frame_found = 1
        # gets user preference
        get_value = get_user_input()
        while frame_found:
            frame_found, image = cv2_object.read()
            # will only get the range of what the user wants to collect
            while frame_number < int(get_value):
                capture = f'{self.directory}/frame{frame_number}.jpg'
                cv2.imwrite(capture, image)
                # will print the number out when collected
                print(f"Collected Frame Number: {frame_number}")
                frame_number += 1
            # thank you message and the loop will end
            print("Thank you!")
            break


if __name__ == '__main__':
    file_path, destination = get_file_and_destination()
    print(file_path)
    print(destination)

    fc = FrameCapture(file_path, destination)
    fc.capture_frames()
