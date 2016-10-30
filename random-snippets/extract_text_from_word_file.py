#You can extract the text content from each Microsoft Word document in a directory
#tree on Windows into a corresponding text file.
#With the PyWin32 extension,we can access Word itself,through COM,to perform
#the conversion:
import fnmatch, os, sys, win32com.client
wordapp = win32com.client.gencache.EnsureDispatch("Word.Application")
try:
    for path, dirs, files in os.walk(sys.argv[1]):
        for filename in files:
        if not fnmatch.fnmatch(filename, '*.doc'): continue
        doc = os.path.abspath(os.path.join(path, filename))
        print "processing %s" % doc
        wordapp.Documents.Open(doc)
        docastxt = doc[:-3] + 'txt'
        wordapp.ActiveDocument.SaveAs(docastxt,
            FileFormat=win32com.client.constants.wdFormatText)
        wordapp.ActiveDocument.Close( )
finally:
    # ensure Word is properly shut down even if we get an exception
    wordapp.Quit( )