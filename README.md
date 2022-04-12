# Backend
Repository นี้เก็บการทำงานในส่วน Backend ทั้งหมดเป็นทั้งที่เก็บข้อมูลการดำเนินการของเกมต่างๆ และส่งข้อมูลระหว่าง Frontend และ Firmware พัฒนาโดยใช้ภาษา `Python`

- `main.py` โปรแกรมหลักในการทำงานของส่วน Backend  
- `data/` เป็นโฟลเดอร์สำหรับเก็บข้อมูล
- `service/` เก็บตัวอย่างการ Request ข้อมูล
- `FileOP.py` Module สำหรับการอ่านและเขียนเพื่อใช้เก็บข้อมูล
- `RequestModel.py` Module ที่เก็บ BaseModel ต่างๆ ในการรับ/ส่งข้อมูล

### Library
- FastAPI
- uvicorn
