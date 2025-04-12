# import cv2
# import numpy as np
# import os
# import time
# import sys

# def test_dependencies():
#     print("Testing dependencies...")
#     try:
#         print(f"OpenCV version: {cv2.__version__}")
#     except Exception as e:
#         print(f"Error with OpenCV: {e}")
#         return False
    
#     try:
#         import mediapipe as mp
#         print(f"MediaPipe version: {mp.__version__}")
#     except Exception as e:
#         print(f"Error with MediaPipe: {e}")
#         return False
    
#     try:
#         print(f"NumPy version: {np.__version__}")
#     except Exception as e:
#         print(f"Error with NumPy: {e}")
#         return False
    
#     try:
#         import tensorflow as tf
#         print(f"TensorFlow version: {tf.__version__}")
#     except Exception as e:
#         print(f"Warning: TensorFlow not available: {e}")
#         print("Some AI features may not work, but basic functionality should be fine.")
    
#     return True

# def test_camera():
#     print("Testing camera access...")
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Could not open camera.")
#         return False
    
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Could not read frame from camera.")
#         cap.release()
#         return False
    
#     print(f"Camera working. Frame shape: {frame.shape}")
#     cap.release()
#     return True

# def test_file_access():
#     print("Testing file access...")
    
#     # Test output directory
#     output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Test models directory
#     models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
#     os.makedirs(models_dir, exist_ok=True)
    
#     # Test file writing
#     test_file = os.path.join(output_dir, "test_file.txt")
#     try:
#         with open(test_file, 'w') as f:
#             f.write("Test file write successful")
        
#         with open(test_file, 'r') as f:
#             content = f.read()
        
#         os.remove(test_file)
#         print("File access working.")
#         return True
#     except Exception as e:
#         print(f"Error with file access: {e}")
#         return False

# def test_modules():
#     print("Testing application modules...")
    
#     try:
#         from hand_tracking import HandTracker
#         tracker = HandTracker()
#         print("Hand tracking module working.")
#     except Exception as e:
#         print(f"Error with hand tracking module: {e}")
#         return False
    
#     try:
#         from gesture_recognition import GestureRecognizer
#         recognizer = GestureRecognizer()
#         print("Gesture recognition module working.")
#     except Exception as e:
#         print(f"Error with gesture recognition module: {e}")
#         return False
    
#     try:
#         from canvas_engine import CanvasEngine
#         canvas = CanvasEngine(640, 480)
#         print("Canvas engine module working.")
#     except Exception as e:
#         print(f"Error with canvas engine module: {e}")
#         return False
    
#     try:
#         from ui import UIManager
#         ui = UIManager(640, 480)
#         print("UI module working.")
#     except Exception as e:
#         print(f"Error with UI module: {e}")
#         return False
    
#     try:
#         from ai_features import AIFeatures
#         ai = AIFeatures()
#         print("AI features module working.")
#     except Exception as e:
#         print(f"Error with AI features module: {e}")
#         return False
    
#     try:
#         from optimizations import PerformanceOptimizer
#         optimizer = PerformanceOptimizer()
#         print("Optimizations module working.")
#     except Exception as e:
#         print(f"Error with optimizations module: {e}")
#         return False
    
#     return True

# def test_main_application():
#     print("Testing main application import...")
    
#     try:
#         from main import GestureArt
#         print("Main application module working.")
#         return True
#     except Exception as e:
#         print(f"Error with main application module: {e}")
#         return False

# def run_tests():
#     print("Running GestureArt system tests...")
#     print("-" * 50)
    
#     tests = [
#         ("Dependencies", test_dependencies),
#         ("Camera", test_camera),
#         ("File Access", test_file_access),
#         ("Modules", test_modules),
#         ("Main Application", test_main_application)
#     ]
    
#     all_passed = True
    
#     for name, test_func in tests:
#         print(f"\nTesting {name}...")
#         try:
#             result = test_func()
#             if result:
#                 print(f"✓ {name} test PASSED")
#             else:
#                 print(f"✗ {name} test FAILED")
#                 all_passed = False
#         except Exception as e:
#             print(f"✗ {name} test ERROR: {e}")
#             all_passed = False
    
#     print("\n" + "-" * 50)
#     if all_passed:
#         print("All tests PASSED! GestureArt should work correctly.")
#         print("Run 'python main.py' to start the application.")
#     else:
#         print("Some tests FAILED. Please check the errors above.")
    
#     return all_passed

# if __name__ == "__main__":
#     success = run_tests()
#     sys.exit(0 if success else 1)












import cv2
import numpy as np
import os
import time
import sys
def test_dependencies():
    print("Testing dependencies...")
    try:
        print(f"OpenCV version: {cv2.__version__}")
    except Exception as e:
        print(f"Error with OpenCV: {e}")
        return False
    try:
        import mediapipe as mp
        print(f"MediaPipe version: {mp.__version__}")
    except Exception as e:
        print(f"Error with MediaPipe: {e}")
        return False
    try:
        print(f"NumPy version: {np.__version__}")
    except Exception as e:
        print(f"Error with NumPy: {e}")
        return False
    try:
        import tensorflow as tf
        print(f"TensorFlow version: {tf.__version__}")
    except Exception as e:
        print(f"Warning: TensorFlow not available: {e}")
        print("Some AI features may not work, but basic functionality should be fine.")
    return True
def test_camera():
    print("Testing camera access...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return False
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from camera.")
        cap.release()
        return False
    print(f"Camera working. Frame shape: {frame.shape}")
    cap.release()
    return True
def test_file_access():
    print("Testing file access...")
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    os.makedirs(models_dir, exist_ok=True)
    test_file = os.path.join(output_dir, "test_file.txt")
    try:
        with open(test_file, 'w') as f:
            f.write("Test file write successful")
        with open(test_file, 'r') as f:
            content = f.read()
        os.remove(test_file)
        print("File access working.")
        return True
    except Exception as e:
        print(f"Error with file access: {e}")
        return False
def test_modules():
    print("Testing application modules...")
    try:
        from hand_tracking import HandTracker
        tracker = HandTracker()
        print("Hand tracking module working.")
    except Exception as e:
        print(f"Error with hand tracking module: {e}")
        return False
    try:
        from gesture_recognition import GestureRecognizer
        recognizer = GestureRecognizer()
        print("Gesture recognition module working.")
    except Exception as e:
        print(f"Error with gesture recognition module: {e}")
        return False
    try:
        from canvas_engine import CanvasEngine
        canvas = CanvasEngine(640, 480)
        print("Canvas engine module working.")
    except Exception as e:
        print(f"Error with canvas engine module: {e}")
        return False
    try:
        from ui import UIManager
        ui = UIManager(640, 480)
        print("UI module working.")
    except Exception as e:
        print(f"Error with UI module: {e}")
        return False
    try:
        from ai_features import AIFeatures
        ai = AIFeatures()
        print("AI features module working.")
    except Exception as e:
        print(f"Error with AI features module: {e}")
        return False
    try:
        from optimizations import PerformanceOptimizer
        optimizer = PerformanceOptimizer()
        print("Optimizations module working.")
    except Exception as e:
        print(f"Error with optimizations module: {e}")
        return False
    return True
def test_main_application():
    print("Testing main application import...")
    try:
        from main import GestureArt
        print("Main application module working.")
        return True
    except Exception as e:
        print(f"Error with main application module: {e}")
        return False
def run_tests():
    print("Running GestureArt system tests...")
    print("-" * 50)
    tests = [
        ("Dependencies", test_dependencies),
        ("Camera", test_camera),
        ("File Access", test_file_access),
        ("Modules", test_modules),
        ("Main Application", test_main_application)
    ]
    all_passed = True
    for name, test_func in tests:
        print(f"\nTesting {name}...")
        try:
            result = test_func()
            if result:
                print(f"✓ {name} test PASSED")
            else:
                print(f"✗ {name} test FAILED")
                all_passed = False
        except Exception as e:
            print(f"✗ {name} test ERROR: {e}")
            all_passed = False
    print("\n" + "-" * 50)
    if all_passed:
        print("All tests PASSED! GestureArt should work correctly.")
        print("Run 'python main.py' to start the application.")
    else:
        print("Some tests FAILED. Please check the errors above.")
    return all_passed
if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)