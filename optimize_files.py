import os
import cv2
import sys



def compress(self, source, destination, QUALITY_PERCENTAGE = 90):
        UNKNOWN_DIR = source
        COMPRESS_DIR = destination+"/Optimized/"
        
        if not os.path.exists(COMPRESS_DIR):
            os.mkdir(COMPRESS_DIR)
        print("Optimizing", UNKNOWN_DIR)

        count = fileCount(UNKNOWN_DIR)
        curr_count = 0

        for path, _, files in os.walk(UNKNOWN_DIR):

            for img_name in files:
                curr_count+=1
                self.label_4.setText(str(str(curr_count)+" out of "+str(count)+" images optimized"))
                img_path = os.path.join(path, img_name)

                img_rel_path = os.path.relpath(img_path, UNKNOWN_DIR)

                img_name = os.path.basename(img_path)
                try:
                    img = cv2.imread(img_path)
                except:
                    continue

                if img is not None:
                    self.label_4.setText(str(str(curr_count)+" out of "+str(count)+" images optimized"))
                    print('Original Dimensions : '+img_name,img.shape)
                    scale_percent = 60 
                    shape = img.shape
                    if shape[0] > shape[1]:
                        if shape[0] <= 2160:
                            scale_percent = 100
                        else:
                            scale_percent = 216000 / shape[0]
                            print(scale_percent)
                    else:
                        if shape[1] <= 2160:
                            scale_percent = 100
                        else:
                            scale_percent = 216000 / shape[1]
                            print(scale_percent)

                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                    
                    print('Resized Dimensions : ',resized.shape)

                    dir_name = os.path.dirname(img_rel_path)
                    if not os.path.exists(COMPRESS_DIR+dir_name) and not COMPRESS_DIR+dir_name == "":
                        os.makedirs(COMPRESS_DIR+dir_name)
                    img_rel_path = img_rel_path.rsplit(".", 1)[0]+".jpg"
                    cv2.imwrite(COMPRESS_DIR+img_rel_path, resized, [int(cv2.IMWRITE_JPEG_QUALITY), QUALITY_PERCENTAGE])

        self.label_4.setText("Complete. "+str(count)+" images optimized")

def fileCount(folder):
    "count the number of files in a directory"
    exts = ['.bmp', '.dib','.jpeg','.jpg','.jp2','.png','.webp',
            '.pbm','.pgm','.ppm','.pxm','.pnm','.pfm','.sr','.ras',
            '.tiff','.tif','.exr','.hdr','.pic']
    count = 0

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        
        if os.path.isfile(path):
            if path.endswith(tuple(exts)):
                count += 1
        elif os.path.isdir(path):
            count += fileCount(path)

    return count
