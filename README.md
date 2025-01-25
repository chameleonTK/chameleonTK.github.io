# About Me

![IMTK](/assets/img/me.png?raw=true "IMTK")

Hi, I'm Pakawat Nakwijit (please call me **TK**). I'm a unofficial PhD under the supervision of [Prof. Matthew Purver](http://www.eecs.qmul.ac.uk/~mpurver/) at Queen Mary University of London.

My main research interests lie in Computational Linguistics, particularly its applications in the Thai language 🇹🇭. Specifically, my current research focuses on the semantics of spelling variation in Thai. For example, considering *มาก* and *มว๊าก* —while both mean `a lot`, the latter seems to be `a lot more` than the former one. Similarly, *มึง* and *เมิง* both literally serve as second-person pronouns, but the latter carries a relatively less aggressive tone. 
                    
Moreover, I'm also interested in Mathematics, and Philosophy in general.

Professionally, I work as a web developer and, more recently, as a project manager (?). I have contributed to the development of various web platforms, including an online magazine, a data-intensive platform designed to handle terabytes of data and generate extensive reports, and a mobile application leveraging web technologies.

In my spare time, I play a lot of boardgames [[BGG account](https://boardgamegeek.com/user/chameleontk)] and enjoy sharing my passion through my own blog (mostly written in Thai 🇹🇭).


Btw, thank to [Type on Strap](https://github.com/sylhare/Type-on-Strap) for this really cool template.

## Write a new blog
* create a file in `_post` in format `YYYY-MM-DD-blog_name.md`
* Then, copy a template from the previous blogs
    * check `tags`, `color` and `thumbnail`

* After it works ok locally then please upload all images to the google drive 
* run `_migrate/list_folders.py` 
* copy new content from `_img_folders.csv`to `img_folders.csv`
* run `_migrate/list_images.py` to generate `imgs.csv`
* then copy the new post to `_posts_local`
* then run `_migrate/convert_local_posts_to_posts.py` to generate posts in `_posts`

* finally, push everything

## Serve the website locally
```
bundle exec jekyll serve
```


## Create Google Credential
1. Open the [Google Cloud console](https://console.cloud.google.com/).
2. At the top-left, click Menu menu > APIs & Services > Credentials.
3. Click Create Credentials > OAuth client ID.
4. Click Application type > Desktop application.
5. Enable Google Drive API






