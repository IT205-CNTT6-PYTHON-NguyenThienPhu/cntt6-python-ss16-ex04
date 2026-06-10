"""
PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP:
1. find_patient_index(records: list, patient_id: str) -> int
- Input: Danh sách hồ sơ (records), Mã BN cần tìm (patient_id).
- Output: Vị trí (index) kiểu int. Nếu không thấy trả về -1.
- Luồng xử lý: Duyệt qua records bằng vòng lặp. Dùng .split("-")[0] để lấy ra Mã BN từ chuỗi rồi so sánh với patient_id.
2. display_records(records: list) -> None
- Input: Danh sách hồ sơ.
- Output: Không (chỉ in ra màn hình).
- Luồng xử lý: Kiểm tra rỗng. Nếu có dữ liệu, duyệt qua từng chuỗi, tách bằng .split("-") thành 4 phần và in theo định dạng cột.
3. add_patient(records: list) -> None
- Input: Danh sách hồ sơ.
- Output: Không (thêm trực tiếp vào danh sách).
- Luồng xử lý: 
    + Nhập và validate Mã BN (không trùng).
    + Nhập Tên BN, đổi ký tự "-" thành khoảng trắng bằng .replace(), viết hoa .title().
    + Nhập Năm sinh, ép kiểu nguyên, kiểm tra khoảng 1900 -> năm hiện tại.
    + Nhập Chẩn đoán, đổi ký tự "-", viết hoa .capitalize().
    + Dùng toán tử "+" hoặc "-".join() để ghép 4 chuỗi lại và .append() vào mảng.
4. update_diagnosis(records: list) -> None
- Input: Danh sách hồ sơ.
- Output: Không (cập nhật trực tiếp list).
- Luồng xử lý: Nhập Mã BN -> Tìm index. Nếu tìm thấy, tách chuỗi tại index đó ra thành mảng 4 phần tử. Nhập chẩn đoán mới, gán đè vào index 3 của mảng vừa tách. Cuối cùng, .join() lại và gán đè vào records[index].
5. generate_age_report(records: list) -> None
- Input: Danh sách hồ sơ.
- Output: Không (chỉ in ra màn hình).
- Luồng xử lý: Khởi tạo 3 biến đếm (trẻ em, trưởng thành, cao tuổi). Duyệt danh sách, lấy phần tử index 2 sau khi .split("-"), ép sang kiểu int, lấy năm hiện tại trừ đi để ra tuổi. Phân loại bằng if-elif và tăng biến đếm.
"""

# Phần 2.code
from datetime import datetime
def get_non_empty_input(prompt: str, error_msg: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(error_msg)
            continue
        return user_input


def find_patient_index(records: list, patient_id: str) -> int:
    normalized_id = patient_id.strip().upper()
    for index, record in enumerate(records):
        current_id = record.split("-")[0]
        if current_id == normalized_id:
            return index
    return -1


def display_records(records: list) -> None:
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return
    print("---- DANH SÁCH BỆNH NHÂN " + "-" * 50)
    for i, record in enumerate(records, start=1):
        parts = record.split("-")
        p_id, p_name, p_year, p_diag = parts[0], parts[1], parts[2], parts[3]
        print(f"{i}. [{p_id}] {p_name:<16} | Năm sinh: {p_year} | Chẩn đoán: {p_diag}")
    print("-" * 74)

def add_patient(records: list) -> None:
    print("--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    while True:
        patient_id = get_non_empty_input("Nhập mã bệnh nhân: ", "Mã bệnh nhân không được để trống!")
        patient_id = patient_id.upper()
        if find_patient_index(records, patient_id) != -1:
            print("Mã bệnh nhân đã tồn tại!")
            continue
        break
    patient_name = get_non_empty_input("Nhập tên bệnh nhân: ", "Tên bệnh nhân không được để trống!")
    patient_name = patient_name.replace("-", " ").title()
    current_year = datetime.now().year
    while True:
        year_input = input("Nhập năm sinh: ").strip()
        if not year_input.isdigit():
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
            continue
        year_int = int(year_input)
        if year_int < 1900 or year_int > current_year:
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
            continue
        birth_year = str(year_int)
        break
    diagnosis = get_non_empty_input("Nhập chẩn đoán: ", "Chẩn đoán không được để trống!")
    diagnosis = diagnosis.replace("-", " ").capitalize()
    new_record = f"{patient_id}-{patient_name}-{birth_year}-{diagnosis}"
    records.append(new_record)
    print("Thêm hồ sơ bệnh nhân thành công!")


def update_diagnosis(records: list) -> None:
    print("--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    patient_id = get_non_empty_input("Nhập mã bệnh nhân cần cập nhật: ", "Mã bệnh nhân không được để trống!")
    index = find_patient_index(records, patient_id)
    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id.upper()}!")
        return
    parts = records[index].split("-")
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")
    new_diagnosis = get_non_empty_input("Nhập chẩn đoán mới: ", "Chẩn đoán không được để trống!")
    new_diagnosis = new_diagnosis.replace("-", " ").capitalize()
    parts[3] = new_diagnosis
    records[index] = "-".join(parts)
    print("Cập nhật chẩn đoán thành công!")


def generate_age_report(records: list) -> None:
    print("--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    children_count = 0
    adult_count = 0
    elderly_count = 0
    current_year = datetime.now().year
    for record in records:
        birth_year = int(record.split("-")[2])
        age = current_year - birth_year
        if age < 16:
            children_count += 1
        elif 16 <= age <= 60:
            adult_count += 1
        else:
            elderly_count += 1
    print(f"Trẻ em: {children_count} bệnh nhân")
    print(f"Trưởng thành: {adult_count} bệnh nhân")
    print(f"Người cao tuổi: {elderly_count} bệnh nhân")
    print("-" * 38)


def main():
    patient_records = [
        "BN001-Nguyen Van A-1985-Viem Phoi",
        "BN002-Tran Thi B-1990-Sot Xuat Huyet",
        "BN003-Le Van C-2015-Viem Phe Quan"
    ]

    while True:
        print("\n" + "=" * 50)
        print("===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("=" * 50)
        choice = input("Chọn chức năng (1-5): ").strip()
        match choice:
            case "1":
                display_records(patient_records)
            case "2":
                add_patient(patient_records)
            case "3":
                update_diagnosis(patient_records)
            case "4":
                generate_age_report(patient_records)
            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                break
            case _:
                print("Lựa chọn không hợp lệ")
if __name__ == "__main__":
    main()