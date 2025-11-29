- Database:
  
DROP DATABASE IF EXISTS hotel_db;

CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;


CREATE TABLE IF NOT EXISTS `users` (
   `user_id` int NOT NULL AUTO_INCREMENT,
   `username` varchar(50) DEFAULT NULL,
   `password` varchar(255) DEFAULT NULL,
   `role` enum('manager','receptionist') NOT NULL,
   PRIMARY KEY (`user_id`),
   UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- Bảng rooms
CREATE TABLE IF NOT EXISTS `rooms` (
   `room_id` int NOT NULL AUTO_INCREMENT,
   `room_name` varchar(50) DEFAULT NULL,
   `room_type` varchar(50) DEFAULT NULL,
   `price` decimal(10,2) DEFAULT NULL,
   `status` enum('empty','occupied','repair') DEFAULT 'empty',
   PRIMARY KEY (`room_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- Bảng bookings
CREATE TABLE IF NOT EXISTS `bookings` (
    `booking_id` int NOT NULL AUTO_INCREMENT,
    `room_id` int NOT NULL,
    `customer_name` varchar(100) DEFAULT NULL,
    `customer_phone` varchar(20) DEFAULT NULL,
    `customer_email` varchar(100) DEFAULT NULL,
    `check_in` date DEFAULT NULL,
    `check_out` date DEFAULT NULL,
    `total` float DEFAULT NULL,
    `status` enum('booked','checked_in','checked_out','cancelled') NOT NULL DEFAULT 'booked',
    `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    `deposit` decimal(10,2) DEFAULT '0.00',
    PRIMARY KEY (`booking_id`),
    KEY `room_id` (`room_id`),
    CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`room_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- Bảng services
CREATE TABLE IF NOT EXISTS `services` (
   `service_id` int NOT NULL AUTO_INCREMENT,
   `service_name` varchar(100) NOT NULL,
   `service_type` enum('food','laundry','spa','transport','other') DEFAULT 'other',
   `price` decimal(10,2) DEFAULT NULL,
   `unit` varchar(20) DEFAULT 'lần',
   `description` text,
   `status` enum('active','inactive') DEFAULT 'active',
   `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- Bảng service_usage
CREATE TABLE IF NOT EXISTS `service_usage` (
   `usage_id` int NOT NULL AUTO_INCREMENT,
   `booking_id` int NOT NULL,
   `service_id` int NOT NULL,
   `quantity` int DEFAULT '1',
   `unit_price` decimal(10,2) DEFAULT NULL,
   `total_price` decimal(10,2) DEFAULT NULL,
   `usage_date` date DEFAULT NULL,
   `notes` text,
   `status` enum('pending','completed','cancelled') DEFAULT 'pending',
   `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (`usage_id`),
   KEY `booking_id` (`booking_id`),
   KEY `service_id` (`service_id`),
   CONSTRAINT `service_usage_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`booking_id`),
   CONSTRAINT `service_usage_ibfk_2` FOREIGN KEY (`service_id`) REFERENCES `services` (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- Bảng invoices
CREATE TABLE IF NOT EXISTS `invoices` (`invoice_id` int NOT NULL AUTO_INCREMENT,
   `booking_id` int NOT NULL,
   `total_amount` decimal(10,2) DEFAULT NULL,
   `paid_amount` decimal(10,2) DEFAULT NULL,
   `payment_method` enum('cash','credit_card','bank_transfer') DEFAULT 'cash',
   `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
   `invoice_number` varchar(50) DEFAULT NULL,
   `invoice_date` date DEFAULT NULL,
   `room_charge` decimal(10,2) DEFAULT '0.00',
   `service_charge` decimal(10,2) DEFAULT '0.00',
   `extra_charges` decimal(10,2) DEFAULT '0.00',
   `discount` decimal(10,2) DEFAULT '0.00',
   `tax_rate` decimal(5,2) DEFAULT '10.00',
   `payment_status` enum('pending','paid','partial','refunded') DEFAULT 'pending',
   `due_date` date DEFAULT NULL,
   `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   PRIMARY KEY (`invoice_id`),
   UNIQUE KEY `invoice_number` (`invoice_number`),
   KEY `booking_id` (`booking_id`),
   CONSTRAINT `invoices_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- Bảng invoice_services
CREATE TABLE IF NOT EXISTS `invoice_services` (
   `invoice_service_id` int NOT NULL AUTO_INCREMENT,
   `invoice_id` int NOT NULL,
   `service_id` int NOT NULL,
   `service_name` varchar(100) DEFAULT NULL,
   `quantity` int DEFAULT '1',
   `unit_price` decimal(10,2) DEFAULT NULL,
   `total_price` decimal(10,2) DEFAULT NULL,
   PRIMARY KEY (`invoice_service_id`),
   KEY `invoice_id` (`invoice_id`),
   KEY `service_id` (`service_id`),
   CONSTRAINT `invoice_services_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`invoice_id`),
   CONSTRAINT `invoice_services_ibfk_2` FOREIGN KEY (`service_id`) REFERENCES `services` (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


INSERT INTO `users` (`username`, `password`, `role`) VALUES
('admin', '123', 'manager'),
('reception', '123', 'receptionist');

INSERT INTO `rooms` (`room_name`, `room_type`, `price`, `status`) VALUES
('Phòng 101', 'Standard', 500000.00, 'empty'),
('Phòng 102', 'Standard', 500000.00, 'empty'),
('Phòng 201', 'Deluxe', 800000.00, 'empty'),
('Phòng 202', 'Deluxe', 800000.00, 'empty'),
('Phòng 301', 'Suite', 1200000.00, 'empty');

INSERT INTO `services` (`service_name`, `service_type`, `price`, `unit`, `description`) VALUES
('Bữa sáng', 'food', 100000.00, 'người', 'Bữa sáng buffet'),
('Giặt ủi', 'laundry', 50000.00, 'kg', 'Dịch vụ giặt ủi'),
('Massage', 'spa', 300000.00, 'giờ', 'Massage thư giãn'),
('Đưa đón sân bay', 'transport', 200000.00, 'chuyến', 'Dịch vụ đưa đón');

SELECT * FROM  `rooms`;
ALTER TABLE rooms 
MODIFY COLUMN status ENUM('empty','booked','occupied','repair') DEFAULT 'empty';

-- Cập nhật các phòng đang 'occupied' về 'empty' nếu cần
UPDATE rooms SET status = 'empty' WHERE status = 'occupied';



