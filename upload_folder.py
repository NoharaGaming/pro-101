import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadFile(self, fileFrom, fileTo):
        dbx  = dropbox.Dropbox(self.access_token)
        # f=open(fileFrom,"rb")
        # dbx.files_upload(f.read(),fileTo)
        for root, dirs, files in os.walk(fileFrom):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, fileFrom)
                dropbox_path = os.path.join(fileTo, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))

                    
    def valededat(self, access_token):
        dbx = dropbox.Dropbox(self.access_token)
        print(dbx)


access_token = "sl.A9waIRKYoTZD4gcQ0_Jbf0OcmYzU-vQiXfucij6K6SmGL91QcI-OlEMdJ-MhYXT8nBY8lnvFr4_RHYuBK7nqml2Te4CpuGeFBmfwReIbu9r5Px6yzWIEtJsNWnduatEMkQZk48oqa2Dy"
transferData = TransferData(access_token)
transferData.valededat(access_token)

fileFrom =input("Enter your file you want to upload:- ")
fileTo = input("Enter where you want to save it:- ")

transferData.uploadFile(fileFrom,fileTo)
