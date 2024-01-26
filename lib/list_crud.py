# create_an_empty_list
def create_an_empty_list():
    return []

# create_a_list
def create_a_list():
    return [2,9,8,19]

# add_element_to_end_of_list
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

# add_element_to_start_of_list
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

# remove_element_from_end_of_list
def remove_element_from_end_of_list(l):
    l.pop()
    return l

# remove_element_from_start_of_list
def remove_element_from_start_of_list(l):
    del l[0]
    return l

# retrieve_first_element_from_list
def retrieve_first_element_from_list(l):
    return l[0]

# etrieve_element_from_index
def retrieve_element_from_index(l, index):
    retrieve = l[index]
    return retrieve

# etrieve_last_element_from_list
def retrieve_last_element_from_list(l):
    red=l.pop()
    return red
