from LeKyBa_support_programe import print_programe, print_space, stop_programe, print_table_colum
from LeKyBa_support_programe import print_input, print_table_2, print_money, space
# Hàm xem ngày tháng:
def Ba_xemlich(entermonth):
    if entermonth == ( 1 or 3 or 5 or 7 or 8 or 10 or 12 ):
        return(f'==    Tháng {entermonth} có 31 ngày.')
    elif entermonth != 2:
        return(f'==    Tháng {entermonth} có 30 ngày.')
    else:
        while True:
            try:
                enteryear = int(input(print_input("==    Hãy nhập năm:",40)))
                if enteryear > 0:
                    when = False
                    break
                elif enteryear <0:               
                    when = input(print_input("== Ý bạn là năm trước công nguyên? (yes/no)",40))
                    if when.lower() == 'yes':
                        when = True
                        break
                    elif when.lower()=="no":                        
                        print("=="+' '*36+"---NHẬP LẠI ---!")
                
            except ValueError:
                print("=="+' '*36+"---NHẬP LẠI ---!")
        if enteryear%4 == 0 and (enteryear%100 != 0 or (enteryear%100 == 0 and enteryear%400 == 0)) :
            return (f'==    Tháng 2 của năm {enteryear} có 29 ngày.') if when != True else (f'==    Tháng 2 của năm {-enteryear} TCN có 29 ngày.')
        else:
            return (f'==    Tháng 2 của năm {enteryear} có 28 ngày.') if when != True else (f'==    Tháng 2 của năm {-enteryear} TCN có 28 ngày.')
# Hàm tính lương:
def Ba_sumwage(enterTime,enterhourwage):
    "Giờ làm, Lương giờ"
    sumwage = 0
    if enterTime <= 40:
        sumwage = enterTime*enterhourwage
    else:
        sumwage = (enterhourwage*40) + ((enterTime-40)*(1.5*enterhourwage))
    return(sumwage)
# Hàm sắp xếp lương nhân viên:
def Ba_xemLuongNv(sonhanvien):
    "Số lượng nhân viên" 
    danhsachnhanvien = []
    for i in range(sonhanvien): # Nhập dữ liệu nhân viên
        tennhanvien = input(print_input(f"==    Nhập tên nhân viên {i+1}:",40))
        while True:
            try:
                luongnhanvien = float(input(print_input(f"==    Nhập lương nhân viên {i+1}:",40)))
                if luongnhanvien>0:
                    break
                else:
                    print("=="+' '*36+"---NHẬP LẠI---!")
            except ValueError:
                print("=="+' '*36+"---NHẬP LẠI ---!")
        danhsachnhanvien.append([tennhanvien,luongnhanvien])
    for i in range(len(danhsachnhanvien)-1):  # Sắp xếp lại lương nhân viên
        for j in range(i+1,len(danhsachnhanvien),1):
            if danhsachnhanvien[i][1] >= danhsachnhanvien[j][1]:
                danhsachnhanvien.insert(i,danhsachnhanvien[j])
                danhsachnhanvien.pop(j+1) 
    return(danhsachnhanvien)
# Hàm xem thông tin nhân viên:
def Ba_thongTin_Nv(nhaptennhanvien): # Trả về tên đệm và tên lót
    "Nhập tên nhân viên"
    firstname = ""
    lastname = ""
    danhsachchucai = []
    lengthname = 0
    while lengthname<len(nhaptennhanvien): # Bắt đầu tạo danh sách các thành phần trong tên
        if nhaptennhanvien[lengthname] !=" " :
            for j in range(lengthname,len(nhaptennhanvien),1):
                if nhaptennhanvien[j] == " " or (nhaptennhanvien[j] == nhaptennhanvien[-1]) :
                    danhsachchucai.append(nhaptennhanvien[lengthname:j if nhaptennhanvien[j] == " " else (j+1) ])
                    lengthname = j
                    break
        lengthname += 1
    try:
        firstname += danhsachchucai[-1][0].upper() + danhsachchucai[-1][1:]    # Khởi tạo lại tên đã chỉnh sửa  
        for i in range(len(danhsachchucai)-1):
            lastname += danhsachchucai[i][0].upper() + danhsachchucai[i][1:] + " "
    except IndexError:
        print("=="+' '*36+"---Bạn chưa nhập tên---")
    # print("- Họ và tên lót của nhân viên là:", lastname)
    # print("- Tên của nhân viên là:", firstname)
    # print("- Tên đầy đủ của nhân viên là:", lastname + firstname)
    return lastname, firstname
# Hàm tính điểm số trung bình:
def Ba_tinhDiemTb(somonhoc):
    "Nhập số môn học"
    diemtrungbinh = 0
    tongheso = 0
    tongsodiem = 0
    for i in range(somonhoc):
        while True: # Nhập điểm môn học_f
            try:
                diemmonhoc = float(input(print_input(f"==    Nhập số điểm môn học {i +1}",40)))
                if 10>=diemmonhoc>=0:
                    break
                else:
                    print("=="+' '*36+"---Nhập lại!---")
            except ValueError:
                print("=="+' '*36+"---Nhập lại!---")
        while True: # Nhập hệ số điểm_f
            try:
                hesodiem = float(input(print_input(f"==    Nhập hệ số điểm của môn học {i + 1}",40)))
                if 1<=hesodiem<=3 and hesodiem%0.5 == 0:
                    tongsodiem += diemmonhoc*hesodiem
                    tongheso += hesodiem
                    break
                else:
                    print("=="+' '*36+"---Nhập lại!---")
            except ValueError:
                print("=="+' '*36+"---Nhập lại!---")
    diemtrungbinh = tongsodiem/tongheso
    return(tongheso),round(diemtrungbinh,2)
# Hàm TRẢ VỀ BẢNG KẾT QUẢ LIÊN QUAN TỪ KHÓA TÌM KIẾM
def search_table(search,danhsach,search_way): 
        "từ khóa tìm kiếm, danh sách tra cứu,lựa chọn tìm kiếm"
        search_way -= 1
        lens = 0
        count = 0
        result = []
        for i in range(len(danhsach)):
            while lens <= len(danhsach[i][search_way])-len(search):
                if search == danhsach[i][search_way][lens:lens+len(search)] and search!=danhsach[i][search_way]:
                    count += 1
                    lens = lens + len(search)
                else:
                    lens += 1
            if count > 0:
                result.append([danhsach[i][0],danhsach[i][1],danhsach[i][2],count])
            lens = 0
            count = 0
        for i in range(len(result)-1):
            for j in range(i+1,len(result),1):
                if result[j][-1]>result[i][-1]:
                    small = result[i]
                    result[i] = result[j]
                    result[j] = small
        return result
while True:
    tenchuongtrinh = ["Chương trình xem lịch","Chương trình tính lương","Chương trình xem lương","Chương trình xem thông tin nhân viên","Chương trình tính điểm trung bình","Chương trình nâng cao","Thoát chương trình"]
    print("*"*120)
    print("*"+' '*(118)+"*")
    print(("*"*44)+" |"+"CHƯƠNG TRÌNH HỌC THÔNG MINH "+'| '+("*"*44))
    print("*"+' '*(118)+"*")
    print("="*120)
    print("=="+" "*56+"MENU"+(" "*56)+"==")
    print("="*120)
    print_space(tenchuongtrinh)
    print("="*120)
    while True: # Nhập số của chương trình_f
        try:
            programenumber = int(input("==    Nhập số của chương trình:"))
            if 0<programenumber<8:
                break
            else:
                print("=="+' '*36+"---NHẬP LẠI ---!")
        except ValueError:
            print("=="+' '*36+"---NHẬP LẠI ---!")
    
    if   programenumber == 1:     # Chương trình xem lịch_f:
        print_programe("Chương trình xem lịch ")
        while True:
            while True:
                try:
                    entermonth = int(input(print_input("==    Nhập tháng muốn kiểm tra ",40)))
                    if 0< entermonth <13:
                        break
                    else:
                        print("=="+' '*36+"---NHẬP LẠI ---!")
                except ValueError:
                    print("=="+' '*36+"---NHẬP LẠI ---!")
            print(Ba_xemlich(entermonth))
            if stop_programe(tenchuongtrinh,programenumber):
                space(5)
                break
    elif programenumber == 2:   # Chương trình tính lương_f:
        print_programe("Chương trình tính lương ")
        while True:
            while True:
                try:
                    enterTime = float(input(print_input("==    Nhập thời gian làm việc(giờ)",40)))
                    if enterTime >=0:
                        break
                    else:
                        print("=="+' '*36+"---Nhập lại!---")
                except ValueError:
                    print("=="+' '*36+"---Nhập lại!---")
            don_vi = input(print_input("==    Nhập đơn vị tiền",40))
            while True:
                try:
                    enterhourwage = float(input(print_input("==    Nhập số lương theo giờ",40)))
                    if enterhourwage > 0:
                        break
                    else:
                        print("=="+' '*36+"---Nhập lại!---")
                except ValueError:
                    print("=="+' '*36+"---Nhập lại!---")
            luong = Ba_sumwage(enterTime,enterhourwage)
            print(print_input("==    Tổng số lương (đã làm tròn) là:",40),print_money(luong,don_vi))
            print(print_input("==    Tổng số lương (thực tế) là:",40),luong,don_vi)
            if stop_programe(tenchuongtrinh,programenumber):
                space(5)
                break
    elif programenumber == 3:   # Chương trình sắp xếp lương nhân viên_f:
        print_programe("Chương trình sắp xếp lương nhân viên")
        while True:
            while True:
                try:
                    sonhanvien = int(input("==    Nhập số lượng nhân viên của bạn:"))
                    if sonhanvien >= 0:
                        break
                    else:
                        print("=="+' '*36+"---Nhập lại!---")
                except ValueError:
                    print("=="+' '*36+"---Nhập lại!---")
            donvi_2 = input(print_input("==    Nhập đơn vị tiền:",40))
            danhsachnhanvien = Ba_xemLuongNv(sonhanvien)
            print_table_2("Tên nhân viên", f"Lương({donvi_2})")
            for i in danhsachnhanvien:
                print_table_2(i[0],print_money((i[1]),donvi_2))
            if stop_programe(tenchuongtrinh,programenumber):
                space(5)
                break
    elif programenumber == 4:   # Chương trình xem thông tin nhân viên_f:
        print_programe("Chương trình xem thông tin nhân viên")
        while True:
            nhaptennhanvien = input(print_input("==    Nhập tên nhân viên vào đây",40))
            danhsachtennv = Ba_thongTin_Nv(nhaptennhanvien)
            if len(nhaptennhanvien) >0:
                print(print_input("==    Tên nhân viên là",40),danhsachtennv[-1] )  
                print(print_input("==    Họ và tên lót của nhân viên là",40),danhsachtennv[0])
                print(print_input("==    Tên đầy đủ của nhân viên là",40),danhsachtennv[0] + danhsachtennv[1])
            if stop_programe(tenchuongtrinh,programenumber):
                space(5)
                break    
    elif programenumber == 5:   # Chương trình tính điểm trung bình_f:
        print_programe("Chương trình tính điểm trung bình ")
        while True:
            while True:
                try:
                    somonhoc = int(input(print_input("==    Nhập số môn học vào đây",40)))
                    if somonhoc>0:
                        break
                    else:
                        print("=="+' '*36+"---Nhập lại!---")
                except ValueError:
                    print("=="+' '*36+"---Nhập lại!---")
            diemtrungbinh = Ba_tinhDiemTb(somonhoc)
            print_table_2("Tổng số môn học là:",str(somonhoc))
            print_table_2("Tổng hệ số là:",str(diemtrungbinh[0]))
            print_table_2("Điểm trung bình là:",str(diemtrungbinh[1]))
            if stop_programe(tenchuongtrinh,programenumber):
                space(5)
                break
    elif programenumber == 7: # Thoát chương trình
        print_programe("-"*10+"Bạn đã thoát chương trình!"+"-"*10)
        break
    elif programenumber == 6: # Chương trình nâng cao
        space(5)
        print_programe("---Chương trình quản lý thông tin---")
        print("-"*120)
        print(" "*40+"Chương trình lưu trữ thông tin trên thiết bị của bạn !")
        while True:              
            linkfile = "D:\\danhsachthongtin_Ba_project.txt"
            # Tạo danh sách thông tin cơ bản
            danhsachthongtin = []
            with open(linkfile,"a+",encoding="utf-8") as read_file: # mở file và lưu thông tin vào mảng
                read_file.seek(0)
                length = len(read_file.readlines())
                read_file.seek(0)
                for i in range(length):
                    danhsachthongtin.append(read_file.readline().strip().split("*"))
            print("-"*120)
            print_programe("Các chức năng")
            print_table_colum(['1.Thêm thông tin','2.Tìm thông tin','3.Xóa thông tin','4.Thoát'],4)
            print("-"*120)
            while True: # Nhập lựa chọn chức năng_f
                try:
                    add_or_read = int(input(print_input("Chọn chức năng",40)))
                    if add_or_read in [1,2,3,4]:
                        break
                    else:
                        print(" "*40+"Vui lòng nhập đúng số!")
                except ValueError:
                    print(" "*40+"Vui lòng nhập đúng số!")
            if add_or_read == 1: # Thêm thông tin vào file
                while True: # Nhập số lượng người muốn thêm_f
                    try:
                        soluongnguoi = int(input(print_input("Nhập số người",40))) # Thêm thông tin
                        if soluongnguoi>0:
                            break
                    except ValueError:
                        print("-"*36+"Vui lòng nhập số nguyên !")
                for i in range(soluongnguoi): # Nhập thông tin để thêm_f
                    print("-"*120)
                    # Nhập tên
                    while True:
                        ten_in = input(print_input(f"nhập tên {i+1}:",40))
                        if len(ten_in)>0:
                            break
                        else:
                            print(" "*40+"Vui lòng nhập tên!")
                    print(" "*10+"-"*100)
                    print(" "*30+"Nhập thông tin ngày sinh và số điện thoại")
                    # Nhập năm sinh_f
                    while True:
                        try:
                            nam_sinh_in = (input(print_input("Nhập năm sinh:",40)))
                            if nam_sinh_in == "":
                                nam_sinh_in = "----"
                            if nam_sinh_in == '----' or int(nam_sinh_in)!=0:
                                break
                            else:
                                print("Nhập lại năm sinh!")
                        except ValueError:
                            print("Nhập lại năm sinh!")
                    # Nhập tháng sinh_f
                    while True:
                        try:
                            thang_sinh_in = (input(print_input("Nhập tháng sinh:",40)))
                            if thang_sinh_in == '':
                                thang_sinh_in = "--"
                                break
                            elif int(thang_sinh_in) == 2 and nam_sinh_in =='' :
                                nam_sinh_in = int(input(print_input("Hãy nhập năm:",40)))
                            if nam_sinh_in != '----':
                                nam_sinh_in = int(nam_sinh_in)
                                if nam_sinh_in%4 == 0 and (nam_sinh_in%100 != 0 or (nam_sinh_in%100 == 0 and nam_sinh_in%400 == 0)) :
                                    con_year = 1 # năm nhuận
                                else:
                                    con_year = 0 # năm không nhuận               
                            if 0<int(thang_sinh_in)<13:
                                thang_sinh_in = int(thang_sinh_in)
                                break
                            else:
                                print(" "*40+"Nhập lại tháng sinh!")
                        except ValueError:
                            print(" "*40+"Nhập lại tháng sinh!")
                    # Nhập ngày sinh_f
                    while True:
                        try:
                            ngay_sinh_in = (input(print_input("Nhập ngày sinh:",40)))
                            if ngay_sinh_in == '':
                                ngay_sinh_in = "--"
                                break
                            else:
                                ngay_sinh_in = int(ngay_sinh_in)
                                if (thang_sinh_in in [4,6,9,11]) and 0<ngay_sinh_in<31:
                                    break
                                elif (thang_sinh_in in [1,3,5,7,8,10,12]) and 0<ngay_sinh_in<32:
                                    break
                                elif thang_sinh_in == 2 and 0<ngay_sinh_in<30 and con_year == 1:
                                    break
                                elif thang_sinh_in == 2 and 0<ngay_sinh_in<29 and con_year == 0:
                                    break
                                else:
                                    print(" "*40+"Nhập lại ngày sinh!")
                                
                        except ValueError:
                            print(" "*40+"Nhập lại ngày sinh!")
                    birthdaysInformation = f"{ngay_sinh_in}/{thang_sinh_in}/{nam_sinh_in}" # cắt thông tin ngày sinh chỉ cần cắt chuỗi ở dấu cách
                    while True: # Nhập số điện thoại, nếu không nhập cũng được, nhập sai sẽ nhập lại
                            phoneNum = (input(print_input(f"Nhập số điện thoại :",40)))
                            try:
                                if phoneNum == "":
                                    phoneNum = "Chưa nhập"
                                    break
                                elif type(int(phoneNum)) == int :                               
                                    break
                                else: print(" "*40+"Enter again!")
                            except ValueError:
                                print(" "*40+"Enter again!")
                    with open(linkfile,"a",encoding="utf-8") as thongtin: # Hoàn thành lưu trữ thông tin trong file
                        thongtin.write(ten_in+"*"+birthdaysInformation+"*"+phoneNum+"\n")
            elif add_or_read == 2: # tra cứu thông tin có sẵn
                print("-"*120)
                print_table_colum(['1.Toàn bộ thông tin','2.Tra thông tin'],2)
                print("-"*120)
                while True: # Lựa chọn tra cứu thông tin_f
                    try:
                        choose_print = int(input(print_input("Nhập lựa chọn của bạn",40)))
                        if choose_print in [1,2]:
                            break
                        else:
                            print(" "*40+"Nhập lại!")
                    except ValueError:
                        print(" "*40+"Vui lòng nhập đúng số!")
                if choose_print == 1: # in ra cả bảng_f
                    space(3)
                    print(" "*40+"Danh sách thông tin")
                    print_table_colum(['Tên','Ngày sinh','Số điện thoại'],3)
                    for i in range(len(danhsachthongtin)): # in bảng thông tin đã được thêm ra màn hình
                        print_table_colum(danhsachthongtin[i],3)
                    print("-"*30*3)
                elif choose_print == 2: # Tra cứu thông tin
                    print('-'*120)
                    print_space(["Tra tên",'Tra ngày sinh','Tra số điện thoại'])
                    print('-'*120)
                    while True: # Nhập lựa chọn tìm kiếm_f
                        try:
                            choose_option = int(input(print_input("Nhập lựa chọn của bạn:",40))) # chọn số 1,2,3 when find the value will -1
                            if 0<choose_option<4:
                                break
                        except ValueError:
                            print(" "*40+"Nhập số:")
                    while True: # Nhập từ khóa tìm kiếm_f
                        space(2)
                        print("(Không nhập gì sẽ thoát)")                        
                        search = input(print_input("--> Nhập từ khóa :",40))
                        if search == '':
                            print(" "*40+"Đã thoát chế độ tìm kiếm")
                            break
                        if choose_option == 2: #nếu tìm ngày sinh
                            newsearch = ''
                            for i in range(len(search)):
                                if search[i] in ['-',' '] and i!=0:
                                    newsearch += '/'
                                elif (search[i] =='/'or search[i]!="0") or (search[i]=='0' and search[i-1] not in ['-','/',' ']) :
                                    newsearch += search[i]
                            search = newsearch
                        space(3)
                        result_array = [] # Tìm kiếm kết quả khớp hoàn toàn với từ khóa
                        for i in range(len(danhsachthongtin)): 
                            if search == (danhsachthongtin[i][choose_option-1]) and (danhsachthongtin[i] not in result_array):
                                result_array.append(danhsachthongtin[i])
                        print(" "*20+f"Kết quả tìm kiếm cho từ khóa: '{search}'") # in kết quả_f
                        print_table_colum(['Tên','Ngày sinh','Số điện thoại'],3)
                        for i in range(len(result_array)):
                            print_table_colum(result_array[i],3) #   TRẢ VỀ KẾT QUẢ ĐÚNG HOÀN TOÀN
                        print("-"*30*3)
                        print(" ")
                        # TRẢ VỀ KẾT QUẢ LIÊN QUAN
                        print("-"*120)
                        print(" "*30+"Kết quả liên quan")
                        ket_qua_timKiem = search_table(search,danhsachthongtin,choose_option)
                        print_table_colum(['Tên','Ngày sinh','Số điện thoại','Số lần xuất hiện'],4)
                        for i in range(len(ket_qua_timKiem)):
                            print_table_colum(ket_qua_timKiem[i],4)
                        print("-"*30*4)
            elif add_or_read == 3: # xóa thông tin có trong file
                print_table_colum(['1.Xóa toàn bộ','2.Xóa một phần'],2)
                print("-"*120)
                option_remove = int(input(print_input("Chọn chế độ",40)))
                if option_remove == 1: # xóa toàn bộ thông tin trong file
                    print(" "*40+"Ấn phím bất kỳ để hủy")
                    con_remove_all = input(" "*40+"Ấn Yes(Y) để xác nhận xóa:")
                    if con_remove_all == "Y" or con_remove_all == "y":
                        with open(linkfile,"w",encoding="utf-8") as file:
                            file.write("")
                        print(" "*40+"Bạn đã xóa toàn bộ thông tin lưu trữ!")
                elif option_remove == 2: # xóa một phần thông tin trong file
                    for i in range(len(danhsachthongtin)): # in bảng thông tin đã được thêm ra màn hình
                        print_table_colum(danhsachthongtin[i],3)
                    print("-"*30*3)
                    line_remove = input(print_input("Hãy nhập đúng tên người bạn muốn xóa:",40))
                    for i in range(len(danhsachthongtin)):
                        if danhsachthongtin[i][0] == line_remove:
                            search_remove = danhsachthongtin[i]
                            print(" "*40+"Đây có phải thông tin mà bạn muốn xóa?")
                            print_table_colum(danhsachthongtin[i],3)
                            print("-"*30*3)
                            confirm = input("---Yes(Y) or No(N):")
                            if confirm == "Y" or confirm == "y":
                                danhsachthongtin.pop(i)
                                with open(linkfile,"w",encoding="utf-8") as file:
                                    for inf in range(len(danhsachthongtin)):
                                        file.write(danhsachthongtin[inf][0]+"*"+danhsachthongtin[inf][1]+"*"+danhsachthongtin[inf][2]+"\n")
                                for i in range(len(danhsachthongtin)): # in bảng thông tin ra màn hình
                                    print_table_colum(danhsachthongtin[i],3)
                                space(3)
                                print(' '*40+"Đã xóa!")
                                break
                        elif i == (len(danhsachthongtin)-1):
                            print(" "*40+"Không có kết quả phù hợp!")
            elif add_or_read == 4:
                space(3)
                print("-"*120)
                print(" "*40+"Đã thoát chương trình nâng cao")
                print("-"*120)
                break
                    


        



                
                
                





        
    
    
