import os
from dotenv import load_dotenv
from pathlib import Path

import google.generativeai as genai

load_dotenv(dotenv_path=Path('./.env'))
GOOGLE_API_KEY = os.getenv('API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


def extract_description(description):
    prompt = f"Ta có thông tin rao bán nhà bằng tiếng Việt như sau: \
        {description} \n \
        Hãy trích xuất thông tin trên và trả về 8 trường thông tin dưới đây. \
        Danh sách các trường: num_bedroom, \
        num_diningroom, num_kitchen, num_toilet, num_floor (nếu là nhà trọ thì có mấy tầng), \
        current_floor (phòng trọ ở tầng mấy), direction (hướng nhà, 1 trong 4 giá trị Đông/Tây/Nam/Bắc), \
        street_width (số thực, theo mét). \
        Trường nào không xuất hiện thì để là 0.\
        Các trường thông tin ngăn cách bởi dấu phẩy.\
        Ví dụ: \"0,0,1,1,0,0,Đông,0\", hoặc \"1,0,1,1,0,0,0,0\" nếu không có direction."

    response = model.generate_content(prompt)
    return response.text

    response = model.generate_content(prompt)
    return response.text

str = "Cho thuê phòng khép kín full nội thất tại Chính Kinh giá từ 5-6 triệu.\r\nChính chủ cần cho thuê phòng trọ tại Chính Kinh, ngay ga tàu điện Thượng Đình.\r\nDiện tích 25-30m2 full nội thất, điều hòa, nóng lạnh, tủ lạnh, máy giặt riêng\r\nThang máy, khóa cửa vân tay, giờ giấc tự do.\r\nGiá từ 5 đến 6 triệu.\r\nLiên hệ xem nhà mr Điệp O379 28 3456.\r\nCảm ơn quý khách đã xem tin."

# extract_description(str)
print(extract_description(str))
