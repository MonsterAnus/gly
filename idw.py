#distance formula
def euc_dist(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

#IDW formula
def idw_head(coordinate_list,head,beta):
    excluded_coords = []
    for x, y, val in coordinate_list:
        head[x,y] = val
        excluded_coords.append((x,y))
    for i in range(len(head)):
        for i_n in range(len(head)):
            #set up w, wizi
            w = []
            w_i_z_i = 0
            if (i, i_n) in excluded_coords:
                continue
            else:
                for i_w in range(len(coordinate_list)):
                    w.append(round(euc_dist(i,coordinate_list[i_w][0],i_n,coordinate_list[i_w][1]),6))
                w_i = round(sum(w),6)
                for i_w_z in range(len(coordinate_list)):
                    w_i_z_i += w[i_w_z]*coordinate_list[i_w_z][2]

                z0 = round(w_i_z_i/w_i,6)
                head[i,i_n] = z0
    #             print(i,i_n)
    #             print(w)
    #             print(w_i)
    #             print(w_i_z_i)
    #             print(z0)
    #             print('\n')

#Example of Usage:
#head
head = np.ones((nx, ny))

#0 is x, 1 is y, and 2 is the hydraulic head
coordinate_list = [(0, 0, 30),
                   (int(nx)-1,int(ny)-1, 36),
                   (47, 89, 32),
                   (157,36,41),
                   (354,450,39)
                  ]

#set beta
beta = 1

#Run IDW
idw_head(coordinate_list,head,beta)

plt.imshow(head, cmap='jet')
plt.colorbar()
plt.show()
