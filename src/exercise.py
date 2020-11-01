from apartment import Apartment

def main():
  manhattan_studio_apt = Apartment(1, 16, 5500)
  atlanta_two_bedroom_apt = Apartment(2, 38, 4200)
  bangor_three_bedroom_apt = Apartment(3, 78, 2500)

  print(manhattan_studio_apt.more_expensive_than(atlanta_two_bedroom_apt))  # true
  print(bangor_three_bedroom_apt.more_expensive_than(atlanta_two_bedroom_apt))   # false


if __name__ == '__main__':
  main()
  from apartment import Apartment
else:
  from src.apartment import Apartment
  
