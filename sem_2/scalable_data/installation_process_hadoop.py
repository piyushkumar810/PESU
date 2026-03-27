'''

START
│
├── 🖥️ Step 1: Install WSL
│   │
│   └── Command:
│       wsl --install
│
│   ✔ Result: WSL installed successfully
│
├── 🔄 Step 2: Restart System
│   │
│   └── (Required for WSL to activate)
│
│   ✔ Result: System ready for WSL
│
├── 📦 Step 3: Check / Verify WSL
│   │
│   └── Command:
│       wsl -v
│
│   ✔ Result: WSL version confirmed
│
├── 📁 Step 4: Create Folder in C Drive
│   │
│   └── Command:
│       mkdir C:\hadoop
│
│   ✔ Result: Storage location created
│
├── 📂 Step 5: Locate TAR File
│   │
│   └── Path:
│       C:\Users\piyush kumar\Downloads\bigdata-env.tar
│
│   ✔ Result: File ready for import
│
├── 📥 Step 6: Import Linux Environment
│   │
│   └── Command:
│       wsl --import bigdata-env C:\hadoop "C:\Users\piyush kumar\Downloads\bigdata-env.tar"
│
│   ✔ Result: Custom environment installed
│
├── 📋 Step 7: Verify Installation
│   │
│   └── Command:
│       wsl --list
│
│   ✔ Output:
│       Ubuntu (Default)
│       bigdata-env
│
├── 🚀 Step 8: Start Environment
│   │
│   └── Command:
│       wsl -d bigdata-env
│
│   ✔ Result: Entered Linux environment
│
├── 👤 Step 9: Switch User
│   │
│   └── Command:
│       su - hadoop
│
│   ✔ Result: Logged in as Hadoop user
│
└── ⚡ Step 10: Test PySpark
    │
    └── Command:
        pyspark
       
    ✔ Result: Spark running 🎉
    
    '''






# ---------------- to start after installation
'''
START
│
├── Open Command Prompt / PowerShell
│
├── Run:
│   wsl -d bigdata-env
│
├── Inside Linux:
│   su - hadoop
│
└── Run:
    pyspark

    Ctrl + D --> to exit pyspark
'''



'''
Windows CMD
   ↓
wsl -d bigdata-env
   ↓
Linux Terminal (WSL)
   ↓
su - hadoop
   ↓
Run Hadoop commands ✅
'''