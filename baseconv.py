import string
import base64
# def main():
#     n = "Vm0wd2QyVkhV"
#     maxx = 5000
#     for index in range(len(n)):
#         for index2 in range(index + 1, len(n)):
#             if n[index] == n[index2] and index2 - index < maxx:
#                 maxx = index2 - index
#                 print(n[index], index, index2)
#
#
# main()

# Program to print all combination
# of size r in an array of size n

# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# combinationUtil()
def printCombination(arr, n, r):
    # A temporary array to store
    # all combination one by one
    data = [0] * r

    # Print all combination using
    # temprary array 'data[]'
    combinationUtil(arr, n, r, 0, data, 0)


''' arr[] ---> Input Array 
n     ---> Size of input array 
r     ---> Size of a combination to be printed 
index ---> Current index in data[] 
data[] ---> Temporary array to store 
            current combination 
i     ---> index of current element in arr[]     '''


def combinationUtil(arr, n, r, index, data, i):
    # Current cobination is ready,
    # print it
    if index == r:
        # with open(r'C:\Users\Alex\Desktop\halo.txt', 'a') as f:
        #     for j in range(r):
        #         f.write(data[j])
        #     f.write("\n")
        #     return
        custom_b64 = ""
        for j in range(r):
            custom_b64 += data[j]
        stringToBeDecoded = "Vm0wd2QyVkhV"
        standard_b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        temp_decoded = ""
        for ch in stringToBeDecoded:
            if ch in custom_b64:
                temp_decoded += standard_b64[str.find(custom_b64, str(ch))]
            elif ch == '=':
                temp_decoded += '='
        decoded = base64.b64decode(temp_decoded)
        print(decoded)
        return

    # When no more elements are
    # there to put in data[]
    if (i >= n):
        return

    # current is included, put
    # next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1)

    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    combinationUtil(arr, n, r, index,
                    data, i + 1)


# Driver Code
if __name__ == "__main__":
    arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    r = len(arr)
    n = len(arr)
    printCombination(arr, n, r)