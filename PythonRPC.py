# https://youtu.be/VeIiU9qTsGI

import keyboard
import socket
import time

print("Python's working")
host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

#큐브 시작 위치 
startPos = [0, 0, 0] #Vector3   +X = 0, +Y = 0, +Z = 0

#무한루프
while True:
    key_input = keyboard.read_key();

    # 0.5초 마다 (sleep 0.5 sec)
    time.sleep(0.5)

    if key_input == 'left':
        print("Left");
        startPos[0] -=1; # -X 방향

    elif key_input == "right":
        print("Right");
        startPos[0] +=1; # +X 방향
        
    elif key_input == "up":
        print("Up");
        startPos[2] +=1; # +Z 방향
        
    elif key_input == "down":
        print("Down");
        #startPos[3] +=1;
        startPos[2] -=1; # -Z 방향
        

    # 벡터를 스트링으로 바꾼다
    posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
    print(posString)

    #위에 문자(스트링)를 바이트로 전환하고 보낸다(send)
    sock.sendall(posString.encode("UTF-8")) #Converting string to Byte, and sending it to C#
    # C#에서 데이터를 다시 받는 부분
    receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
    print(receivedData)