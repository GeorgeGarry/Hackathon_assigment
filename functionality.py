# import win32api
# from flask import Flask, render_template
from datetime import datetime
import csv
import os.path
final_list = []

            # getting name of the concenttrator and the indexes of required lines (start and end)
def read_report(file_name):
    reader = open(file_name, "r")
    list_report = reader.readlines()
    cnc_name = list_report[0].replace("No.:", "")
    report_start_line = 0
    report_end_line = 0
    check_not_empty = "empty"
    for i in range(len(list_report)-1):
        if "_Meter__"  in list_report[i]:
            report_start_line = i+1
            check_not_empty = "not_empty"
            break
            pass
    if check_not_empty == "not_empty":
        for i in range(report_start_line, len(list_report)):
            if len(list_report[i]) == 1:
                report_end_line = i
                break
                pass
            pass
        pass
    return {"start": report_start_line, "end": report_end_line, "list_report": list_report, "cnc_name": cnc_name, "check_not_empty": check_not_empty }
    # return [report_start_line, report_end_line, list_report, cnc_name, empty_report]
    pass

            # function getting the required data of a single text file
# def get_one_report_result(start, end, report_array, concentrator_number, empty_report):
def get_one_report_result(keys):
    if keys["check_not_empty"] == "empty":
        columns = []
        row = []
        row.append("Empty report")
        row.append("Empty report")
        row.append("Empty report")
        row.append(keys["cnc_name"])
        columns.append(row)
        pass
    else:
        columns = []
        for i in range(keys["start"], keys["end"]):
            print
            row = []
            one_line = keys["list_report"][i].split("|")
            row.append(one_line[0])
            row.append(one_line[2])
            row.append(one_line[6])
            row.append(keys["cnc_name"])
            columns.append(row)
            pass
        pass
    
    return columns
    pass

            # writing final array of reports to a CSV file
def filling_report(reports_list):
    headers = ["Meter", "Date", "kWh", "Concentrator #"]
    if os.path.exists("final_report_" + str(datetime.now()) + ".csv"):
        file_name = "final_report_" + str(datetime.now()) + ".csv"
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            for i in reports_list:
                for j in i:
                    writer.writerow(j)
                pass
    else:
        file_name = "final_report_" + str(datetime.now()) + ".csv"
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for i in reports_list:
                for j in i:
                    writer.writerow(j)
                pass 
    file.close()
    return file_name
    pass

