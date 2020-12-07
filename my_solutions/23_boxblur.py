def boxBlur(image):
    blur=[]
    blur_row=[]
    row=0
    column=0
    for i in range(0,len(image)-2):
        tmp=[]
        for j in range(0,len(image[0])-2):
            total=0
            for m in range(row,row+3):
                for n in range(column,column+3):
                    total=total+image[m][n]
            column=column+1
            blur_row.append(int(total/9))
        blur.append(blur_row)
        blur_row=[]
        row=row+1
        column=0
    return blur
