class Plain():
    def __init__(self,left=-10,right=5,bottom=-10,top=5,distance=1,nx = 100,ny = 100):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.distance = 1/distance
        self.len_lines = nx
        self.len_colunms = ny

    def get_scalar_param_ul(self):
        return self.left,self.right,self.len_lines

    def get_scalar_param_vl(self):
        return self.bottom,self.top,self.len_colunms

