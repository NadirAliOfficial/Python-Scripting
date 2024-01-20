import csv


def csv_to_txt(csv_file):
    with open(csv_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Assuming the first row is the header

        # Use the first column to generate the txt file name
        txt_file_name = header[0].lower() + "_output.txt"

        # Create and write to the txt file
        with open(txt_file_name, "w") as txt_file:
            for row in reader:
                for value in row:
                    txt_file.write(value + "\n")


print("ello")
if __name__ == "__main__":
    csv_file_path = r"C:\Users\MS Computer\Downloads\order30078.csv"  # Replace with your actual CSV file path
    csv_to_txt(csv_file_path)
