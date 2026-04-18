import os
from werkzeug.utils import secure_filename

# Chỉ cho phép các đuôi ảnh này
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "gif"}


def is_allowed_file(filename):
    """
    Kiểm tra file có đúng định dạng ảnh cho phép hay không.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def tao_thu_muc_neu_chua_co(path):
    """
    Tạo thư mục nếu chưa tồn tại.
    """
    os.makedirs(path, exist_ok=True)


def luu_nhieu_anh_khach_san(files, ma_khach_san):
    """
    Lưu nhiều ảnh khách sạn vào:
    app/static/images/khachsan/ks_<ma_khach_san>/

    Trả về:
        'khachsan/ks_<ma_khach_san>'
    """
    relative_folder = f"khachsan/ks_{ma_khach_san}"
    absolute_folder = os.path.join("app", "static", "images", relative_folder)

    tao_thu_muc_neu_chua_co(absolute_folder)

    stt = 1
    for file in files:
        if file and file.filename and is_allowed_file(file.filename):
            ext = file.filename.rsplit(".", 1)[1].lower()
            new_filename = f"{stt}.{ext}"
            save_path = os.path.join(absolute_folder, secure_filename(new_filename))
            file.save(save_path)
            stt += 1

    return relative_folder


def luu_nhieu_anh_loai_phong(files, ma_loai_phong):
    """
    Lưu nhiều ảnh loại phòng vào:
    app/static/images/loaiphong/lp_<ma_loai_phong>/

    Trả về:
        'loaiphong/lp_<ma_loai_phong>'
    """
    relative_folder = f"loaiphong/lp_{ma_loai_phong}"
    absolute_folder = os.path.join("app", "static", "images", relative_folder)

    tao_thu_muc_neu_chua_co(absolute_folder)

    stt = 1
    for file in files:
        if file and file.filename and is_allowed_file(file.filename):
            ext = file.filename.rsplit(".", 1)[1].lower()
            new_filename = f"{stt}.{ext}"
            save_path = os.path.join(absolute_folder, secure_filename(new_filename))
            file.save(save_path)
            stt += 1

    return relative_folder