import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def uploadFile(self, fileFrom, fileTo):
        dbx  = dropbox.Dropbox(self.access_token)
        f=open(fileFrom,"rb")
        dbx.files_upload(f.read(),fileTo)
    def valededat(self, access_token):
        dbx = dropbox.Dropbox(self.access_token)
        print(dbx)
access_token = "sl.A9waIRKYoTZD4gcQ0_Jbf0OcmYzU-vQiXfucij6K6SmGL91QcI-OlEMdJ-MhYXT8nBY8lnvFr4_RHYuBK7nqml2Te4CpuGeFBmfwReIbu9r5Px6yzWIEtJsNWnduatEMkQZk48oqa2Dy"
transferData = TransferData(access_token)
transferData.valededat(access_token)
fileFrom = "test.txt"
fileTo = "/text.txt"
transferData.uploadFile(fileFrom,fileTo)
# f=open(fileFrom,"rb")
# print(f)
