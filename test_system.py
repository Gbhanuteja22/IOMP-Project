import cv2
import numpy as np
import os
import sys

def run_basic_check():
    print("Running basic GestureArt system check...")
    print("-" * 50)
    try:
        import mediapipe
        import tensorflow
        print(f"OpenCV: {cv2.__version__}")
        print(f"MediaPipe: {mediapipe.__version__}")
        print(f"NumPy: {np.__version__}")
        print(f"TensorFlow: {tensorflow.__version__}")
    except Exception as e:
        print(f"Error during dependency check: {e}")
        return False

    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            print("Camera check failed.")
            return False
    except Exception as e:
        print(f"Camera access error: {e}")
        return False

    print("✓ All basic checks PASSED")
    return True

if __name__ == "__main__":
    success = run_basic_check()
    print("-" * 50)
    if success:
        print("All tests PASSED! GestureArt is ready to run.")
    else:
        print("Some checks FAILED. Please verify your setup.")
    sys.exit(0 if success else 1)
