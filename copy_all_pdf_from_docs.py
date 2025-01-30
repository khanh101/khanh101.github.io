import os
import shutil

dst_dir = "blog/pdf"
src_dir = "/Users/khanh/docs/latex_code"

if __name__ == "__main__":
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)

    for name in os.listdir(src_dir):
        pdf_path = f"{src_dir}/{name}/main.pdf"
        if os.path.exists(pdf_path):
            dst_pdf_path = f"{dst_dir}/{name}.pdf"
            shutil.copyfile(pdf_path, dst_pdf_path)

    