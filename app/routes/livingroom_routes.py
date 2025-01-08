from flask import render_template, request, redirect, url_for, Response, current_app as app
import cv2

global camera
camera = None
global streaming
streaming = False

@app.route('/livingroom')
def livingroom():
    return render_template('livingroom.html')

@app.route('/toggle_light', methods=['POST'])
def toggle_light():
    light_status = request.form.get('light_status')
    print(f'Light status: {light_status}')
    return redirect(url_for('livingroom'))

def gen_frames():
    global camera
    camera = cv2.VideoCapture(0)  # Use 0 for webcam
    global streaming
    while streaming:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_camera')
def start_camera():
    global streaming
    streaming = True
    return redirect(url_for('livingroom'))

@app.route('/stop_camera')
def stop_camera():
    global streaming
    streaming = False
    global camera
    if camera is not None:
        camera.release()
        camera = None
    return redirect(url_for('livingroom'))
