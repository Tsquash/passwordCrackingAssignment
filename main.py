# Import all methods from the method file -- Also runs the file
#///from methods import *
import sys, getopt

mode = []

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:")
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h"):
         print('test.py -i <inputfile> -o <outputfile>')
         mode.append(opt)
         ##sys.exit()
      elif opt in ("-i"):
         inputfile = arg
         mode += opt
      elif opt in ("-o"):
         outputfile = arg
         mode += opt
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)
   

def decrypt(option):
   if '-i' in mode:
      print("h");
   if '-h' in mode:
      print("what")
if __name__ == "__main__":
   main(sys.argv[1:])