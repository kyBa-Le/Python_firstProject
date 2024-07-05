def print_programe(programe_name): # in tên chương trình trong khung
    dodai = len(programe_name)
    maxdai = 120
    candoi = int((maxdai-dodai-4)/2)
    print("="*maxdai)
    print("=="+" "*(maxdai-4)+"==")
    print("=="+(" "*candoi)+programe_name+" "*candoi+"==")
    print("=="+" "*(maxdai-4)+"==")
    print("="*maxdai)
def print_input(in_name,max_len):  # ghi chú trong input cho cân bằng
    "ghi chú nhập vào, độ dài tối đa"
    return in_name+" "*(max_len-len(in_name))+":"
def print_space(list_name):             # hỗ trợ in bảng menu
    " đưa danh sách chuỗi vào ô dấu cách, max là 120"
    for i in range(len(list_name)):
        len_name = 120-len(list_name[i])-10
        print("=="+(" "*4)+(f"{i+1}.")+list_name[i]+(" "*len_name)+"==")
def print_table_2(name1,name2):     # in 2 nội dung trong 2 ô liên tiếp
    "text trong ô 1, text trong ô 2"
    print("-"*70)
    print("|"+" "*9+name1+" "*(45-len(name1)-10)+"|"+" "*4+name2+" "*(25-len(name2)-5)+"|")
    print("-"*70)
def space(soluong): # in ra số hàng bỏ trống
    "Nhập số lượng hàng muốn bỏ trống"
    print("-"*130)
    print("\n"*soluong)
def stop_programe(tenchuongtrinh,programenumber): # điều kiện ngừng chương trình
    con = input("==    Nhấn phím ENTER để thoát "+tenchuongtrinh[programenumber - 1]+" hoặc ấn phím khác để tiếp tục:")
    if con == "" and 0<programenumber<6:
        return True
    else:
        return False
def print_money(number,donvi):# in đơn tiền với dấu chấm
    "Nhập số tiền, đơn vị"
    number = str(int(round(number,0)))
    new_number1 =''
    new_number2 =''
    count = 0
    for i in range(len(number)-1,-1,-1):
        new_number1 += number[i]
        count += 1
        if count == 3 and i!=0:
            new_number1 += ' '
            count = 0
    for j in range(len(new_number1)-1,-1,-1):
        new_number2 += new_number1[j]
    return (new_number2+" "+donvi)
def print_table_colum(danhsach,socot): # in danh sách theo số cột cho trước
    "danh sách sẽ in ra, số cột"
    print("-"*30*socot)
    for i in range(socot):
        print("|"+" "*5+str(danhsach[i])+" "*(30-7-len(str(danhsach[i])))+"|",end = "" if (i+1)!=socot else "\n")        