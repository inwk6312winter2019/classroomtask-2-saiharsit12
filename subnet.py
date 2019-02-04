import sys
import ipcalc

class ip_calc():
      
      def __init__(self,ip=[0,0,0,0],nm=[0,0,0,0]):
      
          self.ip = ip
          self.nm = nm
      
      def __str__(self):
      
          ipformat = ""
          for ips in self.ip:
              ipformat = ipformat + str(ips) +  "."
          return("The ip address is:" + ipformat)

myip = ip_calc([192,168,0,0],[255,255,255,0])

print(myip)
