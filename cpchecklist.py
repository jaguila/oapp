import win32com.client
import os
from time import gmtime, strftime


study=raw_input("What study is this for?")
rid=raw_input("What is the report id?")
rname=raw_input("What is the full report name?")
#website=raw_input("what is the website in which you found this job?")
#f=raw_input("what is the file location of coverletter? (If you do not know type NA)")
f2=raw_input("location of checklist? (If you do not know type NA)")
#if f2=="NA":
#	f3="H:\templates\CP Checklist_latest2.docx"
#else:
#	f3=f2



docstuff='.docx'
study2=str(rname+docstuff)
#study5=str(study+'resume'+docstuff)

folder2=str(os.path.join("H:\\studies",study))
print folder2
#raw_input("1?")
folder3=str(os.path.join("H:\\studies",study,rid))
print folder2

def createfolder(folder2):
	if not os.path.exists(folder2):
		os.makedirs(folder2)
	else:
		print "folder already exists"

		

createfolder(folder2)
createfolder(folder3)

study3=str(os.path.join("H:\\studies",study,rid,study2))
#study4=str(os.path.join("C:\\Users\\Dex\\Dropbox\\resumes",study,study5))


def wordreplace(word_file, replaceit, replaceit2,docname):
	wdFindContinue =1
	wdReplaceAll = 2
	e=win32com.client.Dispatch("Word.Application");
	#makes doc visible
	e.Visible=1
	e.DisplayAlerts = 0
	#open coverletter.doc
	if word_file=="NA":
		doc=e.Documents.Open("H:\\templates\\cptemplate.docx")
	else:
		doc=e.Documents.Open(word_file)
	#find this text
	e.Selection.Find.Execute('<studynum>', False, False, False, False, False, True, wdFindContinue, False, replaceit, wdReplaceAll)
	e.Selection.Find.Execute('<tester>', False, False, False, False, False, True, wdFindContinue, False, "Dexter Aguila", wdReplaceAll)
	e.Selection.Find.Execute('<report name>', False, False, False, False, False, True, wdFindContinue, False, replaceit2, wdReplaceAll)
	e.Selection.Find.Execute('<date>', False, False, False, False, False, True, wdFindContinue, False, strftime("%d %b %y") , wdReplaceAll)
	e.ActiveDocument.SaveAs(docname)
#	e.ActiveDocument.Close(SaveChanges=True)
#	e.Quit()
	return


wordreplace(f2, study,rid, study3)

"""
def wordreplace2(word_file, replaceit, replaceit2,docname):
	wdFindContinue =1
	wdReplaceAll = 2
	e=win32com.client.Dispatch("Word.Application");
	#makes doc visible
	e.Visible=1
	e.DisplayAlerts = 0
	#open coverletter.doc
	if word_file=="pharma":
		doc=e.Documents.Open("C:\Users\Dex\Dropbox\resumes\anwar\AguilaJohnDextertemplate.doc")
	else:
		doc=e.Documents.Open(word_file)
	#find this text
	e.Selection.Find.Execute('[position]', False, False, False, False, False, True, wdFindContinue, False, replaceit, wdReplaceAll)
	e.Selection.Find.Execute('[website]', False, False, False, False, False, True, wdFindContinue, False, replaceit2, wdReplaceAll)
	e.ActiveDocument.SaveAs(docname)
	e.ActiveDocument.Close(SaveChanges=True)
	e.Quit()
	return
wordreplace2(f2, pos, website, f2)
"""
"""
def search_replace_all(word_file, find_str, replace_str):
	wdFindContinue =1
	wdReplaceAll = 2
	
	#Dispatch() attempts to do a getobject() before creating a new one.
	#dispatchex() just creates a new one.
	app = win32com.client.DispatchEx("Word.Application")
	app.Visible = 1
	app.DisplayAlerts = 0
	app.Documents.Open(word_file)
    # expression.Execute(FindText, MatchCase, MatchWholeWord,	
    #   MatchWildcards, MatchSoundsLike, MatchAllWordForms, Forward, 
    #   Wrap, Format, ReplaceWith, Replace)
	app.Selection.Find.Execute(find_str, False, False, False, False, False, True, wdFindContinue, False, replace_str, wdReplaceAll)
	app.ActiveDocument.Close(SaveChanges=True)
	app.Quit()

f="C:\Python27\cover letter.doc"
search_replace_all(f, '1111', pos)
"""






"""
 .Forward = True
    .Wrap = wdFindContinue
    .Format = False
    .MatchCase = False
    .MatchWholeWord = False
    .MatchKashida = False
    .MatchDiacritics = False
    .MatchAlefHamza = False
    .MatchControl = False
    .MatchWildcards = False
    .MatchSoundsLike = False
    .MatchAllWordForms = False

End With
Selection.Find.Execute Replace:=wdReplaceAll

doc.Range().Text=coverletter
"""
 
