#!/bin/python

from __future__ import print_function
import sys
import os
from pdfrw import PdfReader
import sys

def getName(fname):
    try :
        title = PdfReader(fname).Info.Title
    except Exception as e:
        print("WARNING: cannot read %s : %s" % (fname, str(e)), file=sys.stderr)
        return None

    return title.strip("()") + ".pdf" if title is not None else None

for x in sys.argv[1:]:
    name = getName(x)
    if name is None:
        print("WARNING: %s does not have a title" % (x), file=sys.stderr)
    else :
        newName = os.path.join(os.path.dirname(x), name)

        if os.path.exists(newName):
            print("WARNING: %s already exists" % (newName), file=sys.stderr)
        else:
            # print("Renaming %s -> %s" % (x, newName))

            try :
                os.rename(x, newName)
            except Exception as e:
                print("WARNING: cannot rename %s : %s" % (x, str(e)), file=sys.stderr)


