import os
class fileposition:
    def new_file(report_dir):
     lists=os.listdir(report_dir)
     lists.sort(key=lambda fn:os.path.getatime(report_dir+"\\"+fn))
     file_path=os.path.join(report_dir,lists[-1])
     return  file_path