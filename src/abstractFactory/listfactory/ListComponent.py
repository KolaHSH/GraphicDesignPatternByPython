from abstractFactory.factory.Component import Link, Tray


class ListLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def makeHTML(self):
        return " <li><a href=\"{0}\">{1}</a></li>\n".format(self.url, self.caption)


class ListTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def makeHTML(self):
        buffer = ""
        buffer += "<li>\n"
        buffer += self.caption + "\n"
        buffer += "<ul>\n"
        for _, tray in enumerate(self.tray):
            buffer += tray.makeHTML()
        buffer += "</ul>\n"
        buffer += "</li>\n"
        return buffer
