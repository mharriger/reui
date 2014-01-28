import reui
import pydispatch

app = reui.App()

def hdlr(self, **args):
    print args

pydispatch.dispatcher.connect(hdlr, sender=pydispatch.any)
