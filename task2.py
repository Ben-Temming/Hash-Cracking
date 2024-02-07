#task 2 code
import hashlib

def hash_str(password_str): 
    #create sha512 object
    sha512 = hashlib.sha512() 
    #update object with encoded password_str
    sha512.update(password_str.encode())
    #generate and return hashed string
    return sha512.hexdigest()


def dictionary_crack_hashes(dict_vals, hash_list): 
    result_list = ["Not found"]*len(hash_list)
    uncracked_hashes_indexes = set(range(len(hash_list)))

    dict_counter = 0 #keeping track of which password to check in the dict_vals list
    dict_len = len(dict_vals)

    while uncracked_hashes_indexes and (dict_counter < dict_len):
        #select the dictionary password to check 
        password_str = dict_vals[dict_counter]
        #compute hash of the password 
        password_hash = hash_str(password_str)

        #for every uncracked hash check if there is a match
        for index in list(uncracked_hashes_indexes): 
            #check if the hash from hash list is the same as the password hash 
            if hash_list[index] == password_hash: 
                #matching hash, update result list with password and remove the hash 
                # index from uncracked hashes set
                result_list[index] = password_str
                uncracked_hashes_indexes.remove(index)

        # if there are no more uncracked hashes stop checking dictionary 
        if not uncracked_hashes_indexes: 
            break
        #move to next word in dictionary list
        dict_counter += 1

    return result_list


if __name__ == "__main__": 
    #load dictionary values 
    file_name = "PasswordDictionary.txt"
    password_dictionary_list = []
    with open(file_name, "r") as file: 
        #read each line in the file, strip spaces and add password to list 
        for line in file: 
            password_dictionary_list.append(line.strip())

    #list of hashes that we want to crack
    hash_list = [
        '31a3423d8f8d93b92baffd753608697ebb695e4fca4610ad7e08d3d0eb7f69d75cb16d61caf7cead0546b9be4e4346c56758e94fc5efe8b437c44ad460628c70', 
        '9381163828feb9072d232e02a1ee684a141fa9cddcf81c619e16f1dbbf6818c2edcc7ce2dc053eec3918f05d0946dd5386cbd50f790876449ae589c5b5f82762', 
        'a02f6423e725206b0ece283a6d59c85e71c4c5a9788351a24b1ebb18dcd8021ab854409130a3ac941fa35d1334672e36ed312a43462f4c91ca2822dd5762bd2b', 
        '834bd9315cb4711f052a5cc25641e947fc2b3ee94c89d90ed37da2d92b0ae0a33f8f7479c2a57a32feabdde1853e10c2573b673552d25b26943aefc3a0d05699', 
        '0ae72941b22a8733ca300161619ba9f8314ccf85f4bad1df0dc488fdd15d220b2dba3154dc8c78c577979abd514bf7949ddfece61d37614fbae7819710cae7ab', 
        '6768082bcb1ad00f831b4f0653c7e70d9cbc0f60df9f7d16a5f2da0886b3ce92b4cc458fbf03fea094e663cb397a76622de41305debbbb203dbcedff23a10d8a', 
        '0f17b11e84964b8df96c36e8aaa68bfa5655d3adf3bf7b4dc162a6aa0f7514f32903b3ceb53d223e74946052c233c466fc0f2cc18c8bf08aa5d0139f58157350', 
        'cf4f5338c0f2ccd3b7728d205bc52f0e2f607388ba361839bd6894c6fb8e267beb5b5bfe13b6e8cc5ab04c58b5619968615265141cc6a8a9cd5fd8cc48d837ec', 
        '1830a3dfe79e29d30441f8d736e2be7dbc3aa912f11abbffb91810efeef1f60426c31b6d666eadd83bbba2cc650d8f9a6393310b84e2ef02efa9fe161bf8f41d', 
        '3b46175f10fdb54c7941eca89cc813ddd8feb611ed3b331093a3948e3ab0c3b141ff6a7920f9a068ab0bf02d7ddaf2a52ef62d8fb3a6719cf25ec6f0061da791'
        ]

    #get list of passwords
    password_list = dictionary_crack_hashes(password_dictionary_list, hash_list)
    #print each password in the terminal
    for password in password_list: 
        print(password)