import os
import sys
import PyPDF2

def Extract_TimeTable_Pdf(input_path, output_path, start_page, end_page):
    with open(input_path, 'rb') as input_file:
        Pdf_Reader = PyPDF2.PdfReader(input_file)
        Pdf_Write = PyPDF2.PdfWriter()
        for page_num in range(start_page - 1, min(end_page, len(Pdf_Reader.pages))):
            Pdf_Write.add_page(Pdf_Reader.pages[page_num])
        with open(output_path, 'wb') as output_file:
            Pdf_Write.write(output_file)

Path = os.path.dirname(__file__)
Preset_Path = Path+"/Preset"
Cache_Path = Path+"/Cache"
if not os.path.exists(Preset_Path):
    os.makedirs(Preset_Path)
    print("Presetフォルダ内に指定されたファイルをいれてください")
    sys.exit(1)
TimeTable_Pdf_Preset_Path = Preset_Path+"/時間割.pdf"
if not os.path.isfile(TimeTable_Pdf_Preset_Path):
    print("Presetフォルダ内に'時間割.pdf'が存在していません")
    sys.exit(1)
if not os.path.exists(Cache_Path):
    os.makedirs(Cache_Path)

TimeTable_Pdf_Start = int(input("最初のページ番号を入力してください: "))
TimeTable_Pdf_End = int(input("最後のページ番号を入力してください: "))
TimeTable_Pdf_Cache_Path = Cache_Path+"/時間割.pdf"
Extract_TimeTable_Pdf(TimeTable_Pdf_Preset_Path, TimeTable_Pdf_Cache_Path, TimeTable_Pdf_Start, TimeTable_Pdf_End)
