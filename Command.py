import argparse
import cv2
from rembg import remove
from PIL import Image
import os


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    #print(args.input)
    #print(args.output)

    input_path = args.input
    output_path = args.output
    
    #inputパス確認
    if os.path.exists(input_path) == True :
       print("Path exists!")

       #背景削除
       input = Image.open(input_path)
       output = remove(input)
       output.save(output_path)
       os.remove(input_path)

       #outputパス確認
       if os.path.exists(output_path) == False :
        print("outPath doesn't exist!")


    else :
       print("inPath doesn't exist!")




    #input_path = "CommandInput/" + args.name + args.extension
    #print(input_path)
    #output_path = 'CommandOutput/003.png'

    #input = Image.open(input_path)
    #output = remove(input)
    #output.save(output_path)

    #img = cv2.imread(input_path)
    #cv2.imshow("image",img)
    #cv2.waitKey(0)
                
                

                
                
             
                