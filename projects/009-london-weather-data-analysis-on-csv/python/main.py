import csv

def read_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("Errore: File non trovato.")
    return data

def general_analysis(data):
    total_max_temp = 0
    max_sunshine = 0
    sunny_day = None
    total_precipitation_august = 0
    cloud_cover_days = 0
    total_days = 0

    for row in data:
        total_days += 1
        max_temp = float(row['max_temp'])
        sunshine = float(row['sunshine'])
        cloud_cover = float(row['cloud_cover'])
        precipitation = float(row['precipitation'])
        date = row['date']

        total_max_temp += max_temp
        if sunshine > max_sunshine:
            max_sunshine = sunshine
            sunny_day = date
        if date.startswith('2023-08'):
            total_precipitation_august += precipitation
        if cloud_cover > 0.5:
            cloud_cover_days += 1

    avg_max_temp = total_max_temp / total_days if total_days > 0 else 0
    cloud_cover_percentage = (cloud_cover_days / total_days) * 100 if total_days > 0 else 0

    return avg_max_temp, sunny_day, total_precipitation_august, cloud_cover_percentage

def weather_extremes(data):
    highest_temp = -float('inf')
    highest_temp_date = None
    highest_precipitation = 0
    highest_precipitation_date = None
    max_snow = 0
    max_snow_date = None

    for row in data:
        max_temp = float(row['max_temp'])
        precipitation = float(row['precipitation'])
        snow_depth = float(row['snow_depth'])
        date = row['date']

        if max_temp > highest_temp:
            highest_temp = max_temp
            highest_temp_date = date
        if precipitation > highest_precipitation:
            highest_precipitation = precipitation
            highest_precipitation_date = date
        if snow_depth > max_snow:
            max_snow = snow_depth
            max_snow_date = date

    return highest_temp_date, highest_temp, highest_precipitation_date, highest_precipitation, max_snow_date, max_snow

def seasonal_analysis(data):
    monthly_totals = {}
    for row in data:
        date = row['date']
        month = date[:7]
        max_temp = float(row['max_temp'])
        precipitation = float(row['precipitation'])

        if month not in monthly_totals:
            monthly_totals[month] = {'max_temp_total': 0, 'precipitation_total': 0, 'days': 0}
        monthly_totals[month]['max_temp_total'] += max_temp
        monthly_totals[month]['precipitation_total'] += precipitation
        monthly_totals[month]['days'] += 1

    monthly_averages = []
    for month, totals in monthly_totals.items():
        avg_max_temp = totals['max_temp_total'] / totals['days']
        avg_precipitation = totals['precipitation_total'] / totals['days']
        monthly_averages.append((month, avg_max_temp, avg_precipitation))

    return monthly_averages

def main():
    data = read_csv("projects/009-london-weather-data-analysis-on-csv/python/data.csv")
    avg_max_temp, sunny_day, total_precipitation_august, cloud_cover_percentage = general_analysis(data)
    print("\n=== Analisi Generale ===")
    print(f"Temperatura massima media: {avg_max_temp:.2f}°C")
    print(f"Giorno con più sole: {sunny_day}")
    print(f"Totale precipitazioni in agosto 2023: {total_precipitation_august:.2f} mm")
    print(f"Percentuale giorni con copertura nuvolosa > 50%: {cloud_cover_percentage:.2f}%")

    highest_temp_date, highest_temp, highest_precipitation_date, highest_precipitation, max_snow_date, max_snow = weather_extremes(data)
    print("\n=== Valori Estremi ===")
    print(f"Giorno più caldo: {highest_temp_date} ({highest_temp:.2f}°C)")
    print(f"Giorno con più precipitazioni: {highest_precipitation_date} ({highest_precipitation:.2f} mm)")
    print(f"Giorno con neve più profonda: {max_snow_date} ({max_snow:.2f} cm)")

    monthly_averages = seasonal_analysis(data)
    print("\n=== Analisi Stagionale ===")
    for month, avg_max_temp, avg_precipitation in monthly_averages:
        print(f"{month}: Temp Max Media: {avg_max_temp:.2f}°C, Precipitazioni Medie: {avg_precipitation:.2f} mm")

if __name__ == "__main__":
    main()