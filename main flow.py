import os
import shutil
import cv2


class FrameCapture:
    """
        Class definition to capture frames
    """

    def __init__(self, file_path):
        """
            initializing directory where the captured frames will be stored.
            Also truncating the directory where captured frames are stored, if exists.
        """
        self.directory = "captured_frames"
        self.file_path = file_path
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_frames(self):
        """
            This method captures the frames from the video file provided.
            This program makes use of openCV library
        """
        cv2_object = cv2.VideoCapture(self.file_path)

        frame_number = 0
        frame_found = 1

        while frame_found:
            frame_found, image = cv2_object.read()
            capture = f'{self.directory}/frame{frame_number}.jpg'
            cv2.imwrite(capture, image)

            frame_number += 1

    def getting_webcam(self):
        cap = cv2.VideoCapture(0)
        # loop to get frames

        while 1:
            # read every frame from
            ret, videoframe = cap.read()

            # Display the frame
            cv2.imshow('Camera', videoframe)
            # delay
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # quit_now = input("QUIT?")
            # return quit_now
        #  camera realesing
        cap.release()

        # destroying all windows
        cv2.destroyAllWindows()


if __name__ == '__main__':
    user_input = input("You wanna get webcam?")
    file_path = "caa.mp4"
    fc = FrameCapture(file_path)
    if user_input == "yes":
        fc.getting_webcam()

    fc.capture_frames()
