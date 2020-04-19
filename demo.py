from pathlib import Path
import struct

judge={".jpg":b"\xff\xd8",".png": b"\x89P", ".bmp":b"BM",".pdf":b"%P",".docx":b"PK",".pptx":b"PK",".exe":b"MZ"}
def check(suf,fileHeader):
    if judge[suf]==fileHeader:
        return 1
    else:
        return 0

def moveFlies(file,desfile):
    Path(file).rename(desfile/Path(file).name)



root=input("输入要查错的目录:")


desfile=input("输入输出目录:")

Path(desfile).mkdir(exist_ok=True)

WFlies=Path(desfile)/Path("异常")
RFlies=Path(desfile)/Path("正常")


Path(WFlies).mkdir(exist_ok=True)
Path(RFlies).mkdir(exist_ok=True)


files=Path(root).glob("**/*")

tfiles={}
for file in files:
    if Path(file).is_file():
        st=Path(file).stat()
        tfiles[file]=st.st_size

files={k:v for k,v in sorted(tfiles.items(),key=lambda x: x[1],reverse=True)}


for file in files:
    # print(file)
    
    
    suf=Path(file).suffix

    with open(file,'rb') as f:
        fileHeader=f.read(2)

    if check(suf,fileHeader):
        moveFlies(file,RFlies)
    else:
        moveFlies(file,WFlies)      