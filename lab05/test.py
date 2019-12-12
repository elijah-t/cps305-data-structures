import unittest
from hashing import HashTable

class HashTableTest(unittest.TestCase):

    def testput(self):
        data = HashTable()
        data.put(90, "apple")
        self.assertEqual(data.get(data.slots[2]), "apple")

    def testBeforeResize(self):
        data = HashTable()
        data[97]="apple"
        data[50]="banana"
        data[44]="cherry"
        data[27]="grape"
        data[86]="orange"
        self.assertEqual(data.get(data.slots[9]), "apple")
        self.assertEqual(data.get(data.slots[6]), "banana")
        self.assertEqual(data.get(data.slots[10]), "orange") #Collision
    
    def testAfterResize(self):
        data = HashTable()
        data[97]="apple"
        data[50]="banana"
        data[44]="cherry"
        data[27]="grape"
        data[86]="orange"
        data[64]="papaya"
        data[39]="grape"
        self.assertEqual(data.get(data.slots[6]), "apple")
        self.assertEqual(data.get(data.slots[5]), "banana")
        self.assertEqual(data.get(data.slots[4]), "grape") #Collision
        self.assertEqual(data.get(data.slots[17]), "orange")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)