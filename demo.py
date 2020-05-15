from pathlib import Path


judge={".jpg":b"\xff\xd8",".png": b"\x89PNG", 
    ".bmp":b"BM",".pdf":b"%PDF",".docx":b"PK\x03\x04",".pptx":b"PK\x03\x04",".exe":b"MZ"}

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

for file in files:
    # print(file)
    if Path(file).is_file()== False:
        continue
    
    suf=Path(file).suffix

    with open(file,'rb') as f:
        fileHeader=f.read(len(judge[suf]))
    
    if judge[suf]==fileHeader:
        moveFlies(file,RFlies)
    else:
        moveFlies(file,WFlies)      