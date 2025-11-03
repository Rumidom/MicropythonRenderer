import framebuf
import math

pastelColorPallet = [(27,133,184),(90,82,85),(85,158,131),(174,90,65),(195,203,113),(249,107,75),(249,167,143),(195,155,211),(161,126,111)]

def sin(ang):
    ang = int(ang)
    ang = ang%360
    sintable = (0.0, 0.0175, 0.0349, 0.0523, 0.0698, 0.0872, 0.1045, 0.1219, 0.1392, 0.1564, 0.1736, 0.1908, 0.2079, 0.225, 0.2419, 0.2588, 0.2756, 0.2924, 0.309, 0.3256, 0.342, 0.3584, 0.3746, 0.3907, 0.4067, 0.4226, 0.4384, 0.454, 0.4695, 0.4848, 0.5, 0.515, 0.5299, 0.5446, 0.5592, 0.5736, 0.5878, 0.6018, 0.6157, 0.6293, 0.6428, 0.6561, 0.6691, 0.682, 0.6947, 0.7071, 0.7193, 0.7314, 0.7431, 0.7547, 0.766, 0.7771, 0.788, 0.7986, 0.809, 0.8192, 0.829, 0.8387, 0.848, 0.8572, 0.866, 0.8746, 0.8829, 0.891, 0.8988, 0.9063, 0.9135, 0.9205, 0.9272, 0.9336, 0.9397, 0.9455, 0.9511, 0.9563, 0.9613, 0.9659, 0.9703, 0.9744, 0.9781, 0.9816, 0.9848, 0.9877, 0.9903, 0.9925, 0.9945, 0.9962, 0.9976, 0.9986, 0.9994, 0.9998, 1.0, 0.9998, 0.9994, 0.9986, 0.9976, 0.9962, 0.9945, 0.9925, 0.9903, 0.9877, 0.9848, 0.9816, 0.9781, 0.9744, 0.9703, 0.9659, 0.9613, 0.9563, 0.9511, 0.9455, 0.9397, 0.9336, 0.9272, 0.9205, 0.9135, 0.9063, 0.8988, 0.891, 0.8829, 0.8746, 0.866, 0.8572, 0.848, 0.8387, 0.829, 0.8192, 0.809, 0.7986, 0.788, 0.7771, 0.766, 0.7547, 0.7431, 0.7314, 0.7193, 0.7071, 0.6947, 0.682, 0.6691, 0.6561, 0.6428, 0.6293, 0.6157, 0.6018, 0.5878, 0.5736, 0.5592, 0.5446, 0.5299, 0.515, 0.5, 0.4848, 0.4695, 0.454, 0.4384, 0.4226, 0.4067, 0.3907, 0.3746, 0.3584, 0.342, 0.3256, 0.309, 0.2924, 0.2756, 0.2588, 0.2419, 0.225, 0.2079, 0.1908, 0.1736, 0.1564, 0.1392, 0.1219, 0.1045, 0.0872, 0.0698, 0.0523, 0.0349, 0.0175, 0.0, -0.0175, -0.0349, -0.0523, -0.0698, -0.0872, -0.1045, -0.1219, -0.1392, -0.1564, -0.1736, -0.1908, -0.2079, -0.225, -0.2419, -0.2588, -0.2756, -0.2924, -0.309, -0.3256, -0.342, -0.3584, -0.3746, -0.3907, -0.4067, -0.4226, -0.4384, -0.454, -0.4695, -0.4848, -0.5, -0.515, -0.5299, -0.5446, -0.5592, -0.5736, -0.5878, -0.6018, -0.6157, -0.6293, -0.6428, -0.6561, -0.6691, -0.682, -0.6947, -0.7071, -0.7193, -0.7314, -0.7431, -0.7547, -0.766, -0.7771, -0.788, -0.7986, -0.809, -0.8192, -0.829, -0.8387, -0.848, -0.8572, -0.866, -0.8746, -0.8829, -0.891, -0.8988, -0.9063, -0.9135, -0.9205, -0.9272, -0.9336, -0.9397, -0.9455, -0.9511, -0.9563, -0.9613, -0.9659, -0.9703, -0.9744, -0.9781, -0.9816, -0.9848, -0.9877, -0.9903, -0.9925, -0.9945, -0.9962, -0.9976, -0.9986, -0.9994, -0.9998, -1.0, -0.9998, -0.9994, -0.9986, -0.9976, -0.9962, -0.9945, -0.9925, -0.9903, -0.9877, -0.9848, -0.9816, -0.9781, -0.9744, -0.9703, -0.9659, -0.9613, -0.9563, -0.9511, -0.9455, -0.9397, -0.9336, -0.9272, -0.9205, -0.9135, -0.9063, -0.8988, -0.891, -0.8829, -0.8746, -0.866, -0.8572, -0.848, -0.8387, -0.829, -0.8192, -0.809, -0.7986, -0.788, -0.7771, -0.766, -0.7547, -0.7431, -0.7314, -0.7193, -0.7071, -0.6947, -0.682, -0.6691, -0.6561, -0.6428, -0.6293, -0.6157, -0.6018, -0.5878, -0.5736, -0.5592, -0.5446, -0.5299, -0.515, -0.5, -0.4848, -0.4695, -0.454, -0.4384, -0.4226, -0.4067, -0.3907, -0.3746, -0.3584, -0.342, -0.3256, -0.309, -0.2924, -0.2756, -0.2588, -0.2419, -0.225, -0.2079, -0.1908, -0.1736, -0.1564, -0.1392, -0.1219, -0.1045, -0.0872, -0.0698, -0.0523, -0.0349, -0.0175)
    return(sintable[ang])

def cos(ang):
    return sin(90-ang)

def tan(ang):
    ang = int(ang)
    ang = ang%360
    tantable = (0.0, 0.0175, 0.0349, 0.0524, 0.0699, 0.0875, 0.1051, 0.1228, 0.1405, 0.1584, 0.1763, 0.1944, 0.2126, 0.2309, 0.2493, 0.2679, 0.2867, 0.3057, 0.3249, 0.3443, 0.364, 0.3839, 0.404, 0.4245, 0.4452, 0.4663, 0.4877, 0.5095, 0.5317, 0.5543, 0.5774, 0.6009, 0.6249, 0.6494, 0.6745, 0.7002, 0.7265, 0.7536, 0.7813, 0.8098, 0.8391, 0.8693, 0.9004, 0.9325, 0.9657, 1.0, 1.0355, 1.0724, 1.1106, 1.1504, 1.1918, 1.2349, 1.2799, 1.327, 1.3764, 1.4281, 1.4826, 1.5399, 1.6003, 1.6643, 1.7321, 1.804, 1.8807, 1.9626, 2.0503, 2.1445, 2.246, 2.3559, 2.4751, 2.6051, 2.7475, 2.9042, 3.0777, 3.2709, 3.4874, 3.7321, 4.0108, 4.3315, 4.7046, 5.1446, 5.6713, 6.3138, 7.1154, 8.1443, 9.5144, 11.4301, 14.3007, 19.0811, 28.6363, 57.29, 99999999.0, -57.29, -28.6363, -19.0811, -14.3007, -11.4301, -9.5144, -8.1443, -7.1154, -6.3138, -5.6713, -5.1446, -4.7046, -4.3315, -4.0108, -3.7321, -3.4874, -3.2709, -3.0777, -2.9042, -2.7475, -2.6051, -2.4751, -2.3559, -2.246, -2.1445, -2.0503, -1.9626, -1.8807, -1.804, -1.7321, -1.6643, -1.6003, -1.5399, -1.4826, -1.4281, -1.3764, -1.327, -1.2799, -1.2349, -1.1918, -1.1504, -1.1106, -1.0724, -1.0355, -1.0, -0.9657, -0.9325, -0.9004, -0.8693, -0.8391, -0.8098, -0.7813, -0.7536, -0.7265, -0.7002, -0.6745, -0.6494, -0.6249, -0.6009, -0.5774, -0.5543, -0.5317, -0.5095, -0.4877, -0.4663, -0.4452, -0.4245, -0.404, -0.3839, -0.364, -0.3443, -0.3249, -0.3057, -0.2867, -0.2679, -0.2493, -0.2309, -0.2126, -0.1944, -0.1763, -0.1584, -0.1405, -0.1228, -0.1051, -0.0875, -0.0699, -0.0524, -0.0349, -0.0175, -0.0, 0.0175, 0.0349, 0.0524, 0.0699, 0.0875, 0.1051, 0.1228, 0.1405, 0.1584, 0.1763, 0.1944, 0.2126, 0.2309, 0.2493, 0.2679, 0.2867, 0.3057, 0.3249, 0.3443, 0.364, 0.3839, 0.404, 0.4245, 0.4452, 0.4663, 0.4877, 0.5095, 0.5317, 0.5543, 0.5774, 0.6009, 0.6249, 0.6494, 0.6745, 0.7002, 0.7265, 0.7536, 0.7813, 0.8098, 0.8391, 0.8693, 0.9004, 0.9325, 0.9657, 1.0, 1.0355, 1.0724, 1.1106, 1.1504, 1.1918, 1.2349, 1.2799, 1.327, 1.3764, 1.4281, 1.4826, 1.5399, 1.6003, 1.6643, 1.7321, 1.804, 1.8807, 1.9626, 2.0503, 2.1445, 2.246, 2.3559, 2.4751, 2.6051, 2.7475, 2.9042, 3.0777, 3.2709, 3.4874, 3.7321, 4.0108, 4.3315, 4.7046, 5.1446, 5.6713, 6.3138, 7.1154, 8.1443, 9.5144, 11.4301, 14.3007, 19.0811, 28.6363, 57.29, 99999999.0, -57.29, -28.6363, -19.0811, -14.3007, -11.4301, -9.5144, -8.1443, -7.1154, -6.3138, -5.6713, -5.1446, -4.7046, -4.3315, -4.0108, -3.7321, -3.4874, -3.2709, -3.0777, -2.9042, -2.7475, -2.6051, -2.4751, -2.3559, -2.246, -2.1445, -2.0503, -1.9626, -1.8807, -1.804, -1.7321, -1.6643, -1.6003, -1.5399, -1.4826, -1.4281, -1.3764, -1.327, -1.2799, -1.2349, -1.1918, -1.1504, -1.1106, -1.0724, -1.0355, -1.0, -0.9657, -0.9325, -0.9004, -0.8693, -0.8391, -0.8098, -0.7813, -0.7536, -0.7265, -0.7002, -0.6745, -0.6494, -0.6249, -0.6009, -0.5774, -0.5543, -0.5317, -0.5095, -0.4877, -0.4663, -0.4452, -0.4245, -0.404, -0.3839, -0.364, -0.3443, -0.3249, -0.3057, -0.2867, -0.2679, -0.2493, -0.2309, -0.2126, -0.1944, -0.1763, -0.1584, -0.1405, -0.1228, -0.1051, -0.0875, -0.0699, -0.0524, -0.0349, -0.0175)
    return (tantable[ang])

def color565(rgb):
    return (rgb[0] & 0xf8) << 8 | (rgb[1] & 0xfc) << 3 | rgb[2] >> 3

def rotPnt(pnt,ang):
    rotY = getYrot(ang[1]) 
    rotX = getXrot(ang[0])
    rot_a = transformVec(rotY[0],rotY[1],rotY[2],rotX[0])
    rot_b = transformVec(rotY[0],rotY[1],rotY[2],rotX[1])
    rot_c = transformVec(rotY[0],rotY[1],rotY[2],rotX[2])
    pnt_out = transformVec(rot_a,rot_b,rot_c,pnt)
    return pnt_out
    
def getYrot(ang):
    xhat = (cos(ang),0.0,sin(ang))
    yhat = (0.0,1.0,0.0)
    zhat = (-sin(ang),0.0,cos(ang))
    return (xhat,yhat,zhat)
    
def getXrot(ang):
    xhat = (1.0,0.0,0.0)
    yhat = (0.0,cos(ang),-sin(ang))
    zhat = (0.0,sin(ang),cos(ang))
    return (xhat,yhat,zhat)

def rotcamPnt(pnt,ang):
    rotY = getYrot(-ang[1]) 
    rotX = getXrot(-ang[0])
    rot_a = transformVec(rotX[0],rotX[1],rotX[2],rotY[0])
    rot_b = transformVec(rotX[0],rotX[1],rotX[2],rotY[1])
    rot_c = transformVec(rotX[0],rotX[1],rotX[2],rotY[2])
    pnt_out = transformVec(rot_a,rot_b,rot_c,pnt)
    return pnt_out

def transformVec(xhat,yhat,zhat,pnt):
    out_x = xhat[0]*pnt[0]+yhat[0]*pnt[1]+zhat[0]*pnt[2]
    out_y = xhat[1]*pnt[0]+yhat[1]*pnt[1]+zhat[1]*pnt[2]
    out_z = xhat[2]*pnt[0]+yhat[2]*pnt[1]+zhat[2]*pnt[2]
    #print((out_x,out_y,out_z))
    return (out_x,out_y,out_z)
    
def dot_2d(a,b):
    return (a[0]*b[0] + a[1]*b[1])

def dot_3d(a,b):
    return (a[0]*b[0] + a[1]*b[1]+ a[2]*b[2])

def cross_3d(a,b):
    return (a[1]*b[2]-a[2]*b[1],-(a[0]*b[2]-a[2]*b[0]),a[0]*b[1]-a[1]*b[0])
    
def getperpendicular_clock(a):
    return (a[1],-a[0])

def posPnt(pnt,pos):
    return((pnt[0]+pos[0],pnt[1]+pos[1],pnt[2]+pos[2]))

def verticeToScreen(vertice,ang,pos,screen_size,cam_ang = (0,0)):
    pnt = rotPnt(vertice,ang)
    pnt = posPnt(pnt,pos)
    pnt = rotcamPnt(pnt,cam_ang)
    FOV = 60
    screenHeightWorld = tan(FOV/2)*2
    if pnt[2] <= 0:
        return None
    pixelsPerUnitWorld = screen_size[1]/screenHeightWorld/pnt[2]
    pixelOffset = (pnt[0]*pixelsPerUnitWorld,pnt[1]*pixelsPerUnitWorld)

    
    return ((screen_size[0]/2)+pixelOffset[0],(screen_size[1]/2)+pixelOffset[1])

def getlineX(strt_pnt,slope,y):
    x0,y0 = strt_pnt
    if slope == 0:
        return x0 
    elif slope == math.inf:
        return x0
    else:
        return int(((y-y0)/slope)+x0)

def transformColor(Color,ilumi):
    newColor = []
    #for i in range(3):
        #col = int(Color[i]*(ilumi-0.5))
        #if col > 255:
        #    col = 255
        #elif col < 0:
        #    col = 0
        #newColor.append(col)
    #print(Color,' -> ',newColor)
    return tuple(Color)
    
def PointsDistance3d(a,b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 )
    
class line_2d():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def isPointOnRightSide(self,pnt):
        ap = (pnt[0]-self.a[0],pnt[1]-self.a[1])
        ab_perp = getperpendicular_clock((self.b[0]-self.a[0],self.b[1]-self.a[1]))
        return (Dot_2d(ap,ab_perp) >= 0)

    def getSlope(self):
        subx = (self.a[0] - self.b[0])
        if subx == 0:
            return math.inf
        return (self.a[1] - self.b[1])/subx
    
class triangle_2d():
    def __init__(self,a,b,c,color = (255, 255, 255),lumination=0):
        stdpnts = sorted([a,b,c], key=lambda tup: tup[1])
        #print(stdpnts)
        self.a = (int(stdpnts[0][0]),int(stdpnts[0][1]))
        self.b = (int(stdpnts[1][0]),int(stdpnts[1][1]))
        self.c = (int(stdpnts[2][0]),int(stdpnts[2][1]))
        self.ab = line_2d(self.a,self.b)
        self.bc = line_2d(self.b,self.c)
        self.ca = line_2d(self.c,self.a)
        self.ab_slope = self.ab.getSlope()
        self.bc_slope = self.bc.getSlope()
        self.ca_slope = self.ca.getSlope()
        self.color = color
        
    def triangleArea(self):
        ac = (self.c[0]-self.a[0],self.c[1]-self.a[1])
        ab_perp = getperpendicular_clock((self.b[0]-self.a[0],self.b[1]-self.a[1]))
        return dot_2d(ac,ab_perp)
        
    def pointInTriangle(self,pnt):        
        max_x = max(self.a[0],self.b[0],self.c[0])
        max_y = max(self.a[1],self.b[1],self.c[1])
        min_x = min(self.a[0],self.b[0],self.c[0])
        min_y = min(self.a[1],self.b[1],self.c[1])
        if pnt[0] < max_x and pnt[0]> min_x:
            if pnt[1] < max_y and pnt[1]> min_y:
                check_ab = self.ab.isPointOnRightSide(pnt)
                check_bc = self.bc.isPointOnRightSide(pnt)
                check_ca = self.ca.isPointOnRightSide(pnt)
                return (check_ab and check_bc and check_ca)
        return False

    def half_render(self,ystart,ystop,pnt0,pnt1,slope0,slope1,fbuf,im_size,wireframe=False):
        for y in range(int(ystart),int(ystop)):
            x0 = getlineX(pnt0,slope0,y)
            x1 = getlineX(pnt1,slope1,y)             
            x0 = max(min(x0, im_size[0]-1), 0)
            x1 = max(min(x1, im_size[0]-1), 0)
            y = max(min(y, im_size[1]-1), 0)
            #print(x0,x1)
            #print(slope0,' ',x0) 
            x_pnts = sorted([x0,x1])
            if wireframe:
                fbuf.pixel(x_pnts[0],y, color565(self.color))
                fbuf.pixel(x_pnts[1],y, color565(self.color))
            else:
                for x in range(x_pnts[0],x_pnts[1]):
                    #print(x,y)
                    fbuf.pixel(x,y, color565(self.color))
                    
    def render(self,fbuf,im_size):
        #print(self.triangleArea()," ",self.a,self.b,self.c)
        self.half_render(self.a[1],self.b[1],self.a,self.a,self.ab_slope,self.ca_slope,fbuf,im_size)
        self.half_render(self.b[1],self.c[1],self.b,self.a,self.bc_slope,self.ca_slope,fbuf,im_size)

class triangle_3d():
    def __init__(self,a,b,c,ang,pos,color = (255, 255, 255) ):
        self.a = a
        self.b = b
        self.c = c
        self.color = color
        self.ang = ang
        self.pos = pos

    def facingVectorCheck(self,camNormal):
        dot = dot_3d(self.getNormal(),camNormal) 
        #print(self.getNormal(),' ',dot)
        return (dot> 0)
        
    def getNormal(self):
        a,b,c = self.getUpdatedVertices()
        ac = (c[0]-a[0],c[1]-a[1],c[2]-a[2])
        ab = (b[0]-a[0],b[1]-a[1],b[2]-a[2])
        cross = cross_3d(ac,ab)
        crosslen = math.sqrt(cross[0]**2+cross[1]**2+cross[2]**2)
        normal = (cross[0]/crosslen,cross[1]/crosslen,cross[2]/crosslen)
        return normal
        
    def getClosestdistance(self,pnt):
        distances = []
        for v in [self.a,self.b,self.c]:
            distances.append(PointsDistance3d(v,pnt))
        return min(distances)
        
    def getCentroid(self):
        cx = (self.a[0]+self.b[0]+self.c[0])/3
        cy = (self.a[1]+self.b[1]+self.c[1])/3
        cz = (self.a[2]+self.b[2]+self.c[2])/3
        return((cx,cy,cz))
    
    def getDistanceToCentroid(self,pnt):
        c = self.getCentroid()
        #print(c)
        c = rotPnt(c,self.ang)
        c = posPnt(c,self.pos)
        return PointsDistance3d(c,pnt)
        
    def trig_3dToTrig_2d(self,cam_ang,im_size):
        a_ = verticeToScreen(self.a,self.ang,self.pos,im_size,cam_ang = cam_ang)
        b_ = verticeToScreen(self.b,self.ang,self.pos,im_size,cam_ang = cam_ang)
        c_ = verticeToScreen(self.c,self.ang,self.pos,im_size,cam_ang = cam_ang)
        if a_ == None or b_ == None or c_ == None:
            return None
        lightdirection = (0,0.8,0.2)
        global_ilumi = 0.7
        ilumi = dot_3d(lightdirection,self.getNormal())
        ilumi += global_ilumi
        if ilumi < 1:
            ilumi = 1 +ilumi
        if ilumi > 1.5:
            ilumi = 1.5
        newColor = transformColor(self.color,ilumi)
        return triangle_2d(a_,b_,c_,color=newColor)
    
    def getUpdatedVertices(self):
        a = rotPnt(self.a,self.ang)
        a = posPnt(a,self.pos)
        b = rotPnt(self.b,self.ang)
        b = posPnt(b,self.pos)
        c = rotPnt(self.c,self.ang)
        c = posPnt(c,self.pos)
        return (a,b,c)
    
    def update(self,ang,pos):
        self.pos = pos
        self.ang = ang
        
    def render(self,fbuf,im_size,cam_ang):
        #self.trig_3dToTrig_2d().render_old(im)
        tri_2d = self.trig_3dToTrig_2d(cam_ang,im_size)
        if tri_2d != None:
            tri_2d.render(fbuf,im_size)
        
class model():
    def __init__(self,vertices,faces,tri_indexes,pos=(0,0,0),ang=(0,0),updateVertices = False):
        self.vertices = vertices
        self.faces = faces
        self.tri_indexes = tri_indexes
        self.ang = ang
        self.pos = pos
        self.colorPallet = pastelColorPallet
        self.triangles = []
        self.updateTriangles(updateVertices=updateVertices)
        
    def updateTriangles(self,updateVertices=False):
        self.triangles = []
        if updateVertices:
            for i in range(len(self.vertices)):
                #print(": ",self.vertices[i])
                self.vertices[i] = rotPnt( self.vertices[i],self.ang)
                self.vertices[i] = posPnt( self.vertices[i],self.pos)
                #self.vertices[i] = (round(self.vertices[i][0], 2),round(self.vertices[i][1], 2),round(self.vertices[i][2], 2))
                #print("> ",self.vertices[i])
            self.ang = (0,0)
            self.pos = (0,0,0)
        for j,t_i in enumerate(self.tri_indexes):
            a = self.vertices[t_i[0]]
            b = self.vertices[t_i[1]]
            c = self.vertices[t_i[2]]
            t = triangle_3d(a,b,c,self.ang,self.pos,color=self.colorPallet[j%len(self.colorPallet)])
            #print(t.color)
            self.triangles.append(t)    

    def setColorPallet(self,colorPallet):
        self.colorPallet = colorPallet
        for t in self.triangles:
            t.color = self.colorPallet[j%len(self.colorPallet)]
        
    def render(self,fbuf,im_size,cameraFacingCheck = False,cam_ang=(0,0)):
        tup_list = []
        for t in self.triangles:
            t.update(self.ang,self.pos)
            cam_dist = t.getDistanceToCentroid((0,0,0))
            tup_list.append((t,cam_dist))
        tup_list = sorted(tup_list, key=lambda tup: tup[1],reverse=True)
        #print(tup_list)
        for tup in tup_list:
            #print(tup[0].facingVectorCheck((0,0,1)))
            if tup[0].facingVectorCheck((0,0,-1)) or not cameraFacingCheck:
                tup[0].render(fbuf,im_size,cam_ang)

class multipart_model(model):
    def __init__(self,models = []):
        model.__init__(self, [], [],[])
        self.models = models
        self.lastIndex = 0
        
    def addModel(self,m_obj):
        m_obj.updateTriangles(updateVertices=True)
        self.models.append(m_obj)
        self.triangles.extend(m_obj.triangles)
        
def loadObj(path,pos=(0,0,0),ang=(0,0)):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    triangles = []
    faces = []
    vertices = []
    for line in lines:
        if line[0:2] == 'v ':
            vertice_str = line[2:].split(' ')
            v = []
            for item in vertice_str:
                v.append(float(item))
            #print(v)
            vertices.append(v)
        if line[0:2] == "f ":
            face_str = line[2:].split(' ')
            f = []
            for tstr in face_str:
                f.append(int(tstr.split('/')[0]))
            faces.append(tuple(f))
    for face in faces:
        #print(face)
        a = face[0]-1
        for i in range(len(face)-2):
            b = face[i+1]-1
            c = face[i+2]-1
            triangles.append((a,b,c))
    
    return(model(vertices,faces,triangles,pos=pos,ang=ang))