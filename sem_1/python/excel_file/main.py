# import openpyxl
# wb=openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\global_superstore.xlsx")
# # print(type(wb))
# ws=wb.active
# # print(ws)
# # print(f"maximum row in worksheet {ws.max_row} and maximum column in worksheet {ws.max_column}")
# # working with cell
# print(ws['A1'].value)
# # the value of cell 1 is order_id
# # getting all the column 
# # values=[ws.cell(row=i,column=6).value for i in range(2, ws.max_row+1)]
# # print(values)

# '''
# # vv
# my_list = []
# # ---------- Step 3: Read rows from Excel ----------
# for value in ws.iter_rows(
#         min_row=1,
#         max_row=11,
#         min_col=1,
#         max_col=4,
#         values_only=True):
#     my_list.append(value)
# for ele1, ele2, ele3, ele4 in my_list:
#     # print(ele1, ele2, ele3, ele4)
#     print("{:<20}{:<50}{:<50}{:<20}".format(ele1, ele2, ele3, ele4))
# '''

# # writing in a excelsheet
# ws['T1']='hello prabhat'
# ws.cell(row=2,column=15,value='no prabhat')

# # creating new column

# wb.save("C:\\Users\\piyush kumar\\Downloads\\global_superstore.xlsx")







#------------------------ adding new column
# import openpyxl

# # Load workbook
# wb = openpyxl.load_workbook(
#     "C:\\Users\\piyush kumar\\Downloads\\global_superstore.xlsx"
# )

# # Select active worksheet
# ws = wb.active

# # Add header for new column
# ws.cell(row=1, column=20).value = "Total Salary"

# # Loop through all data rows
# for row in range(2, ws.max_row + 1):
#     total = 0
#     for col in [16,19]:  # G(7) to J(10)
#         value = ws.cell(row=row, column=col).value
#         if value is not None:
#             total += value

#     # Write total into column K
#     ws.cell(row=row, column=20).value = total

# # Save to new file
# wb.save("C:\\Users\\piyush kumar\\Downloads\\global_superstore.xlsx")

# print("New column created and totals calculated successfully")



# 
# import openpyxl

# # Load Excel file
# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# ws = wb.active

# # Add header for Total_Sales (column F)
# ws.cell(row=1, column=6).value = "Total_Sales"

# # Loop through all data rows (skip header)
# for row in range(2, ws.max_row + 1):

#     NA_Sales = ws.cell(row=row, column=2).value or 0   # B
#     EU_Sales = ws.cell(row=row, column=3).value or 0   # C
#     JP_Sales = ws.cell(row=row, column=4).value or 0   # D
#     Other_Sales = ws.cell(row=row, column=5).value or 0 # E

#     total_sales = NA_Sales + EU_Sales + JP_Sales + Other_Sales

#     # Write Total_Sales into column F
#     ws.cell(row=row, column=6).value = total_sales

# # Save to new file
# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")

# print("Total_Sales column created successfully")




# -----------------------adding a row
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# ws = wb.active

# # New row data (must match column order)
# new_row = ["Game D", 210, 180, 160, 140]

# # Add row at the end
# ws.append(new_row)

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")

# print("New row added successfully")



# ------------------------------ delete a row
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# ws = wb.active

# # Delete row number 3
# ws.delete_rows(3)

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")

# print("Row 3 deleted successfully")


# # ------------------------------- coutif
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# ws = wb.active

# # Label
# ws["H1"] = "Count of Game A"

# # COUNTIF formula
# ws["H2"] = '=COUNTIF(A2:A100,"Game A")'

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")



# ------------------------------- sumif
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# ws = wb.active

# # Label
# ws["H4"] = "Total NA Sales of Game A"

# # SUMIF formula
# ws["H5"] = '=SUMIF(A2:A100,"Game A",B2:B100)'

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")



# ------------------------------ celing()
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# ws = wb.active

# # Header
# ws["G1"] = "Rounded_Total_100"

# # Apply CEILING formula for all rows
# for row in range(2, ws.max_row + 1):
#     ws[f"G{row}"] = f"=CEILING(F{row},100)"

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")




# ------------------------------- creatiing new worksheet
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")

# # Create a new worksheet
# ws_new = wb.create_sheet(title="Summary")

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# print("New worksheet created")
'''
🧠 What happens

A new sheet named Summary is added
It appears at the end of the workbook


📌 Create at a specific position
wb.create_sheet(title="Report", index=0)

➡ Creates sheet as first sheet
'''




# -------------------- deleting a worksheet
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")

# # Delete worksheet by name
# del wb["Summary"]

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# print("Worksheet deleted")
'''
⚠️ Important

Sheet name must exist
You cannot undo deletion

❌ Wrong way (common mistake)
wb.remove("Summary")  # ❌ wrong
'''


# -------------------------- duplicate copy of the worksheet
# import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")

# ws = wb["VideoSales"]

# # Copy worksheet
# copy_ws = wb.copy_worksheet(ws)
# copy_ws.title = "VideoSales_Copy"

# wb.save("C:\\Users\\piyush kumar\\Downloads\\VideoSales_With_Values.xlsx")
# print("Worksheet duplicated")
'''
🧠 What gets copied
✔ Data
✔ Formatting
✔ Formulas

❌ Charts & images may not copy fully
'''