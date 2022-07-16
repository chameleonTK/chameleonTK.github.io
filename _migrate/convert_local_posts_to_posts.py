import os
import re

from shutil import copyfile

root="../_posts_local"
target="../_posts"
gimages = {}

with open("../_migrate/imgs.csv") as fin:
    for line in fin:
        line = line.strip().split(",")
        # print(line)
        gimages[line[0]] = line[1]

for path, subdirs, files in os.walk(root):
    newpath = path.replace(root, target)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for name in files:
        p = os.path.join(newpath, name)
        fout = open(p, "w", encoding="utf-8")

        print(os.path.join(path, name))
        with open(os.path.join(path, name), encoding="utf-8") as fin:
            for line in fin:

                # change local image to image in google drive
                # if "include aligner.html" in line:
                if line.strip().startswith("{% include aligner.html"):
                    match = re.search("images=['\"](.*)['\"]", line)
                    images = match.group().replace("\"", "").replace("images=", "").split(",")

                    links_to_gdrive = []
                    for img in images:
                        if img in gimages:
                            links_to_gdrive.append(f"https://drive.google.com/uc?export=view&id={gimages[img]}")
                        else:
                            print("NO", line, os.path.join(path, name))
                            links_to_gdrive.append(img)
                    
                    match = re.search("column=(\d+)", line)
                    if match is None:
                        c = 1
                    else:
                        column = match.group()
                        c = int(column.replace("column=", ""))
                    
                    images = ",".join(links_to_gdrive)
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
        # break
    # break
        
        
