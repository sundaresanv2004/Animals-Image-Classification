import cv2
# import tensorflow as tf

cap = cv2.VideoCapture(0)
# model = tf.keras.models.load_model('first.h5')

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(5) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()