import cv2
from django.http import HttpResponseBadRequest, StreamingHttpResponse
from django.views.decorators import gzip

# Create a generator function to capture frames from the webcam
def generate_frames(camera_index):
    cap = cv2.VideoCapture(camera_index)
    
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        # Yield the frame as part of the multipart stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Define the video feed view with gzip compression
@gzip.gzip_page
def video_feed(request, camera_index=1):
    try:
        # Ensure the camera_index is an integer
        camera_index = int(camera_index)
    except ValueError:
        return HttpResponseBadRequest("Invalid camera index")

    # Set the content type for multipart streaming
    content_type = 'multipart/x-mixed-replace; boundary=frame'
    
    # Use the generator function to stream frames from the specified camera
    return StreamingHttpResponse(generate_frames(camera_index), content_type=content_type)
