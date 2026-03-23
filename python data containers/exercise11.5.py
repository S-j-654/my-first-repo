batch_1 = [1, 2, 3]
batch_2 = batch_1
batch_3 = batch_1.copy()
batch_1.append(4)
print (f"Batch 2: {batch_2}")
print (f"Batch 3: {batch_3}")
batch_2 changed because running batch_2 = batch_1 created a new reference but to thesame list as batch_1
batch_3 did not change because running that code creates a shallow copy of the list which creates a new object 
containing just the current vaalues of batch_1 hence changing anythig in the original list will not affect it.

