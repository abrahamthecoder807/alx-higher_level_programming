#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    elif idx == []:
        return None
    else:
        return my_list[idx]
