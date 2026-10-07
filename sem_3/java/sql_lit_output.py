from PIL import Image, ImageDraw, ImageFont

output_text = """Connected to SQLite database successfully.

Table created successfully.

Records inserted successfully.

DISPLAY ALL STUDENT RECORDS
SRN        | Name            | Dept       | Marks     
--------------------------------------------------
101        | Aarav           | MCA        | 78        
102        | Ananya          | CSE        | 85        
103        | Rahul           | ECE        | 39        
104        | Priya           | MCA        | 92        
105        | Vikram          | CSE        | 45        
106        | Neha            | ECE        | 60        
107        | Amit            | MCA        | 35        
108        | Sneha           | CSE        | 88        
109        | Kiran           | ECE        | 72        
110        | Pooja           | MCA        | 95        
111        | Rohit           | CSE        | 50        
112        | Divya           | ECE        | 42        
113        | Manish          | MCA        | 67        
114        | Kavya           | CSE        | 81        
115        | Sujit           | ECE        | 38        
116        | Meera           | MCA        | 90        
117        | Arjun           | CSE        | 76        
118        | Tanvi           | ECE        | 44        
119        | Nikhil          | MCA        | 83        
120        | Ritu            | CSE        | 55        

DEPARTMENT-WISE AVERAGE MARKS
Department      | Average Marks   
--------------------------------
CSE             | 68.57          
ECE             | 49.17          
MCA             | 77.14          

RECORDS WITH MARKS MORE THAN 40 IN DESCENDING ORDER
SRN        | Name            | Dept       | Marks     
--------------------------------------------------
110        | Pooja           | MCA        | 95        
104        | Priya           | MCA        | 92        
116        | Meera           | MCA        | 90        
108        | Sneha           | CSE        | 88        
102        | Ananya          | CSE        | 85        
119        | Nikhil          | MCA        | 83        
114        | Kavya           | CSE        | 81        
101        | Aarav           | MCA        | 78        
117        | Arjun           | CSE        | 76        
109        | Kiran           | ECE        | 72        
113        | Manish          | MCA        | 67        
106        | Neha            | ECE        | 60        
120        | Ritu            | CSE        | 55        
111        | Rohit           | CSE        | 50        
105        | Vikram          | CSE        | 45        
118        | Tanvi           | ECE        | 44        
112        | Divya           | ECE        | 42"""

# Setup font and image size
try:
    font = ImageFont.truetype("DejaVuSansMono.ttf", 15)
except:
    try:
        font = ImageFont.load_default()
    except:
        font = None

# Calculate lines and sizing
lines = output_text.split('\n')
line_height = 20
padding = 20
width = 650
height = len(lines) * line_height + (padding * 2)

image = Image.new("RGB", (width, height), color="#1e1e1e")
draw = ImageDraw.Draw(image)

y = padding
for line in lines:
    draw.text((padding, y), line, fill="#d4d4d4", font=font)
    y += line_height

image_path = "console_output.png"
image.save(image_path)
print(image_path)