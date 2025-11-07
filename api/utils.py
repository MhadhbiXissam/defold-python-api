import os 




class Utils : 
    def pathjoin(*args) : 
        return os.path.join(*args)





if __name__ == "__main__" : 
    x = ("1","2")
    print(Utils.pathjoin(*x))