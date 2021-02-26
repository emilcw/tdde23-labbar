"""
Emil Wiman, emiwi425
August Nordin, augno992
Laboration 5, del C uppgift H. Testning och undantagshantering.
"""


def test_all():
    def pixel_constraint(hlow,hhigh,slow,shigh,vlow,vhigh):
        """
        Function that returns a function that returns a 1 if its in the correct
        range and 0 i its out of bounds.
        """
        def compareer(pixel):
        try:
            (h,s,v) = pixel
        except ValueError:
                print("Tupel must consist of three numerical values between 0 and 255")

            if h > hlow and h < hhigh and \
                    s > slow and s < shigh and \
                    v > vlow and v < vhigh:
                return 1
            else:
                return 0
        return compareer


    def generator_from_image(orig_list):
        """
        This function returns a function that returns the index of the input index.
        """
        def generated_list(index):
        try:
            pixel = orig_list[index]
        except IndexError:
            print("Index out of range")

            return pixel
        return generated_list


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
        try:
            for i in range(len(hsv_list)):
                hold = cond(hsv_list[i])
                cond_list.append(hold)
        except ValueError:
            print("Tupel must consist of three numerical values between 0 and 255")
        try:
            for i in range(len(hsv_list)):
                rbg_list.append(gen2(i))
        except IndexError:
            print("Index out of range")
        for i in range(len(hsv_list)):
            if cond_list[i] == 1:
                rbg_list[i] = gen1(rbg_list[i])
        return rbg_list
