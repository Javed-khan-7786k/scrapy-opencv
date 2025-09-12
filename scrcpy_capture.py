import cv2
import numpy as np
import mss
import pygetwindow as gw

class ScrcpyCapture:
    def __init__(self, window_title="phonecam"):
        """
        Initialize ScrcpyCapture
        :param window_title: Title of the scrcpy window (use --window-title when starting scrcpy)
        """
        # Find scrcpy window
        windows = gw.getWindowsWithTitle(window_title)
        if not windows:
            raise Exception(f"❌ Scrcpy window '{window_title}' not found! "
                            f"Run scrcpy with: scrcpy --window-title {window_title}")
        self.win = windows[0]

        # Define bounding box
        self.bbox = (
            self.win.left,
            self.win.top,
            self.win.left + self.win.width,
            self.win.top + self.win.height,
        )

        # Initialize mss
        self.sct = mss.mss()

    def read(self):
        """
        Capture a single frame (like VideoCapture.read())
        :return: (ret, frame)
        """
        screenshot = self.sct.grab(self.bbox)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        return True, frame

    def release(self):
        """Release resources (not strictly needed for mss)"""
        self.sct.close()
# Example usage 
#cap = ScrcpyCapture(window_title="phonecam")  # Match the title you used with scrcpy