import cv2

# Program parameters
Q_PARAMETER = 10
GOP_MODE = False
GOP_SIZE = 4


f_cnt = 1
vid = cv2.VideoCapture('input.avi')
ret, prev_frame = vid.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('quantized.avi', fourcc, int(vid.get(5)), (int(vid.get(3)), int(vid.get(4))), False)
out.write(prev_frame)
while vid.isOpened():
    ret, c_frame = vid.read()
    f_cnt += 1
    if not ret:
        break
    c_frame = cv2.cvtColor(c_frame, cv2.COLOR_BGR2GRAY)
    if GOP_MODE:
        if f_cnt % GOP_SIZE != 0:
            diff = (c_frame - prev_frame) // Q_PARAMETER
            out.write(diff)
        else:
            out.write(c_frame)
    else:
        diff = (c_frame - prev_frame) // Q_PARAMETER
        out.write(diff)
    prev_frame = c_frame

vid.release()
out.release()
