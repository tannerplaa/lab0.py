def weight_on_planets():
  weight = int(input('What do you weigh on Earth? '))
  mars = str(0.38 * weight)
  jupiter = str(2.34 * weight)
  print('On Mars you would weigh ' + weight + ' pounds.\nOn Jupiter you would weigh ' + weight + ' pounds.')
   
if __name__ == '__main__':
   weight_on_planets()
