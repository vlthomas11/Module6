def measurements(a_list):
    """This function measures the area and perimeter of a square or rectangle"""

    def area(a_list):
        area = 0
        if len(a_list) == 1:
            area = a_list[0] * a_list[0]
            print(area)
        elif len(a_list) == 2:
            area = a_list[0] * a_list[1]
        else:
            print("Invalid number of elements")
            raise ValueError
        return area

    def perimeter(a_list):
        perimeter = 0
        if len(a_list) == 1:
            perimeter = a_list[0] * 4
        elif len(a_list) == 2:
            perimeter = ( a_list[0] * 2) + (a_list[1] * 2)
        else:
            print("Invalid number of elements")
            raise ValueError

        return perimeter
    a = area(a_list)
    p = perimeter(a_list)
    #"Perimeter = {Perimeter output} Area = {Area output}"
    return "Perimeter = " + str(p) + " Area = " + str(a)


if __name__ == '__main__':
    measurements()
