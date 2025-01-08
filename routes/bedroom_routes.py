from flask import render_template, request, redirect, url_for, Response, current_app as app
import cv2

bedroom_camera_url = "https://127.168.123.31:4000"

@app.route('/bedroom')
def bedroom():
    return render_template('bedroom.html')

def gen_bedroom_frames():
    camera = cv2.VideoCapture(bedroom_camera_url)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/bedroom_video_feed')
def bedroom_video_feed():
    return Response(gen_bedroom_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_bedroom_camera')
def start_bedroom_camera():
    return redirect(url_for('bedroom'))

@app.route('/stop_bedroom_camera')
def stop_bedroom_camera():
    global camera
    if camera is not None:
        camera.release()
        camera = None
    return redirect(url_for('bedroom'))
