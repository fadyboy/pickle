# create functions to pickle and unpickle objects
import pickle

def list_pickler(my_list, my_file):
    '''
        This function takes a list object and pickles it to a file on disk
    '''
    # assign my_list to a list
    #my_list = ["one", 33, "two", "jasmine", 45]

    # create a file object for the pickle in write binary mode
    my_file = open('pickle_file', 'wb')
    #
    # # pickle the list to the file using the pickle dump()
    pickle.dump(my_list, my_file)
    #
    my_file.close()
    #
    #return my_pickle


def unpickler(pickle_file):
    '''
        This function takes a pickled object and unpickles to a variable
    '''
    # open picked object in read binary mode which is the parameter parsed in
    pickle_file = open('pickle_file', 'rb')
    #
    # # unpickle the pickled object by calling the pickle load() and assign to a variable
    my_unpickle = pickle.load(pickle_file)
    #
    # # close file
    pickle_file.close()
    # return the my_unpickle object
    return my_unpickle


