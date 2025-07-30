
# In-memory storage (you can switch to database later)
stored_data = []

def store_analysis(sector, raw_data, analysis, report_file):
    stored_data.append({
        "sector": sector,
        "raw_data": raw_data,
        "analysis": analysis,
        "report_file": report_file
    })

def get_all_stored_data():
    return stored_data
