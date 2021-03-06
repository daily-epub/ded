from dominate.tags import *
import uuid

class Chapter:
    def __init__(self, title=None, subtitle=None):
        self.id = uuid.uuid4()

        self.chapter = article(_class="chapter")

        self.chapter.add(h1(title, id=self.id, _class="chapter__title"))
        if subtitle:
            self.chapter.add(p(subtitle, _class="chapter__subtitle"))
        self.chapter.add(hr())

        self.content = self.chapter.add(div(_class="chapter__content"))
        self.appendixes = []

    def add(self, what):
        return self.content.add(what)

    def add_appendix(self, appendix):
        appendix.add(br())
        appendix.add(a("<< Back", href="#{0}".format(self.id), _class="appendix__back_to_chapter"))
    
        return self.appendixes.append(appendix)

class Appendix:
    def __init__(self, title=None, subtitle=None, id=""):
        self.appendix = article(_class="appendix")
        
        self.appendix.add(h4(title, id=id, _class="appendix__title"))
        if subtitle:
            self.appendix.add(p(subtitle, _class="appendix__subtitle"))

        self.content = self.appendix.add(div(_class="appendix__content"))
        
    def add(self, what):
        return self.content.add(what)
