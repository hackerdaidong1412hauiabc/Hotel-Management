# import tkinter as tk
# from view.login_view import LoginView
# from controller.auth_controller import AuthController
#
#
# class HotelManagementApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Hệ Thống Quản Lý Khách Sạn")
#         self.root.geometry("400x300")
#         self.root.resizable(False, False)
#
#         # Center window
#         self.center_window()
#
#         self.setup_app()
#
#     def center_window(self):
#         """Căn giữa màn hình"""
#         self.root.update_idletasks()
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.root.winfo_screenheight() // 2) - (height // 2)
#         self.root.geometry(f'{width}x{height}+{x}+{y}')
#
#     def setup_app(self):
#         """Khởi tạo ứng dụng với MVC"""
#         # Tạo view
#         login_view = LoginView(self.root)
#         login_view.pack(expand=True, fill="both")
#
#         # Tạo controller và kết nối
#         auth_controller = AuthController(login_view)
#         login_view.set_controller(auth_controller)
#
#     def run(self):
#         """Chạy ứng dụng"""
#         self.root.mainloop()
#
#
# if __name__ == "__main__":
#     app = HotelManagementApp()
#     app.run()

# import tkinter as tk
# from controller.room_controller import RoomController
# from view.room_view import RoomView
#
#
# class RoomManagementApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Hệ Thống Quản Lý Phòng - Khách Sạn")
#         self.root.geometry("1000x700")
#         self.root.configure(bg='#f0f0f0')
#
#         # Center window
#         self.center_window()
#
#         self.setup_app()
#
#     def center_window(self):
#         """Căn giữa màn hình"""
#         self.root.update_idletasks()
#         width = 1000
#         height = 700
#         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.root.winfo_screenheight() // 2) - (height // 2)
#         self.root.geometry(f'{width}x{height}+{x}+{y}')
#
#     def setup_app(self):
#         """Khởi tạo ứng dụng với MVC"""
#         # Tạo view trước
#         room_view = RoomView(self.root, None)
#         room_view.pack(fill="both", expand=True, padx=10, pady=10)
#
#         # Tạo controller và kết nối
#         room_controller = RoomController(room_view)
#         room_view.controller = room_controller
#
#         # Tải dữ liệu ban đầu
#         self.root.after(100, room_controller.load_rooms)
#
#     def run(self):
#         """Chạy ứng dụng"""
#         self.root.mainloop()
#
#
# def init_sample_data():
#     """Khởi tạo dữ liệu mẫu cho testing (chạy 1 lần)"""
#     from model.db import Database
#
#     db = Database()
#
#     # Kiểm tra xem đã có dữ liệu mẫu chưa
#     check_sql = "SELECT COUNT(*) as count FROM rooms"
#     cursor = db.execute(check_sql)
#     result = cursor.fetchone()
#
#     if result['count'] == 0:
#         print("Đang thêm dữ liệu mẫu...")
#
#         # Thêm dữ liệu mẫu
#         sample_rooms = [
#             ('P101', 'Standard', 500000, 'empty'),
#             ('P102', 'Standard', 500000, 'booked'),
#             ('P103', 'Standard', 500000, 'empty'),
#             ('P201', 'Deluxe', 800000, 'empty'),
#             ('P202', 'Deluxe', 800000, 'repair'),
#             ('P301', 'Suite', 1200000, 'empty'),
#             ('P302', 'Suite', 1200000, 'booked'),
#             ('VIP01', 'VIP', 2000000, 'empty'),
#             ('VIP02', 'VIP', 2000000, 'empty')
#         ]
#
#         insert_sql = """
#             INSERT INTO rooms (room_name, room_type, price, status)
#             VALUES (%s, %s, %s, %s)
#         """
#
#         for room in sample_rooms:
#             try:
#                 db.execute(insert_sql, room)
#                 print(f"Đã thêm phòng: {room[0]}")
#             except Exception as e:
#                 print(f"Lỗi khi thêm phòng {room[0]}: {e}")
#
#         print("✅ Đã thêm dữ liệu mẫu thành công!")
#     else:
#         print("✅ Đã có dữ liệu phòng trong database")
#
#
# if __name__ == "__main__":
#     print("🚀 Khởi động hệ thống quản lý phòng...")
#
#     # Khởi tạo dữ liệu mẫu (chỉ chạy lần đầu)
#     try:
#         init_sample_data()
#     except Exception as e:
#         print(f"⚠️ Không thể khởi tạo dữ liệu mẫu: {e}")
#         print("📝 Vui lòng chạy file SQL để tạo bảng rooms trước")
#
#     # Chạy ứng dụng
#     app = RoomManagementApp()
#     app.run()


# import tkinter as tk
# from controller.booking_controller import BookingController
# from view.booking_view import BookingView
#
#
# class BookingApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Hệ Thống Đặt Phòng - Khách Sạn")
#         self.root.geometry("1200x700")
#
#         self.setup_app()
#
#     def setup_app(self):
#         """Khởi tạo ứng dụng"""
#         # Tạo view
#         booking_view = BookingView(self.root, None)
#         booking_view.pack(fill="both", expand=True, padx=10, pady=10)
#
#         # Tạo controller và kết nối
#         booking_controller = BookingController(booking_view)
#         booking_view.controller = booking_controller
#
#         # Tải dữ liệu ban đầu
#         self.root.after(100, booking_controller.load_available_rooms)
#         self.root.after(200, booking_controller.load_all_bookings)
#
#     def run(self):
#         """Chạy ứng dụng"""
#         self.root.mainloop()
#
#
# if __name__ == "__main__":
#     print("🚀 Khởi động hệ thống đặt phòng...")
#     app = BookingApp()
#     app.run()


# import tkinter as tk
# from controller.invoice_controller import InvoiceController
# from view.invoice_view import InvoiceView
#
#
# class InvoiceApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Hệ Thống Hóa Đơn & Thanh Toán - Khách Sạn")
#         self.root.geometry("1300x750")
#         self.root.configure(bg='#f5f5f5')
#
#         # Center window
#         self.center_window()
#
#         self.setup_app()
#
#     def center_window(self):
#         """Căn giữa màn hình"""
#         self.root.update_idletasks()
#         width = 1300
#         height = 750
#         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.root.winfo_screenheight() // 2) - (height // 2)
#         self.root.geometry(f'{width}x{height}+{x}+{y}')
#
#     def setup_app(self):
#         """Khởi tạo ứng dụng"""
#         # Tạo view
#         invoice_view = InvoiceView(self.root, None)
#         invoice_view.pack(fill="both", expand=True, padx=10, pady=10)
#
#         # Tạo controller và kết nối
#         invoice_controller = InvoiceController(invoice_view)
#         invoice_view.controller = invoice_controller
#
#         # Tải dữ liệu ban đầu
#         self.root.after(100, lambda: print("🔄 Đang tải dữ liệu..."))
#         self.root.after(200, invoice_controller.load_bookings_for_invoice)
#         self.root.after(300, invoice_controller.load_all_invoices)
#         self.root.after(400, invoice_controller.load_statistics)
#
#     def run(self):
#         """Chạy ứng dụng"""
#         self.root.mainloop()
#
#
# def init_sample_data():
#     """Khởi tạo dữ liệu mẫu cho testing"""
#     from model.db import Database
#     from datetime import datetime, timedelta
#
#     db = Database()
#
#     try:
#         # Kiểm tra xem đã có booking chưa
#         check_booking_sql = "SELECT COUNT(*) as count FROM bookings"
#         cursor = db.execute(check_booking_sql)
#         booking_count = cursor.fetchone()['count']
#
#         if booking_count == 0:
#             print("📝 Đang tạo dữ liệu mẫu...")
#
#             # Tạo booking mẫu
#             sample_bookings = [
#                 (1, 'Nguyễn Văn A', '0912345678', '2024-01-01', '2024-01-03', 1000000),
#                 (2, 'Trần Thị B', '0923456789', '2024-01-02', '2024-01-04', 1600000),
#                 (3, 'Lê Văn C', '0934567890', '2024-01-03', '2024-01-05', 1200000)
#             ]
#
#             insert_booking_sql = """
#                 INSERT INTO bookings (room_id, customer_name, customer_phone, check_in, check_out, total)
#                 VALUES (%s, %s, %s, %s, %s, %s)
#             """
#
#             for booking in sample_bookings:
#                 db.execute(insert_booking_sql, booking)
#
#             print("✅ Đã tạo booking mẫu")
#
#         # Kiểm tra xem đã có hóa đơn chưa
#         check_invoice_sql = "SELECT COUNT(*) as count FROM invoices"
#         cursor = db.execute(check_invoice_sql)
#         invoice_count = cursor.fetchone()['count']
#
#         if invoice_count == 0:
#             print("🧾 Đang tạo hóa đơn mẫu...")
#
#             # Tạo hóa đơn mẫu
#             sample_invoices = [
#                 (1, 1500000, 1500000, 'cash'),
#                 (2, 2400000, 2000000, 'credit_card'),
#                 (3, 1800000, 0, 'cash')
#             ]
#
#             insert_invoice_sql = """
#                 INSERT INTO invoices (booking_id, total_amount, paid_amount, payment_method)
#                 VALUES (%s, %s, %s, %s)
#             """
#
#             for invoice in sample_invoices:
#                 db.execute(insert_invoice_sql, invoice)
#
#             print("✅ Đã tạo hóa đơn mẫu")
#
#     except Exception as e:
#         print(f"⚠️ Không thể khởi tạo dữ liệu mẫu: {e}")
#
#
# if __name__ == "__main__":
#     print("🚀 Khởi động hệ thống hóa đơn & thanh toán...")
#     print("📊 Kiểm tra database...")
#
#     # Khởi tạo dữ liệu mẫu
#     try:
#         init_sample_data()
#     except Exception as e:
#         print(f"📝 Ghi chú: {e}")
#         print("💡 Tiếp tục chạy ứng dụng...")
#
#     # Chạy ứng dụng
#     app = InvoiceApp()
#     print("✅ Ứng dụng đã sẵn sàng!")
#     app.run()

import tkinter as tk
from controller.dashboard_controller import DashboardController
from view.dashboard_view import DashboardView


class DashboardApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard - Hệ Thống Quản Lý Khách Sạn")
        self.root.geometry("1400x800")
        self.root.configure(bg='#ecf0f1')

        self.setup_app()

    def setup_app(self):
        """Khởi tạo ứng dụng dashboard với MVC đúng thứ tự"""
        # Tạo view trước (với controller = None)
        dashboard_view = DashboardView(self.root, None)
        dashboard_view.pack(fill="both", expand=True)

        # Tạo controller và kết nối với view
        dashboard_controller = DashboardController(dashboard_view)
        dashboard_view.controller = dashboard_controller

        # Tải dữ liệu ban đầu
        self.root.after(100, dashboard_controller.refresh_all)

    def run(self):
        """Chạy ứng dụng"""
        self.root.mainloop()


if __name__ == "__main__":
    print("🚀 Khởi động Dashboard tổng quan...")
    app = DashboardApp()
    app.run()