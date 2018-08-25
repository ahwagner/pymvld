from ftplib import FTP
import os
from pymvld.definitions import *


class HGNC:

    SOURCE_URL = 'ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/json/hgnc_complete_set.json'
    JSON = str(DATA_ROOT / 'hgvs.json')

    def __init__(self):
        if os.path.isfile(HGNC.JSON): # TODO: Check for recentness of file
            self.load_from_file()
        else:
            self.load_from_url()

    def load_from_url(self, file=None):
        if file is None:
            file = HGNC.JSON
        ebi = FTP('ftp.ebi.ac.uk')
        resp = ebi.login()
        assert '230 Login successful.' == resp
        resp = ebi.cwd('pub/databases/genenames/new/json/')
        assert '250 Directory successfully changed.' == resp
        with open(file, 'wb') as f:
            resp = ebi.retrbinary('RETR hgnc_complete_set.json', f.write)
        assert '226 Transfer complete.' == resp
        self.load_from_file(file)

    def load_from_file(self, file=None):
        if file is None:
            file = HGNC.JSON