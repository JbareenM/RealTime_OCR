import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import PIL.Image as Pim


def convert_to_frames(new_folder, file):
    cap = cv2.VideoCapture(file)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fc = 0
    ret = True

    rgb_folder = new_folder + '/RGB'
    grey_folder = new_folder + '/greyscale'
    os.mkdir(rgb_folder)
    os.mkdir(grey_folder)

    while (fc < frameCount  and ret):
        ret, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(rgb_folder + '/' + str(fc) + '.png', frame)
        cv2.imwrite(grey_folder + '/' + str(fc) + '.png', gray_frame)
        fc += 1

    cap.release()


def video_to_numpy_rgb_array(file):
    cap = cv2.VideoCapture(file)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))
    fc = 0
    ret = True

    while (fc < frameCount and ret):
        ret, buf[fc] = cap.read()
        fc += 1
    cap.release()

    return buf


def video_to_numpy_grey_array(file):
    cap = cv2.VideoCapture(file)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth), np.dtype('uint8'))
    fc = 0
    ret = True

    while (fc < frameCount and ret):
        ret, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        buf[fc] = gray_frame
        fc += 1
    cap.release()

    return buf

def flow_to_numpy_array(file):
    cap = cv2.VideoCapture(file)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    u_buf = np.empty((frameCount - 1, frameHeight, frameWidth))
    v_buf = np.empty((frameCount - 1, frameHeight, frameWidth), np.dtype('uint8'))
    mag_buf = np.empty((frameCount - 1, frameHeight, frameWidth))
    ang_buf = np.empty((frameCount - 1, frameHeight, frameWidth))
    fc = 0
    ret = True
    prev_grey = None

    while fc < frameCount and ret:
        ret, frame = cap.read()
        next_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if fc >= 1:
            flow = cv2.calcOpticalFlowFarneback(prev_grey, next_grey, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            mag_buf[fc - 1] = mag
            ang_buf[fc - 1] = ang
            u_buf[fc - 1] = flow[:, :, 0]
            v_buf[fc - 1] = flow[:, :, 1]

        prev_grey = next_grey
        fc += 1

    cap.release()

    return u_buf, v_buf, mag_buf, ang_buf


def save_optical_flow_to_folder(file, folder):
    cap = cv2.VideoCapture(file)
    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame1)
    hsv[..., 1] = 255
    fc = 0
    ret = True
    while (ret):
        ret, frame2 = cap.read()
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imwrite(folder + str(fc) + '.png', bgr)
        fc += 1

    cap.release()


if __name__ == "__main__":

    folder = "D:/Stage/Data/Avenue/testing_videos/"

    # for file in os.listdir(folder):
    #     if file.endswith(".avi"):
    #         file_base_name = file[:-4]
    #         new_folder = folder + file_base_name + '_frames'
    #         os.mkdir(new_folder)
    #         convert_to_frames(new_folder, folder + file)

    # u_buf, v_buf, mag_buf, ang_buf = flow_to_numpy_array(folder + '01.avi')

    save_optical_flow_to_folder(folder + '01.avi', folder + '01_frames/optical_flow/')

    #
    # np.save('u_buf.npy', u_buf)
    # np.save('v_buf.npy', v_buf)
    # np.save('ang_buf.npy', ang_buf)
    # np.save('mag_buf.npy', mag_buf)

    # u_buf = np.load('u_buf.npy')
    # v_buf = np.load('v_buf.npy')
    # mag_buf = np.load('mag_buf.npy')
    # ang_buf = np.load('ang_buf.npy')

    # frames = u_buf.shape[0]
    # im_height = u_buf.shape[1]
    # im_width = u_buf.shape[2]
    #
    # hsv = np.zeros((im_height, im_width, 3))
    # hsv[..., 1] = 255
    # #
    # mag = np.sqrt(u_buf[0] ** 2 + v_buf[0] ** 2)
    # ang = np.arctan2(v_buf[0], u_buf[0])
    #
    # plt.imshow(mag)
    # plt.show()
    # plt.imshow(mag_buf[0])
    # plt.show()
    # plt.imshow(ang)
    # plt.show()
    # plt.imshow(ang_buf[0])
    # plt.show()

    # frame_width = mag_buf.shape[1]
    # frame_height= mag_buf.shape[2]
    #
    # hsv = np.zeros((frame_width, frame_height, 3))
    # hsv[..., 1] = 255
    #
    # for i in range(14):
    #     hsv[..., 0] = ang_buf[i] * 180 / np.pi / 2
    #
    #     # min_mag = np.min(mag_buf[i])
    #     # max_mag = np.max(mag_buf[i])
    #     # diff = max_mag - min_mag
    #     # hsv[..., 2] = (mag_buf[i] - min_mag) / diff
    #
    #     hsv[..., 2] = cv2.normalize(mag_buf[i], None, 0, 255, cv2.NORM_MINMAX)
    #
    #     im = Pim.fromarray(hsv, 'HSV')
    #     im.convert('RGB').save(folder + '01_frames/optical_flow/' + str(i) + '.png')