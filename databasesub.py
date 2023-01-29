import sqlite3

conn = sqlite3.connect('submission.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('submission.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_filelist (file_name) VALUES (?)", (x,))
            print(x)
        
        
