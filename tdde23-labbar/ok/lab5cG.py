"""
Emil Wiman, emiwi425
August Nordin, augno992
Laboration 5, del C uppgift G. Testning och undantagshantering.
"""


def test_all():
    def pixel_constraint(hlow,hhigh,slow,shigh,vlow,vhigh):
        """
        Function that returns a function that returns a 1 if its in the correct
        range and 0 i its out of bounds.
        """
        def compareer(pixel):
            (h,s,v) = pixel
            if h > hlow and h < hhigh and \
                    s > slow and s < shigh and \
                    v > vlow and v < vhigh:
                return 1
            else:
                return 0
        return compareer

    compareer = pixel_constraint(0,255,0,255,0,255)
    assert compareer((123,123,123)) == 1    #Value in range, therefore its valid
    assert compareer((0,0,0)) == 0          #Value is out of bounds, therefore invalid
    assert compareer((100,125,150)) == 1    #Different values in range works

    def generator_from_image(orig_list):
        """
        This function returns a function that returns the index of the input index.
        """
        def generated_list(index):
            pixel = orig_list[index]
            return pixel
        return generated_list

    generated_list = generator_from_image([1,2,3])
    assert generated_list(1) == 2       #Test with index 1 returns the value of that place
    assert generated_list(2) == 3       #Test with index 2 returns the value of that place
    assert generated_list(0) == 1       #Test with index 3 returns the value of that place


    def generator1(index):
        """
        Generates a  night sky.
        """
        val = random.random() * 255 if random.random() > 0.99 else 0
        return (val, val, val)


    def combine_images(hsv_list, cond, gen1, gen2):
        """
        Function that combines images
        """
        cond_list = []
        rbg_list = []
        for i in range(len(hsv_list)):
            hold = cond(hsv_list[i])
            cond_list.append(hold)
        for i in range(len(hsv_list)):
            rbg_list.append(gen2(i))
        for i in range(len(hsv_list)):
            if cond_list[i] == 1:
                rbg_list[i] = gen1(rbg_list[i])
        return rbg_list

    cond = pixel_constraint(250,255,250,255,250,255)
    gen1 = generator1
    gen2 = generator_from_image([(1,1,1)])
    gen2_2 = generator_from_image([(0,0,0)])
    
    assert combine_images([(1,1,1,)],cond, gen1, gen2) == [(1,1,1)]
    # List with elements that are out of range should return the same elements
    assert combine_images([(0,0,0)], cond, gen1, gen2_2) == [(0,0,0)]
    #List with elements that are out of range should return the same elements

    print ("passed all tests")
