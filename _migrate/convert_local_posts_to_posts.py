import os
import re
import sys
from shutil import copyfile
from encryption import *

root="../_posts_local"
target="../_posts"
gimages = {}

with open("../_migrate/imgs.csv") as fin:
    for line in fin:
        line = line.strip().split(",")
        # print(line)
        gimages[line[0].lower()] = line[1]

def encryptContent(localpath):
    secret = input("Please Enter Secret Key: ")
    if secret=="":
        return localpath
    
    newlocalpath = localpath.replace(".secret.md", ".md")
    fout = open(newlocalpath, "w", encoding="utf-8")
    with open(localpath, encoding="utf-8") as fin:
        secretMode = False
        secretText = ""
        for line in fin:
            if line.strip().startswith('<div class="secret">'):
                secretMode = True
            
            if secretMode:
                secretText += line+"\n"
            else:
                fout.write(line)
            if secretMode and line.strip().startswith('</div>'):
                print("secret text:")
                
                encrypted = encrypt(secret, secretText)
                fout.write('<div class="secret encrypted-secret">\n')
                fout.write(encrypted+"\n")
                fout.write('</div>\n')
                secretMode = False
    fout.close()
    
    return newlocalpath

def convert(path, name):
    newroot = path.replace(root, target)
    
    
    localpath = os.path.join(path, name)
    if localpath.endswith(".secret.md"):
        localpath = encryptContent(localpath)
        name = name.replace(".secret.md", ".md")
        
    
    prodpath = os.path.join(newroot, name)
    fout = open(prodpath, "w", encoding="utf-8")
    with open(localpath, encoding="utf-8") as fin:
        for line in fin:

            # change local image to image in google drive
            # if "include aligner.html" in line:
            if line.strip().startswith("{% include aligner.html"):
                match = re.search("images=['\"](.*)['\"]", line)
                images = match.group().replace("\"", "").replace("images=", "").split(",")

                # if "IMG_3763" in line:
                #     print(images)
                #     assert(False)

                links_to_gdrive = []
                for img in images:
                    if " " in img:
                        img = img.split(" ")[0]

                    img = img.lower()
                    if img in gimages:
                        links_to_gdrive.append(f"https://lh3.googleusercontent.com/d/{gimages[img]}")
                    else:
                        print("NO", img, line)
                        links_to_gdrive.append(img)
                
                match = re.search("column=(\\d+)", line)
                if match is None:
                    c = 1
                else:
                    column = match.group()
                    c = int(column.replace("column=", ""))
                
                images = ",".join(links_to_gdrive)


                custom = ""
                match = re.search("customclass=['\"](.*)['\"]", line)
                if match is not None:
                    custom = match.group().replace("\"", "").replace("customclass=", "")
                    line = '{% include aligner.html images="'+images+'" column='+str(c)+' customclass="'+custom+'" %}\n'    
                else:
                    line = '{% include aligner.html images="'+images+'" column='+str(c)+' %}\n'    
                # print(line)
            
            # save feature images to local
            elif line.strip().startswith("thumbnail:"):
                feat_image = line.replace("thumbnail:", "").replace("\"", "").replace("\'", "").strip()
                new_feat_image = feat_image.replace("assets/img/", "assets/feats/")

                
                p = "/".join(new_feat_image.split("/")[0:-1])
                
                # if not os.path.exists(p):
                #     os.makedirs(p)

                # if not os.path.exists(new_feat_image):
                #     print(feat_image, new_feat_image)
                #     copyfile(feat_image, new_feat_image)

                line = line.replace("assets/img/", "assets/feats/")

            elif line.strip().startswith("feature-img:"):
                
                feat_image = line.replace("feature-img:", "").replace("\"", "").replace("\'", "").strip()
                new_feat_image = feat_image.replace("assets/img/", "assets/feats/")

                
                p = "/".join(new_feat_image.split("/")[0:-1])
                
                # if not os.path.exists(p):
                #     os.makedirs(p)

                # if not os.path.exists(new_feat_image):
                #     copyfile(feat_image, new_feat_image)

                line = line.replace("assets/img/", "assets/feats/")

            fout.write(line)
    fout.close()
    
# for path, subdirs, files in os.walk(root):
    # newpath = path.replace(root, target)
#     if not os.path.exists(newpath):
#         os.makedirs(newpath)
        
        
#     for name in files:
#         if name.endswith(".DS_Store"):
#             continue
    
#         p = os.path.join(newpath, name)
#         print(p)
#         convert(path, name)
#         # break
#     # break
        
        
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No arguments provided.")
        sys.exit()
    
    path = sys.argv[1]
    splits = path.split("/")
    
    convert("/".join(splits[0:-1]), splits[-1])

    # # --- Test ---
    # KEY = "A"
    # original = "Hello from Python!"
    # encrypted = encrypt(KEY, original)
    # print(f"Encrypted: {encrypted}")

    # decrypted = decrypt(KEY, encrypted)
    # print(f"Decrypted: {decrypted}")