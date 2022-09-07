import serial
import time
import pygame

import cv2

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

X = 480
Y = 320
cap= cv2.VideoCapture(0)
cap.set(3, X )  # Set horizontal resolution
cap.set(4, Y )  # Set vertical resolution
cap.set(5, 31)

def cv2ImageToSurface(cv2Image):
    if cv2Image.dtype.name == 'uint16':
        cv2Image = (cv2Image / 256).astype('uint8')
    size = cv2Image.shape[1::-1]
    if len(cv2Image.shape) == 2:
        cv2Image = np.repeat(cv2Image.reshape(size[1], size[0], 1), 3, axis = 2)
        format = 'RGB'
    else:
        format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
        cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.01)
    arduino.write(bytes('0', 'utf-8'))
    data = arduino.readline()
    return data


pygame.init()
white = (236, 0, 117)
display =pygame.display.set_mode((X, Y ))
pygame.display.set_caption('T-Liftzz')
pygame.display.update()

mouses2=150

while True:
    ret, frame = cap.read()
    frame= cv2.rotate(frame, cv2.ROTATE_180)
    frame= cv2ImageToSurface(frame)
    pygame.draw.circle( display, white, (X,Y), 1,1 )
    display.fill(white)
    frame = pygame.transform.scale(frame, ((X,Y)))
    display.blit(frame, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
         
    keys = pygame.key.get_pressed()
    mouses= int(pygame.mouse.get_pos()[0])
    mouse_move=mouses2-mouses
        
    if mouse_move>0:
         value = write_read("q")
    elif mouse_move<0:
         value = write_read("e") 

    if keys[pygame.K_w]:
        value = write_read("w")
    if keys[pygame.K_s]:
        value = write_read("s")
    if keys[pygame.K_a]:
        value = write_read("a")
    if keys[pygame.K_d]:
        value = write_read("d")
    if keys[pygame.K_q]:
        value = write_read("q")
    if keys[pygame.K_e]:
        value = write_read("e") 
    if keys[pygame.K_1]:
        value = write_read("1")
    if keys[pygame.K_2]:
        value = write_read("2")
    elif keys[pygame.K_3]:
        value = write_read("3") 
    mouses2= int(pygame.mouse.get_pos()[0])
    
    pygame.display.update() 
                
cap.release()

