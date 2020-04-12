"""Manager class to store data about weekly points, transfer deductions and other information"""

class Manager(object):
    def __init__(self, name):
        self.name = name
        pass

    def __doc__(self):
        return """Class Manager storing manager name"""

    # def get

class Gameweek(Manager):
    def __init__(self,name, gw_no, gw_point, gw_points_ded):
        Manager.__init__(self,name)
        self.gw_no = "Gameweek "+ str(gw_no)
        self.gw_point = gw_point
        self.gw_points_ded = gw_points_ded
        self.net_points = self.gw_point - self.gw_points_ded

    def __str__(self):
        return "Manager \t \t \t Gameweek No. \t  GW Points \t  Transfer Ded. \t Net Points \n" \
               "%s  \t  %s  \t   %s  \t \t \t  %s  \t \t \t \t  %s" % (self.name, self.gw_no, self.gw_point, self.gw_points_ded, self.net_points)

    def __doc__(self):
        return """A subclass of Manager with name, gw number, gw points and points deduction"""

# BishalGW1 = Gameweek("Bishal Khatri",1,104,4)
# Manager_name =BishalGW1.name.split(" ")
# print(BishalGW1)