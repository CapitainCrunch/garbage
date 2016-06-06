__author__ = 'Bogdan'
# encoding=utf-8


class Hashtable(object):

    def __init__(self, size):
        self.size = size
        self.hashtable = []
        for i in xrange(self.size):
            self.hashtable.append([])
        self.all_entries = []

    def string(self, key):
        count = 0
        for k in key:
            count = count + ord(k) #конвертирует строку длиной 1 в циферки, которые обозначают позицию в Unicode таблице
            bucket_no = count % self.size
        return bucket_no

    def get_bucket(self, key):
        bucket_no = self.string(key)
        return self.hashtable[bucket_no]

    def get_entry(self, bucket, key):
        for entry in bucket:
            if entry[0]==key:
                return entry
        return None

    def add(self, key, value):
        bucket_no = self.string(key)
        bucket = self.get_bucket(key)
        entry = self.get_entry(bucket, key)
        if entry:
            entry[1] = value
            self.update_all_entries(key, value)
            return self.hashtable
        elif len(bucket)==0:
            bucket.append([key, value])
        else:
            collision = self.collision_handling(key, bucket_no)
            if collision:
                collision[1] = value
                self.update_all_entries(key, value)
                return self.hashtable
            else:
                collision.append([key, value])
            self.all_entries.append([key, value])

    def collision_handling(self, key, bucket_no):
        for bucket in self.hashtable:
            bucket_no += 1
            if bucket_no >= len(self.hashtable):
                bucket_no = 0
            check_bucket = self.hashtable[bucket_no]
            if len(check_bucket)==0:
                return check_bucket
            else:
                for entry in check_bucket:
                    if entry[0]==key:
                        return entry
        raise ValueError

    def find(self, key):
        bucket_no = self.string(key)
        entry = self.get_entry(self.get_bucket(key), key)
        if entry:
            return entry[1]
        else:
            collision = self.collision_handling(key, bucket_no)
            if collision:
                return collision[1]
            return "Error! {} is not a key in the hashtable".format(key)

    def update_all_entries(self, key, value):
        #по идее надо для изменения размера, но я могу ошибаться в псевдокоде
        for each in self.all_entries:
            if each[0]==key:
                each[1]=value

    #не имею понятия :)
    def delete(self, key):
        bucket = self.get_bucket(key)
        entry = self.get_entry(bucket, key)
        if entry:
            bucket.remove(entry[:2])
            self.all_entries.remove(entry[:2])
        return 'Deleted'


hashtable1 = Hashtable(1000)


print hashtable1
