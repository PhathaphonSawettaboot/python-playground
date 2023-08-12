def be_to_ad(buddhist_year):
    return buddhist_year - 543

buddhist_year = int(input("Enter a year in Buddhist Era (BE): "))

anno_domini_year = be_to_ad(buddhist_year)
print(f"{buddhist_year} BE is equivalent to {anno_domini_year} AD.")