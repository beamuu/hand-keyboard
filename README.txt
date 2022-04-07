# README

ชื่อกลุ่ม: bongbong
สมาชิคกลุ่ม:
  
  6210500579  สรวิชญ์ ทรัพย์มี  
  6210503578  ณัฐชนน จันทรศัพท์
  6210503594  ธนพล โอวาทวรวรัญญู 
  
Source Code:
    
  
  
  Server-Side
  
    - server.py 
      โปรแกรม python ที่เปิดการเชื่อมต่อแบบ socket (TCP) เพื่อให้อุปกรณ์ (ถุงมือ keyboard) 
      เชื่อมต่อและสื่อสารกับ computer ผ่าน Internet โดยต้องเชื่อมต่อบน local network เดียวกันเท่านั้น
      server ใช้ library ที่ชื่อว่า pynput ในการจำลองการพิมพ์คีย์บอร์ดบนเครื่องนั้นๆ
  
  Client-Side
  
    - broadcast.py
      ตัวสื่อสารกับ server ที่รันบนบอร์ด ESP32 (NodeMCU) โดยสื่อสารผ่าน socket (TCP) ไปยัง IP ของเครื่องที่มี server รันอยู่
      
    - bridge.cpp
      ทำหน้าที่เป็นเหมือนสะพานเชื่อมต่อระหว่างบอร์ดที่ใช้ socket (keyboard.py) กับกลุ่มของบอร์ดที่ใช้ espnow เนื่องจาก ESP32 สามารถ
      ใช้งาน WiFi channel ได้แค่ 1 process (ไม่ต่อ WiFi ก็ต้อง ใช้ espnow) ทำให้ไม่สามารถรันทั้ง 2 process พร้อมกันได้
      
    - gate.py  
      ทำหน้าที่รับคำส่งต่างๆจากกลุ่มของบอร์ดที่เชื่อมต่อกันด้วย espnow เพื่อส่งข้าม bridge ไปหา broadcast.py
      
    - controller.cpp
      ควบคุม hardware ที่อยู่บนถุงมือด้านขวา ใช้สำหรับการยืนยันการพิมพ์ และ ฟีเจอร์ต่างๆ
    
    - controller-comm.py
      รับคำสั่งจาก controller เพื่อส่งไปให้ gate และ guesture ประมวลผล
      
    - guesture.cpp
      ควบคุม Flex sensor ที่อยู่บนถุงมือด้านซ้ายเพื่อแปลง pattern ของการขยับนิ้วในรูปแบบต่างไปเป็นตัวอักษรที่กำหนด
    
    - guesture-comm.py
      รับคำสั่งจาก guesture เพื่อส่งไปให้ gate และ event การพิมพ์ตัวอักษรจาก controller
      
    
