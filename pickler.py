# create functions to pickle and unpickle objects
import pickle

def list_pickler(my_list, my_file):
    '''
        This function takes a list object and pickles it to a file on disk
    '''
    pickle_file = open(my_file, 'wb')
    pickle.dump(my_list, pickle_file)

    pickle_file.close()


def unpickler(pickle_file):
    '''
        This function takes a pickled object and unpickles to a variable
    '''
    # open picked object in read binary mode which is the parameter parsed in
    #pickle_file = open('pickle_file', 'rb')
    unpickle_file = open(pickle_file, 'rb')

    # # unpickle the pickled object by calling the pickle load() and assign to a variable
    my_unpickle = pickle.load(unpickle_file)
    #
    # close file
    unpickle_file.close()
    # return the my_unpickle object
    return my_unpickle


