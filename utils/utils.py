#-*-coding:utf-8-*-

def add_page_to_sitemap(url):
    file_content =''
    with open('/home/sivigik/Sivigik/public/sitemap.xml', 'r') as file:
        file_content = file.read()

    file_content = file_content.replace('</urlset>', '\n')
    file_content += '<url><loc>' + url + '</loc></url>\n</urlset>'

    with open('/home/sivigik/Sivigik/public/sitemap.xml', 'w') as file:
        file.write(file_content)
