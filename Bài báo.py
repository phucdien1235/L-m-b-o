from guizero import App, Text, Picture, Box
app = App(title = "Báo", width = 1500, height = 1000, bg = "lightyellow")
greeting = Text(app, text = "Người Việt mua ôtô điện nhiều thứ hai Đông Nam Á", size = 20, color = "red")
box_1 = Box(app, width = 1500, height = 250, border = True)
box_2 = Box(app, width = 1500, height = 750, border = True)
content = Text(box_1, text = "Sau 8 tháng đầu 2025, thị trường Việt tiêu thụ 89.970 xe thuần điện, Thái Lan dẫn đầu với 92.665 xe. Việt Nam là thị trường ôtô số xe mới hàng năm sau\n"
              " Indonesia, Malaysia, Thái Lan, nhưng nếu tính riêng xe thuần điện lớn thứ 4 Đông Nam Á về doanh chạy bằng pin (BEV - Battery Electric Vehicle), Việt\n"
              " Nam hiện xếp thứ hai.\n"
              "Số liệu của Indonesia, Thái Lan, Malaysia tính theo lượng xe tới tay khách hàng tiêu dùng cuối. Trong khi con số ở Philippines tính theo số giao tới đại lý.\n"
              " Số liệu của Việt Nam là số xuất từ nhà máy của VinFast. Các hãng bán xe điện khác như BYD, Wuling, Mercedes, BMW... không công bố số liệu chi tiết.\n"
              "Doanh số 8 tháng đầu 2025 của VinFast vượt lượng bán của cả năm 2024 (khoảng 87.000 xe). Với số liệu này, Việt Nam bám sát Thái Lan với khoảng\n"
              " cách 2.700 xe.\n"
              "Theo các chuyên gia bán hàng, khoảng cách khá nhỏ, vì vậy cơ hội để Việt Nam trở thành thị trường tiêu thụ nhiều xe điện nhất Đông Nam Á đến\n"
              " cuối 2025 là rất lớn.\n"
              , align = "top", size = 15, color = "black")
picture = Picture(box_2, image = "Bài báo.png", align = "top")

app.display()