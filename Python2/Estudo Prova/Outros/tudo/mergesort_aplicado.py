def mergeSort(list):
       if len(list)>1:
        mid = len(list)//2
        esquerdo = list[:mid]
        direito = list[mid:]

        mergeSort(esquerdo)
        mergeSort(direito)

        i=0
        j=0
        k=0
        while i<len(esquerdo) and j<len(direito):
            if esquerdo[i]<direito[j]:
                list[k]=esquerdo[i]
                i=i+1
            else:
                list[k]=direito[j]
                j=j+1
            k=k+1

        while i<len(esquerdo):
            list[k]=esquerdo[i]
            i=i+1
            k=k+1

        while j<len(direito):
            list[k]=direito[j]
            j=j+1
            k=k+1
   
list = [45,56,93,17,44,-1,49,-13,20]
mergeSort(list)
print(list)

