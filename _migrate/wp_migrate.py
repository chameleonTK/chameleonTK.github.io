from nerodia.browser import Browser

browser = Browser(browser='chrome')
browser.goto('http://wp.curve.in.th/wp-login.php?loggedout=true&wp_lang=en_US&jetpack-sso-show-default-form=1')
t = browser.text_field(id='user_login')
t.value = '**'

t = browser.text_field(id='user_pass')
t.value = '***'

browser.button(id='wp-submit').click()
browser.wait_until(timeout=2, interval=0.5, method=lambda e: e.title.startswith("Dashboard"))

posts = []
for i in range(1, 6):
    browser.goto(f'http://wp.curve.in.th/wp-admin/edit.php?paged={i}')

    for t in browser.trs(class_name="type-post"):
        p = {}
        date = t.td(class_name="date").span().text
        date = date.replace("/", "-")
        p["date"] = date
        link = t.div(class_name="row-actions").span(class_name="view").link().href
        p["view_link"] = link
        
        p["name"] = link.replace("http://wp.curve.in.th/", "")
        if "?" in p["name"]:
            print("SKIP", p["name"])
            continue
        p["edit_link"] = t.link(class_name="row-title").href
        p["title"] = t.link(class_name="row-title").text
        p["tags"] = [l.text for l in t.td(class_name="column-categories").links()]
        posts.append(p)

def export(p):
    fo = open(f"_export/{p['date']}-{p['name']}.md", "w", encoding="utf-8")
    browser.goto(p["edit_link"])
    text = ""
    text += '---'+'\n'
    text += 'layout: post'+'\n'
    text += f'title: {p["title"]}'+'\n'
    text += f'tags: [Archive, {",".join(p["tags"])}]'+'\n'
    text += f'thumbnail: "assets/img/{p["name"]}"'+'\n'
    text += 'author: Pakawat Nakwijit'+'\n'
    text += 'excerpt_separator: <!--more-->'+'\n'
    text += f'color: rgb(19, 196, 165)'+'\n'

    text += '---'+'\n\n'

    browser.divs(class_name="components-panel__body")[6].click()
    excerpt = browser.divs(class_name="components-panel__body")[6].textarea().value
    text += '## TL;DR'+'\n'
    text += excerpt+'\n'
    text += '<!--more-->'+'\n'

    body = browser.div(class_name="mce-content-body").text
    text += body+'\n'

    fo.write(text)
    fo.close()

cnt = 0
for p in posts:
    export(p)
    cnt +=1
    print("DONE", p["name"])
    # if cnt==5:
    #     break
    